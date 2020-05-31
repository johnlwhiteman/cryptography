"use strict";

const CHARS = ['A', 'B', 'C', 'D', 'E', 'F', 'G',
               'H', 'I', 'J', 'K', 'L', 'M', 'N',
               'O', 'P', 'Q', 'R', 'S', 'T', 'U',
               'V', 'W', 'X', 'Y', 'Z'];

const SHIFT = 3;

function mapChars(chars) {
    let mChars = {};
    for (let i = 0; i < chars.length; i++)
        mChars[chars[i]] = i;
    return mChars;
}

function decrypt(c, shift=SHIFT, chars=CHARS) {
    c = c.toUpperCase();
    let p = '';
    let mChars = mapChars(chars);
    let n = chars.length;
    for (let i = 0; i < c.length; i++) {
        let j = mChars[c[i]];
        if (typeof j !== 'undefined')
            p += chars[(j - shift + n) % n];
        else
            p += c[i];
    }
    return p;
}

function encrypt(p, shift=SHIFT, chars=CHARS) {
    p = p.toUpperCase();
    let c = '';
    let mChars = mapChars(chars);
    let n = chars.length;
    for (let i = 0; i < p.length; i++) {
        let j = mChars[p[i]];
        if (typeof j !== 'undefined')
            c += chars[(j + shift) % n];
        else
            c += p[i];
    }
    return c;
}

let p1 = "I am Z the World Leader Mr. X!";
let c = encrypt(p1);
let p2 = decrypt(c);
console.log(p1);
console.log(c);
console.log(p2);