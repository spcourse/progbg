# Extra practice 2: for vs while

### 1

Write a **for** loop that prints the numbers 0 to 9.

Example:

    0 1 2 3 4 5 6 7 8 9

### 2

Write a **while** loop that prints the numbers 0 to 9.

Example:

    0 1 2 3 4 5 6 7 8 9

### 3

Write a **for** loop that computes the sum of the numbers 1 to 10.

Example:

    The sum of the numbers 1 2 3 4 5 6 7 8 9 10 is 55

    ### 3


### 4

Write a **while** loop that computes the sum of the numbers 1 to 10.

Example:

    The sum of the numbers 1 2 3 4 5 6 7 8 9 10 is 55

### 5
Write a **for** loop that computes the squares and the cumulative sum of the squares
of the numbers 0 to 6

Example:

    square: 0; sum of squares: 0
    square: 1; sum of squares: 1
    square: 4; sum of squares: 5
    square: 9; sum of squares: 14
    square: 16; sum of squares: 30
    square: 25; sum of squares: 55
    square: 36; sum of squares: 91

### 6
Write a **while** loop that computes the squares and the cumulative sum of the squares
of the numbers 0 to 6

Example:

    square: 0; sum of squares: 0
    square: 1; sum of squares: 1
    square: 4; sum of squares: 5
    square: 9; sum of squares: 14
    square: 16; sum of squares: 30
    square: 25; sum of squares: 55
    square: 36; sum of squares: 91

### 7

Ask the user to enter a positive integer m. Write a loop that computes the sum
$$1 + 2 + 3 + ...$$ until the sum gets bigger than m. You can choose yourself
which type loop (for or while) you want to use.

Example:

    Enter a number: 36
    The sum of the numbers 1 2 3 4 5 6 7 8 9 is 45, which is bigger than 36.


### 8

#### a
Without running it, predict what the following piece of code will do:

    for i in range(3):
        for j in range(4):
            print('.', end = '')
        print()

#### b
Now run it and check if you were right.

#### c
Rewrite the code, but use while loops in stead of for loops.


### 9
Write a **for** loop that computes the squares and the cumulative sum of the squares
of the numbers 0 to 6. Use an **if** statement to make sure you only print something
if the sum of squares is divisible by 5.

Example:

    square: 0; sum of squares: 0
    square: 4; sum of squares: 5
    square: 16; sum of squares: 30
    square: 25; sum of squares: 55


### 10
Write a piece of code using two *for* loops (one nested in the other), to print a
4 by 5 square of hashes ('#').

Example:

    #####
    #####
    #####
    #####

### 11
Write a piece of code using two *while* loops (one nested in the other), to print a
4 by 5 square of hashes ('#').

Example:

    #####
    #####
    #####
    #####

### 12

Adapt the code from 10 or 11, so that it will print only one hash on the first line,
two on the second, etc. So that you will get a pyramid like below.

Example:

    #
    ##
    ###
    ####
