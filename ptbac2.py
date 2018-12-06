import math
print("Giai phuong trinh bac hai")
print "Moi nhap a: "
a = float(input())
print "Moi nhap so b: "
b = float(input())
print "Moi nhap so c: "
c = float(input())
d = b*b - 4*a*c
if d < 0:
    print "Vo nghiem"
elif d == 0:
    print "Nghiem kep x1 = x2 = %3.2f" % (-b/2*a)
else:
    x1 = (-b + math.sqrt(d))/(2*a)
    x2 = (-b - math.sqrt(d))/(2*a)
    print "Hai nghiem rieng biet x1 = %3.2f va x2 = %3.2f " % (x1, x2)
