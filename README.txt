Emme McCabe
Mission 7
Wednesday, December 12th, 2018

Overview: 

The system is called, Daily Sting, since it uses today's news to generate a movie script. From a high level, the system scrapes top news sites from around the country and world, builds an article, divides the article to different characters through NLP, then mutates to inspire satire. The main algorithms are genetically modeled, and include testing fitness based on the length of spoken lines, and count of unique words.

Setup: 

To run code: in Terminal

$ python daily-sting.py

User will be prompted to enter the desired output file location.
I have included some empty example files, for testing. (example11.txt->example15.txt)

* please be patient if you receive the following error, and run terminal command again *

newspaper.article.ArticleException: Article `download()` failed with No connection adapters were found for '://' on URL ://

The site has not yet been updated, if the news_site was recently used (within the last 10 minutes or so in my tedious experience) This was a hindrance!!

System Architecture: 

In more detail, the system uses the newspaper build to break up an article (with acceptable length) into speaking roles for characters. The characters were pulled from the article using NLP tokenization. Then the dialogue in the form of a list is mutated based on the fitness of lines chosen by weighted probability, a genetic approach. The mutations occur for a given constant number of iterations. This could be changed to increase or decrease straying from the original article, and thus, altering the level of satire (my emphasis).

I chose to focus on satire. 
I was intrigued by findings from an article, "Automatic satire detection: are you having a laugh?" by Clint Burfoot	and Timothy Baldwin, of the University of Melbourne, VIC Australia. (https://dl.acm.org/citation.cfm?id=1667633). They used SVMs, feature scaling, and lexical and semantic feature types, to detect truth from sarcasm and satire. I was able to use their idea that altering the truth very subtly can create satiric content.

The satire was accomplished through the randomization of assigning lines to unlikely/random characters, and through the different mutations (removing lines, repeating lines, changing words in lines, and changing the character)

See System Architecture. (sys-arch.jpg)

Computational Creativity:
Throughout the course, I have been grappling with the definition of what it means for a system to be creative. Although I am still exploring this idea, and how to improve my techniques to achieve such creativity, I can define a creative system as a multi-dimensional process to create ANYTHING that is intentionally novel and valuable to a given audience (not necessarily a human), aligned with Boden's definition. 

The Daily Sting system had a significant ability strength in "Dealing with Uncertainty," as the plethora of news stories is infinite, varied in formatting, and inclination for satirical improvement. I was limited by the rate limits placed on scraping the sites, and downloading error, which causes the system to basically self destruct. 


Personal Challenges: 

This course has been challenging for me. It was also (by far) the class I have learned the most theory and technical skills, thus far in 3 years at Bowdoin, which I can credit to the subjects (cookies) and instructions! I was instantly engaged in the class and built up my confidence as a computer scientist, although I'll admit I was very intimidated at first. This assignment was no exception. I challenged myself to use web scraping, which I always stray away from. I also used Object-Oriented Programming for my Script class, which was such a useful tool. It was a challenge, since I have not used it much since Intro to CS, and never fully understood the techniques until now. I was excited about my high-level idea and spent a lot of time tweaking my system. I thought the idea was unique and funny. I didn't want to do something too serious. I also got to read current events during my many trial iterations. This assignment was a great culmination of everything we learned throughout the semester. I truly loved this course, and cannot take another Prof. Harmon course when I return from my spring semester abroad!

