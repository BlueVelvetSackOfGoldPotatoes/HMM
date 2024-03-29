
from FOMM import *

def deploy_FOMM(data, filename, words=0):
    """Create the classifier and return the fitted classifier.

    PARAMETERS:
        Variable: (data) -> the data to fit the HMM on.
        Variable: (filename) -> the filename to save the graph under.
        Variable: (words) -> the flag for fitting on the characters (0) or whole symbols/word (1) of a string.
    """
    clf = FOMM()
    if words:
        clf.fit(data, 1)
    else:
        clf.fit(data)

    clf.print_content()
    clf.get_graph(filename)
    return clf

def main():
    d1 = "Alice went down the rabbit hole."

    clf1 = deploy_FOMM(d1, "words", 1)
    clf2 = deploy_FOMM(d1, "characters")

    # d2 = ['A', 'B', 'C', 'A', 'C', 'C', 'B']
    # clf2 = deploy_FOMM(d2)

    print(clf1.classify(" "))
    print(clf1.classify("rabbit"," "))

if __name__ == "__main__":
    main()

""" Todo 
    1. Emission probabilities are the character of the word while the hidden states are the words.
"""

