
from FOMM import *

def deploy_HMM(data, filename, words=0):
    clf = FOMM()
    if words:
        clf.fit(data, 1)
    else:
        clf.fit(data)

    clf.print_content()
    clf.get_graph(filename)
    return clf

# TODO write a meta-HMM for the text that is built on the word and not character.

def main():
    d1 = "Lisa is very beautiful and smart! And Peter and Mary and wtv Lisa is very beautiful and smart! And Peter and Mary and wtv Lisa is very beautiful and smart! And Peter and Mary and wtv Lisa is very beautiful and smart! And Peter and Mary and wtv Lisa is very beautiful and smart! And Peter and Mary and wtv Lisa is very beautiful and smart! And Peter and Mary and wtv Lisa is very beautiful and smart! And Peter and Mary and wtv ! Lisa is very beautiful and smart! And Peter and Mary and wtv Lisa is very beautiful and smart! And Peter and Mary and wtv Lisa is very beautiful and smart! And Peter and Mary and wtv Lisa is very beautiful and smart! And Peter and Mary and wtv Lisa is very beautiful and smart! And Peter and Mary and wtv Lisa is very beautiful and smart! And Peter and Mary and wtv Lisa is very beautiful and smart! And Peter and Mary and wtv ! Lisa is very beautiful and smart! And Peter and Mary and wtv Lisa is very beautiful and smart! And Peter and Mary and wtv Lisa is very beautiful and smart! And Peter and Mary and wtv Lisa is very beautiful and smart! And Peter and Mary and wtv Lisa is very beautiful and smart! And Peter and Mary and wtv Lisa is very beautiful and smart! And Peter and Mary and wtv Lisa is very beautiful and smart! And Peter and Mary and wtv !"
    
    clf1 = deploy_HMM(d1, "words", 1)
    clf2 = deploy_HMM(d1, "characters")

    # d2 = ['A', 'B', 'C', 'A', 'C', 'C', 'B']
    # clf2 = deploy_HMM(d2)

    print(clf1.classify(" "))
    # print(clf2.classify("C","A"))

if __name__ == "__main__":
    main()