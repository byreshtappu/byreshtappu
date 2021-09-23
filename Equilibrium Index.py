a = [3,-2,4,4,6,0,0,17,0,-1,-1]
i = 0
rsum = sum(a)
lsum = 0
while lsum <= rsum:
    lsum += a[i]
    rsum -= a[i]
    i += 1
    if lsum == rsum:
        print("Mid is {} @ position {}".format(a[i],i))
        break
else:
    print("No mid!")
