s = input()
def greetings(s):
    name = s.split()
    g = name[0]
    h = name[1]
    s = 'Доброго времени суток, {} "Человек" {}!'.format(g,h)
    return s
print(greetings(s))

