text_file = '''C:/Users/Davinder/PycharmProjects/adventofcode2018/day5input.txt'''

s = open(text_file, 'r').read().strip()


def is_opp(a, b):
    return a.lower() == b.lower() and ((a.isupper() and b.islower()) or (a.islower() and b.isupper()))

# def reduction(line):

def react(line):
    reduced_list = []
    for i in line:
        if len(reduced_list) > 0 and is_opp(i, reduced_list[-1]):
            reduced_list.pop()
        else:
            reduced_list.append(i)
    return len(reduced_list)

x = 'dabAcCaCBAcCcaDA'

x_unique = set(s.lower())

def min_react(line):
    results = []
    for i in x_unique:
        results.append(react(line.replace(i, '').replace(i.upper(), '')))
    return min(results)

# or as a list comprehension
# min([react(s.replace(i, '').replace(i.upper(), '')) for i in x_unique])

