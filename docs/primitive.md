**Def:**
 Let $n$ be a positive integer and let $gcd(a, n) = 1$. The order of $a$ modulo $n$, denoted $ord_{n}(a)$, is the smallest positive integer $k$ s.t. $a^k \equiv 1\ mod\ n$.

**Ex1:**
Let $a = 2$
Let $n = 7$

$ord_{7}(2) = x$

**Step 1: Check if relatively prime:**

$2 = \{\textcolor{orange}{1},2\}$

$7 = \{\textcolor{orange}{1},7\}$

$2$ and $7$ are relatively prime since the only common factor is $1$ between them.

**Step 2: Find the order:**

Let $k$ represent the order
Given $a^k \equiv b\ mod\ n$

| $k$ |   | $a^k$ |          | $b\ mod\ n$ |          |             |          |   |
|:---:|:-:|:-----:|:--------:|:-----------:|:--------:|:-----------:|:--------:|:-:|
|  1  |   | $2^1$ | $\equiv$ | $2\ mod\ 7$ | $\equiv$ |      ~      | $\equiv$ | 2 |
|  2  |   | $2^2$ | $\equiv$ | $4\ mod\ 7$ | $\equiv$ |      ~      | $\equiv$ | 4 |
|  3  |   | $2^3$ | $\equiv$ | $8\ mod\ 7$ | $\equiv$ | $1\ mod\ 7$ | $\equiv$ | 1 |

$ord_{7}(2) = 3$ since $k=3$ when $1\ mod\ 7$ is found.

***

**Ex2:**
Let $a = 3$
Let $n = 7$

$ord_{7}(3) = x$

**Step 1: Check if relatively prime:**

$3 = \{\textcolor{orange}{1},3\}$

$7 = \{\textcolor{orange}{1},7\}$

$3$ and $7$ are relatively prime since the only common factor is $1$ between them.

**Step 2: Find the order:**

Let $k$ represent the order
Given $a^k \equiv b\ mod\ n$

| $k$ |   | $a^k$ |          |  $b\ mod\ n$  |          |             |          |   |
|:---:|:-:|:-----:|:--------:|:-------------:|:--------:|:-----------:|:--------:|:-:|
|  1  |   | $3^1$ | $\equiv$ | $3\ mod\ 7$   | $\equiv$ |      ~      | $\equiv$ | 3 |
|  2  |   | $3^2$ | $\equiv$ | $9\ mod\ 7$   | $\equiv$ | $2\ mod\ 7$ | $\equiv$ | 2 |
|  3  |   | $3^3$ | $\equiv$ | $27\ mod\ 7$  | $\equiv$ | $6\ mod\ 7$ | $\equiv$ | 6 |
|  4  |   | $3^4$ | $\equiv$ | $81\ mod\ 7$  | $\equiv$ | $4\ mod\ 7$ | $\equiv$ | 4 |
|  5  |   | $3^5$ | $\equiv$ | $243\ mod\ 7$ | $\equiv$ | $5\ mod\ 7$ | $\equiv$ | 5 |
|  6  |   | $3^6$ | $\equiv$ | $729\ mod\ 7$ | $\equiv$ | $1\ mod\ 7$ | $\equiv$ | 1 |

$ord_{7}(3) = 6$ since $k=6$ when $1\ mod\ 7$ is found.