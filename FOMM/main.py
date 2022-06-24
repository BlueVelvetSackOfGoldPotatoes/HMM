
from FOMM import *

def main():
    # INITIAL PARAMETERS
    w = ["A", "C", "A", "C"]

    clf = FOMM()
    clf.fit(w)
    clf.print_content()
    # print(clf.classify("A","C"))
    # print(clf.classify("C","A"))

if __name__ == "__main__":
    main()