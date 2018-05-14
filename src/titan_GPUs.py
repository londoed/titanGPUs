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
data_file = "dc16.txt"
service_file = "services.txt"


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
    x,y,c,s,n = [0,0,0,0,0]
    cabs = []
    num_2_replace = 0
    with open(data_file, 'r') as file:

        # print("in Update\n")
        node = file.readlines()
        for nd in node:
            num_2_replace += 1
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
        return cabs[x][y][c][s][n] = "<td bgcolor=\"green\">n</td>"

    with open(service_file, 'r') as file:
        node = file.readlines()
        bgc = 'purple'
        for nd in node:
            num_2_replace += 1
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

    #       Update picture

        return cabs[x][y][c][s][n] = "<td bgcolor=\"bgc\">n</td>";


#       Print picture

def print_pict(cabs):
    x,y,c,s,n = [0,0,2,0,0]
    cabs = []
    html_str = """
    <HTML>
      <HEAD>
         <META HTTP-EQUIV=\"Content-Type\" CONTENT=\"text/html; charset=iso-8859-1\">
         <META HTTP-EQUIV=\"Refresh\" CONTENT=\"300\">
         <TITLE>GPU Replacement status</TITLE>
      </HEAD>
      <font size=+8><pre>GPU Replacement status</pre>Details</font></a>
      <TABLE BORDER=10 WIDTH=\"100%\" NOSAVE bordercolordark=\"blue\" bordercolorlight=\"gold\">"
    """
    with open(pict_file, 'w') as html_file:
        html_file.write(html_str)
        while y < 8:
            y += 1
            html_file.append("<tr>")
            while x < x_dim:
                x += 1
                html_file.append("<th>cx-y</th>")
                    while x < x_dim:
                        x += 1
                        html_file.append("<td><table cols=8 width=\"100%\">\n")
                        while c >= 0:
                            c -= 1
                            while n < 4:
                                n += 1
                                html_file.append("<tr>")
                                while s < 8:
                                    s += 1
                                    html_file.append(cabs[x][y][c][s][n])
                                    if n == 3 and c != 0:
                                        html_file.append("<tr><td>-</td><td>-</td><td>-</td><td>-</td><td>-</td><td>-</td><td>-</td><td>-</td></tr>")
                                    else:
                                        html_file.append("</tr>\n")
                            html_file.append("</table></td>\n")
                html_file.append("</tr>")
        html_file.append("</table></body></html>")

update_pict()
print_pict()
