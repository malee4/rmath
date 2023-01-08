from collections import Counter
import numpy as np
from tools import intake, count_candidate_votes

def loss_count_candidate_votes(eliminated_candidate_index, candidates, candidate_votes = None, lost_voters = 0, loss = 0.01):
    if not candidate_votes:
        # create empty list to store votes
        candidate_votes = list()

        for i in range(len(candidates)):
            votes = 0

            if i == 0: 
                votes += i
            else:
                votes += (candidates[i] - candidates[i-1]) / 2.0

            if i == (len(candidates) - 1):
                votes += 1.0 - candidates[i]
            else:
                votes += (candidates[i+1] - candidates[i]) / 2.0

            candidate_votes.append(votes) # add it on!

        return candidate_votes, candidates, lost_voters
    else:
        # under
        if eliminated_candidate_index == 0:
            candidate_votes[eliminated_candidate_index + 1] += (1.0 - loss) * candidates[eliminated_candidate_index]
        else:
            candidate_votes[eliminated_candidate_index - 1] += (1.0 - loss) * ((candidates[eliminated_candidate_index] - candidates[eliminated_candidate_index - 1]) / 2)
        # over
        if eliminated_candidate_index == len(candidates) - 1:
            candidate_votes[eliminated_candidate_index - 1] += (1.0 - loss) * (1 - candidates[eliminated_candidate_index])
        else:
            candidate_votes[eliminated_candidate_index + 1] += (1.0 - loss) * ((candidates[eliminated_candidate_index + 1] - candidates[eliminated_candidate_index]) / 2)
        
    candidates.pop(eliminated_candidate_index)
    candidate_votes.pop(eliminated_candidate_index)

    return candidate_votes, candidates, lost_voters

def loss_perform_instant_runoff(candidates, loss = 0.01, rounding_decimalplace = 6):
    if len(candidates) == 1:
        return
    election_round = 1
    lost_voters = 0
    eliminated_candidate_index = -1

    # perform the initial count
    candidate_votes, candidates = loss_count_candidate_votes(eliminated_candidate_index, candidates, None, lost_voters, loss)

    while len(candidates) > 1:
        # round the values
        candidate_votes = [
            round(votes, rounding_decimalplace) for votes in candidate_votes
        ]

        # find the eliminated candidate location
        eliminated_candidate_index = min(range(len(candidate_votes)),
                               key=candidate_votes.__getitem__)

        tied = Counter(candidate_votes)[min(candidate_votes)] != 1
        if tied:
            print("There was a tie!")
            return 1

        # calculate the votes
        candidate_votes, candidates, lost_voters = loss_count_candidate_votes(eliminated_candidate_index, candidates, candidate_votes, lost_voters)

        lost_voters = round(lost_voters, rounding_decimalplace)
        # print out the results
        print('Election round', election_round, ' results: ', candidates)
        print('New list:', candidates)
        print('Voters lost:', lost_voters)

        election_round += 1

    print()        
    print("Winner: ", candidates[0])
    return 

if __name__ == '__main__':
    candidates = intake()
    loss_perform_instant_runoff(candidates)
    