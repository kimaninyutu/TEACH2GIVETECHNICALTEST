function reverseInteger(n) {
    const reversed = parseInt(Math.abs(n).toString().split('').reverse().join(''));
    return n < 0 ? -reversed : reversed;
}
console.log(reverseInteger(500));
console.log(reverseInteger(-56));
