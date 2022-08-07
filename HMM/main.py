
from HMM import *

def deploy_HMM(data, filename):
    """Create the classifier and return the fitted classifier.

    PARAMETERS:
        Variable: (data) -> the data to fit the HMM on.
        Variable: (filename) -> the filename to save the graph under.
    """
    clf = HMM()
    clf.fit(data)

    clf.print_content()
    clf.get_graph(filename)
    return clf

def main():
    d1 = "Alice went down the rabbit hole."

    clf1 = deploy_HMM(d1)

    print(clf1.classify(" "))
    print(clf1.classify("rabbit"," "))

if __name__ == "__main__":
    main()

""" Todo 
    1. Emission probabilities are the character of the word while the hidden states are the words.
    2. Need to create a model for emitted states and use that to infer the hidden state.
"""

