from collections import Counter
from tools import *
import numpy as np

# def polarized_count_candidate_votes(eliminated_candidate, candidates, lost_voters, most_liberal = False):
#     if not most_liberal:
#         index = eliminated_candidate - 1
#         candidates[index] += candidates[eliminated_candidate]
#     else:
#         lost_voters += candidates[eliminated_candidate]

#     candidates.pop(eliminated_candidate)
#     return candidates

def polarized_count_candidate_votes(eliminated_candidate_index, candidates, candidate_votes=None, lost_voters=0):
    if not candidate_votes:
          ...
    elif eliminated_candidate_index <= 0:
      candidates[eliminated_candidate_index - 1] += candidates[eliminated_candidate_index]
    else: 
      lost_voters += candidates[eliminated_candidate_index]

    candidates.pop(eliminated_candidate_index)
    return candidate_votes, lost_voters

def polarized_perform_instant_runoff(candidates, rounding_decimalplace=6):
    lost_voters = 0
    eliminated_candidate_index = -1
    election_round = 1
    candidate_votes, lost_voters = polarized_count_candidate_votes(-1, candidates)

    while len(candidates) > 1:
      candidate_votes = [
        round(votes, rounding_decimalplace) for votes in candidate_votes
      ]
      sorted = np.argsort(candidate_votes)
      if len(sorted) > 1 and sorted[0] == sorted[1]:
        print('there was a tie')
        return 1
      else: 
        eliminated_candidate_index = sorted[0]
      candidate_votes, lost_voters = polarized_count_candidate_votes(eliminated_candidate_index, candidates, candidate_votes, lost_voters)
      election_round += 1 # increment by 1
    return


# TODO: Auto win for >.5 vote
def perform_instant_runoff(candidates, rounding_decimalplace = 6):
  print('Candidates:')
  print(candidates)
  print()

  election_round = 1
  while len(candidates) > 1:
    candidate_votes = count_candidate_votes(candidates)
    print('Election round', election_round, 'results:')
    candidate_votes = [
      round(votes, rounding_decimalplace) for votes in candidate_votes
    ]
    print(candidate_votes)

    eliminated_candidate = min(range(len(candidate_votes)),
                               key=candidate_votes.__getitem__)

    tied = Counter(candidate_votes)[min(candidate_votes)] != 1
    # print(Counter(candidate_votes))
    if tied:
      print('There was a tie don\'t consider this')
      return None

    print('Eliminated:', candidates[eliminated_candidate])

    candidates.pop(eliminated_candidate)
    print('New list:', candidates)

    election_round += 1

  print()
  print('Winner:', candidates[0])