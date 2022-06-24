/* A First Order Markov Model, where w(t) is the state at any time t, a sequence of length T is denoted by W^T = {w(1), w(2), w(3), ..., w(T)}. Transition probability: P(wj(t+1) | wi(t)) = aij -> this is the probability of having state wj at step t+1 given that the state at time t was wi.

Note that,
    (1) FOMM are not strictly symmetric: aij != aji;
    (2) The next state might be the current state: aii != 0;

Returns:
    FOMM: A First Order Markov Model object, capable of fitting a list of temporally related symbols and classifying the probability of a state following another state.
*/
#include "FOMM.h"
#include <iostream>

using namespace std;

FOMM::FOMM() {
    cin >> 
}
