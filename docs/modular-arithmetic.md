# Modular Arithmetic

In cryptography everything must be done in finite sets.

Natural Number: {1, 2, 3, ..., N - 1}

Whole Number: {0, 1, 2, 3, ..., N - 1} (Rember the '0'h in whole)


if $a,b \in \Z$ and $m \in \Z^{+}$, 

   then $a \equiv b\ (mod\ m)$ iff $m\ |\ a - b$ 


Don't say m = 1 ... kills everything


$a \equiv b\ (mod\ n)$
1. a and b have the same "remainder" when they are divided by "n"
2. $a = k*n + b$  Note: b is the remainder 
3. $n|(a-b)$  Note: $(a-b)$ is a multiple of n 

Example:
$10 \equiv 14\ (mod\ 4)$

Remember rule 1 where both a and b are divisible by n

$10 \div 4=2R2$

$14 \div 4=3R2$ 

## How to Find the Inverse of a Number in Modular Arthmetic.

Let's say you have $27^{-1}\ mod\ 392$.

### Extended Euclidean Geometry

$$
27^{-1}\ mod\ 392 \equiv 1
\\~\\
27x = 1
\\~\\
x = \frac{1}{27}=27^{-1}
\\~\\
27x\ mod\ 393 \equiv 1
$$
Unfortunately, we can't represent $27^{-1}$ since it's really a fraction $\frac{1}{27}$ and fractions don't exist in our a key space of $n=393\ \{0,1,2,3,...,391\}$

We need to use the Euclidean algorithm to figure this stuff out.

$$
Let\ n = 393
\\~\\
Let\ b = 27^{-1}
\\~\\
27^{-1}\ mod\ 392
$$
First, create an equation with n on left side and the inverse of b on the right side times the number of times it can divide into n plus the remainder if any
$$
392 = 27 * (int(392/27)) + remainder 
\\~\\
392 = 27 * (14) + 14 
$$
We move just b (27) to the right side of the equation, replacing 392. On the right side we remove everything else except the remainder and set it up like before as such:
$$
27 = 14 * (int(27/14)) + remainder
\\~\\
27 = 14 * (1) + 13
$$
Rinse and repeat ...
$$

$$


