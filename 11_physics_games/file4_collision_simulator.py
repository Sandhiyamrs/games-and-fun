m1, v1 = 2, 5
m2, v2 = 3, -2

v1f = ((m1-m2)/(m1+m2))*v1 + ((2*m2)/(m1+m2))*v2
v2f = ((2*m1)/(m1+m2))*v1 + ((m2-m1)/(m1+m2))*v2

print("Final velocities:", v1f, v2f)
