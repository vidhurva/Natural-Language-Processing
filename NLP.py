#libraries
import spacy

nlp = spacy.load('en_core_web_lg')

#Texts used in NLP pipeline
text_Amalfi = """The Amalfi Coast (Italian: Costiera Amalfitana) is a stretch of coastline on the northern coast of the Salerno Gulf on the Tyrrhenian Sea, located in the Province of Salerno of southern Italy. The Amalfi Coast is a popular tourist destination for the region and Italy as a whole, attracting thousands of tourists annually.[1] In 1997, the Amalfi Coast was listed as a UNESCO World Heritage Site."""

text_Shakira = """Shakira Isabel Mebarak Ripoll, born 2 February 1977) is a Colombian singer, songwriter, dancer, businesswoman, and philanthropist. Shakira has received numerous awards, including 3 Grammy Awards, 13 Latin Grammy Awards, 4 MTV Video Music Awards, 7 Billboard Music Awards, 39 Billboard Latin Music Awards and has been Golden Globe-nominated."""

#Sentences are parsed
parse = nlp(text_Amalfi)
parseara = nlp(text_Shakira)

#Outputs the corresponding entity 
for entity in parse.ents:
    print(f"{entity.text} ({entity.label_})")
print("")

for entity in parseara.ents:
    print(f"{entity.text} ({entity.label_})")
