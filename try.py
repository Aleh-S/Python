d = {'b': 'da'}

def par(d):
    l = ['a', 'b', 'c', 'd', 'e']
    l2 = []
    for i in l:
        l2.append(d.get(i, "def val"))

    print(l2)
par(d)