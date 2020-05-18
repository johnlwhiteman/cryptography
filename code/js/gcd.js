"use strict";

function getDivisors(num) {
    var divisors = [];

    for (let i = 1; i <= num; i++) {
        if (0 == (num % i)) {
            divisors.push(i);
        }
    }
    return divisors;
}

function getGCD(num1, num2) {
    var candidates = [];
    var bigNum = null;

    if (num1 < num2) {
        candidates = getDivisors(num1);
        bigNum = num2;
    } else if (num1 > num2) {
        candidates = getDivisors(num2);
        bigNum = num1;
    } else {
        return num1;
    }
    for (let i = candidates.length - 1; i >= 0; i--) {
        if (0 == (bigNum % candidates[i])) {
            return (candidates[i]);
        }
    }
    return null;
}

function getGCD(num1, num2) {
    return (getGCD(num1, num2));
}

function getLCD(num1, num2) {
    var numerator = Math.abs(num1 * num2);
    var denominator = getGCD(num1, num2);
    
    if (0 == denominator) {
        return null;
    }
    return (numerator / denominator);
}

function isCoprime(num1, num2) {
    return (1 == getGCD(num1, num2));
}

function isRelativePrime(num1, num2) {
    return (isCoprime(num1, num2));
}

let num1 = 24;
let num2 = 54;
console.log("num1: " + num1 + ", num2: " + num2);
console.log(getDivisors(num1).toString());
console.log(getDivisors(num2).toString());
console.log(getGCD(num1, num2));
console.log(isCoprime(num1, num2));

num1 = 9;
num2 = 28;
console.log("num1: " + num1 + ", num2: " + num2);
console.log(getDivisors(num1).toString());
console.log(getDivisors(num2).toString());
console.log(getGCD(num1, num2));
console.log(isCoprime(num1, num2));

num1 = 234;
num2 = 123;
console.log("num1: " + num1 + ", num2: " + num2);
console.log(getDivisors(num1).toString());
console.log(getDivisors(num2).toString());
console.log(getGCD(num1, num2));
console.log(isCoprime(num1, num2));
