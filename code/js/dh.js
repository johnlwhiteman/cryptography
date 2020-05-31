"use strict";
var prime = require('./prime.js');
var order = require('./order.js');

function calculateKey(s, g, n) {
    return g**s % n;
}

function areParametersValid(g, n) {
    // Test if n is prime
    if (!prime.isPrime(n)) {
        console.log(`Error: ${n} is not a prime number`);
        return false;
    }

    // Test if g is a primitive root modulo n
    if (!order.isPrimitiveRootModulo(g, n)) {
        console.log(`Error: ${g} is not a primitive root modulo ${n}`);
        return false;
    }

    return true;
}

function test() {
    let n = 23;
    let g = 5;
    let aliceSecret = 4;
    let bobSecret = 3;

    if (!areParametersValid(g, n))
        return;

    // Generate the public keys
    let alicePubKey = calculateKey(aliceSecret, g, n);
    let bobPubKey = calculateKey(bobSecret, g, n);

    console.log("Alice's Public Key: " + alicePubKey);
    console.log("Bob's Public Key: " + bobPubKey);

    // Calculate the shared secret
    let alicePriKey = calculateKey(aliceSecret, bobPubKey, n);
    let bobSPriKey = calculateKey(bobSecret, alicePubKey, n);

    console.log("\nKeys exchanged\n");

    console.log("Alice's Shared Secret: " + alicePriKey);
    console.log("Bob's Shared Secret: " + bobSPriKey);
}

test();