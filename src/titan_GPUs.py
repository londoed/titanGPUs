#!/user/Desktop/Scripts/Python
#
#       Python 3 script to monitor memory, health, and heartbeat errors on a
#       Cray XK7 system.
#       The script runs on the smw atached to the XK7 and monitors the
#       eventlog file for occurrences of these errors
#
#       An occurence is evaluated and entered into one of five tables. An
#       uncorrectable memory error table, a correctable memory error table,
#       a health fault table.
#
#       The table is then formatted into an html file for display by a
#       web browser.
#
#
#       Red: A multiple occurence of an uncorrectable error
#       Yellow: A single occurrence of an uncorrectable error
#
#####################

#       Include modules


import numpy as np

#       Configuration variables

x_dim = 25 # Number of columns of system (Titan has 25, 0-24)
y_dim = 8 # Number of rows in system (Titan has 8, 0-7)
cabs = []

#       Define file locations

pict_file = "dc16.html"


#       Initialize cabinets


x,y,c,s,n = [0,0,0,0,0] # (x,y) = cabinet position, c = cage, s = slot, n = node


while x < x_dim:
    x += 1
    while y < y_dim:
        y += 1
        while c < 3:
            c += 1
            while s < 8:
                s += 1
                while n < 4:
                    n += 1
                    cabs[x][y][c][s][n] = "<td>n</td>"

#       Update picture

def update_pict(cabs):
    num_2_replace = 0
    file1 = open("dc16.txt", 'r')
    # print("in Update\n")
    node = file1.readlines()
    for i in node:
        num_2_replace += 1
        nd = i
        if nd[2] == '-':
            x = nd[1],
            y = nd[3],
            c = nd[5],
            s = nd[7],
            n = nd[9],
        else:
            x = 1 * nd[1] + nd[2],
            y = nd[4],
            c = nd[6],
            s = nd[8],
            n = nd[10],

#       Print cabs
print(cabs[x][y][c][s][n])
cabs[x][y][c][s][n] = "<td bgcolor=\"red\">$n</td>"
file1.close()

file2 = open("service.txt", 'r')
while True:
    node = list(file2.readlines())
    l = node.split(/ /)
    bgc = 'purple'

#       Update picture

nd = l[0].split(//)
if nd[2] == '-':
    x = nd[1],
    y = nd[3],
    c = nd[5],
    s = nd[7],
    n = nd[9],
else:
    x = 10 * nd[1] + nd[2],
    y = nd[4],
    c = nd[6],
    s = nd[8],
    n = nd[10],

cabs[x][y][c][s][n] = "<td bgcolor=\"bgc\">n</td>";
file2.close()

file1 = open("dc16.txt", 'r')
#       Print cabs
while True:
    num_2_replace += 1
    nd = list(file1.readlines())
    if nd[2] == '-':
        x = nd[1],
        y = nd[3],
        c = nd[5],
        s = nd[7],
        n = nd[9],
    else:
        x = 10 * nd[1] + nd[2],
        y = nd[4],
        c = nd[6],
        s = nd[8],
        n = nd[10],
    if not nd:
        break

#       Update picture


#       Print cabs
cabs[x][y][c][s][n] = "<td bgcolor=\"green\">n</td>"
file1.close()

#       Print picture

def print_pict(cabs):
    num_todo = num_2_replace - num_completed
    print("In Print\n")


#
