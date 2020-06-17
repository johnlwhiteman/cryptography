# Euclidean Algorithm to Find GCD and Multiplicative Inverse

First solve for GCD then if 1 we can say it has a multiplicative inverse. *The extended Euclidean algorithm is particularly useful when a and b are coprime. With that provision, x is the modular multiplicative inverse of a modulo b, and y is the modular multiplicative inverse of b modulo a.*

## Bézout's Identity (Bay-ZOO)

Let $a$ and $b$ be integers with the greatest commond divisor $d$. Then, there exist integers $S$ and $T$ such that $aS + bT = d$. More generally, the integers of the form $aS + bT$ are exactly the multiples of $d$.

Given: (rework w/difference value)
$$
\textcolor{red}{710} = \textcolor{blue}{310} \times \textcolor{gray}{2} + \textcolor{green}{90}
\\~\\
\textcolor{blue}{310} = \textcolor{green}{90} \times \textcolor{gray}{3} + \textcolor{orange}{40}
\\~\\
\textcolor{green}{90} = \textcolor{orange}{40} \times \textcolor{gray}{2} + \textcolor{purple}{10}\ (answer)
\\~\\
\textcolor{orange}{40} = \textcolor{purple}{10} \times \textcolor{gray}{4} + 0
$$


## ToDo Section

Find $gcd(161, 28)$ and also $s$ and $t$

Standard Assumptions:

Assume: $s_{1} = 1$
Assume: $s_{2} = 0$
Assume: $t_{1} = 0$
Assume: $t_{2} = 1$

Given: $s = s_{1} - s_{2} \times q$
Given: $t = t_{1} - t_{2} \times q$

Then Shift Terms:
$s_{1} = s_{2}$
$s_{2} = s$
$t_{1} = t{2}$
$t_{2} = t$


| a    | b    | r    | q    | s1   | s2   | s    | t1   | t2   | t    |
|:----:|:----:|:----:|:----:|:----:|:----:|:----:|:----:|:----:|:----:|
|  161 |  28  |  21  |  5   |  1   |  0   |  1   |  0   |  1   | -5   |
|  28  |  21  |  7   |  1   |  0   |  1   | -1   |  1   | -5   |  6   |
|  21  |  7   |  0   |  3   |  1   | -1   |  4   | -5   |  6   | -23  |
|  7   |  0   |  X   |  X   | -1   |  4   |  X   |  6   | -23  |  X   |


Note: If GCD is not $1$ then there is NOT inverse.

For last row ...
$gcd = a$
$s = s_{1}$
$t = t_{1}$

$gcd(161, 28) = 7$
//https://www.youtube.com/watch?v=shaQZg8bqUM
https://www.youtube.com/watch?v=mgvA3z-vOzc


### References

* [Wikipedia - Bézout's Identity](https://en.wikipedia.org/wiki/B%C3%A9zout%27s_identity)
* [Wikipedia - Modular Multiplicative Inverse](https://en.wikipedia.org/wiki/Modular_multiplicative_inverse)

