import vector as v

q1 = v.Vector((-0.221, 7.437))
q2 = v.Vector((8.813, -1.331, -6.247))
q3 = v.Vector((5.581, -2.136))
q4 = v.Vector((1.996, 3.108, -4.554))

q_list = [q1, q2, q3, q4]

for x in q_list:
    print(x.get_magnitude())
    print(x.normalize())