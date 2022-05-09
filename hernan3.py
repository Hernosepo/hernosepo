#3.1 Write a program to prompt the user for hours and rate per hour using input
#to compute gross pay. Pay the hourly rate for the hours up to 40 and 1.5 times
#the hourly rate for all hours worked above 40 hours. Use 45 hours and a rate of
#10.50 per hour to test the program (the pay should be 498.75). You should use
#input to read a string and float() to convert the string to a number.
#Do not worry about error checking the user input - assume the user types numbers properly.


while True :
    try:
        hrs = input("Enter Hours:")
        h = float(hrs)
        rte = input("Enter Rate:")
        r = float(rte)
        ext = h * r
        old = (h - 40) * (r * 0.5)
        if h > 40 :
            fin = ext + old
    except :
        print('invalid')
        continue
    else:
        if h < 40 :
            mex = 40 - h
            print('te faltaron: ',mex,' para un extra')
        fin = h * r
        if fin == fin :
            print('Su cuenta final es ', fin)
            print('Horas trabajadas: ', h,'Rate calculado: ',r)
            break
