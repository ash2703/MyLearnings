import spacy

nlp = spacy.load("en_core_web_sm")   #python3 -m spacy download en_core_web_sm

# doc = nlp("Apple is bigger than microsoft")
# doc = nlp("Proud citizen of India")
doc = nlp("Apple is looking at buying U.K. startup for $1 billion")


# ent is property of a Doc object.
for ent in doc.ents:
    print(ent.text, ent.label_)