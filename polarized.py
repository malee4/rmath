from collections import Counter
from tools import *

def polarized_count_candidate_votes(eliminated_candidate, candidates, lost_voters, most_liberal = False):
    if not most_liberal:
        index = eliminated_candidate - 1
        candidates[index] += candidates[eliminated_candidate]
    else:
        lost_voters += candidates[eliminated_candidate]

    candidates.pop(eliminated_candidate)
    return candidates

def polarized_perform_instant_runoff(candidates, rounding_decimalplace = 6):
    lost_voters = 0 # voters who end up not voting in the election because their candidate has been eliminated, and all other candidates are more conservative
    

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