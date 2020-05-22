"use strict";

let SET = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M',
           'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z'];


class Caesar {

    constructor(set=null, n=null) {

        this.set = set;
        if (this.set == null)
            this.set = SET;
        if (n != null) {
            this.n = n;
        } else {
            this.n = this.set.length;
        }
        this.rset = {};
        for (let i = 0; i < this.set.length; i++) {
            this.rset[this.set[i]] = i;
        }




    }

    encrypt(P, shift=3) {
        for (const p of P) {
            console.log(p);
        }
    }

    decrypt(C, shift=3) {

    }

}

let cipher = new Caesar();

cipher.encrypt("Hello Squirrel", 3);