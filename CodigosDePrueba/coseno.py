import math

p1 = [0.5,0.4]
p2 = [0.5,0.3]
p3 = [0.3,0.3]

c = math.sqrt(((p1[0]-p2[0])**2)+((p1[1]-p2[1])**2))##p1 a p2
b = math.sqrt(((p1[0]-p3[0])**2)+((p1[1]-p3[1])**2))##p1 a p3
a = math.sqrt(((p2[0]-p3[0])**2)+((p2[1]-p3[1])**2))##p2 a p3

print(f"p1 a p2: {c}\np1 a p3: {b}\np2 a p3: {a}")

B = math.acos(((b**2)-(a**2)-(c**2))/(-2*a*c))
print(B)
B = B * (180/math.pi)
print(B)