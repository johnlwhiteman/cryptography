# Shift (Ceasar) Cipher

Definition:

$$
Let\ p, c, k, \in \Z_{26}
\\~\\
Encryption: E_{k}(p)\ \equiv p + k\mod\ 26 \equiv c
\\~\\
Decryption: D_{k}(c)\ \equiv c + k\mod\ 26 \equiv p
$$


Operated on letters, not numbers or bits.

Here we shift letters in an alphabet.

Notice convention here where plaintext is uppercase and ciphertext is lowercase.

What is the keyspace. Well it would be 26 options for every letter. Since the shift key ciper is fixed for each letter, then the keyspace is 26.

Boneh says that this is not a cipher at all since their is no random key. We could say the shift is the random key.

Another thought is that there are two secrets: length and direction of the shift. 

However, the direction of the shift can be negated such that there is an equivelnt shift 






Let K be the key:

Example:

$$

Let\ K = 3
\\~\\
A \Rightarrow d
\\~\\
B \Rightarrow e
\\~\\
.
\\~\\
.
\\~\\
.
\\~\\
W \Rightarrow z
\\~\\
X \Rightarrow a
\\~\\
Y \Rightarrow b
\\~\\
Z \Rightarrow c
$$


Two possible attacks include:
* Frequency analysis
* Brute force

Map the alphabet to numbers ...

|  A  |  B  |  C  |  D  |  E  |  F  |  G  |  H  |  I  |  J  |  K  |  L  |  M  |
|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|
|  0  |  1  |  2  |  3  |  4  |  5  |  6  |  7  |  8  |  9  |  10 |  11 |  12 |

.


|  N  |  O  |  P  |  Q  |  R  |  S  |  T  |  U  |  V  |  W  |  X  |  Y  |  Z  |
|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|
|  13 |  14 |  15 |  16 |  17 |  18 |  19 |  20 |  21 |  22 |  23 |  24 |  25 |
