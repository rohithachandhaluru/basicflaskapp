# app.py

from flask import Flask, render_template, request

app = Flask(__name__)

def evod(n):
    if n % 2 == 0:
        print(f'{n} is even.\n')
        return f'{n} is even.'
    else:
        print(f'{n} is odd.\n')
        return f'{n} is odd.'

def rev(n):
    reversed_str = ''
    for digit in str(n):
        reversed_str = digit + reversed_str  # Add the current digit at the beginning
    print(f'Riverse of {n} is {reversed_str}\n')
    return reversed_str

def sumdig(n):
    total = 0
    for digit in str(n):
        total += int(digit)  # Convert each character back to an integer
    print(f'Sum of {n}: {total}\n')
    return total

def pallindrome(n):
    is_palindrome = True
    num_str = str(n)
    for i in range(len(num_str) // 2):
        if num_str[i] != num_str[-(i + 1)]:
            is_palindrome = False
            break
    print(f'Is {n} a palindrome? {is_palindrome}\n')
    return is_palindrome

def fact(n):
    res = 1
    for i in range(1, n + 1):
        res *= i
    print(f'Factorial of {n}: {res}\n')
    return res

def sum_n(n):
    total = 0
    for i in range(1, n + 1):
        total += i
    print(f'Sum of first {n} numbers: {total}\n')
    return total

def evsum(n):
    total = 0
    for i in range(1, n + 1):
        if i % 2 == 0:
            total += i
    print(f'Sum of first {n} even numbers: {total}\n')
    return total

def oddsum(n):
    total = 0
    for i in range(1, n + 1):
        if i % 2 == 1:
            total += i
    print(f'Sum of first {n} odd numbers: {total}\n')
    return total

def evcount(n):
    evens = []
    for i in range(1, n + 1):
        if i % 2 == 0:
            evens.append(i)
    print(f'First {n} even numbers: {evens}\n')
    return evens

def oddcount(n):
    odds = []
    for i in range(1, n + 1):
        if i % 2 == 1:
            odds.append(i)
    print(f'First {n} odd numbers: {odds}\n')
    return odds

def prime(n):
    count = 0
    for i in range(1, n + 1):
        if n % i == 0:
            count += 1
    is_prime = (count == 2)
    print(f'Is {n} prime? {is_prime}\n')
    return is_prime

def primeseries(n):
    primes = []
    for i in range(2, n + 1):
        is_prime = True
        for j in range(2, int(i**0.5) + 1):
            if i % j == 0:
                is_prime = False
                break
        if is_prime:
            primes.append(i)
    print(f'First {n} prime numbers: {primes}\n')
    return primes

def square(n):
    squares = []
    for i in range(1, n + 1):
        squares.append(i * i)
    print(f'Squares of first {n} numbers: {squares}\n')
    return squares

def cube(n):
    cubes = []
    for i in range(1, n + 1):
        cubes.append(i * i * i)
    print(f'Cubes of first {n} numbers: {cubes}\n')
    return cubes

@app.route('/', methods=['GET', 'POST'])
def home():
    if request.method == 'POST':
        n = int(request.form['number'])
        operation = request.form['operation']
        result = ""

        if operation == '1':
            result = evod(n)
        elif operation == '2':
            result = f'Reverse of {n} is: {rev(n)}'
        elif operation == '3':
            result = f'Sum of {n}: {sumdig(n)}'
        elif operation == '4':
            result = f'Is palindrome: {pallindrome(n)}'
        elif operation == '5':
            result = f'Factorial of {n} : {fact(n)}'
        elif operation == '6':
            result = f'Sum of first {n} numbers: {sum_n(n)}'
        elif operation == '7':
            result = f'Sum of first {n} even numbers: {evsum(n)}'
        elif operation == '8':
            result = f'Sum of first {n} odd numbers: {oddsum(n)}'
        elif operation == '9':
            result = f'First {n} even numbers: {evcount(n)}'
        elif operation == '10':
            result = f'First {n} odd numbers: {oddcount(n)}'
        elif operation == '11':
            result = f'Is prime: {prime(n)}'
        elif operation == '12':
            result = f'First {n} prime numbers: {primeseries(n)}'
        elif operation == '13':
            result = f'Squares of first {n} numbers: {square(n)}'
        elif operation == '14':
            result = f'Cubes of first {n} numbers: {cube(n)}'
        elif operation == '15':
            results = []
            results.append(evod(n))
            results.append(rev(n))
            results.append(f'Sum of Digits: {sumdig(n)} \n')
            results.append(f'Palindrome: {pallindrome(n)} \n')
            results.append(f'Factorial: {fact(n)}\n')
            results.append(f'Sum of First n Numbers: {sum_n(n)} \n')
            results.append(f'Sum of First n Even Numbers: {evsum(n)}\n')
            results.append(f'Sum of First n Odd Numbers: {oddsum(n)}\n')
            results.append(f'First n Even Numbers: {evcount(n)}\n')
            results.append(f'First n Odd Numbers: {oddcount(n)}\n')
            results.append(f'Is Prime: {prime(n)}\n')
            results.append(f'First n Prime Numbers: {primeseries(n)}\n')
            results.append(f'Squares of First n Numbers: {square(n)}\n')
            results.append(f'Cubes of First n Numbers: {cube(n)}\n')
            
            # Join all results with line breaks
            result = "\n".join(results)

        return render_template('index.html', result=result, n=n)

    return render_template('index.html', result="", n=None)

if __name__ == '__main__':
    app.run(debug=False,host='0.0.0.0')
