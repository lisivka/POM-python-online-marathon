"""
The string defining the points of the quadrilateral has the next form: "#LB1:1#RB4:1#LT1:3#RT4:3"

 LB - Left Bottom point
 LT - Left Top point
 RT - Right Top point
 RB - Right Bottom point
numbers after letters are the coordinates of a point.
Write a function figure_perimetr() that calculates the perimeter of a quadrilateral

The formula for calculating the distance between points:
sqrt(x2-x1)**2+(y2-y1)2


For example:

Test	Result
test1 = "#LB1:1#RB4:1#LT1:3#RT4:3"
print(figure_perimetr(test1))
10.0
test2 = "#LB0:1#RB5:1#LT4:5#RT8:3"
print(figure_perimetr(test2))
18.73454147995595
"""

def figure_perimetr(p: str):
    def distance(a: list, b: list):
        length = ((int(a[0]) - int(b[0])) ** 2 + (int(a[1]) - int(b[1])) ** 2) ** 0.5
        return length

    points = {}
    for i in p.split("#")[1:]:
        points[i[:2]] = i[2:].split(":")  # >>>{'LB':['1','1'],'RB': ['4','1'],'LT': ['1','3'],'RT':['4','3']}

    # print(points)
    perimetr = distance(points['LB'], points['LT'])
    perimetr += distance(points['RB'], points['RT'])
    perimetr += distance(points['LB'], points['RB'])
    perimetr += distance(points['LT'], points['RT'])

    return perimetr  # "{:.2f}".format(perimetr)


test1 = "#LB1:1#RB4:1#LT1:3#RT4:3"
print(figure_perimetr(test1))  # 10.0

test2 = "#LB0:1#RB5:1#LT4:5#RT8:3"
print(figure_perimetr(test2))  # 18.73454147995595

# print(distance([0, 0], [3, 4]))
