#include <vector>
#include <map>
#include <string>

class FOMM {
    private:
        std::vector<std::string> data;
        std::map<std::string, std::map<std::string, int>> theta;
        std::map<std::string, std::map<std::string, int>> sub_counts;
        std::map<std::string, int> histogram;
        std::map<std::string, int> frequency;

    public:
        FOMM();
        void init_transition_model();
        void fit(std::vector<std::string> _data);
};