a = float(input("Side a = "))
b = float(input("Side b = "))
c = float(input("Side c = "))

if a + b >= c and a + c >= b and b + c >= a:
    print("Triangle existed")
    half_p = (a + b + c) / 2
    square = (half_p * (half_p - a) * (half_p - b) * (half_p - c)) ** 0.5
    print(square)
else:
    print("Triangle NOT existed")
