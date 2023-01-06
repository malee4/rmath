from collections import OrderedDict
import numpy as np

def sort_dict_keys(my_dict):
    sorted_dict = dict()
    my_keys = list(my_dict.keys())
    my_keys.sort()
    sorted_dict = {i: my_dict[i] for i in my_keys}
    return sorted_dict

def sort_dict_values(my_dict):
    my_keys = list(my_dict.keys())
    my_values = list(my_dict.values())
    my_values_indices = np.argsort(my_values)
    sorted_dict = {my_keys[i]: my_values[i] for i in my_values_indices}
    return sorted_dict

def modified_intake():
    candidates = {}
    line = input()
    while line!= 'done' and line != 'end':
        try:
            candidate_position = float(line)
            if candidate_position < 0.0 or candidate_position > 1.0:
                print("Invalid value range")
            else: 
                candidates[candidate_position] = 0
        except ValueError: 
            print("Invalid input")
        
        line = input()
    
    candidates = sort_dict_keys(candidates)
    return candidates

if __name__ == '__main__':
    my_dict = {}
    print(sort_dict_values(my_dict))