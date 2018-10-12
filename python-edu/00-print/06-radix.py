#!/usr/bin/python3

a, b, c, d = 16, 27, 38, 49

# multiple values
print("%d" %a, "%x" %b, "%o" %c, "%c" %d)

# single value
print("%d %x %o %c" %(a, b, c, d))


# width.precision
# for f1:  8.5     8 < width(f1)=9, so, 9;   5>4, so 0 is added;
# for f2:  15.2    15 > width(f2), so 15;    2<prec(f2)=6, so shorten
f1=1234.1234
f2=12.123456
print("%8.5f\n%15.2f" %(f1, f2))

print("=====================")

# "-" left-aligned;
print("%8.5f\n%-15.2f" %(f1, f2))


print("#%d #%x #%o #%c" %(a, b, c, d))

