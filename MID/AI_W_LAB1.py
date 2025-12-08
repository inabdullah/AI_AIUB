temp=int(input("Enter Temp :"))
if temp>25:
    print("Wear light clothes")
elif 15<=temp<=25:
    print("Wear normal clothes")
else:
    print("Wear Warm clothes")
print(type(temp))
