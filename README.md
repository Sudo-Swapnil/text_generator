In this project, we create a program that can generate various meaningful sentences based on a given word. 

Technology, Modules and Extras used:

1. Python 3
2. NLTK -> for tokenization
3. A corpus containing 23 thounsand dialogues from 'Game of Thrones' series 

Brief description:

In stage 1, we open the given text corpus, break the text into separate words, and obtain some properties of the corpus.
In stage 2, we transform the preprocessed corpus into a list of bigrams.
In the final stage, we transform the preprocessed corpus into trigrams for better results, create a Markov chain that shows the probability of certain words appearing after a given chain of words and use this to generate a text starting with a word and handle exceptions. Finally, we modify the algorithm so that sentences always start with capital letters and end with punctuation marks.