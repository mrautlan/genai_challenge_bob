# grades.py - grade calculator for "Intro to Programming"
# written 2014 by a tutor, last change 2019
# DO NOT TOUCH - it works!!!
#
# usage: python grades.py [file.csv]

import csv, sys

f = "students.csv"
l = []
d = {}
x = 0


def calc(e, a, b):
    # bonus
    if b > 10:
        b = 10
    e = e + b
    t = e * 0.6 + (a / 50 * 100) * 0.4
    t = round(t, 1)
    return t


def g(t, e):
    # check exam
    if e < 50:
        return 5.0
    if t > 95:
        return 1.0
    elif t > 90:
        return 1.3
    elif t > 85:
        return 1.7
    elif t > 80:
        return 2.0
    elif t > 75:
        return 2.3
    elif t > 70:
        return 2.7
    elif t > 65:
        return 3.0
    elif t > 60:
        return 3.3
    elif t > 55:
        return 3.7
    elif t > 50:
        return 4.0
    else:
        return 5.0


def doit(fn):
    global x
    try:
        fh = open(fn)
    except:
        print("file not found")
        return
    r = csv.DictReader(fh)
    for row in r:
        try:
            e = int(row["exam"])
        except:
            e = 0
        try:
            a = int(row["assignments"])
        except:
            a = 0
        try:
            b = int(row["bonus"])
        except:
            b = 0
        t = calc(e, a, b)
        gr = g(t, e)
        l.append([row["name"], row["id"], t, gr])
        d[row["id"]] = gr
        x = x + 1
    fh.close()
    l.sort()
    # print
    print("=" * 50)
    print("RESULTS Intro to Programming")
    print("=" * 50)
    for i in l:
        print(i[0] + " (" + i[1] + "): " + str(i[2]) + " -> " + str(i[3]))
    print("-" * 50)
    s = 0
    p = 0
    for k in d:
        s = s + d[k]
        if d[k] <= 4.0:
            p = p + 1
    print("Students: " + str(x))
    print("Pass rate: " + str(round(p / x * 100, 1)) + "%")
    print("Average grade: " + str(round(s / len(d), 2)))
    # print("Average grade: " + str(s / p))
    bst = None
    for i in l:
        if bst == None or i[3] < bst[3]:
            bst = i
    print("Best student: " + bst[0])


if len(sys.argv) > 1:
    f = sys.argv[1]
doit(f)
