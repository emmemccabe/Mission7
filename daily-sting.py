"""
Emme McCabe
December 12th, 2018
Mission 7 Skeleton

High level plan: 

-emphasize satire from today's news headlines.
-take the longest article from different publications to generate initial population

-ALGORITHM: 
    initialization:
        -create script by chopping up the article between different characters (NLP)
        -CHARACTERs: nltk person tags, assign lines as DONALD TRUMP: lines... [trump, line]

    evaluation/selection: for longest line = least fit

    mutation: 
        options: 
        character change
        repetition
        change dialougue to synonym or antonym

    stopping criteria: num of iterations, top rated movie (based on unique words)

web scraping instructions via : https://codeburst.io/web-scraping-101-with-python-beautiful-soup-bb617be1f486
wordnet help: https://www.tutorialspoint.com/python/python_synonyms_and_antonyms.htm
"""
import random
import numpy
import requests
from newspaper import Article
import newspaper
from nltk.corpus import wordnet
import nltk
nltk.download('wordnet')

# Constants
NUM_ITERATIONS = 50
NUM_SCRIPTS = 5
bestMovie = False


# SOURCES
urls = ["http://washingtonpost.com", "http://usatoday.com", "http://wsj.com", "http://latimes.com", 
    "http://nydailynews.com", "http://nypost.com", "http://Boston.com", "http://ChicagoTribune.com",  
    "http://msncbc.com", "http://www.theatlantic.com/world/", "http://www.foxnews.com/",
    "http://www.cnbc.com/", "http://www.economist.com/"]

# WEBSITE DICTIONARY
news_sites = {"http://washingtonpost.com": "Washington Post", "http://usatoday.com": "USA Today", "http://wsj.com": "The Wall Street Journal", "http://latimes.com":
"The LA Times", "http://nydailynews.com": "NY Daily News", "http://nypost.com": "The NY Post", "http://Boston.com": "Boston News",
 "http://ChicagoTribune.com": "The Chicago Tribune", "http://msncbc.com": "MSNBC News", "http://www.theatlantic.com/world/": "The Atlantic",
  "http://www.foxnews.com/": "Fox News", "http://www.cnbc.com/": "CNBC", "http://www.economist.com/":"The Economist"}


#Classes

class Script():

    def __init__(self):
        self.title = ""
        self.dialougue = []
        self.summary = ""
        self.characters = []

    def __str__(self):
        name_list = self.title.replace("-"," ").split(" ")
        title_string = ""
        for word in name_list:
            word = word.capitalize()
            title_string += word + " "
        
        return title_string

    def addLine(self, new_line):
        self.dialougue.append(new_line)
        return 

# Begin Functions
def scrape(urls):
    """scrape different news publications urls and choose one headline to genereate the movie"""

    url = random.choice(urls)
    #url = "http://www.latimes.com"
    print("reading: " + url)

    front_page = newspaper.build(url)

    headlines = []

    for article in front_page.articles:
        headlines.append(article.url)

    return headlines, url


def longest_article(headline_list):
    ''''''
    max_len = 3500
    chosen_url = ''

    for url in headline_list:
        print(url)
        article = Article(url)
        #Sometimes the url is not the correct format, and cannot be downloaded, so move to the next
        try:
            article.download()
            article.parse()
            article.nlp()
        except:
            continue

    #get the longest article
        if len(article.text) > max_len:
            print(article.text)
            print(max_len)
            chosen_url = url
            max_len = len(article.text)

    chosen_article = Article(chosen_url)
  
    return chosen_article


def title(article):
#TODO: Make this more fun... artcle - Movie, or Revenge of the
    
    keyword = random.choice(article.keywords)

    title1 = "the-" + keyword
    title2 = "revenge-of-the-" + keyword
    title3 = keyword + "-movie"

    title = random.choice([title1, title2, title3])
    print(title)
    return title

def choose_characters(article):
    """given article in string form, pull names"""
    qry = article.text
    tokens = nltk.tokenize.word_tokenize(qry)
    pos = nltk.pos_tag(tokens)
    sentt = nltk.ne_chunk(pos, binary = False)
    #print(sentt)
    person = []
    for subtree in sentt.subtrees(filter=lambda t: t.label() == 'PERSON'):
        for leaf in subtree.leaves():
            person.append(leaf)

    character_list = []

    for people in person:
        if people[0] not in character_list:
            character_list.append(people[0])

    num_ppl_in_article = len(character_list)
    movie_stars = random.choices(character_list, k = int(num_ppl_in_article/2))
    print(movie_stars)
    return movie_stars



def mutate(script, line_index, line):

    mutation = random.randint(1,5)

    #remove the line
    if mutation == 1:
        print("Mutation 1: " + str(line_index))
        script.dialougue.pop(line_index)
        return script

    # make another character say the line
    if mutation == 2:
        print("Mutation 2: " + str(line_index))

        #choose the new character
        new_char = random.choice(script.characters)

        #change the speaker
        script.dialougue[line_index][0] = new_char
        return script

    #repeat the line a random number of times, by the same character
    if mutation == 3:
        print("Mutation 3: "+ str(line_index))

        repetitions = random.randint(0,5)
        for i in range(repetitions):
            new_index = random.randint(0,len(script.dialougue))
            script.dialougue.insert(new_index, line)
        return script

    # change the some words in the lines to random synonyms (if the word has a synonym)
    if mutation == 4 and line[1] != '':
        print("Mutation 4: "+ str(line_index))
        #choose a word to mutate, longer word is more likely chosen given weighted probability

        weights = []
        word_list = line[1].split(" ")
        for word in word_list:
            weights.append(len(word))

        word = random.choices(word_list, weights, k=1)[0]
        print(word)

        #create list of all synonyms of chosen word

        synonyms = []

        for syn in wordnet.synsets(word):
            for lm in syn.lemmas():
                synonyms.append(lm.name())

        print(synonyms)
        # if the synonym list isn't empty
        if len(synonyms) > 0:
            #assign weights based on length of similar words
            weights2 = []
            for word in synonyms:
                weights2.append(len(word))

            #pick a replacement word using weighted probability
            new_word = random.choices(synonyms, weights2, k=1)[0]
            script.dialougue[line_index][1] = script.dialougue[line_index][1].replace(word, new_word)

        return script

    else:
        return script


    # change the words in the line to random antonyms
    if mutation == 5 and line[1] != '':
        print("Mutation 5: "+ str(line_index))
        #choose a word to mutate
        
        weights = []
        word_list = line[1].split(" ")

        for word in word_list:
            weights.append(len(word))

        word = random.choices(word_list, weights, k=1)[0]
        print(word)


        #create list of all synonyms of chosen word
        antonyms = []

        for syn in wordnet.synsets(word):
            for lm in syn.lemmas():
                if lm.antonyms():
                    antonyms.append(lm.antonyms()[0].name())

        print(antonyms)
        # if the antonym list isn't empty
        if len(antonyms) > 0:
                    #assign weights based on length of similar words
            weights2 = []
            for word in antonyms:
                weights2.append(len(word))

            #pick a replacement word using weighted probability
            new_word = random.choices(antonyms, weights2, k=1)[0]
            script.dialougue[line_index][1] = script.dialougue[line_index][1].replace(word, new_word)

        return script



def generate_movie(headlines, url):

    article = longest_article(headlines) #this is an Article object
    print(article.text)

    article.download()
    article.parse()
    article.nlp()

    characters = choose_characters(article)
    


    name = title(article)
    print(name)

    #Create script object
    script = Script()
    script.title = name

    script.characters = characters
    script.summary = article.summary

    lines = article.text.split("\n")

    for line in lines:
        character = random.choice(characters)
        line = line.replace('\n', '')
        line = line.strip("()")
        line = line.strip()
        if len(line) >= 0:
            script.dialougue.append([character, line])


    return script, url

def write_to_file(script, news_site):
    '''writes the script to a text file, with proper formatting'''
   
    # write script name
    with open("example_output/example10.txt", "w+") as file:
        file.write(script.__str__() + "\n")
        file.write("Inspired by: " + news_site + "\n\n")


        for line in movie_script.dialougue:
            line[0] = line[0].upper()
            if line[1] != '':
                file.write(line[0] + ":\t" + line[1] + ".\n")
                file.write("\n")

def unique_words(script):
    unique_words = []
    for sentence in script.dialougue:
        word_list = sentence[1].split(" ")
        for word in word_list:
            if word not in unique_words:
                unique_words.append(word)
    return len(unique_words)

#MAIN METHOD
#Scrape
#Evaluate and mutate script
if __name__ == "__main__":

    headlines, url = scrape(urls)

    movie_theater = []

    for i in range(NUM_SCRIPTS):
        
        movie_script, url = generate_movie(headlines, url)

        # ORDERED list of spoken lines:
        for i in range(NUM_ITERATIONS):
            # take random line to mutate, weighted by the longest lines (least fit)
            weights = []
            for line in movie_script.dialougue:
                weights.append(len(line))
            selection = random.choices(movie_script.dialougue, weights, k=1)[0]
            print(selection)

            index = 0
            for i in range(len(movie_script.dialougue)-1):
                if movie_script.dialougue[i] == selection:
                    index = i

            print(index)

            print(movie_script.dialougue[index])

            #pass in the script object and location of chosen selection
            movie_script = mutate(movie_script, index, selection)

            #print the mutated line
            print(movie_script.dialougue[index])

        movie_theater.append(movie_script)

    max_score = 0
    for script in movie_theater:
        unique = unique_words(script)
        if unique > max_score:
            best_script = script
            max_score = unique

    print(best_script.title + "\n")

    for line in best_script.dialougue:
        line[0] = line[0].upper()
        if line[1] != '':
            print(line[0] + ":" + "\t" + line[1] + "\n")

    print("Open /Mission7/example_output to view script of: " + best_script.__str__())

    #pull news site from dictionary
    site = news_sites[url]
    
    print(site)

    write_to_file(best_script, site)

