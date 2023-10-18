from scipy.spatial import Voronoi, ConvexHull, convex_hull_plot_2d
import matplotlib.pyplot as plot
import numpy as np
from plotutils import voronoi_plot_2d


def flip(points):
  out = []
  # reflect across x = 0
  for p in points:
    if len(p) != 2:
      return
    out.append(p)
    out.append([-p[0], p[1]])
    out.append([2 - p[0], p[1]])
    out.append([p[0], -p[1]])
    out.append([p[0], 2 - p[1]])
  return out


# find the area of the given set of vertices
def find_area(point_order, vertices):
  points = []
  for i in point_order:
    points.append(vertices[i])
  hull = ConvexHull(points)
  # plt = convex_hull_plot_2d(hull)
  # plt.show()
  return hull.volume


def find_all_areas(points, graph=False, round=1, round_decimal=6):
  flipped = flip(points)  # create symmetry around bounds
  vor = Voronoi(flipped)

  # print(vor.regions)
  # print(vor.point_region)
  # print(vor.vertices)

  areas = []

  # sort the regions based on corresponding point index
  sorted_regions = []
  for i in vor.point_region:
    sorted_regions.append(vor.regions[i])

  # find the area
  for i in range(len(points)):
    friend = i * 5
    ar = find_area(sorted_regions[friend], vor.vertices)
    # print('found area ', ar)
    # print(type(round_decimal))
    areas.append(ar)

  if graph:
    plt = voronoi_plot_2d(vor)
    plt.savefig('voronoi' + str(round) + '.png')

  return areas


if __name__ == '__main__':
  points = np.array([[.2, .5], [.6, .1], [.8, .2]])
  areas = find_all_areas(points, graph=True)
  print('points: ', points)
  print('areas: ', areas)

  # # plt = voronoi_plot_2d(vor)
  # plt.savefig('voronoi.png')
