parrot = "Norwegian Blue"
vowels = ['a','e','i','o','u']
count = 0
for character in parrot:
    #print(character)
    if character in vowels:
        count += 1
print("Number of vowels in {0} are {1}".format(parrot,count))
