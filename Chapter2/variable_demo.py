print("*** Program 2-7 ***")
room = 503
print("I am staying in room number " + str(room))

print("I am staying in room number", end=" ")
print(room)

print("I am staying in room number", room)

print("*** Program 2-8 ***")
topSpeed = 160
distance = 300
print("The top speed is " + str(topSpeed))
print("The distance traveled is " + str(distance))

print("*** Program 2-10 ***")
dollars = 2.749
print("I have " + str(dollars) + " in my account.")
print("I have " + format(dollars, ".2f") + " in my account.")
print("I have " + format(dollars, ".0f") + " in my account.")
print("I have " + str(int(dollars)) + " in my account.")

dollars = 99.95
print("But now I have " + str(dollars) + " in my account!")

print(type("Hello")) #str
print(type(503)) # int
print(type(2.75)) # float
print(type(True)) # bool

print("*** SWAP VARIABLES ***")
breakfast = "omelette"
lunch = "pork tenderloin"
# temp = breakfast
# breakfast = lunch
# lunch = temp
breakfast, lunch = lunch, breakfast
print("I ate a(n) " + breakfast + " for breakfast.")
print("I ate a(n) " + lunch + " for lunch")