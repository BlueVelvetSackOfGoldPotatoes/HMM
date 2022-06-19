import copy

class FOMM:
    def __init__(self, data):
        self.__data = data
        self.__init_transition_matrix = self.init_transition_model()
        self.__theta = self.init_transition_model()
        self.__sub_counts = self.init_transition_model()
        self.__histogram = self.init_hist()
        self.__frequency = self.calculate_freq()

    def init_transition_model(self):
        theta = {}

        for ele in self.__data:
            theta[ele] = {}
            for i in range(len(self.__data)):
                theta[ele][self.__data[i]] = 0
                
        return theta

    def init_hist(self):
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
        w_freq = {}
        for ele in self.__histogram:
            w_freq[ele] = self.__histogram[ele]/len(self.__data) * 100

        return w_freq

    def fit(self):
        print("Fitting...")
        theta = self.__init_transition_matrix
        for ele in self.__init_transition_matrix:
            for i in range(1,len(self.__data)):
                if self.__data[i-1] != ele:
                    continue
                else:
                    theta[ele][self.__data[i]] += 1
        self.__sub_counts = copy.deepcopy(theta)

        for ele in theta:
            for other_state in theta[ele]:
                theta[ele][other_state] = round(theta[ele][other_state] / (len(self.__data)-1) * 100, 2)

        self.__theta = theta

    def classify(self, currentState, nextState):
        print("Classifying...")
    
    # GETTERS ---------- --------------------- ---------- V
    def get_sub_counts(self):
        return self.__sub_counts

    def get_init_model(self):
        return self.__init_transition_matrix

    def get_hist(self):
        return self.__histogram

    def get_freq(self):
        return self.__frequency

    def get_theta(self):
        return self.__theta