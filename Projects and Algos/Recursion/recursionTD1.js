// using recusion write function that returns the sum of intergers UP TO that number. 
// Example: rSigma(5) = 15 (1+2+3+4+5); rSigma(2.5) = 3 (1+2); rSigma(-1) = 0.
function sigma(num){
    if (num == 0) {
        return num;
    }
    return num + sigma(num -1)
}
// Given num, return the product of ints from 1 up to num. If less than zero, treat as zero. If not an integer, truncate. 
// Experts tell us 0! is 1. rFact(3) = 6 (1*2*3). Also, rFact(6.5) = 720 (1*2*3*4*5*6).
function factorial(num){
    if (num == 1) {
        return num;
    }
    return num * factorial(num -1);
}
