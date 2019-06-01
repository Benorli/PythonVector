import vector as v

t1 = v.Vector((8.218, -9.341))
t2 = v.Vector((-1.129, 2.111))
t3 = v.Vector((7.119, 8.215))
t4 = v.Vector((-8.223, 0.878))
t5 = v.Vector((1.671, -1.012, -0.318))

print(t1 + t2)
print(t3 - t4)
print(t5.scalar_multiply(7.41))