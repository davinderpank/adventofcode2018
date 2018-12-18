text_file = '''C:/Users/Davinder/PycharmProjects/adventofcode2018/day1input.txt'''

with open(text_file, 'r') as f:
    x = [int(line.strip()) for line in f]

# Day 1
# Part 1
def final_freq():
    counter = 0
    for i in x:
        counter += int(i)
    print counter
print sum(x)


# Part 2
def duplicate_freq():
    running_total = 0
    condition = True
    a = set()

    while condition:
        for i in x:
            running_total += i
            print running_total
            if running_total in a:
                condition = False
                print 'Duplicate is' + ' ' + str(running_total)
                break
            else:
                a.add(running_total)