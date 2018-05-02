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

from time import localtime

#       Configuration variables

x_dim = 25
y_dim = 8

#       Define file locations

pict_file = "dc16.html"

update_pict()
print_pict()

#       Initialize cabinets


x,y,c,s,n = [0,0,0,0,0]


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
                    [x][y][c][s][n] = "<td>n</td>"

#       Update picture

def update_pict():
    num_2_replace = 0
    file1 = open("dc16.txt", 'r')
    file1.read()
    print("in Update\n")
    while file1.read():
        num_2_replace += 1
        node = None
    nd = node.split(//)
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

#       Print cabs

[x][y][c][s][n] = "<td bgcolor=\"red\">$n</td>"
file1.close()

file2 = open("service", 'd')
file2.read()
while file2.read():
    l = None.split(/ /)
    bgc = 'purple'
    node = None

#       Update picture

nd = l[1].split(//)
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

[x][y][c][s][n] = "<td bgcolor=\"$bgc\">$n</td>";
file2.close()

#       Print cabs


#       Update picture


#       Print cabs


#       Print picture

def print_pict():
    num_todo = num_2_replace - num_completed
    print("In Print\n")


#