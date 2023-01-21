#Import libraries for natural language processing
import spacy

# declare a model for natural language processing
nlp = spacy.load('en_core_web_md')

#Open the file with the list of movies and descriptions and append the 
#movie names and descriptions in lists
f = open("movies.txt" , "r")

descriptions = []
movie_names = []

for line in f:

    descriptions.append(line[9:].strip("\n"))
    movie_names.append(line[0:9])

f.close

# Define a function that gets as input a movie description and returns the best match for a movie recommendation
def watch_next(description_input):

    description_input_nlp = nlp(description_input)
    similarity = []

    for description in descriptions:
        similarity.append(nlp(description).similarity(description_input_nlp))
    
    index_max = similarity.index(max(similarity))

    print(f"The movie with the highest similarity of {round(similarity[index_max]*100),2}% of match is {movie_names[index_max]} {descriptions[index_max]}")


#Declare a description to enter it in the function’s argument
description_in = "Will he save their world or destroy it? When the Hulk becomes too dangerous for the Earth, the Illuminati trick Hulk into a shuttle and launch him into space to a planet where the Hulk can live in peace. Unfortunately, Hulk land on the planet Sakaar where he is sold into slavery and trained as a gladiator."

#call the function created with the input information
watch_next(description_in)
