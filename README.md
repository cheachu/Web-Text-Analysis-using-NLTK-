<h>IMPORT HTML DATA FROM AN EXCEL FILE AND PERFORM ANALYSIS USING NLTK MODULE</h>
The Project uses python and some of its libraries to import url data from a HTML page for data scrapping (WEB SCRAPPING)

<h1>Requirements</h1>
opoen terminal and run the below command so that all the requiremets/ dependencies are installed so that we dont get a ModuleNotFound Error
pip install -r requirements.txt

once the requirements are installed, Go to the data_input.py file which is located in the py_files folder 

**One needs to modify the code on basis of their requirements hence its important to open the data_input.py file and make appropriate changes**


<h2>What does data_input.py do?</h2>
The data_input file takes input for websracpping from an excel sheet which mostly has a url 
You can also direclty scrap data by providing the url directly by modifying the URL_ID code
The code uses beautifulsoup, a web scrapping module of python to scrap data from the given url/website 
the code is mostly built in such a way that ,it only extracts text files present in the website and stores it in a '.txt' format

once the txt file is created sucessfully , we can move to the analysis part

<h3>DATA ANALYSIS USING NLTK</h3>
NLTK, is a suite of libraries and programs for symbolic and statistical natural language processing for English written in the Python programming language. It supports classification, tokenization, stemming, tagging, parsing, and semantic reasoning functionalities
We create a TextBlob where in data is stored and hence ready for analysis 
the following things are calculated and are carried out for analysis


**Positive Score**: This score is calculated by assigning the value of +1 for each word if found in the Positive Dictionary and then adding up all the values.<br>
**Negative Score**: This score is calculated by assigning the value of -1 for each word if found in the Negative Dictionary and then adding up all the values. We multiply the score with -1 so that the score is a positive number.<br>
**Polarity Score**: This is the score that determines if a given text is positive or negative in nature. It is calculated by using the formula: <br>
**Polarity Score** = (Positive Score – Negative Score)/ ((Positive Score + Negative Score) + 0.000001)
Range is from -1 to +1<br>
**Subjectivity Score**: This is the score that determines if a given text is objective or subjective. It is calculated by using the formula: <br>
**Subjectivity Score** = (Positive Score + Negative Score)/ ((Total Words after cleaning) + 0.000001)
Range is from 0 to +1<br>
**Average Sentence Length** = the number of words / the number of sentences<br>
**Percentage of Complex words** = the number of complex words / the number of words <br>
**Fog Index** = 0.4 * (Average Sentence Length + Percentage of Complex words)<br>
**Average Number of Words Per Sentence** = the total number of words / the total number of sentences<br>
**Complex Word Count**:-Complex words are words in the text that contain more than two syllables.<br>
**Word Count**:-We count the total cleaned words present in the text by removing the stop words (using stopwords class of nltk package).<br>
removing any punctuations like ? ! , . from the word before counting.<br>

**Syllable Count Per Word**:-We count the number of Syllables in each word of the text by counting the vowels present in each word. We also handle some exceptions like words ending with "es","ed" by not counting them as a syllable.

**Personal Pronouns**:-To calculate Personal Pronouns mentioned in the text, we use regex to find the counts of the words - “I,” “we,” “my,” “ours,” and “us”. Special care is taken so that the country name US is not included in the list.

**Average Word Length**:-Average Word Length is calculated by the formula:
(Sum of the total number of characters in each word)/(Total number of words)

Once all these values are calculated, these values are stored in an excel sheet where all these attributes are mentioned in a columns 


**IF ALL MODIFICATIONS ARE DONE PROPERLY, WE ARE READY TO RUN THE  main.py FILE TO GET THE OUTPUT**


