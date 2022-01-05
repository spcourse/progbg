# Extra practice 1: Input validation

### 1

Write a program that asks the user to enter a float. If the float is smaller than 0, ask again. Otherwise print the input.

Example:

    Enter a number: -3.5
    Enter a number: -9
    Enter a number: 3.2
    3.2


### 2

Write a program that asks the user to enter a float. The input should be between 4 (inclusive) and 6.5 (exclusive). If this is not the case, ask again. Otherwise print the input.

Example:

    Enter a number: 3
    Enter a number: 6.8
    Enter a number: 6.5
    Enter a number: 4
    4.0


### 3

Write a program that asks the user to enter an integer. The input should be bigger than 2. If this is not the case, print "Wrong input!" end the program. Otherwise print the input.

Example 1:

    Enter a number: 1
    Wrong input!

Example 2:

    Enter a number: 3
    3


### 4

Write a program that asks the user to enter a uppercase letter. If the input is not an uppercase letter, ask again. Otherwise print the input.

Example:

    Enter an uppercase letter: a
    Enter an uppercase letter: QUEST
    Enter an uppercase letter: 1
    Enter an uppercase letter: Z
    Z

### 5

Write a program that asks the user to enter a text. If the text too long (more than 10 characters), ask again. Otherwise print the input.

Example:

    Enter a text: Hippopotomonstrosesquippedaliophobia
    Enter a text: Sorry
    Sorry


### 6

Write a program that asks the user to enter a text. The text should start with an 'A'. If this is not the case, print the message "Enter a text that starts with an 'A'" and ask again for input. Otherwise print the input.

Example:

    Enter a text: Hippopotomonstrosesquippedaliophobia
    Enter a text that starts with an 'A': Ahippopotomonstrosesquippedaliophobia
    Ahippopotomonstrosesquippedaliophobia


### 7

Write a program that asks the user to enter an even number lower than 10. If the user enters a number that doesn't fit the description, ask again. Otherwise, print the input.

Example:

    Enter an even number lower than 10: 3
    Enter an even number lower than 10: 12
    Enter an even number lower than 10: -1
    Enter an even number lower than 10: 6
    6

### 8

Write a program that asks the user to enter an even number that's divisible by 7. If the user enters a number that doesn't fit the description, ask again. Otherwise, print the input.

Example:

    Enter a number: 4
    Enter a number: 21
    Enter a number: 7
    Enter a number: 14
    14


### 9

Write a program that asks the user to enter a float between 0.1 and 0.9 or between 19 and 160. If the user enters a number that doesn't fit the description, ask again. Otherwise, print the input.

Example:

    Enter a number: 10
    Enter a number: 0
    Enter a number: 170
    Enter a number: 0.5
    0.5


### 10

Write a program that asks the user to enter an integer between 1 and 9 but isn't 2 or 3 If the user enters a number that doesn't fit the description, ask again. Otherwise, print the input.

Example:

    Enter a number: 0
    Enter a number: 2
    Enter a number: 3
    Enter a number: 1
    1


### 11
Write a program that asks the user to enter two floats. If the second float is more than twice as big as the first, ask both numbers again. Otherwise, print the input.

Example:

    Enter number 1: 10.5
    Enter number 2: 25
    Enter number 1: 9
    Enter number 2: 9.5
    9, 9.5


### 12
Write a program that asks the user to enter two floats. If the second float is more than twice as big as the first, ask the second number again. Otherwise, print the input.

Example:

    Enter number 1: 10.5
    Enter number 2: 25
    Enter number 2: 9.5
    1.5, 9.5
