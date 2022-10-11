hrs = input('Enter hours:')
h = float(hrs)
rate = input('Enter Rate:')
r = float(rate)

def computepay(h, r):
    if h <=40 :
        salary = h * r
        return(salary)
    else :
        overtime = h - 40
        regulartime = 40
        OTrate = r * 1.5
        Extsalary = regulartime * r + overtime * OTrate
        return(Extsalary)

p = computepay(h,r)
print("Pay", p)
