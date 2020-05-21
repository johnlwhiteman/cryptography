"use strict";

var gcd = require('./gcd.js');

class Affine {

    constructor(A, B, N, set = null) {
        this._A = A;
        this._B = B;
        this._N = N;
        this._set = set;
        this._rset = {};
        if (set == null)
            this._set = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M',
                         'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z'];
        for (let i = 0; i < this._N; i++) {
            this._rset[this._set[i]] = i;
        }
    }

    get A() {
        return this._A;
    }

    get B() {
        return this._B;
    }

    get N() {
        return this._N;
    }

    get rset() {
        return this._rset;
    }

    get set() {
        return this._set;
    }

    get setSize() {
        return this._set.length;
    }

    encrypt(P) {
        this.verify();
        let p = P.toUpperCase();

    }

    decrypt(C) {
        throw("Affine.decrypt is not implemented yet");
    }

    verify() {
        if (!gcd.isCoprime(this._A, this._set.length)) {
            throw(`A is not coprime with the size of the set: ${this._A}, ${this._set.length}`);
        }
        if (this._B < 0 || this._B > (this._N - 1)) {
            throw(`B is not >= 0 or < N - 1: ${this._B}`);
        }
    }
}


let cipher = new Affine(27, 3, 26);

cipher.encrypt("I am world leader pretend");
