text_file = '''C:/Users/Davinder/PycharmProjects/adventofcode2018/input.txt'''


with open(text_file, 'r') as f:
    x = [int(line.strip()) for line in f]

def final_freq():
    counter = 0
    for i in x:
        counter += int(i)
    print counter

print sum(x)

https://stackoverflow.com/questions/45114203/find-the-first-duplicate-number-for-which-the-second-occurrence-has-the-minimal
