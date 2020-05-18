# Multiplicative Inverse

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
OR
\\~\\
5 \times 5^{-1} = 1
$$

Also if we multiply a number by 1, the result will always be the number. This is called the multiplicative identity.

## Modular Arithmetic Revisited

We often need to find the multiplicate inverse of a number when doing modular arithmetic. 

Example:

$$
Let\ n = 9
\\
Let\ a = 2
$$
And we might be tempted to do something like this:
$$
2 \times 2^{-1}=1\ mod\ 9
$$
The problem with this is that $2^{-1}$ is a fraction. There are no franctions in our mod 9 set, only these numbers: {0,1,2,3,4,5,6,7,8}. We can only use these whole numbers.

So we have to find a multiplicative inverse that is in our set. 

## Euclidean Algorithm to Find the Multiplicative Inverse

Example

$$
x^{-1} \equiv ?\ mod\ n
\\~\\
OR
\\~\\
x^{-1} mod\ n \equiv ?
$$

We can rewrite to be a multiplicative inverse:

$$
x^{-1}x \equiv 1\ mod\ n
$$

Before we can continue, we ALSO must ensure that $gcd(x,n) = 1$. That is to say the greatest common denominator between x and n is 1. The largest value that divides evening into both of them with a remainder. 