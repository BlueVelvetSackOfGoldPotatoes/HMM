
from FOMM import *

def main():
    
    w = "This is a sentence, what will happen then, uh?"

    clf = FOMM()
    clf.fit(w)
    clf.print_content()
    print(clf.classify(" "))
    print(clf.classify("C","A"))

if __name__ == "__main__":
    main()