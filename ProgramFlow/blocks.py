# for i in range(1 , 13):
#     print("No. {:2} squared is  {:3} and cubed is {}".format(i, i ** 2, i ** 3))
#     print("*" * 80)

#------------------------------------------------------------------------------------------
name = input("Please enter your name: ")
age = int(input("How old are you , {0}? ".format(name)))
print(age)
# if age >= 18 :
#     print("You are old enough to vote")
#     print("Please put an X in the box")
# else:
#     print("Please come back in {0} years".format(18 - age))
if age < 18 :
    print("Please come back in {0} years".format(18 - age))
elif age == 900 :
    print("Sorry, you die in return of Jedi")
else:
    print("You are old enough to vote")
    print("Please put an X in the box")
#------------------------------------------------------------------------------------
# a=10
# print(format(a,'b'))
# print(bin(a))
