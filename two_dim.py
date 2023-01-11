from scipy.integrate import quad
import numpy as np
from voronoi import find_all_areas  # (points)
from collections import Counter

# NOTE: THIS METHOD RETURNS UNSORTED CANDIDATES
def m_dimension_intake():
  try:
    dim = float(input("Input dimensions: "))
  except ValueError:
    print("Input valid dimensions.")
    exit()

  end_intake = False

  candidates = []

  while end_intake == False:
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

def two_dim_perform_instant_runoff(points):
  count = 1
  while len(points) > 1:
    # find areas of new set of points
    areas = find_all_areas(points, graph = True, round = count)
    print('Points: ', points)
    print('Areas: ', areas)
    
    eliminated_candidate_index = min(range(len(areas)),
                               key=areas.__getitem__)

    tied = Counter(areas)[min(areas)] != 1
    
    if tied:
      print('Tie.')
      return 1
    
    points.pop(eliminated_candidate_index)
    areas.pop(eliminated_candidate_index)

    print(eliminated_candidate_index, ' removed')
    count += 1

  print('Winner: ', points[0])
  return





if __name__ == '__main__':
  candidates = m_dimension_intake()
  two_dim_perform_instant_runoff(candidates)
