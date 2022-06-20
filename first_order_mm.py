
from FOMM import *

def main():
    # INITIAL PARAMETERS
    state1 = "1"
    state2 = "2"
    state3 = "3"
    state4 = "4"
    w = [state1, state2, state1, state2, state1, state1, state3, state4]

    clf = FOMM()
    clf.fit(w)
    clf.print_content()
    print(clf.classify("ajshdgfkugsdugls","4"))
    print(clf.classify("1","4"))
    print(clf.classify("1","2"))
if __name__ == "__main__":
    main()