text_file = '''C:/Users/Davinder/PycharmProjects/adventofcode2018/day2input.txt'''

with open(text_file, 'r') as f:
    data = [str(line.strip()) for line in f]


# func to decompose ids into dic of key letter and count letter
def to_dict(x):
    d = {}
    for i in list(x):
        if i in d:
            d[i] += 1
        else:
            d[i] = 1
    return d


# looping through dictionary to flag 2's and 3's
def two_three_detector(x):
    two = 0
    three = 0
    for k in x:
        if x[k] == 2:
            two = 1
        elif x[k] == 3:
            three = 1
    return two, three


def return_checksum():
    twos = 0
    threes = 0
    for i in data:
        twos += two_three_detector(to_dict(i))[0]
        threes += two_three_detector(to_dict(i))[1]
    print twos * threes


# to find count of differences between two string inputs
def differences(x, y):
    diffs = 0
    for i in range(26):
        if not x[i] == y[i]:
            diffs += 1
    return diffs


# comparison loop comparing one to another only once using indexing
def find_match():
    for i in range(len(data)):
        for j in range(i + 1, len(data)):
            if differences(data[i], data[j]) == 1:
                return data[i], data[j]


print find_match()







