"use strict";

// Use this for super large bases and/or exponents
// https://en.wikipedia.org/wiki/Modular_exponentiation
function getModularPower(base, exponent, modulus) {
    if (modulus == 1) {
        return 1;
    }
    let c = 1;
    for (let i = 0; i < exponent; i++) {
        c = (c * base) % modulus;
    }
    return c;
}

// Both min and max are inclusive
function getRandomNumberInRange(min, max) {
    return Math.floor(Math.random() * (max - min + 1)) + min;
}

// Both min and max are inclusive
function getRandomNumbersInRange(min, max, uniqueOnlyFlag=false) {
    let rnums = [];
    min = Math.ceil(min);
    max = Math.floor(max);
    let cnt = max - min + 1;
    if (max < min)
        return null;
    while (rnums.length < cnt) {
        let r = getRandomNumberInRange(min, max);
        if (!uniqueOnlyFlag) {
            rnums.push(r);
        } else if (!rnums.includes(r)) {
            rnums.push(r);
        }
    }
    return rnums;
}
function hasDecimal(n) {
    return (n % 1 != 0)
}

module.exports = {
    getModularPower,
    getRandomNumberInRange,
    getRandomNumbersInRange,
    hasDecimal
};