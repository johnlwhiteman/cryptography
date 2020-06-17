"use  strict";

function getCyclicGroup(n) {
    let group = [];
    for (let i = 0; i < n; i++)
        group.push(i);
    return group;
}

function getCyclicSubGroup(g, n) {
    let group = [];
    let x = g;

    if (0 == g)
        return [0];
    else if (1 == g)
        return getCyclicGroup(n);

    while(true) {
        let y = x % n;
        if (group.includes(y))
            break;
        group.push(y);
        x += g;
    }
    return group;
}

function getCyclicSubGroups(n) {
    let groups = [];
    for (let g = 0; g < n; g++)
        groups.push(getCyclicSubGroup(g, n))
    return groups
}

console.log(getCyclicGroup(7));
console.log(getCyclicSubGroups(7));
