
from FOMM import *

def main():
    # INITIAL PARAMETERS
    w = ["one", "1", "2", "one", "three", "3", 3, "4", "1", "hello", "!", "!", "!"]

    clf = FOMM()
    clf.fit(w)
    clf.print_content()
    print(clf.classify("ajshdgfkugsdugls","4"))
    print(clf.classify("1","4"))
    print(clf.classify("1","2"))
if __name__ == "__main__":
    main()