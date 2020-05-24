"use strict";

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

function isPrimeByTrialDivision(n) {
    for (let i = 2; i <= Math.sqrt(n); i++) {
        if (0 == n % i) {
            return false;
        }
    }
    return true;
}

function getPrimesByTrialDivsion(n) {
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

console.log(getPrimesByTrialDivsion(100));
console.log(getPrimesBySieveOfEratosthenes(100));
console.log(getPrimesBySieveOfEratosthenesAsGrid(100));