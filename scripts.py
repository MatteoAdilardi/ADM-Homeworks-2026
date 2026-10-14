# Introduction

'''
Say "Hello, World!" With Python
'''
if __name__ == "__main__":
    print("Hello, World!")

'''
If-Else
'''
import math
import os
import random
import re
import sys

if __name__ == "__main__":
    n = int(input().strip())
    if n % 2 != 0:
        print("Weird")
    elif n % 2 == 0 and (2 <= n <= 5):
        print("Not Weird")
    elif n % 2 == 0 and (6 <= n <= 20):
        print("Weird")
    elif n % 2 == 0 and n > 20:
        print("Not Weird")

'''
Arithmetic Operators
'''
if __name__ == "__main__":
    a = int(input())
    b = int(input())
    print(f"{a + b}\n{a - b}\n{a * b}")

'''
Python: Division
'''
if __name__ == '__main__':
    a = int(input())
    b = int(input())
    print(f"{a//b}\n {a/b}")

'''
Loops
'''
if __name__ == '__main__':
    n = int(input())
    for i in range (0,n):
        print(i**2)

'''
Write a function
'''
def is_leap(year):
    leap = False

    if year % 400 == 0:
        return True
    elif year % 100 == 0:
        return False
    elif year % 4 == 0:
        return True

    return leap

year = int(input())
print(is_leap(year))

'''
Print Function
'''
if __name__ == '__main__':
    n = int(input())
    for i in range (1, n+1):
        print(i, end = "")

# Data types

'''
List Comprehensions
'''
if __name__ == '__main__':
    x = int(input())
    y = int(input())
    z = int(input())
    n = int(input())

    result = [
        [i, j, k]
        for i in range(x + 1)
        for j in range(y + 1)
        for k in range(z + 1)
        if i + j + k != n
    ]

    print(result)

'''
Find the Runner-Up Score!
'''
if __name__ == '__main__':
    n = int(input())
    arr = map(int, input().split())
    arr = list(arr)
    if n == len(arr):
        arr_ordinati_univoci = sorted(set(arr))
        print(arr_ordinati_univoci[-2])
    else:
        print("Input sbagliato")

'''
Nested Lists
'''
if __name__ == '__main__':
    students = []
    for _ in range(int(input())):
        name = input()
        score = float(input())
        students.append([name, score])
    scores = []
    for student in students:
        scores.append(student[1])
    scores = sorted(set(scores))
    second_lowest  = scores[1]
    
    print_student = []
    for student in students:
        if student[1] == second_lowest :
            print_student.append(student[0])
    for student in sorted(print_student):
        print(student)
    
'''
Finding the percentage
'''
if __name__ == '__main__':
    n = int(input())
    student_marks = {}
    for _ in range(n):
        name, *line = input().split()
        scores = list(map(float, line))
        student_marks[name] = scores
    query_name = input()
    
    scores = student_marks[query_name]
    
    media = sum(scores) / len(scores)
    
    print(f"{media:.2f}")

'''
Lists
'''
if __name__ == '__main__':
    N = int(input())

    my_list = []

    for _ in range(N):
        command = input().split()

        if command[0] == "insert":
            my_list.insert(int(command[1]), int(command[2]))

        elif command[0] == "print":
            print(my_list)

        elif command[0] == "remove":
            my_list.remove(int(command[1]))

        elif command[0] == "append":
            my_list.append(int(command[1]))

        elif command[0] == "sort":
            my_list.sort()

        elif command[0] == "pop":
            my_list.pop()

        elif command[0] == "reverse":
            my_list.reverse()

'''
Tuples
'''
if __name__ == '__main__':
    n = int(input())

    integer_list = tuple(map(int, input().split()))

    print(hash(integer_list))

# Strings

'''
sWAP cASE
'''
def swap_case(s):
    reversal_s = ''
    for i in s:
        if i.islower():
            i = i.upper()
            reversal_s = reversal_s +i 
        elif i.isupper():
            i = i.lower()
            reversal_s = reversal_s + i 
        else: 
            reversal_s = reversal_s + i 
    return reversal_s

if __name__ == '__main__':
    s = input()
    result = swap_case(s)
    print(result)

'''
String Split and Join
'''
def split_and_join(line):
    line = line.split(" ")
    line = "-".join(line)
    
    return line

if __name__ == '__main__':
    line = input()
    result = split_and_join(line)
    print(result)

'''
What's Your Name?
'''
def print_full_name(first, last):
    print(f"Hello {first} {last}! You just delved into python.")
if __name__ == '__main__':
    first_name = input()
    last_name = input()
    print_full_name(first_name, last_name)

'''
Mutations
'''
def mutate_string(string, position, character):
    string = string[:position] + character + string[position+1:]
    return string

if __name__ == '__main__':
    s = input()
    i, c = input().split()
    s_new = mutate_string(s, int(i), c)
    print(s_new)

'''
Find a string
'''
def count_substring(string, sub_string):
    count = 0
    
    length_substring = len(sub_string)
    
    for i in range(len(string) - len(sub_string) + 1):
        if string[i:length_substring+i] == sub_string:
            count += 1
    
    return count 

if __name__ == '__main__':
    string = input().strip()
    sub_string = input().strip()
    
    count = count_substring(string, sub_string)
    print(count)

'''
String Validators
'''
if __name__ == '__main__':
    s = input()

    print(any(char.isalnum() for char in s))
    print(any(char.isalpha() for char in s))
    print(any(char.isdigit() for char in s))
    print(any(char.islower() for char in s))
    print(any(char.isupper() for char in s))

'''
Text Alignment
'''
thickness = int(input())
c = 'H'

for i in range(thickness):
    print((c * i).rjust(thickness - 1) + c + (c * i).ljust(thickness - 1))

for i in range(thickness + 1):
    print((c * thickness).center(thickness * 2) +
          (c * thickness).center(thickness * 6))

for i in range((thickness + 1) // 2):
    print((c * thickness * 5).center(thickness * 6))

for i in range(thickness + 1):
    print((c * thickness).center(thickness * 2) +
          (c * thickness).center(thickness * 6))

for i in range(thickness):
    print(((c * (thickness - i - 1)).rjust(thickness) +
           c +
           (c * (thickness - i - 1)).ljust(thickness)).rjust(thickness * 6))


'''
Text Wrap
'''
import textwrap

def wrap(string, max_width):
    return "\n".join(textwrap.wrap(string, max_width))

if __name__ == '__main__':
    string, max_width = input(), int(input())
    result = wrap(string, max_width)
    print(result)

'''
Designer Door Mat
'''
if __name__ == '__main__':
    N, M = map(int, input().split())

    for i in range(N // 2):
        pattern = '.|.' * (2 * i + 1)
        print(pattern.center(M, '-'))

    print('WELCOME'.center(M, '-'))

    for i in range(N // 2 - 1, -1, -1):
        pattern = '.|.' * (2 * i + 1)
        print(pattern.center(M, '-'))

'''
String Formatting
'''
def print_formatted(number):
    width = len(bin(number)[2:])

    for i in range(1, number + 1):
        print(
            str(i).rjust(width),
            oct(i)[2:].rjust(width),
            hex(i)[2:].upper().rjust(width),
            bin(i)[2:].rjust(width)
        )

if __name__ == '__main__':
    n = int(input())
    print_formatted(n)

'''
Alphabet Rangoli
'''
def print_rangoli(size):
    lettere = "abcdefghijklmnopqrstuvwxyz"
    larghezza = 4 * size - 3

    righe = []

    for i in range(size):
        sinistra = lettere[size - 1:size - i - 1:-1]
        destra = lettere[size - i - 1:size]

        riga = "-".join(sinistra + destra)
        riga = riga.center(larghezza, "-")

        righe.append(riga)

    for riga in righe:
        print(riga)

    for riga in righe[-2::-1]:
        print(riga)


if __name__ == '__main__':
    n = int(input())
    print_rangoli(n)

'''
Capitalize!
'''
def solve(s):
    words = s.split(' ')

    result = []

    for word in words:
        if word != '':
            word = word[0].upper() + word[1:]

        result.append(word)

    return ' '.join(result)


if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    s = input()

    result = solve(s)

    fptr.write(result + '\n')

    fptr.close()

'''
The Minion Game
'''
def minion_game(string):
    vowels = "AEIOU"

    kevin = 0
    stuart = 0

    for i in range(len(string)):
        if string[i] in vowels:
            kevin += len(string) - i
        else:
            stuart += len(string) - i

    if kevin > stuart:
        print("Kevin", kevin)
    elif stuart > kevin:
        print("Stuart", stuart)
    else:
        print("Draw")


if __name__ == '__main__':
    s = input()
    minion_game(s)

'''
Merge the Tools!
'''
def merge_the_tools(string, k):

    for i in range(0, len(string), k):
        part = string[i:i+k]

        result = ""

        for char in part:
            if char not in result:
                result += char

        print(result)


if __name__ == '__main__':
    string, k = input(), int(input())
    merge_the_tools(string, k)

# Sets 
'''
Introduction to Sets
'''
def average(array):
    distinct_values = set(array)
    return sum(distinct_values) / len(distinct_values)
    
if __name__ == '__main__':
    n = int(input())
    arr = list(map(int, input().split()))
    result = average(arr)
    print(result)

'''
No Idea!
'''
if __name__ == '__main__':
    n,m = set(map(int, input().split()))
    array = list(map(int, input().split()))
    A = set(map(int, input().split()))
    B = set(map(int, input().split()))
    
    happines = 0
    
    for x in array:
        if x in A:
            happines += 1
        elif x in B:
            happines -= 1 
    
    print(happines)

'''
Symmetric Difference
'''
if __name__ == '__main__':
    M = int(input())
    a = set(map(int, input().split()))

    N = int(input())
    b = set(map(int, input().split()))

    result = a.symmetric_difference(b)

    for value in sorted(result):
        print(value)

'''
Set .add()
'''
if __name__ == '__main__':
    n = int(input())
    
    list_of_countries = set()
    
    for i in range (n):
        countries = input()
        list_of_countries.add(countries)
    
   
    numer_of_countries = len(list_of_countries)
    
    
    print(numer_of_countries)

'''
Set .discard(), .remove() & .pop()
'''
if __name__ == '__main__':
    n = int(input())
    s = set(map(int, input().split()))

    number_of_operations = int(input())

    for i in range(number_of_operations):
        command_input = input().split()

        if command_input[0] == 'pop':
            s.pop()
        elif command_input[0] == 'discard':
            s.discard(int(command_input[1]))
        elif command_input[0] == 'remove':
            s.remove(int(command_input[1]))

    print(sum(s))

'''
Set .union() Operation
'''
if __name__ == '__main__':
    number_of_students_eng = int(input())
    id_std_eng = set(map(int, input().split()))
    
    number_of_students_fr = int(input())
    id_std_fr = set(map(int, input().split()))
    
    id_both_sub = id_std_eng.union(id_std_fr)
    
    print(len(id_both_sub))

'''
Set .intersection() Operation
'''
if __name__ == '__main__':
    number_of_students_eng = int(input())
    id_std_eng = set(map(int, input().split()))
    
    number_of_students_fr = int(input())
    id_std_fr = set(map(int, input().split()))
    
    id_both_sub = id_std_eng.intersection(id_std_fr)
    
    print(len(id_both_sub))

'''
Set .difference() Operation
'''
if __name__ == '__main__':
    number_of_students_eng = int(input())
    id_std_eng = set(map(int, input().split()))
    
    number_of_students_fr = int(input())
    id_std_fr = set(map(int, input().split()))
    
    id_both_sub = id_std_eng.difference(id_std_fr)
    
    print(len(id_both_sub))

'''
Set .symmetric_difference() Operation
'''
if __name__ == '__main__':
    number_of_students_eng = int(input())
    id_std_eng = set(map(int, input().split()))
    
    number_of_students_fr = int(input())
    id_std_fr = set(map(int, input().split()))
    
    id_both_sub = id_std_eng.symmetric_difference(id_std_fr)
    
    print(len(id_both_sub))

'''
Set Mutations
'''
if __name__ == '__main__':
    n = int(input())
    s = set(map(int, input().split()))

    number_of_operations = int(input())

    for _ in range(number_of_operations):
        command_input = input().split()
        operation = command_input[0]

        other_set = set(map(int, input().split()))

        if operation == 'intersection_update':
            s.intersection_update(other_set)

        elif operation == 'update':
            s.update(other_set)

        elif operation == 'symmetric_difference_update':
            s.symmetric_difference_update(other_set)

        elif operation == 'difference_update':
            s.difference_update(other_set)

    print(sum(s))

'''
The Captain's Room
'''
if __name__ == '__main__':
    k = int(input())
    rooms = list(map(int, input().split()))

    unique_rooms = set(rooms)

    captain_room = (k * sum(unique_rooms) - sum(rooms)) // (k - 1)

    print(captain_room)

'''
Check Subset
'''
if __name__ == '__main__':
    T = int(input())

    for _ in range(T):
        nA = int(input())
        A = set(map(int, input().split()))

        nB = int(input())
        B = set(map(int, input().split()))

        print(A.issubset(B))

'''
Check Strict Superset
'''
if __name__ == '__main__':
    A = set(map(int, input().split()))
    n = int(input())

    result = True

    for _ in range(n):
        other_set = set(map(int, input().split()))

        if not A.issuperset(other_set) or A == other_set:
            result = False
            break

    print(result)

# Collections

'''
Collections.Counter()
'''
x = int(input())

shoes = list(map(int, input().split()))

n = int(input())

money = 0

for _ in range(n):
    size, price = map(int, input().split())

    if size in shoes:
        money += price
        shoes.remove(size)

print(money)

'''
DefaultDict Tutorial
'''
from collections import defaultdict

n, m = map(int, input().split())

posizioni = defaultdict(list)

for i in range(1, n + 1):
    parola = input()
    posizioni[parola].append(i)

for _ in range(m):
    parola = input()

    if parola in posizioni:
        print(*posizioni[parola])
    else:
        print(-1)

'''
Collections.namedtuple()
'''
from collections import namedtuple

n = int(input())
columns = input().split()

Student = namedtuple('Student', columns)

total_marks = 0

for i in range(n):
    data = input().split()
    student = Student(*data)
    total_marks += int(student.MARKS)

average = total_marks / n

print(f"{average:.2f}")

'''
Collections.OrderedDict()
'''
from collections import OrderedDict

n = int(input())

items = OrderedDict()

for i in range(n):
    data = input().split()

    price = int(data[-1])
    item_name = " ".join(data[:-1])

    if item_name in items:
        items[item_name] += price
    else:
        items[item_name] = price

for item_name, total_price in items.items():
    print(item_name, total_price)

'''
Word Order
'''
from collections import OrderedDict

n = int(input())
words = OrderedDict()

for i in range(n):
    word = input().strip()

    if word in words:
        words[word] += 1
    else:
        words[word] = 1

print(len(words))
print(*words.values())

'''
Collections.deque()
'''
from collections import deque

n = int(input())
d = deque()

for i in range(n):
    command = input().split()

    if command[0] == "append":
        d.append(command[1])

    elif command[0] == "appendleft":
        d.appendleft(command[1])

    elif command[0] == "pop":
        d.pop()

    elif command[0] == "popleft":
        d.popleft()

print(*d)

'''
Company Logo
'''
import math
import os
import random
import re
import sys

if __name__ == '__main__':
    s = input()

    conteggi = {}

    for lettera in s:
        if lettera in conteggi:
            conteggi[lettera] += 1
        else:
            conteggi[lettera] = 1
    ordinati = sorted(conteggi.items(), key=lambda x: (-x[1], x[0]))

    for lettera, frequenza in ordinati[:3]:
        print(lettera, frequenza)

'''
Piling Up!
'''
from collections import deque

numero_test = int(input())

for _ in range(numero_test):
    numero_cubi = int(input())
    cubi = deque(map(int, input().split()))

    cima = float("inf")
    possibile = True

    while cubi:
        sinistra = cubi[0]
        destra = cubi[-1]

        if sinistra >= destra:
            scelto = cubi.popleft()
        else:
            scelto = cubi.pop()

        if scelto <= cima:
            cima = scelto
        else:
            possibile = False
            break

    if possibile:
        print("Yes")
    else:
        print("No")

# Date and Time

'''
Calendar Module
'''
import calendar

if __name__ == '__main__':
    month, day, year = map(int, input().split())

    day_index = calendar.weekday(year, month, day)
    day_name = calendar.day_name[day_index]

    print(day_name.upper())

'''
Time Delta
'''
import math
import os
import random
import re
import sys
from datetime import datetime

def time_delta(t1, t2):
    format_string = "%a %d %b %Y %H:%M:%S %z"

    date1 = datetime.strptime(t1, format_string)
    date2 = datetime.strptime(t2, format_string)

    difference = abs((date1 - date2).total_seconds())

    return str(int(difference))


if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    t = int(input())

    for t_itr in range(t):
        t1 = input()
        t2 = input()

        delta = time_delta(t1, t2)

        fptr.write(delta + '\n')

    fptr.close()

# Exceptions

'''
Exceptions
'''
if __name__ == '__main__':
    T = int(input())

    for _ in range(T):
        a, b = input().split()

        try:
            print(int(a) // int(b))

        except ZeroDivisionError as e:
            print("Error Code:", e)

        except ValueError as e:
            print("Error Code:", e)

# Built-ins

'''
Zipped!
'''
n, x = map(int, input().split())

subjects = []

for i in range(x):
    subjects.append(list(map(float, input().split())))

for student_marks in zip(*subjects):
    average = sum(student_marks) / x
    print(average)

'''
Athlete Sort
'''

import math
import os
import random
import re
import sys



if __name__ == '__main__':
    nm = input().split()

    n = int(nm[0])

    m = int(nm[1])

    arr = []

    for _ in range(n):
        arr.append(list(map(int, input().rstrip().split())))

    k = int(input())

    arr.sort(key=lambda row: row[k])
    
    for row in arr:
        print(*row)

'''
ginortS
'''

if __name__ == '__main__':
    s = input()

    lowercase = []
    uppercase = []
    odd_digits = []
    even_digits = []

    for c in s:
        if c.islower():
            lowercase.append(c)

        elif c.isupper():
            uppercase.append(c)

        elif c.isdigit():
            if int(c) % 2 == 1:
                odd_digits.append(c)
            else:
                even_digits.append(c)

    lowercase.sort()
    uppercase.sort()
    odd_digits.sort()
    even_digits.sort()

    result = lowercase + uppercase + odd_digits + even_digits

    print("".join(result))

# Python Functionals

'''
Map and Lambda Function
'''
cube = lambda x: x ** 3

def fibonacci(n):
    numbers = []

    a = 0
    b = 1

    for i in range(n):
        numbers.append(a)

        next_number = a + b
        a = b
        b = next_number

    return numbers

if __name__ == '__main__':
    n = int(input())
    print(list(map(cube, fibonacci(n))))

'''
Regex and Parsing Challenges
'''