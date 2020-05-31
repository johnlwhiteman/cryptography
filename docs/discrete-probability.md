# Discrete Probability

Probability Distribution

This is a finite set: $U = \{0,1\}^{n}$

$\{0,1\}^2 = \{00, 01, 10, 11\}$

Def: Probability distribution $P$ over $U$ is a function $P:U \Rightarrow [0,1]$ such that:
$$
\sum_{x \in U}^{} P(x)=1
$$

Uniform Distribution: $\forall\  x \in U: P(x) = 1/|U|$
* All weight is divided equally for all elements in the set (universe)

Point Distribution: $P(x_{0}) = 1, \forall\ x \ne x_{0}: P(x) = 0$
* All weight is focused on just one point ... here $x_{0}$

Distribution vector: $( P(000), P(001), P(0101), ... , P(111)) \in |\R^8$

### Events

For a set $A \subseteq U: Pr[A]=\sum_{x \in A} P(x) \in [0,1]$

Note: $Pr[U] =1$

The set $A$ is called an event.



Example: $U=\{0,1\}^8$ which is same as $|U| = 2^8 = 256$

$A = \{$ all $x$ in $U$ such that $lsb_{2}(x)=11 \}$  $ \subseteq U$

for the uniform distribution on $\{0,1\}^8$: Pr[A] = 1/4

### Independence

Evens $A$ and $B$ ad independent is $Pr[A \cap B] = Pr[A] \times Pr[B]$

$U = \{0,1\}^2 = 00 (two\ bits) = \{00,01,10,11\} = 2^2 = 4 (possibilities)$