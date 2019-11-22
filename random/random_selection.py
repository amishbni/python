from random import uniform
from math import fsum

def select(array, total_count, probability):
    probability_accumulative = []
    last_element = 0
    for i in range(len(probability)):
        probability_accumulative.append(last_element + probability[i])
        last_element = probability_accumulative[i]

    result = []

    if(len(array) != len(probability)):
        raise ValueError("array and probability must have the same size.")
    elif(fsum(probability) != 1.0):
        raise ValueError("probabilities do not sum to 1.")
    else:
        for i in range(total_count):
            rand = uniform(0, 1)
            for j in range(len(probability_accumulative)):
                if(rand < probability_accumulative[j]):
                    result.append(array[j])
                    break
    
    return result
