from collections import Counter
from collections import OrderedDict
import numpy as np

def intake():
  candidates = []

  line = input()
  while line != 'done' and line != 'end':
    # TODO: Add fractional input?
    try:
      candidate_position = float(line)
      if candidate_position < 0.0 or candidate_position > 1.0:
        print('Invalid value range, get better')
      else:
        candidates.append(float(line))
    except ValueError:
      print('bruh type numbers in better')

    line = input()

  candidates.sort()
  return candidates


def count_candidate_votes(candidates):
  # print()
  candidate_votes = []

  for i in range(len(candidates)):
    vote = 0

    if i != 0:
      vote += (candidates[i] - candidates[i - 1]) / 2
    else:
      vote += candidates[i]

    if i != len(candidates) - 1:
      vote += (candidates[i + 1] - candidates[i]) / 2
    else:
      vote += 1.0 - candidates[i]
    candidate_votes.append(vote)
  return candidate_votes


# TODO: Auto win for >.5 vote
def perform_instant_runoff(candidates, rounding_decimalplace = 6):
  # print('Candidates:')
  # print(candidates)
  # print()

  election_round = 1
  while len(candidates) > 1:
    candidate_votes = count_candidate_votes(candidates)
    # print('Election round', election_round, 'results:')
    candidate_votes = [
      round(votes, rounding_decimalplace) for votes in candidate_votes
    ]
    # print(candidate_votes)

    eliminated_candidate = min(range(len(candidate_votes)),
                               key=candidate_votes.__getitem__)

    tied = Counter(candidate_votes)[min(candidate_votes)] != 1
    # print(Counter(candidate_votes))
    if tied:
      # print('There was a tie don\'t consider this')
      return 1 # explicitly stated, for my sanity

    # print('Eliminated:', candidates[eliminated_candidate])

    candidates.pop(eliminated_candidate)
    # print('New list:', candidates)

    election_round += 1

  # print()
  # print('Winner:', candidates[0])

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
  
def m_dimension_intake():
  try:
    dim = float(input("Input dimensions: "))
  except ValueError:
    print("Input valid dimensions.")
    exit()

  end_intake = False

  candidates = []

  while end_intake == "False":
    line = input('candidate: ').split()

    # break condition
    if line[0] == 'end' or line[0] == 'done':
      return candidates
    elif len(line) != dim:
      print("Incorrect dimensions. Try again.")
      continue

    candidate = [float(line[i]) for i in range(len(line))]
    candidates.append(candidate)

  return candidates


if __name__=='__main__':
  candidates = intake()
  perform_instant_runoff(candidates)