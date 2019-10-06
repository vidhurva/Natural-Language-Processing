# Natural Language Processing

## Introduction 

  Natural Language Processing (NLP) combines linguistics and artificial intelligence in order to allow Computers to understand human language. NLP is used daily, such as Language translations, predictive texts, and Smart assistants (such as Siri and Alexa). I explore a few of the many usages of NLP. 

## Project 1 - Detecting Entity Types

  In this project, my code uses a NLP pipeline in order to detect the entity type from "keywords". An entity code categorizes nouns in each sentence. For example, in the sentence, "Robert Downey Jr. is awesome!", the program categorizes Robert Downey Jr. as a person. Thus, an example output looks like this:

```
Robert Downey Jr. (PER)
```

Note that (PER) is an entity type, which identifies a person. In order to conduct explore this area of NLP, the spacy library is required, which can be installed in your command line interface by using pip or conda. 

```
$ pip install -U spacy
$ conda install -c conda-forge spacy
```
After the installation was successful, I implemented a NLP pipeline (the spacy library performed most of the work) on a paragraph of text from the Amalfi Coast and Shakira wikipedia page. The code allows me to parse words in each sentence and determine their relationship with one another. This was the resulted output:

```
The Amalfi Coast (LOC)
Italian (NORP)
Costiera Amalfitana (PERSON)
the Salerno Gulf (LOC)
the Tyrrhenian Sea (LOC)
the Province of Salerno (GPE)
Italy (GPE)
The Amalfi Coast (LOC)
Italy (GPE)
thousands (CARDINAL)
1997 (DATE)
the Amalfi Coast (LOC)
UNESCO (ORG)

Shakira Isabel Mebarak Ripoll (PERSON)
February 1977 (DATE)
Colombian (NORP)
Shakira (ORG)
3 (CARDINAL)
13 (CARDINAL)
Latin Grammy Awards (EVENT)
4 (CARDINAL)
MTV (ORG)
7 Billboard Music Awards (FAC)
39 (CARDINAL)
Golden Globe- (ORG)
```
The output conveys a noun, followed by the entity category. (Note that if you want to see the strings, you can view them in my attached code.) One issue I notices with the spacy library is that the library seems to have trouble in identifying a place verses a identifying a person. Costiera Amalfitana is a place, not a person (unless if you poets want to humanize the Amalfi Coast's beauty, then we see no issue). Perhaps the issue is that this library has occasional issues identifying terms that are not in English. 

## References

https://medium.com/@ageitgey/natural-language-processing-is-fun-9a0bff37854e

https://www.wonderflow.co/blog/natural-language-processing-examples

https://en.wikipedia.org/wiki/Amalfi_Coast
