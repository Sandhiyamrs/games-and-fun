m1, m2 = 2, 3
v1, v2 = 5, -2

v1f = ((m1-m2)/(m1+m2))*v1 + ((2*m2)/(m1+m2))*v2
v2f = ((2*m1)/(m1+m2))*v1 + ((m2-m1)/(m1+m2))*v2

print("After Collision:")
print("Object1 velocity:", v1f)
print("Object2 velocity:", v2f)
