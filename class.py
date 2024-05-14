class Circle():
    radius = 0
    x =0
    y =0
    color = ""
    filled = False

c1 = Circle()

c1.radius = 6.2
c1.x = 150
c1.y = 290
c1.color = "RED"
c1.filled = True

c2 = Circle()

c2.radius = 7.2
c2.x = 190
c2.y = 360
c2.color = "GREEN"
c2.filled = False

Circles = [c1, c2]

print(Circles[1].radius)