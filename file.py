s = "vedant is a good boi"

# reading a file

with  open("test.txt", "r") as f:
    s = f.read()
    print(s)




#with open("vedant.txt", "w") as f:
    #f.write(s)

# fp = open("test.txt", "w")
# fp.write(s)
# fp.close()


with open("test.txt", "a") as f:
    f.write(" and is very nice")