hrs=input("Enter hours")
h=float(hrs)
rat=input("Enter pay rate")
r=float(rat)
def computepay(h1, r1) :
    if h1<=40:
        pay=h1*r1
        return pay
    pay=(40*r1+(h1-40)*1.5*r1)
    return pay
p=computepay(h, r)
print("Pay",p)
quit()
