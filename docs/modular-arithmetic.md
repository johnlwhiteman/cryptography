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

A negative trick
$10 \equiv -2\ mod\ 4$ 

Just add $-2 + n$ or $-2 + 4 = 2$


