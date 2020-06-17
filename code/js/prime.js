"use strict";
var gcd = require('./gcd.js');
var math = require('./math.js');

var PRIMES = [2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37, 41, 43, 47, 53, 59, 61, 67, 71, 73, 79, 83, 89, 97];
var CARMICHAEL = [561, 1105, 1729, 2465, 2821, 6601, 8911, 10585, 15841, 29341, 41041, 46657, 52633, 62745, 63973, 75361];

function getPrimesBySieveOfEratosthenes(n) {
    let primes = [];
    let grid = getPrimesBySieveOfEratosthenesAsGrid(n);
    for(let i = 0; i < grid.length; i++) {
        if (grid[i]["p"]) {
            primes.push(grid[i]["n"]);
        }
    }
    if (primes.length < 1) {
        return null;
    }
    return primes;
}

function getPrimesBySieveOfEratosthenesAsGrid(n) {
    let grid = [{"n":1, "p":false}];
    for (let i = 2; i <= n; i++) {
        grid.push({"n":i, "p":null});
    }
    for (let i = 1; i < n; i++) {
        if (grid[i]["p"] != null) {
            continue
        }
        grid[i]["p"] = true;
        let m = grid[i]["n"];
        let j = m;
        let k = m * j;
        while (k <= n) {
            grid[k-1]["p"] = false;
            k = m * j;
            j++;
        }
    }
    return grid;
}

function getPrimesByTrialDivision(n) {
    let primes = [];
    for (let i = 2; i <= n; i++) {
        if (isPrimeByTrialDivision(i)) {
            primes.push(i);
        }
    }
    if (primes.length < 1) {
        return null;
    }
    return primes;
}

function isPrimeByTrialDivision(n) {
    for (let i = 2; i <= Math.sqrt(n); i++)
        if (0 == n % i) return false;
    return n > 1;
}

function isLikelyPrimeByMillerRabin(p, k) {
    if (p === 2 || p === 3)
        return true;
    if (p < 2 || p % 2 === 0)
        return false;

    // write n as 2^s·d + 1 with d odd (by factoring out powers of 2 from p − 1)
    let d = p - 1;
    let s = 0;
    while (0 == d % 2) {
        ++s;
        d /= 2;
    }
    for (let i = 0; i < k; i++) {
        let a = math.getRandomNumberInRange(2, p - 2);
        let x = math.getModularPower(a, d, p)
        if (x === 1 || x === p - 1) {
            continue;
        }
        let flag = false;
        for (let i = 0; i < s; i++) {
            x = math.getModularPower(x, 2, p);
            if (x === p - 1) {
                flag = true;
                break;
            }
        }
        if (flag) continue;
        return false;
    }
    return true;
}

// If a is not a multiple of p then a^p - a is a multiple of p
// More k's the more betta ... see CARMICHAEL
// https://en.wikipedia.org/wiki/Fermat_primality_test
function isLikelyPrimeByFermat(p, k = 3) {
    if (p == 2 || p == 3)
        return true;
    if (p < 2 || p % 2 == 0)
        return false;
    while(k > 0) {
        let a = math.getRandomNumberInRange(2, p - 1);
        let x = math.getModularPower(a, p - 1, p);
        if (x !== 1) {
            return false;
        }
        --k;
    }
    return true;
}

function test() {
    for(let i = 0; i < PRIMES.length; i++) {
        let p = PRIMES[i];
        console.log(p);
        console.log(isLikelyPrimeByMillerRabin(p, 3));
    }
}

module.exports = {
    getPrimesBySieveOfEratosthenes,
    getPrimesBySieveOfEratosthenesAsGrid,
    getPrimesByTrialDivision,
    isLikelyPrimeByFermat,
    isLikelyPrimeByMillerRabin,
    isPrimeByTrialDivision
};
