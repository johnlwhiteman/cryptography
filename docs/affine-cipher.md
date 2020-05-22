# Affine Cipher

The key is divided into two parts:

$$
K = (a,b)
\\~\\
Let\ x,y,a,b \in \Z_{26}.
\\~\\
E_{K}(P) = C \equiv aP + b\ mod\ 26
\\~\\
D_{K}(C) = P \equiv a^{-1} (y - b)\ mod\ 26
\\~\\
C \equiv aP + b\ mod\ n
\\~\\
C - b \equiv aP\ mod\ n
\\~\\
a^{-1}(C - b) \equiv P\ mod\ n
$$


Affine Cipher Encryption:

Rules

* N is size of the alphabet
* A must be coprime with N
* B must be between 0 and N - 1


