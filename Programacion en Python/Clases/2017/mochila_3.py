items = [(4, 12),
         (2, 2),
         (2, 1),
         (1, 1),
         (10, 4)
        ]

c = 0
def ks(index, weight):
    global items
    global c
    c += 1
 
    if index >= len(items):
        return 0
 
    item = items[index]
 
    if item[1] > weight:
        return ks(index + 1, weight)
    else:
        return max(ks(index + 1, weight),ks(index + 1, weight - item[1] + item[0]))

print ("Max sum: %d" % (ks(0, 20),))
print ("Iterations %d" % (c,))
