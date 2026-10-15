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

# Regex and Parsing Challenges

'''
Detect Floating Point Number
'''
import re

T = int(input())

for i in range(T):
    N = input()

    pattern = r'^[+-]?[0-9]*\.[0-9]+$'

    if re.fullmatch(pattern, N):
        print(True)
    else:
        print(False)

'''
Re.split()
'''
regex_pattern = r"[,.]" 

import re
print("\n".join(re.split(regex_pattern, input())))

'''
Group(), Groups() & Groupdict()
'''
import re

s = input()

risultato = re.search(r"([a-zA-Z0-9])\1", s)

if risultato:
    print(risultato.group(1))
else:
    print(-1)

'''
Re.findall() & Re.finditer()
'''
import re

s = input()

risultati = re.findall(r"(?<=[^AEIOUaeiou])([AEIOUaeiou]{2,})(?=[^AEIOUaeiou])", s)

if risultati:
    for risultato in risultati:
        print(risultato)
else:
    print(-1)

'''
Re.start() & Re.end()
'''
import re

s = input()
k = input()

trovato = False

for risultato in re.finditer(r'(?={})'.format(re.escape(k)), s):
    inizio = risultato.start()
    fine = inizio + len(k) - 1

    print((inizio, fine))
    trovato = True

if not trovato:
    print((-1, -1))

'''
Regex Substitution
'''
import re

numero_righe = int(input())

for _ in range(numero_righe):
    riga = input()

    riga = re.sub(r"(?<= )&&(?= )", "and", riga)
    riga = re.sub(r"(?<= )\|\|(?= )", "or", riga)

    print(riga)

'''
Validating Roman Numerals
'''
regex_pattern = r"^M{0,3}(CM|CD|D?C{0,3})(XC|XL|L?X{0,3})(IX|IV|V?I{0,3})$"

import re
print(str(bool(re.match(regex_pattern, input()))))

'''
Validating phone numbers
'''
import re

numero_test = int(input())

for _ in range(numero_test):
    numero = input()

    if re.match(r"^[789]\d{9}$", numero):
        print("YES")
    else:
        print("NO")

'''
Validating and Parsing Email Addresses
'''
import re
import email.utils

numero_email = int(input())

for _ in range(numero_email):
    riga = input()

    nome, indirizzo = email.utils.parseaddr(riga)

    if re.match(r"^[A-Za-z][A-Za-z0-9._-]*@[A-Za-z]+\.[A-Za-z]{1,3}$", indirizzo):
        print(email.utils.formataddr((nome, indirizzo)))

'''
Hex Color Code
'''
import re

numero_righe = int(input())

dentro_blocco = False

for _ in range(numero_righe):
    riga = input()

    if "{" in riga:
        dentro_blocco = True

    if dentro_blocco:
        colori = re.findall(r"#[0-9a-fA-F]{3}(?:[0-9a-fA-F]{3})?", riga)

        for colore in colori:
            print(colore)

    if "}" in riga:
        dentro_blocco = False

'''
HTML Parser - Part 1
'''
from html.parser import HTMLParser

class MyHTMLParser(HTMLParser):

    def handle_starttag(self, tag, attrs):
        print("Start :", tag)

        for name, value in attrs:
            print("->", name, ">", value)

    def handle_endtag(self, tag):
        print("End   :", tag)

    def handle_startendtag(self, tag, attrs):
        print("Empty :", tag)

        for name, value in attrs:
            print("->", name, ">", value)


N = int(input())

parser = MyHTMLParser()

for i in range(N):
    line = input()
    parser.feed(line)

'''
HTML Parser - Part 2
'''
from html.parser import HTMLParser

class MyHTMLParser(HTMLParser):

    def handle_comment(self, data):
        if '\n' in data:
            print(">>> Multi-line Comment")
        else:
            print(">>> Single-line Comment")
        print(data)

    def handle_data(self, data):
        if data != '\n':
            print(">>> Data")
            print(data)


html = ""
for i in range(int(input())):
    html += input().rstrip()
    html += '\n'

parser = MyHTMLParser()
parser.feed(html)
parser.close()

'''
Detect HTML Tags, Attributes and Attribute Values
'''
from html.parser import HTMLParser

class MyHTMLParser(HTMLParser):

    def handle_starttag(self, tag, attrs):
        print(tag)

        for name, value in attrs:
            print("->", name, ">", value)

    def handle_startendtag(self, tag, attrs):
        print(tag)

        for name, value in attrs:
            print("->", name, ">", value)


parser = MyHTMLParser()

n = int(input())

for i in range(n):
    html = input()
    parser.feed(html)

parser.close()

'''
Validating UID
'''
T = int(input())

for i in range(T):
    uid = input()

    maiuscole = 0
    numeri = 0
    valido = True

    if len(uid) != 10:
        valido = False

    if len(set(uid)) != 10:
        valido = False

    for carattere in uid:
        if carattere.isupper():
            maiuscole += 1

        if carattere.isdigit():
            numeri += 1

        if not carattere.isascii() or not carattere.isalnum():
            valido = False

    if maiuscole < 2:
        valido = False

    if numeri < 3:
        valido = False

    if valido:
        print("Valid")
    else:
        print("Invalid")

'''
Validating Credit Card Numbers
'''
import re

N = int(input())

for i in range(N):
    carta = input()
    valido = True

    pattern = r'[456][0-9]{15}|[456][0-9]{3}(-[0-9]{4}){3}'

    if not re.fullmatch(pattern, carta):
        valido = False

    numeri = carta.replace("-", "")

    if re.search(r'([0-9])\1{3}', numeri):
        valido = False

    if valido:
        print("Valid")
    else:
        print("Invalid")

'''
Validating Postal Codes
'''
regex_integer_in_range = r"^[1-9][0-9]{5}$"	
regex_alternating_repetitive_digit_pair = r"(?=(\d)\d\1)"


import re
P = input()

print (bool(re.match(regex_integer_in_range, P)) 
and len(re.findall(regex_alternating_repetitive_digit_pair, P)) < 2)

'''
Matrix Script
'''
import math
import os
import random
import re
import sys

first_multiple_input = input().rstrip().split()

n = int(first_multiple_input[0])
m = int(first_multiple_input[1])

matrix = []

for _ in range(n):
    matrix_item = input()
    matrix.append(matrix_item)

testo = ""

for j in range(m):
    for i in range(n):
        testo += matrix[i][j]

risultato = re.sub(r"(?<=[a-zA-Z0-9])[^a-zA-Z0-9]+(?=[a-zA-Z0-9])", " ", testo)

print(risultato)

# XML
'''
XML 1 - Find the Score
'''
import sys
import xml.etree.ElementTree as etree

def get_attr_number(node):
    total = len(node.attrib)

    for child in node:
        total += get_attr_number(child)

    return total


if __name__ == '__main__':
    sys.stdin.readline()
    xml = sys.stdin.read()
    tree = etree.ElementTree(etree.fromstring(xml))
    root = tree.getroot()
    print(get_attr_number(root))

'''
XML2 - Find the Maximum Depth
'''
import xml.etree.ElementTree as etree

maxdepth = 0

def depth(elem, level):
    global maxdepth

    level += 1

    if level > maxdepth:
        maxdepth = level

    for child in elem:
        depth(child, level)
        
if __name__ == '__main__':
    n = int(input())
    xml = ""
    for i in range(n):
        xml =  xml + input() + "\n"
    tree = etree.ElementTree(etree.fromstring(xml))
    depth(tree.getroot(), -1)
    print(maxdepth)

# Closures and Decorations 
'''
Standardize Mobile Number Using Decorators
'''
def wrapper(f):
    def fun(l):
        numbers = []

        for number in l:
            number = number[-10:]
            number = "+91 " + number[:5] + " " + number[5:]
            numbers.append(number)

        f(numbers)

    return fun

@wrapper
def sort_phone(l):
    print(*sorted(l), sep='\n')

if __name__ == '__main__':
    l = [input() for _ in range(int(input()))]
    sort_phone(l) 

'''
Decorators 2 - Name Directory
'''
import operator

def person_lister(f):
    def inner(people):
        people.sort(key=lambda person: int(person[2]))

        result = []

        for person in people:
            result.append(f(person))

        return result

    return inner

@person_lister
def name_format(person):
    return ("Mr. " if person[3] == "M" else "Ms. ") + person[0] + " " + person[1]

if __name__ == '__main__':
    people = [input().split() for i in range(int(input()))]
    print(*name_format(people), sep='\n')

# Numpy
'''
Arrays
'''
import numpy

def arrays(arr):
    a = numpy.array(arr, dtype=float)
    a = a[::-1]
    return a

arr = input().strip().split(' ')
result = arrays(arr)
print(result)

'''
Shape and Reshape
'''
import numpy as np


if __name__ == '__main__':
    
    num = list(map(int, input().split()))
      
    array = np.array(num)

    matrice = np.reshape(array, (3, 3))

    print(matrice)

'''
Transpose and Flatten
'''
import numpy as np 

if __name__ == '__main__':
    N, M = map(int, input().split())
    
    righe = []

    for _ in range(N):
        numeri = list(map(int, input().split()))
        righe.append(numeri)

    matrice = np.array(righe)

    print(np.transpose(matrice))
    print(matrice.flatten())

'''
Concatenate
'''
import numpy as np 

if __name__ == '__main__':

    N, M, P = map(int, input().split())

    prima_matrice = []
    seconda_matrice = []

    for i in range(N):
        numeri = list(map(int, input().split()))
        prima_matrice.append(numeri)

    for i in range(M):
        numeri = list(map(int, input().split()))
        seconda_matrice.append(numeri)

    prima_matrice = np.array(prima_matrice)
    seconda_matrice = np.array(seconda_matrice)

    risultato = np.concatenate((prima_matrice, seconda_matrice), axis=0)

    print(risultato)

'''
Zeros and Ones
'''
import numpy as np 

if __name__ == '__main__':
    dimensioni = tuple(map(int, input().split()))

    zeri = np.zeros(dimensioni, dtype=int)
    uni = np.ones(dimensioni, dtype=int)

    print(zeri)
    print(uni)

'''
Eye and Identity
'''
import numpy as np 

if __name__ ==  '__main__':
    
    np.set_printoptions(legacy='1.13')
    
    N, M = map(int, input().split())

    matrice = np.eye(N, M)

    print(matrice)

'''
Array Mathematics
'''
import numpy as np

if __name__ == '__main__':
    N, M = map(int, input().split())

    righe_A = []
    righe_B = []

    for i in range(N):
        numeri = list(map(int, input().split()))
        righe_A.append(numeri)

    for i in range(N):
        numeri = list(map(int, input().split()))
        righe_B.append(numeri)

    matrice_A = np.array(righe_A)
    matrice_B = np.array(righe_B)

    print(matrice_A + matrice_B)
    print(matrice_A - matrice_B)
    print(matrice_A * matrice_B)
    print(matrice_A // matrice_B)
    print(matrice_A % matrice_B)
    print(matrice_A ** matrice_B)

'''
Floor, Ceil and Rint
'''
import numpy as np

if __name__ == '__main__':
    np.set_printoptions(legacy='1.13')

    numeri = list(map(float, input().split()))

    array = np.array(numeri)

    risultato_floor = np.floor(array)
    risultato_ceil = np.ceil(array)
    risultato_rint = np.rint(array)

    print(risultato_floor)
    print(risultato_ceil)
    print(risultato_rint)

'''
Sum and Prod
'''
import numpy as np

if __name__ == '__main__':
        
    N, M = map(int, input().split())

    righe = []

    for i in range(N):
        numeri = list(map(int, input().split()))
        righe.append(numeri)

    matrice = np.array(righe)

    somme = np.sum(matrice, axis=0)

    risultato = np.prod(somme)

    print(risultato)

'''
Min and Max
'''
import numpy as np

if __name__ == '__main__':
    N, M = map(int, input().split())

    righe = []

    for i in range(N):
        numeri = list(map(int, input().split()))
        righe.append(numeri)

    matrice = np.array(righe)

    minimi = np.min(matrice, axis=1)

    risultato = np.max(minimi)

    print(risultato)

'''
Mean, Var, and Std
'''
import numpy as np 

if __name__ == '__main__':
    N, M = map(int, input().split())

    righe = []

    for i in range(N):
        numeri = list(map(int, input().split()))
        righe.append(numeri)

    matrice = np.array(righe)

    medie = np.mean(matrice, axis=1)

    varianze = np.var(matrice, axis=0)

    deviazione_standard = np.std(matrice, axis=None)

    print(medie)
    print(varianze)
    print(round(deviazione_standard, 11))

'''
Dot and Cross
'''
import numpy as np

if __name__ == '__main__':
    N = int(input())

    righe_A = []
    righe_B = []

    for i in range(N):
        numeri = list(map(int, input().split()))
        righe_A.append(numeri)

    for i in range(N):
        numeri = list(map(int, input().split()))
        righe_B.append(numeri)

    matrice_A = np.array(righe_A)
    matrice_B = np.array(righe_B)

    risultato = np.dot(matrice_A, matrice_B)

    print(risultato)

'''
Inner and Outer
'''
import numpy as np
if __name__ == '__main__':
    numeri_A = list(map(int, input().split()))
    numeri_B = list(map(int, input().split()))

    array_A = np.array(numeri_A)
    array_B = np.array(numeri_B)

    prodotto_interno = np.inner(array_A, array_B)
    prodotto_esterno = np.outer(array_A, array_B)

    print(prodotto_interno)
    print(prodotto_esterno)

'''
Polynomial
'''
import numpy as np

P = list(map(float, input().split()))
x = float(input())

result = np.polyval(P, x)

print(result)

'''
Linear Algebra
'''
import numpy as np

N = int(input())

matrix = []

for i in range(N):
    row = list(map(float, input().split()))
    matrix.append(row)

A = np.array(matrix)

result = np.linalg.det(A)

print(round(result, 2))

# Birthday Cake Candles
import math
import os
import random
import re
import sys

def birthdayCakeCandles(candles):
    altezza_massima = max(candles)
    conteggio = 0

    for candela in candles:
        if candela == altezza_massima:
            conteggio += 1

    return conteggio
    
if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    candles_count = int(input().strip())

    candles = list(map(int, input().rstrip().split()))

    result = birthdayCakeCandles(candles)

    fptr.write(str(result) + '\n')

    fptr.close()

# Number Line Jumps
import math
import os
import random
import re
import sys

def kangaroo(x1, v1, x2, v2):

    if v1 <= v2:
        return "NO"

    distanza = x2 - x1
    differenza = v1 - v2

    if distanza % differenza == 0:
        return "YES"
    else:
        return "NO"
        
if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    first_multiple_input = input().rstrip().split()

    x1 = int(first_multiple_input[0])

    v1 = int(first_multiple_input[1])

    x2 = int(first_multiple_input[2])

    v2 = int(first_multiple_input[3])

    result = kangaroo(x1, v1, x2, v2)

    fptr.write(result + '\n')

    fptr.close()

# Viral Advertising
import math
import os
import random
import re
import sys

def viralAdvertising(n):
    persone = 5
    totale = 0

    for giorno in range(n):
        like = persone // 2
        totale += like
        persone = like * 3

    return totale
if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input().strip())

    result = viralAdvertising(n)

    fptr.write(str(result) + '\n')

    fptr.close()

# Recursive Digit Sum
import math
import os
import random
import re
import sys

def superDigit(n, k):
    totale = 0

    for cifra in n:
        totale += int(cifra)

    totale = totale * k

    while totale >= 10:
        somma = 0

        for cifra in str(totale):
            somma += int(cifra)

        totale = somma

    return totale 

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    first_multiple_input = input().rstrip().split()

    n = first_multiple_input[0]

    k = int(first_multiple_input[1])

    result = superDigit(n, k)

    fptr.write(str(result) + '\n')

    fptr.close()

# Insertion Sort - Part 1
import math
import os
import random
import re
import sys

def insertionSort1(n, arr):
    numero = arr[n - 1]
    i = n - 2

    while i >= 0 and arr[i] > numero:
        arr[i + 1] = arr[i]
        print(*arr)
        i -= 1

    arr[i + 1] = numero
    print(*arr)

if __name__ == '__main__':
    n = int(input().strip())

    arr = list(map(int, input().rstrip().split()))

    insertionSort1(n, arr)

# Insertion Sort - Part 2
import math
import os
import random
import re
import sys

def insertionSort2(n, arr):

    for i in range(1, n):
        numero = arr[i]
        j = i - 1

        while j >= 0 and arr[j] > numero:
            arr[j + 1] = arr[j]
            j -= 1

        arr[j + 1] = numero

        print(*arr)

if __name__ == '__main__':
    n = int(input().strip())

    arr = list(map(int, input().rstrip().split()))

    insertionSort2(n, arr)