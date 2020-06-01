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

| a    | b    | q    | r    |
|:----:|:----:|:----:|:----:|
|  40  |  15  |  2   |  10  |

Next, add a new row to the table.

On the new line, left shift $b$ and $r$ and ignore $q$ and $r$:

$a \Leftarrow b$

$b \Leftarrow r$

| a    | b    | q    | r    |
|:----:|:----:|:----:|:----:|
|  40  |  15  |  2   |  10  |
|  15  |  10  |      |      |

Solve for $q$ and $r$ like you did before, but with the new values for $a$ and $b$.

| a    | b    | q    | r    |
|:----:|:----:|:----:|:----:|
|  40  |  15  |  2   |  10  |
|  15  |  10  |  1   |  5   |

We repeat.

| a    | b    | q    | r    |
|:----:|:----:|:----:|:----:|
|  40  |  15  |  2   |  10  |
|  15  |  10  |  1   |  5   |
|  10  |  5   |  2   |  0   |

Yet we repeat again. Notice here that $r=0$. This signals the next iteration as the last one.

| a    | b    | q    | r    |
|:----:|:----:|:----:|:----:|
|  40  |  15  |  2   |  10  |
|  15  |  10  |  1   |  5   |
|  10  |  5   |  2   |  0   |
|  5   |  0   |  X   |  X   |

It's time to stop since $\frac{5}{0}$ is undefined. This means that the value of $a$ is the GCD. We are done. This table approach makes it easy to code a solution too.

$gcd(15,40) = 5$


*Note: If the final answer is 1, then it is coprime / relatively prime.*

