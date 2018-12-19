import numpy as np

text_file = '''C:/Users/Davinder/PycharmProjects/adventofcode2018/day3input.txt'''

with open(text_file, 'r') as f:
    data = [str(line.strip()) for line in f]

# first parse the inputs row by row into distleft, left etc
def parse_claims(x):
    claim, _, coord, size = x.split(' ')
    fromleft, fromtop = map(int, coord[:-1].split(','))
    distleft, disttop = map(int, size.split('x'))
    return claim, fromleft, fromtop, distleft, disttop


size = 1000

# then set up a numpy array of zeros
def overlap_inches(x):
    grid = np.zeros((size, size))
    for claim in x:
        claimid, fromleft, fromtop, distleft, disttop = parse_claims(claim)
        grid[fromleft:fromleft + distleft, fromtop:fromtop + disttop] += 1
    return np.size(np.where(grid > 1)[0]), np.sum(np.where(grid > 1, 1, 0))


def unique_claim(x):
    grid = np.zeros((size, size))
    for claim in x:
        claimid, fromleft, fromtop, distleft, disttop = parse_claims(claim)
        grid[fromleft:fromleft + distleft, fromtop:fromtop + disttop] += 1
    for claim in x:
        claimid, fromleft, fromtop, distleft, disttop = parse_claims(claim)
        # or if np.all(grid[fromleft:fromleft + distleft, fromtop:fromtop + disttop] == 1)
        if grid[fromleft:fromleft + distleft, fromtop:fromtop + disttop].max() == 1:
            return claimid
