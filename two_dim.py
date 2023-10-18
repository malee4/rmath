from scipy.integrate import quad
import numpy as np
from voronoi import find_all_areas  # (points)
from collections import Counter
import matplotlib.pyplot as plt

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
      return tied
    
    points.pop(eliminated_candidate_index)
    areas.pop(eliminated_candidate_index)

    print(eliminated_candidate_index, ' removed')
    count += 1

  print('Winner: ', points[0])
  return

def two_dim_pir_func(points):
  count = 1
  while len(points) > 1:
    # find areas of new set of points
    areas = find_all_areas(points, graph = False, round = count)
    #print('Points: ', points)
    #print('Areas: ', areas)
    
    eliminated_candidate_index = min(range(len(areas)),
                               key=areas.__getitem__)

    tied = Counter(areas)[min(areas)] != 1
    
    if tied:
      #print('Tie.')
      return 
    
    points.pop(eliminated_candidate_index)
    areas.pop(eliminated_candidate_index)

    #print(eliminated_candidate_index, ' removed')
    count += 1

  #print('Winner: ', points[0])
  return points[0]

# graph the possible placements for two issues, one existing candidate
def twod_single_candidate():
      iter = 1000
      existing_candidate = [.4, .3]
      x = []
      y = []

      for i in range(1, iter):
            for j in range(1, iter):
                  xp = i * (1 / iter)
                  yp = j * (1 / iter)
                  new_candidate = [xp, yp]
                  points = [existing_candidate, new_candidate]
                  winner = two_dim_pir_func(points) # if none, then tied
                  if winner == new_candidate:
                        x.append(xp)
                        y.append(yp)

      plt.scatter(x, y)
      plt.xlabel('Issue 1')
      plt.ylabel('Issue 2')
      plt.title('Given existing candidate (0.4, 0.3), valid area for X to be placed to win')
      plt.show()
      return

if __name__ == '__main__':
  #candidates = m_dimension_intake()
  # two_dim_perform_instant_runoff(candidates)
  twod_single_candidate()
