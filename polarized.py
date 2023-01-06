from collections import Counter
from tools import *
import numpy as np


def polarized_count_candidate_votes(eliminated_candidate_index, candidates, candidate_votes=None, lost_voters=0):
    if not candidate_votes:
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

    elif eliminated_candidate_index > 0:
        candidate_votes[eliminated_candidate_index -
                   1] += candidates[eliminated_candidate_index]
        candidates.pop(eliminated_candidate_index)
        candidate_votes.pop(eliminated_candidate_index)
    else:
        lost_voters += candidate_votes[eliminated_candidate_index]
        candidates.pop(eliminated_candidate_index)
        candidate_votes.pop(eliminated_candidate_index)

    return candidate_votes, candidates, lost_voters


def polarized_perform_instant_runoff(candidates, rounding_decimalplace=6):
    lost_voters = 0
    eliminated_candidate_index = -1
    election_round = 0

    # get initial voter distribution
    candidate_votes, candidates, lost_voters = polarized_count_candidate_votes(
        -1, candidates)

    while len(candidates) > 1:
        print()
        candidate_votes = [
            round(votes, rounding_decimalplace) for votes in candidate_votes
        ]
        # check for ties
        sorted = np.argsort(candidate_votes)

        if len(sorted) > 1 and candidate_votes[sorted[0]] == candidate_votes[sorted[1]]:
            print('There is a tie.')
            return 1
        else:
            eliminated_candidate_index = sorted[0]
            print('Eliminated:', candidates[eliminated_candidate_index])

        candidate_votes, candidates, lost_voters = polarized_count_candidate_votes(
            eliminated_candidate_index, candidates, candidate_votes, lost_voters)

        lost_voters = round(lost_voters, rounding_decimalplace)
        print('Election round', election_round, ' results: ', candidates)
        print('New list:', candidates)
        print('Voters lost:', lost_voters)
        
        election_round += 1  # increment by 1
    print()
    print('Winner:', candidates[0])
    return


if __name__ == '__main__':
    candidates = intake()
    polarized_perform_instant_runoff(candidates)