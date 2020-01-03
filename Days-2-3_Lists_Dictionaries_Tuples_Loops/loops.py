## FOR LOOP
bag = [10,213,113,23,5,10,4,10,32,253]
print("Length of bag list: {}".format(len(bag)))

print("Items of bag list:")
for item in bag:
    print(item)

i = 0
print("Iterations in bag list:")
for item in bag:
    i = i + 1
    print(i)

print("Looking for 10 in bag list:")
for item in bag:
    if item == 10:
        print("I found a item: {}".format(item))

## WHILE LOOP
i = 1
while i < 11:
    print("yup")
    i += 1
