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

function getEuclideanGCD(n1, n2, includeMetaFlag=false) {
    let a = n1;
    let b = n2;
    let x = null;
    let q, r = x;
    let meta = [];

    if ((!n1) || (!n2))
        return null;
    else if (n1 == n2)
        return n1;

    if (n1 < n2) {
        a = n2;
        b = n1;
    }

    while (true) {
        if (0 == b) {
            if (includeMetaFlag) {
                meta.push([a, b, x, x]);
                return [a, meta];
            }
            return a;
        }
        q = Math.floor(a/b);
        r = a - (q * b);
        meta.push([a, b, r, q]);
        a = b;
        b = r;
    }
    return null;
}

function getExtendedEuclideanGCDAndBezout(n1, n2, includeMetaFlag=false) {
    let a = n1;
    let b = n2;
    let x = null;
    let q, r, s, t = x;
    let s1 = 1;
    let s2 = 0;
    let t1 = 0;
    let t2 = 1;
    let meta = [];


    if ((!n1) || (!n2))
        return null;
    else if (n1 == n2)
        return n1;

    if (n1 < n2) {
        a = n2;
        b = n1;
    }

    while (true) {
        if (0 == b) {
            if (includeMetaFlag) {
                meta.push([a, b, x, x, s1, s2, x, t1, t2, x]);
                if (t1 < 0)
                    t1 += n2;
                return [a, s1, t1, meta];
            }
            return a;
        }
        q = Math.floor(a/b);
        r = a - (q * b);
        s = s1 - (s2 * q);
        t = t1 - (t2 * q);
        meta.push([a, b, r, q, s1, s2, s, t1, t2, t]);
        a = b;
        b = r;
        s1 = s2;
        s2 = s;
        t1 = t2;
        t2 = t;
    }
    return null;

}

function isCoprime(n1, n2) {
    return (1 == getGCD(n1, n2));
}

function isRelativelyPrime(n1, n2) {
    return (isCoprime(n1, n2));
}

function getExtendedEuclidean(n1, n2, includeMetaFlag=false) {
    let meta = getGCDByEuclid(n1, n2, true);

    console.log(meta);
}


//console.log(getExtendedEuclideanGCDAndBezout(197, 3000, true));



//console.log(getGCD(310,710));

module.exports = {getGCD,
                  isCoprime,
                  isRelativelyPrime};
