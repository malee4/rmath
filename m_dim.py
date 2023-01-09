from main import count_candidate_votes
from scipy.integrate import quad
import numpy as np


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


def find_slope(x1, y1, x2, y2):
  if y1 == y2:
    return
  m = -(x2 - x1) / (y2 - y1)
  return m


def find_constant(x1, y1, x2, y2):
  if y1 == y2:
    return
  C = ((y2**2 - y1**2) + (x2**2 - x1**2) / (2 * (y2 - y1)))
  return C


  # this method is for calculating area in two dimensions only
def two_candidate_area(candidates):
  # sort the candidates based on their x-values
  if candidates[1][0] < candidates[0][0]:
    temp = candidates[1][0]
    candidates[1][0] = candidates[0][0]
    candidates[0][0] = temp

  if len(candidates) == 1:
    return [1]
  elif len(candidates) <= 0:
    return []
  elif len(candidates[0]) != 2:
    print("Improper dimensions")

  candidate_votes = []

  m = find_slope(candidates[0][0], candidates[0][1], candidates[1][0],
                 candidates[1][1])
  C = find_constant(candidates[0][0], candidates[0][1], candidates[1][0],
                    candidates[1][1])

  xA = (1 - C) / m
  xC = -C / m
  yB = m + C

  # account for cases where they are equal
  if not m or not C:  # in the case of a vertical dividing line
    candidate_votes.append(xA)
    candidate_votes.append(1 - xA)
  else:
    # re-sort the candidates based on their y-values
    if candidates[1][1] < candidates[0][1]:
      temp = candidates[1][1]
      candidates[1][1] = candidates[0][1]
      candidates[0][1] = temp

    def f(x):
      return m * x + C

    if xA < 0:
      if yB <= 1 and yB >= 0:
        area, err = quad(f, 0, 1)
        candidate_votes.append(area)
        candidate_votes.append(1 - area)
      else:
        print("Error has been reached in the logic.")
    elif xA <= 1:
      if yB < 0:
        area = xA + quad(f, xA, xC)
        candidate_votes.append(area)
        candidate_votes.append(1 - area)
      elif y <= 1:
        area = xA + quad(f, xA, 1)
        candidate_votes.append(area)
        candidate_votes.append(1 - area)
      else:
        area = quad(f, 0, xA) + (1 - xA)
        candidate_votes.append(area)
        candidate_votes.append(1 - area)
    elif x > 1:
      if yB <= 1 and yB >= 0:
        area = quad(f, xC, 1)
        candidate_votes.append(area)
        candidate_votes.append(1 - area)
      else:
        print("Error has been reached in the logic, 2")

  return candidate_votes


def two_count_candidate_votes(elim_index, candidates, candidate_votes=None):

  if len(candidates) == 2:
    two_candidate_area()
  else:
    print('sorry')
    return

  return candidate_votes


def two_perform_instant_runoff(candidates):
  dim = 2
  elim_index = -1
  if len(candidates) <= 0:
    print('No candidates entered.')
    return
  elif len(candidates) == 1:
    print('Winner: ', candidates[0])

  candidate_votes = two_count_candidate_votes(elim_index, candidates)

  # because this is two people, we can determine who won
  ...

  return


if __name__ == '__main__':
  candidates = m_dimension_intake()
  two_perform_instant_runoff(candidates)
