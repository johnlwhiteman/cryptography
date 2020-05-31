# Modular Multiplicative  Inverse

Finding the multiplicative inverse of a number is easy since the inverse of multiplication is division.

Example:

$$
5 \times 9 = 45
\\~\\
5 = \frac{45}{9}
$$

Now if a product of two numbers gives 1, then each number is called the multiplicative inverse of the other.

Example:

$$
5 \times \frac{1}{5} = 1
\\~\\
\cancel{5} \times \frac{1}{\cancel{5}} = 1
\\~\\
OR
\\~\\
5 \times 5^{-1} = 1
$$

Also if we multiply a number by 1, the result will always be the number. This is called the multiplicative identity.

## Modular Arithmetic Revisited

We often need to find the multiplicative inverse of a number when doing modular arithmetic. Again let's we come with this form:

$$
a \equiv b\ mod\ n
$$

We say that $a$ and $b$ are congruent modulo $n$.

$n$ is a positive integer and its set can be denoted as:

$$
\Z_{n} = \{0,1,2,...,n-1\}
$$

Given:

$$
38 = 3\ mod\ 5
\\~\\
a = (q \times n) + r
\\~\\
38 = 3 \times 5 + 3
$$


Example:

$$
Let\ n = 9
\\~\\
Let\ a = 2
\\~\\
$$
And we might be tempted to do something like this:
$$
2 \times 2^{-1}=1\ mod\ 9
$$
The problem with this is that $2^{-1}$ is a fraction. There are no franctions in our mod 9 set, only these numbers: {0,1,2,3,4,5,6,7,8}. We can only use these whole numbers.

So we have to find a multiplicative inverse that is in our set.

## Extended Euclidean Algorithm to Find the Multiplicative Inverse

Example

$$
b^{-1} \equiv ?\ mod\ n
\\~\\
OR
\\~\\
b^{-1}\ mod\ n \equiv ?
$$

We can rewrite to be a multiplicative inverse:

$$
b \times b^{-1} \equiv 1\ mod\ n
$$

Before we can continue, we ALSO must ensure that $gcd(b,n) = 1$. That is to say the greatest common denominator between b and n is 1. The largest value that divides evening into both of them with a remainder. If this is not true then we can say that $b$ and $n$ have no multiplicative inverse.

Brute Force Method:
$$
3\ mod\ 17
\\~\\
3 \times \square \equiv 1\ mod\ 17
$$

Keep trying until $a \times n^{-1} = 1 = b$
$$
\\~\\
3 \times \boxed{1} \equiv 1\ mod\ 17\ (r=3)
\\~\\
3 \times \boxed{2} \equiv 1\ mod\ 17\ (r=6)
\\~\\
3 \times \boxed{3} \equiv 1\ mod\ 17\ (r=9)
\\~\\
3 \times \boxed{4} \equiv 1\ mod\ 17\ (r=12)
\\~\\
3 \times \boxed{5} \equiv 1\ mod\ 17\ (r=15)
\\~\\
\textcolor{green}{ 3 \times \boxed{6} \equiv 1\ mod\ 17\ (r=1)}
$$

The last one is correct since the remainder is 1. The rest are not. Brute force is just fine if the numbers are small. Multiplicative inverses are about finding $1$.

Do all numbers have a multiplicative inverse. No. Not all numbers do. There is a trick you can do before attempting to find the multiplicative inverse. As we said before, we can first check if $b$ and $n$ are coprime / relatively prime such that: $gcd(b,n) = 1$

These are examples are not relatively prime:

$$
3\ mod\ 9
\\~\\
5\ mod\ 10
\\~\\
7\ mod\ 21
$$

And these examples are relatively prime:

$$
3\ mod\ 5
\\~\\
7\ mod\ 24
\\~\\
11\ mod\ 14
$$


### References

* [Wikipedia](https://en.wikipedia.org/wiki/Modular_multiplicative_inverse)
