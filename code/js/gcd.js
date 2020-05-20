"use strict";

function getDivisors(n) {
    var divisors = [];

    for (let i = 1; i <= n; i++) {
        if (0 == (n % i)) {
            divisors.push(i);
        }
    }

    return divisors;
}

function getGCD(n1, n2) {
    let candidates = [];
    let nBiggest = null;

    if ((!n1) || (!n2))
        return null;

    if (n1 == n2)
        return n1;
 
    if (n1 < n2) {
        candidates = getDivisors(n1);
        nBiggest = n2;
    } else {
        candidates = getDivisors(n2);
        nBiggest = n1;
    } 

    for (let i = candidates.length - 1; i >= 0; i--) {
        if (0 == (nBiggest % candidates[i])) {
            return (candidates[i]);
        }
    }
    return null;
}

function getGCDByEuclid(n1, n2) {
    let a,b,q,r = null;
    let history = [[a, b, q, r]];
    
    if ((!n1) || (!n2))
        return null;

    if (n1 == n2)
        return n1;

    if (n1 > n2) {
        a = n1;
        b = n2;
    } else {
        a = n2;
        b = n1;
    }
    while (true) {
        q = Math.floor(a/b);
        r = a - (q * b);
        console.log(`${a} = ${b}(${q}) + (${r})`);
        if (r == 0) {
            if (null === history[0][3]) {
                return b;
            }
            return history[0][3];
        }
        history[0] =[a, b, q, r];
        a = b;
        b = r;
    }
    return null;
}

function isCoprime(n1, n2) {
    return (1 == getGCD(n1, n2));
}

function isRelativePrime(n1, n2) {
    return (isCoprime(n1, n2));
}

function hello() {
    console.log("hello");
}



/*
let n1 = 15;
let n2 = 40;
let gcd = null;
console.log(`gcd(${n1}, ${n2})`);
//console.log(getDivisors(n1).toString());
//console.log(getDivisors(n2).toString());
gcd = getGCD(n1, n2);
console.log(`The GCD is ${gcd}`);
gcd = getGCDByEuclid(n1, n2);
console.log(`The GCD is ${gcd}`);
*/

module.exports.isCoprime = isCoprime;
