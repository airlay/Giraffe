def say_hi(name, age):

    print("hi " + name + "!")
    print("you are " + age)


def cube(num):
    return num*num*num

monthConversions ={
    "Jan" : "January",
    "Feb" : "Febuary"
}

print(monthConversions.get("Febsdf", "Not a valid key"))



word = "airlay"
guess = ""
guess_count = 0
guess_limit = 3
out_of_guess = False

while guess != word and not (out_of_guess):
    if guess_count < guess_limit:
        #guess = input("Enter guess: ")
        guess_count += 1
    else:
        out_of_guess = True
if out_of_guess:
    print("Out of guess.  YOU LOSE")
else:
    print("You win!")

for b in range(3):
    print(b)


def translate(phrase):
    translation = ""
    for letter in phrase:
        if letter in "AEIOUaeiou":
            translation = translation + "g"

        else:
            translation = translation + letter

    return translation

print(translate("asdfi"))

try:
    number = input("enter a number :")
    print (number)
except ZeroDivisionError:
    print("Divided by zero, you dumb?")
except ValueError:
    print("input error")

