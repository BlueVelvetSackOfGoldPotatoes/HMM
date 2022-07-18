import copy

""" A First Order Markov Model, where w(t) is the state at any time t, a sequence of length T is denoted by W^T = {w(1), w(2), w(3), ..., w(T)}. Transition probability: P(wj(t+1) | wi(t)) = aij -> this is the probability of having state wj at step t+1 given that the state at time t was wi.

Note that,
    (1) FOMM are not strictly symmetric: aij != aji;
    (2) The next state might be the current state: aii != 0;

Returns:
    FOMM: A First Order Markov Model object, capable of fitting a list of temporally related symbols and classifying the probability of a state following another state.
"""

class FOMM:
    def __init__(self):
        self.__data = [] # A temporally oriented list of size T: [w(1), w(2), ..., w(T)].
        self.__theta = {} # A model of the transition probabilities for the states: P(wj(t+1) | wi(t)).
        self.__sub_counts = {} # A count of how many times one state follows another {state1 : {state1: 1, ..., stateT: x}, state2: ...}.
        self.__histogram = {} # The number of occurences of each state [state : n_occurrences].
        self.__frequency = {} # The probability of each state in the set {state1:50%, state2:20%, ...}.

    def fit(self, data):
        """Fit the first order markov model on data. Initializes all the object parameters from the data.

        Parameters:
            List: (data) A list of temporally related symbols (w1 -> w2), where w2 occurs after w1.
        """
        self.__data = [str(x) for x in data]
        self.__theta = self.init_transition_model()
        self.__sub_counts = self.init_transition_model()
        self.__histogram = self.init_hist()
        self.__frequency = self.calculate_freq()

        for ele in self.__theta:
            for i in range(1,len(self.__data)):
                if self.__data[i-1] != ele:
                    continue
                else:
                    self.__theta[ele][self.__data[i]] += 1
        self.__sub_counts = copy.deepcopy(self.__theta)

        for ele in self.__theta:
            for other_state in self.__theta[ele]:
                self.__theta[ele][other_state] = round(self.__theta[ele][other_state] / (len(self.__data)-1) * 100, 2)
    
    def init_transition_model(self):
        """Initialize the empty dictionary that saves the transition probability model.

        Returns:
            Dictionary: (theta) The model, where each key represents the state and the sub dictionary for each key represents the next state and its value entry is its probability.
        """
        theta = {}

        for ele in self.__data:
            theta[ele] = {}
            for i in range(len(self.__data)):
                theta[ele][self.__data[i]] = 0
                
        return theta

    def init_hist(self):
        """Initialize the empty dictionary that saves the frequency of each state occurring in the set.

        Returns:
            Dictionary: (elements_hist) The frequency where each key represents the state and its value entry is the number of times it occurs in the set.
        """
        elements_hist = {}
        for ele in self.__data:
            if ele not in elements_hist:
                elements_hist[ele] = 0
            else:
                continue
            for comp in self.__data:
                if comp == ele:
                    elements_hist[ele] += 1

        return elements_hist

    def calculate_freq(self):
        """Initialize the empty dictionary that saves the probability of each state occurring in the set.

        Returns:
            Dictionary: (w_freq) The frequency in probability where each key represents the state and its value entry is its probability.
        """
        w_freq = {}
        for ele in self.__histogram:
            w_freq[ele] = self.__histogram[ele]/len(self.__data) * 100

        return w_freq


    def classify(self, currentState, nextState=None):
        """Finds the transition probability of the given states in some fitted model theta.

        Parameters:
            Variable: (currentState) Will be cast to string - this is the current state.
            Variable: (nextState) Will be cast to string - this is the next state, following currentState.

        Returns:
            Float: In the case of these existing in the model, returns the transition probability for the given states, else returns 0.0 - to be interpreted as the probability of 0, since the transitional states was never seen before by the MM.
        """
        if nextState==None:
            return self.__frequency[currentState]
        elif str(currentState) in self.__theta and str(nextState) in self.__theta[str(currentState)]:
            return self.__theta[str(currentState)][str(nextState)]
        else:
            return 0.0
    
    # GETTERS ---------- --------------------- ---------- V
    def print_theta(self,dic):
        """Prints the transition probability model dictionary or Theta.

        Parameters:
            Dictionary: A dictionary with sub dictionaries.
        """
        for key, value in zip(dic.keys(), dic.values()):
            print("######################")
            print(f"Current state: {key}")
            print("######################")
            for subkey, subvalue in zip(value.keys(), value.values()):
                print(f"P({subkey} | {key}) = {subvalue})\n")
    
    def get_data(self):
        """Returns the data used to fit the model.

        Parameters:
            List: (__data) A list with the transition states used to fit the model.
        """
        return self.__data

    def get_sub_counts(self):
        """Returns the  of each state in the data.

        Parameters:
            Dictionary: (__sub_counts) A count of how many times one state follows another {state1 : {state1: 1, ..., stateT: x}, state2: ...}.
        """
        return self.__sub_counts

    def get_hist(self):
        """Returns the histogram (counts) of each state in the data.

        Parameters:
            Dictionary: (__histogram) The number of occurences of each state [state : n_occurrences].
        """
        return self.__histogram

    def get_freq(self):
        """Returns the probability of each state occurring in the set.

        Parameters:
            Dictionary: (__frequency) The probability of each state in the set {state1:50%, state2:20%, ...}.
        """
        return self.__frequency

    def get_theta(self):
        """Returns the fitted model.

        Parameters:
            Dictionary: A model of the transition probabilities for the states: P(wj(t+1) | wi(t)).
        """
        return self.__theta

    def print_content(self):
        """Prints all the relevant parameters of the model.
        """
        print("~"*50)
        print(f"Data: \n{self.__data}")
        print("~"*50)
        print("~"*50)
        print(f" Fitted \u03B8: \n")
        self.print_theta(self.__theta)
        print("~"*50)
        print("~"*50)
        print(f"Freq: \n{self.__frequency}")
        print("~"*50)
        print("~"*50)
        print(f"Hist: \n{self.__histogram}")
        print("~"*50)
        print("~"*50)
        print(f"Sub Counts: \n{self.__sub_counts}")
        print("~"*50)
