"use strict";
// https://norvig.com/mayzner.html

/**
 * Sort object properties (only own properties will be sorted).
 * @param {object} obj object to sort properties
 * @param {string|int} sortedBy 1 - sort object properties by specific value.
 * @param {bool} isNumericSort true - sort object properties as numeric value, false - sort as string value.
 * @returns {Array} array of items in [[key,value],[key,value],...] format.
 */



const LETTERS2 = {
"E": 12.49,
"T": 9.28,
"A": 8.04,
"O": 7.64,
"I": 7.57,
"N": 7.23,
"S": 6.51,
"R": 6.28,
"H": 5.05,
"L": 4.07,
"D": 3.82,
"C": 3.34,
"U": 2.73,
"M": 2.51,
"F": 2.40,
"P": 2.14,
"G": 1.87,
"W": 1.68,
"Y": 1.66,
"B": 1.48,
"V": 1.05,
"K": 0.54,
"X": 0.23,
"J": 0.16,
"Q": 0.12,
"Z": 0.09}

const LETTERS = {
"A": 8.04,
"B": 1.48,
"C": 3.34,
"D": 3.82,
"E": 12.49,
"F": 2.40,
"G": 1.87,
"H": 5.05,
"I": 7.57,
"J": 0.16,
"K": 0.54,
"L": 4.07,
"M": 2.51,
"N": 7.23,
"O": 7.64,
"P": 2.14,
"Q": 0.12,
"R": 6.28,
"S": 6.51,
"T": 9.28,
"U": 2.73,
"V": 1.05,
"W": 1.68,
"X": 0.23,
"Y": 1.66,
"Z": 0.09
}

let sum = 0.000;
let cnt = 0;
for (let letter in LETTERS) {
    console.log(`${letter}: ${LETTERS[letter]}`);
    sum += LETTERS[letter];
    ++cnt;
}

console.log(sum);
console.log(cnt); 


var items = Object.keys(LETTERS).map(function(key) {
  return [key, LETTERS[key]];
});


items.sort(function(first, second) {
    return second[1] - first[1];
}); 

for (let i in items) {
    console.log(`${i}: ${items[i]}`);
}
