
"""
Before doinh anything need to CLEAR
Delete "Sum.txt" file
Delete the "table.txt" file
if they are there

RUN main for the three positions D1, D2, D3
"""

"""These are the lists containing errors of the respective distances"""
d = []                                      # Contains the Error all errors Developed vs Literature from the file

with open("/Users/SimahoJr/tito/sum.txt") as errors:
    er_ = []
    error = []
    d1 = []
    d3 = []
    d5 = []

    for line in errors:
        error.clear()
        er_ = line.split("_")
        er_[5] = er_[5].strip("\n")

        for i in range(0, len(er_)):
            error.append(float(er_[i]))

        d1.append([error[0], error[1]])           # This contains the literature error, developed error at respective
        d3.append([error[2], error[3]])          # Distances
        d5.append([error[4], error[5]])

        d.append([d1, d3, d5])

"""The values are interpreted as the following
on the list d[x][y][z][u]
x -> is the redundant values, important to keep the structure (it repeats itself three times)
y -> is the position value, there are three positions D1, D2 and D3, hence ranges from 0-2 respective to the data
z -> is the distance used, with the respective position, there are three distances hence the values ranges from 0-2
u -> is the error value recorded, the value can either be of the literature or of the developed algorithm. This value
has two options as it can be the error of the developed or error of the one from the literature.
"""

u = 0   # The algorithm in comparison

avg_D1 = (round(d[0][0][0][u], 3) + round(d[0][0][1][u], 3) + round(d[0][0][2][u], 3))/3
avg_D2 = (round(d[0][1][0][u], 3) + round(d[0][1][1][u], 3) + round(d[0][1][2][u], 3))/3
avg_D3 = (round(d[0][2][0][u], 3) + round(d[0][2][1][u], 3) + round(d[0][2][2][u], 3))/3


"""Now we create the table relative to that of the research"""
print(" ", file=open("table.txt", "a"))
print("        Errors between actual and estimated at a given environment", file=open("table.txt", "a"))
print("="*50, file=open("table.txt", "a"))
print("Position/Distance         1m                  3m                   5m", file=open("table.txt", "a"))
print("D1                       {}              {}                 {}"
      .format(round(d[0][0][0][u], 3), round(d[0][1][0][u], 3), round(d[0][2][0][u], 3)), file=open("table.txt", "a"))
print("D2                       {}              {}                 {}"
      .format(round(d[0][0][1][u], 3), round(d[0][1][1][u], 3), round(d[0][2][1][u], 3)), file=open("table.txt", "a"))
print("D3                       {}              {}                 {}"
      .format(round(d[0][0][2][u], 3), round(d[0][1][2][u], 3), round(d[0][2][2][u], 3)), file=open("table.txt", "a"))
print("Average:                 {}              {}                 {}"
      .format(round(avg_D1, 3), round(avg_D2, 3), round(avg_D3, 3)), file=open("table.txt", "a"))
print("Average Error on this Environment: {}"
      .format((round(avg_D1, 3) + round(avg_D2, 3) + round(avg_D3, 3))/3), file=open("table.txt", "a"))
print("="*50, file=open("table.txt", "a"))

"""the following condes are for the developed algorithm analysis performance"""
print(" ", file=open("table.txt", "a"))
print(" ", file=open("table.txt", "a"))
v = 1       # The developed algorithm

avg_D1_ = (round(d[0][0][0][v], 3) + round(d[0][0][1][v], 3) + round(d[0][0][2][v], 3)) / 3
avg_D2_ = (round(d[0][1][0][v], 3) + round(d[0][1][1][v], 3) + round(d[0][1][2][v], 3)) / 3
avg_D3_ = (round(d[0][2][0][v], 3) + round(d[0][2][1][v], 3) + round(d[0][2][2][v], 3)) / 3


"""Now we create the table relative to that of the research"""
print(" ", file=open("table.txt", "a"))
print("        Errors between actual and estimated at a given environment", file=open("table.txt", "a"))
print("="*50, file=open("table.txt", "a"))
print("Position/Distance         1m                  3m                   5m", file=open("table.txt", "a"))
print("D1                       {}              {}                 {}"
      .format(round(d[0][0][0][v], 3), round(d[0][1][0][v], 3), round(d[0][2][0][v], 3)), file=open("table.txt", "a"))
print("D2                       {}              {}                 {}"
      .format(round(d[0][0][1][v], 3), round(d[0][1][1][v], 3), round(d[0][2][1][v], 3)), file=open("table.txt", "a"))
print("D3                       {}              {}                 {}"
      .format(round(d[0][0][2][v], 3), round(d[0][1][2][v], 3), round(d[0][2][2][v], 3)), file=open("table.txt", "a"))
print("Average:                 {}              {}                 {}"
      .format(round(avg_D1_, 3), round(avg_D2_, 3), round(avg_D3_, 3)), file=open("table.txt", "a"))
print("Average Error on this Environment: {}"
      .format((round(avg_D1_, 3) + round(avg_D2_, 3) + round(avg_D3_, 3)) / 3), file=open("table.txt", "a"))
print("="*50, file=open("table.txt", "a"))






