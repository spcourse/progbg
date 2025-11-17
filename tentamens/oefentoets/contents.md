# Oefentoets (week 4 - na 2.4)

* Maak deze oefenvragen in de tentameneditor: <br>
    [editor](exam_button:practice_bg)
* Doe alsof dit een echt tentamen is. Dus:
        * gebruik geen chatGPT (of andere LLM)
        * gebruik alleen de website zelf als bron (google niets)
        * geen overleg
* Deze oefentoets duurt 45 minuten.
* We verwachten niet dat je alles al helemaal correct kan.
* Voor deze oefening is het belangrijker dat je elke vraag geprobeerd hebt dan dat het helemaal correct is.
Porobeer een kwartier te nemen voor elke vraag en dan door te gaan.


## Assignment 1: Harmonic Mean

Write a function **harmonic_mean(numbers)** that calculates and returns the harmonic mean of a list of numbers.

The **harmonic mean** of a set of numbers $$x_1, x_2, x_3, ..., x_n$$ is defined as:

$$
H = \frac{n}{\frac{1}{x_1} + \frac{1}{x_2} + \frac{1}{x_3} + \dots + \frac{1}{x_n}}
$$

For example, if the list is `[5, 2, 3, 4]`, the harmonic mean is calculated as 4 / (1/5 + 1/2 + 1/3 + 1/4). The function should return the computed harmonic mean as a floating-point value.

### Example Usage

        l1 = [1, 2, 3, 4]
        result1 = harmonic_mean(l1)
        print(result1)

### Expected Output

        1.9200000000000004



## Assignment 2: Dot Product

Write a function **dot_product(v1, v2)** that calculates and returns the dot product of two numerical vectors (lists of equal length).

The **dot product** of two vectors $$v_1 = (a_1, a_2, a_3, ..., a_n)$$ and $$v_2 = (b_1, b_2, b_3, ..., b_n)$$ is defined as:

$$
a_1b_1 + a_2b_2 + a_3b_3 + \dots + a_nb_n
$$

In other words, you multiply the corresponding elements of the two lists and sum up all these products.

For example, if
`v1 = [1, 2, 3]` and `v2 = [1, 10, 100]`,
then the dot product is calculated as
(1 × 1) + (2 × 10) + (3 × 100) = 1 + 20 + 300 = 321.
The function should return this resulting scalar value.

### Example Usage

        v1 = [1, 2, 3]
        v2 = [1, 10, 100]
        result = dot_product(v1, v2)
        print(result)

### Expected Output

        321


## Assignment 3: Strange Product

Write a function **strange_product(v1, v2)** that takes two lists of numbers and returns a new list containing all pairwise products between the elements of the two lists.

This means that for each element in the second list **v2**, you should multiply it by every element in the first list **v1**, and collect all the results in a single list, in the order they are produced.

For example, if
`v1 = [1, 2, 3]` and `v2 = [1, 10, 100]`,
the function should compute:

(1×1), (2×1), (3×1), (1×10), (2×10), (3×10), (1×100), (2×100), (3×100)
which results in the list [1, 2, 3, 10, 20, 30, 100, 200, 300].

### Example Usage

        v1 = [1, 2, 3]
        v2 = [1, 10, 100]
        result = strange_product(v1, v2)
        print(result)

### Expected Output

        [1, 2, 3, 10, 20, 30, 100, 200, 300]
