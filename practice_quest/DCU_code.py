a, b, c = map(int, input("Input 3 integer values>>").split())
if a + b > c and a + c > b and b + c > a:
    print("Yes, this is a triangle.")
else:
    print("No, this is NOT a triangle.")