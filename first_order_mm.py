
from FOMM import *

def main():
    # INITIAL PARAMETERS
    state1 = "1"
    state2 = "2"
    state3 = "3"
    state4 = "4"
    w = [state1, state2, state1, state2, state1, state1, state3, state4]

    clf = FOMM(w)
    print(f"Freq: {clf.get_freq()}")
    print(f"Hist: {clf.get_hist()}")
    print(f"\u03B8: {clf.get_init_model()}")

    clf.fit()
    print(f" Fitted \u03B8: {clf.get_theta()}")

if __name__ == "__main__":
    main()