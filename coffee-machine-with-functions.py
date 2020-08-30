"""
Work on project. Stage 5/6: On a coffee loop
Project: Coffee Machine
Hard 
31 minutes

Description
Just one action is not so interesting, is it? Let's improve the program so it can do multiple actions, one after another. It should repeatedly ask a user what they want to do. If the user types "buy", "fill" or "take", then the program should do exactly the same thing it did in the previous step. However, if the user wants to switch off the coffee machine, they should type "exit". The program should terminate on this command. Also, when the user types "remaining", the program should output all the resources that the coffee machine has.

Objectives
Write a program that will work endlessly to make coffee for all interested persons until the shutdown signal is given. Introduce two new options: "remaining" and "exit".

Do not forget that you can be out of resources for making coffee. If the coffee machine doesn't have enough resources to make coffee, the program should output a message that says it can't make a cup of coffee.

And the last improvement to the program at this step — if the user types "buy" to buy a cup of coffee and then changes his mind, they should be able to type "back" to return into the main cycle.

Example
Your coffee machine should have the the same initial resources as in the example (400 ml of water, 540 ml of milk, 120 g of coffee beans, 9 disposable cups, $550 in cash.

The greater-than symbol followed by space (> ) represents the user input. Notice that it's not the part of the input.

Example 1:

Write action (buy, fill, take, remaining, exit):
> remaining

The coffee machine has:
400 of water
540 of milk
120 of coffee beans
9 of disposable cups
$550 of money

Write action (buy, fill, take, remaining, exit):
> buy

What do you want to buy? 1 - espresso, 2 - latte, 3 - cappuccino, back - to main menu:
> 2
I have enough resources, making you a coffee!

Write action (buy, fill, take, remaining, exit):
> remaining

The coffee machine has:
50 of water
465 of milk
100 of coffee beans
8 of disposable cups
$557 of money

Write action (buy, fill, take, remaining, exit):
> buy

What do you want to buy? 1 - espresso, 2 - latte, 3 - cappuccino, back - to main menu:
> 2
Sorry, not enough water!

Write action (buy, fill, take, remaining, exit):
> fill

Write how many ml of water do you want to add:
> 1000
Write how many ml of milk do you want to add:
> 0
Write how many grams of coffee beans do you want to add:
> 0
Write how many disposable cups of coffee do you want to add:
> 0

Write action (buy, fill, take, remaining, exit):
> remaining

The coffee machine has:
1050 of water
465 of milk
100 of coffee beans
8 of disposable cups
$557 of money

Write action (buy, fill, take, remaining, exit):
> buy

What do you want to buy? 1 - espresso, 2 - latte, 3 - cappuccino, back - to main menu:
> 2
I have enough resources, making you a coffee!

Write action (buy, fill, take, remaining, exit):
> remaining

The coffee machine has:
700 of water
390 of milk
80 of coffee beans
7 of disposable cups
$564 of money

Write action (buy, fill, take, remaining, exit):
> take

I gave you $564

Write action (buy, fill, take, remaining, exit):
> remaining

The coffee machine has:
700 of water
390 of milk
80 of coffee beans
7 of disposable cups
0 of money

Write action (buy, fill, take, remaining, exit):
> exit

Implemented by me on 07.08.2020:

"""

# operations
buy = "buy"
fill = "fill"
take = "take"


def view_state():
    print("The coffee machine has:")
    print(water, 'of water')
    print(milk, 'of milk')
    print(coffee_beans, 'of coffee beans')
    print(disposable_cups, 'of disposable cups')
    print(money, 'of money')


# current state
money = 550
water = 400
milk = 540
coffee_beans = 120
disposable_cups = 9


def espresso():
    global water
    global coffee_beans
    global money
    global disposable_cups
    water -= 250
    coffee_beans -= 16
    money += 4
    disposable_cups -= 1

def latte():
    global water
    global coffee_beans
    global money
    global milk
    global disposable_cups
    water -= 350
    milk -= 75
    coffee_beans -= 20
    money += 7
    disposable_cups -= 1

def cappuccino():
    global water
    global coffee_beans
    global money
    global milk
    global disposable_cups
    water -= 200
    milk -= 100
    coffee_beans -= 12
    money += 6
    disposable_cups -= 1


def do_buy():
    drink = input("What do you want to buy? 1 - espresso, 2 - latte, 3 - cappuccino:")
    if drink == '1':
        espresso()
    elif drink == '2':
        latte()
    elif drink == '3':
        cappuccino()
    view_state()


def do_fill():
    global water
    global milk
    global coffee_beans
    global disposable_cups
    water += int(input("Write how many ml of water do you want to add:"))
    milk += int(input("Write how many ml of milk do you want to add:"))
    coffee_beans += int(input("Write how many grams of coffee beans do you want to add:"))
    disposable_cups += int(input("Write how many disposable cups of coffee do you want to add:"))
    view_state()


def do_take():
    global money
    print("I gave you $" + str(money))
    money = 0
    view_state()


def actions(operation):
    if operation == buy:
        do_buy()
    elif operation == fill:
        do_fill()
    elif operation == take:
        do_take()


view_state()

# read the data
operation = input("Write action (buy, fill, take):")
actions(operation)
