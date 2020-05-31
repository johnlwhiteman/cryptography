"use strict";

var gcd = require('./gcd.js');

function getOrder(r, n, includeMetaFlag=false) {
    let a, b, o;
    let meta = [];

    for (o = 1; o < n; o++) {
        a = r**o;
        b = a % n;
        meta.push([o, a, b, n]);
        if (b == 1)
            break;
    }

    if (b != 1)
        return null;

    if (includeMetaFlag)
        return [o, meta];

    return o;
}

function isPrimitiveRootModulo(r, n) {
    let o = getOrder(r, n, true);
    let set = new Set();

    if (o === null || o[0] != n - 1)
        return false;

    for(let i = 0; i < o[0]; i++) {
        let e = o[1][i][2];
        if (e < 1 || e > n - 1)
            return false
        set.add(e);
    }

    return set.size == n - 1;
}

function test() {
    let r = 2;
    let n = 7;

    console.log(gcd.isRelativelyPrime(r, n));
    console.log(isPrimitiveRootModulo(r, n));
    console.log(getOrder(r, n, true)[1]);

    r = 3;
    n = 7;
    console.log(gcd.isRelativelyPrime(r, n));
    console.log(isPrimitiveRootModulo(r, n));
    console.log(getOrder(r, n, true)[1]);
}

module.exports = {
    getOrder,
    isPrimitiveRootModulo
};