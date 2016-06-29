def computepay(h,r):
    if h > 40:
        hr = h - 40
        return 40*r + hr*r*1.5
    else:
        return h*r


hrs = raw_input("Enter Hours:")
rate = raw_input("Enter Rate:")
hr = float(hrs)
rt = float(rate)
p = computepay(hr, rt)
print "Pay",p