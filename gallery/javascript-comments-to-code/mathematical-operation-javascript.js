//addition of two numbers
function addition(a, b) {
    return a + b;
}

//subtraction of two numbers
function subtraction(a, b) {
    return a - b;
}

//multiplication of two numbers
function multiplication(a, b) {
    return a * b;
}

//division of two numbers
function division(a, b) {
    return a / b;
}

//determine if it's a prime number
function isPrime(num) {
    for (var i = 2; i < num; i++) {
        if (num % i === 0) {
            return false;
        }
    }
    return num > 1;
}