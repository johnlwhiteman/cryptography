# Euclidean Algorithm to Find GCD

We can use the Euclidean Algorithm to find the greatest common demoninator between two numbers.

This is a "table" way to help keeps things organized. First make sure "a" is the larger of the two numbers so we can divide into it later.

$$
Given\ gcd(15,40)
\\~\\
Let\ a = 40
\\~\\
Let\ b = 15
\\~\\
$$

Now create a table to represent this equation:

$$
Let\ a = b(q) + r
\\~\\
where
\\~\\
q = floor(a/b)\ ...\ which\ is\ the\ quotient
\\~\\
r = remainder\ of\ a/b
$$

|    a    |    b    |    q    |    r    |
|:-------:|:-------:|:-------:|:-------:|
|    40   |    15   |    2    |    10   |

Next, add a new row to the table.

On the new line, left shift $b$ and $r$ and ignore $q$ and $r$:

$a \Leftarrow b$

$b \Leftarrow r$

|    a    |    b    |    q    |    r    |
|:-------:|:-------:|:-------:|:-------:|
|    40   |    15   |    2    |    10   |
|    15   |    10   |         |         |

Solve for $q$ and $r$ like you did before, but with the new values for $a$ and $b$.

|    a    |    b    |    q    |    r    |
|:-------:|:-------:|:-------:|:-------:|
|    40   |    15   |    2    |    10   |
|    15   |    10   |    1    |    5    |


Repeat until $r = 0$ since $b$ can't be used to divide into $a$ if $0$.


|    a    |    b    |    q    |    r    |
|:-------:|:-------:|:-------:|:-------:|
|    40   |    15   |    2    |    10   |
|    15   |    10   |    1    |    5    |
|    10   |    5    |    2    |    0    |


The GCD is the value or $r$ from the previous row.


|    a    |    b    |    q    |    r    |
|:-------:|:-------:|:-------:|:-------:|
|    40   |    15   |    2    |    10   |
|    15   |    10   |    1    |   (5)   |
|    10   |    5    |    2    |    0    |

$gcd(15,40) = 5$


If the final answer is 1, then it is coprime / relatively prime.

