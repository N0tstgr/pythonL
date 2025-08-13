f = open("poems.txt", "r")
data = f.read()
if("twinkle" in data):
    print("Twinkle is present in the data")
else:
    print("Twinkle is not present in the data")

# print(data)
f.close()