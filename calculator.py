#!/usr/bin/env python3
import sys

# do something in ValueError
try:
    salary = int(sys.argv[1])
    cash = salary - 3500
    if cash <= 0:
        tax = cash * 0.00 - 0
        print("%.2f" % tax)
    elif cash > 0 and cash <= 1500:
        tax = cash * 0.03 - 0
        print("%.2f" % tax)
    elif cash > 1500 and cash <= 4500:
        tax = cash * 0.1 - 105
        print("%.2f" % tax)
    elif cash > 4500 and cash <= 9000:
        tax = cash * 0.2 - 555
        print("%.2f" % tax)
    elif cash > 9000 and cash < 35000:
        tax = cash * 0.25 - 1005
        print("%.2f" % tax)
    elif cash > 35000 and cash < 55000:
        tax = cash * 0.3 - 2755 
        print("%.2f" % tax)
    elif cash > 55000 and cash < 80000:
        tax = cash * 0.35 - 5505
        print("%.2f" % tax)
    elif cash > 8000:
        tax = cash * 0.45 - 13505
        print("%.2f" % tax)
except ValueError:
    print("Parameter Error")
    exit()
