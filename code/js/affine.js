"use strict";

var gcd = require('./gcd.js');

var CHARACTERS;

class Affine {
    constructor(A, B, characters = null) {
        this._characters = characters;
        if (this._characters == null)
            this._characters = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M',
                'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z'];
        this._N = this._characters.length;
    }

    get characters() {
        return this._characters;
    }

    get N() {
        return this._N;
    }

    encrypt(P) {
        console.log(gcd.isCoprime(1, 2));
    }

    decrypt(C) {


    }

}


let cipher = new Affine();

cipher.encrypt();