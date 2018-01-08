'''Access codes

============

You've discovered the evil laboratory of Dr. Boolean, and you've found that

the vile doctor is transforming your fellow rabbit kin into terrifying

rabbit­zombies! Naturally, you're less­than­happy about this turn of events.

Of course where there's a will, there's a way. Your top­notch assistant, Beta

Rabbit, managed to sneak in and steal some access codes for Dr. Boolean's lab

in the hopes that the two of you could then return and rescue some of the

undead rabbits. Unfortunately, once an access code is used it cannot be used

again. Worse still, if an access code is used, then that code backwards won't

work either! Who wrote this security system?

Your job is to compare a list of the access codes and find the number of

distinct codes, where two codes are considered to be "identical" (not

distinct) if they're exactly the same, or the same but reversed. The access

codes only contain the letters a­z, are all lowercase, and have at most 10

characters. Each set of access codes provided will have at most 5000 codes in

them.

For example, the access code "abc" is identical to "cba" as well as "abc." The

code "cba" is identical to "abc" as well as "cba." The list ["abc," "cba,"

"bac"] has 2 distinct access codes in it.

Write a function answer(x) which takes a list of access code strings, x, and

returns the number of distinct access code strings using this definition of

identical.

Languages

=========

To provide a Python solution, edit solution.py

To provide a Java solution, edit solution.java

Test cases

==========

Inputs:

(string list) x = ["foo", "bar", "oof", "bar"]

Output:

(int) 2

Inputs:

(string list) x = ["x", "y", "xy", "yy", "", "yx"]

Output:

(int) 5

Use verify [file] to test your solution and see how it does. When you are

finished editing your code, use submit [file] to submit your answer. If your

solution passes the test cases, it will be removed from your home folder.'''

solution.py:

def answer(x):

codes = list()

for code in x:

if code not in codes and code[::­1] not in codes:

codes.append(code)

return len(codes)

'''

Minglish lesson

===============

Welcome to the lab, minion. Henceforth you shall do the bidding of Professor Boolean. Some say

he's mad, trying to develop a zombie serum and all... but we think he's brilliant!

First things first ­ Minions don't speak English, we speak Minglish. Use the Minglish dictionary to

learn! The first thing you'll learn is how to use the dictionary.

Open the dictionary. Read the page numbers, figure out which pages come before others. You

recognize the same letters used in English, but the order of letters is completely different in

Minglish than English (a < b < c < ...).

Given a sorted list of dictionary words (you know they are sorted because you can read the page

numbers), can you find the alphabetical order of the Minglish alphabet? For example, if the words

were ["z", "yx", "yz"] the alphabetical order would be "xzy," which means x < z < y. The first two

words tell you that z < y, and the last two words tell you that x < z.

Write a function answer(words) which, given a list of words sorted alphabetically in the Minglish

alphabet, outputs a string that contains each letter present in the list of words exactly once; the

order of the letters in the output must follow the order of letters in the Minglish alphabet.

The list will contain at least 1 and no more than 50 words, and each word will consist of at least 1

and no more than 50 lowercase letters [a­z]. It is guaranteed that a total ordering can be

developed from the input provided (i.e. given any two distinct letters, you can tell which is greater),

and so the answer will exist and be unique.

Languages

=========

To provide a Python solution, edit solution.py

To provide a Java solution, edit solution.java

Test cases

==========

Inputs:

(string list) words = ["y", "z", "xy"]

Output:

(string) "yzx"

Inputs:

(string list) words = ["ba", "ab", "cb"]

Output:

(string) "bac"
'''

solution:

from itertools import islice

from collections import deque

class DAG(object):

def __init__(self):

self.vertices = {}

def add_vertex(self, key):

self.vertices.update({key: Vertex(key)})

def __getitem__(self, val):

return self.vertices.get(val, None)

def iteritems(self):

return self.vertices.iteritems()

def get(self, val):

return self.__getitem__(val)

class Vertex(object):

def __init__(self, key=None):

self.key = key

self.neighbors = list()

def add_neighbor(self, edge):

self.neighbor.append(edge)

# def __repr__(self):

# return "{neighbors}".format(

# neighbors=', '.join(map(str, self.neighbors)))

def answer(words):

""" Given a sorted list of words, output the corresponding alphabet.

["ba", "ab", "cb"]

Sliding window of 2 over the list:

(ba, ab) : '' + b, '' + a, create A, B vertexes, edge B ­> A

(ab, cb) : '' + a, '' + c, create C vertex, edge A ­> C

B ­> A (B < A), A ­> C (A < C) == BAC

[C, CAC, CB, BCC, BA]

(C, CAC) : '' + C, '' + C, create C and A vertexes

(CAC, CB) : C + A, C + B, create B vertex, edge A ­> B (A < B)

(CB, BCC) : '' + C, '' + B, edge C ­> B (C < B)

(BCC, BA) : B + C, B + A, edge C ­> A (C < A)

C < A, A < B, C < B == CAB

"""

return topological_sort(construct_graph(words))

def construct_graph(words):

graph = DAG()

for a, b in zip(*(islice(words, i, None) for i in range(2))):

for letter in set(list(a) + list(b)):

if not graph[letter]:

graph.add_vertex(letter)

vertex, neighbor = get_neighbor(a, b)

if vertex and neighbor:

graph[vertex].neighbors.append(neighbor)

return graph

def get_neighbor(a, b):

""" Parse a pair of words and return the edge, if it exists

Reduce the two words to a length equal to the shortest of

the two, then search for the first non­matching character,

if one exists.

Ex: 'C', 'CAC' ­­> max length 1, 'C', 'CAC'[:1]

'C' <­> 'C', no non­matching tokens

'CAC', 'CB' ­­> max length 2, 'CAC'[:2], 'CB'

'CA' <­> 'CB', 'A' will be connected to 'B'.

"""

max_length = min(map(len, [a, b]))

for _a, _b in zip(a[:max_length], b[:max_length]):

if _a != _b:

return _a, _b

return None, None

def topological_sort(graph):

def visit(node):

if node in temp:

raise Exception("Not a directed acyclic graph.")

if node not in visited:

temp.add(node)

for neighbor in graph[node].neighbors:

visit(neighbor)

visited.add(node)

temp.remove(node)

alphabet.appendleft(node)

alphabet = deque()

temp = set()

visited = set()

for node, neighbors in graph.iteritems():

if node not in visited:

visit(node)

return ''.join(list(alphabet))

def main():

print answer(['c', 'cac', 'cb', 'bcc', 'ba'])

print answer("y, z, xy".split(', '))

print answer("ba, ab, cb".split(', '))

if __name__ == '__main__':

main()

'''

Origins and order

=================

What do we know about Professor Boolean's past? It's mostly rumor and conjecture, but a few

things are known to be true.

Mad Professor Boolean wasn't always a super villain. Early in his career, he was an average

paper pusher, working in an office with some very backwards technology. One of his primary jobs

was to carry date cards between departments. One morning, he tripped over a unicycle and

dropped his date cards on the floor. He hit his head ­ and hit upon the idea of breeding an army of

zombie rabbits to do his bidding and manage simple tasks. But that comes later. Before he could

quit with an explosive YouTube video, the professor had to get his cards back in order.

Aha! It seems he recorded the details of this life­changing event in his diary. Let's try to reproduce

his methods:

The goal is to get the date cards back in order. Each set of date cards consists of 3 cards, each

with a number written on it. When arranged in some order, the numbers make up the

representation of a date, in the form month/day/year. However, sometimes multiple

representations will be possible. For example, if the date cards read 1, 1, 99 it could only mean

01/01/99, but if the date cards read 2, 30, 3, it could mean any one of 02/03/30, 03/02/30, or

03/30/02.

Write a function called answer(x, y, z) that takes as input the 3 numbers on the date cards. You

may assume that at least one valid representation of a date can be constructed from the cards.

If there is only one valid representation, the function should return it as a string, in the form

MM/DD/YY. If there are multiple valid representations, the function should return the string

"Ambiguous." Each of x, y, z will be between 1 to 99 inclusive. You may also assume that there

are no leap years.

Languages

=========

To provide a Python solution, edit solution.py

To provide a Java solution, edit solution.java

Test cases

==========

Inputs:

(int) x = 19

(int) y = 19

(int) z = 3

Output:

(string) "03/19/19"

Inputs:

(int) x = 2

(int) y = 30

(int) z = 3

Output:

(string) "Ambiguous"

Use verify [file] to test your solution and see how it does. When you are finished editing your code,

use submit [file] to submit your answer. If your solution passes the test cases, it will be removed

from your home folder.
'''

solution.py

import itertools

def answer(x, y, z):

month_days = {1: 31,

2: 28,

3: 31,

4: 30,

5: 31,

6: 30,

7: 31,

8: 31,

9: 30,

10: 31,

11: 30,

12: 31}

MONTH = 0

DAY = 1

YEAR = 2

valid_combinations = set()

permutations = itertools.permutations([x, y, z])

for permutation in permutations:

month = permutation[MONTH]

day = permutation[DAY]

if month <= 12 and day <= month_days.get(month):

valid_combinations.add(permutation)

if len(valid_combinations) > 1:

return "Ambiguous"

else:

return "%02d/%02d/%02d" % valid_combinations.pop()

'''
Peculiar balance

================

Can we save them? Beta Rabbit is trying to break into a lab that contains the only known zombie

cure ­ but there's an obstacle. The door will only open if a challenge is solved correctly. The future

of the zombified rabbit population is at stake, so Beta reads the challenge: There is a scale with

an object on the left­hand side, whose mass is given in some number of units. Predictably, the

task is to balance the two sides. But there is a catch: You only have this peculiar weight set,

having masses 1, 3, 9, 27, ... units. That is, one for each power of 3. Being a brilliant

mathematician, Beta Rabbit quickly discovers that any number of units of mass can be balanced

exactly using this set.

To help Beta get into the room, write a method called answer(x), which outputs a list of strings

representing where the weights should be placed, in order for the two sides to be balanced,

assuming that weight on the left has mass x units.

The first element of the output list should correspond to the 1­unit weight, the second element to

the 3­unit weight, and so on. Each string is one of:

"L" : put weight on left­hand side

"R" : put weight on right­hand side

"­" : do not use weight

To ensure that the output is the smallest possible, the last element of the list must not be "­".

x will always be a positive integer, no larger than 1000000000.

Languages

=========

To provide a Python solution, edit solution.py

To provide a Java solution, edit solution.java

Test cases

==========

Inputs:

(int) x = 2

Output:

(string list) ["L", "R"]

Inputs:

(int) x = 8

Output:

(string list) ["L", "­", "R"]

Use verify [file] to test your solution and see how it does. When you are finished editing your code,

use submit [file] to submit your answer. If your solution passes the test cases, it will be removed

from your home folder.
'''

solution.py

def answer(x):

# convert x to balanced ternary

n = x

k = 0

digits = list()

while True:

d = (n % (pow(3, k + 1))) / pow(3, k)

d = ­1 if d == 2 else d

digits.append(d)

n = n ­ d * pow(3, k)

k += 1

if n == pow(3, k):

digits.append(1)

break

if n == 0:

break

balanced_ternary = [['­', 'R', 'L'][i] for i in digits]

while balanced_ternary[­1] == '­':

balanced_ternary.pop(­1)

return balanced_ternary



"""

Hash it out

===========

Something horrible must have gone wrong in that last mission. As you wake in a holding cell, you

realize that you're in

the clutches of Professor Booleans numerous but relatively incompetent minions! Time to plan

another escape. Lucky for

you nobody is around (do these security minions just sleep all the time?), so you have a chance to

examine your cell.

Looking around, you see no signs of surveillance (ha, they must underestimate you already) and

the only thing keeping

you contained is an electronic door lock. Should be easy enough.

You and Beta Rabbit worked together to exfiltrate some of Professor Booleans security

information in anticipation of a

moment just like this one. Time to put it to the test.

If memory serves, this locking mechanism relies on a horribly bad cryptographic hash, and you

should be able to break it

with some rudimentary calculations.

To open these doors, you will need to reverse engineer the hash function it is using. You already

managed to steal the

details of the algorithm used, and with some quiet observation of the guards you find out the

results of the hash (the

digest). Now to break it.

The function takes a 16 byte input and gives a 16 byte output. It uses multiplication (*), bit­wise

exclusive OR (XOR)

and modulo (%) to calculate an element of the digest based on elements of the input message:

digest [i] = ( (129 * message[i]) XOR message[i­1]) % 256

For the first element, the value of message[­1] is 0.

For example, if message[0] ­ 1 and message[1] = 129, then:

For digest[0]: 129*message[0] = 129

129 XOR message[­1] = 129

129 % 256 = 129

Thus digest[0] = 129.

For digest[1]: 129*message[1] = 16641

16641 XOR message[0] = 16640

16640 % 256 = 0

Thus digest[1] = 0.

Write a function answer(digest) that takes an array of 16 integers and returns another array of 16

that correspond to

the unique message that created this digest. Since each value is a single byte, the values are 0 to

255 for both message

and digest.

"""

solution.py

from __future__ import division # Not strictly necessary but good for possible Python 3

compatibility

# This doesn't really *need* to be it's own function. It's more for compartmentalization

def getmultiples(num, lowerbound, upperbound, addnum):

"""

This function finds all the factors of 256 between two given bounds, then adds

a supplied number

"""

lowerfactor = lowerbound // num + 1

upperfactor = upperbound // num + 1

return [factor * num + addnum for factor in range(lowerfactor, upperfactor)]

def answer(digest):

"""

Alright, let's talk math. The hashed function is, as stated above digest[i]

= ( (129 * message[i]) ^ message[i ­ 1]) % 256 NOTE: '^' in python means

bit­wise exclusive OR

Here was my thought process: Let's make this problem a little simpler to

start out with Let x = ((129 * message[i]) ^ message[i­1]) Alrighty then, so

what are we left with?

x mod 256 = digest[i]

There are an unlimited number of solutions to the above problem. Well

shoot... But wait! There are constraints on what 'x' can be! What's the

lowest number we could get from '((129 * message[i]) ^ message[i­1])'? Well

the lowest value message[i] and message[i + 1] could be is 0 and 129 * 0 is

still 0. Thus our lower bound is, you guessed it, 0.

Well what about an upper bound? At most message[i] and message[i­1] could

be 255 (11111111 in binary). Thus our upper bound is 255 * 129 (it says 256

* 129 below which is an error. The program still gets the correct solution

though)

Now then, we know that 'x mod 256 = digest[i]' means 'the remainder of x

divided by 256 is digest[i]' right? So in other words (according to the

division theorem which states that any number 'a' can be expressed as 'bq +

r' b and q are two quotients and r is the remainder) x = 256q + digest[i].

So then, let's find all multiples of 256 between our bounds and add digest[i]

to them.

Awesome! That gives us a very long list of possible values for x but at

least it's a finite number!

Alrighty then, before we go much further, let's talk about bit­wise XOR.

Basically the only thing one needs to know in terms of this problem can be

expressed thusly:

a XOR b = c

b XOR a = c

c XOR b = a

c XOR a = b

So not only is XOR communitive, but it is also it's own inverse operation.

It undoes itself.

This means that since for any message[i] we will also know message[i­1] we

can easily narrow down that long list of possible values of x. Since ((129 *

message[i]) XOR message[i­1]) = x, it can also be stated that message[i­1]

XOR x = 129 * message[i]. Which also means that:

(message[i­1] XOR x)/129 = message[i]

Since we know that message[i] is a whole number, that means that

message[i­1] XOR x must be divisible by 129. Or, expressed as a modular

arithmatic expression:

(message[i­1] XOR x) mod 129 = 0

So then, let's just go through and find all of the possible values for x

that when XORed with the previous message character are divisible by 129.

When we XOR it with message[i­1] and divide it by 129. Also, since we know

these messages must be less than a byte each, we also need to convert it to

mod 256.

Fin

"""

message = []

for charnum in range(len(digest)):

if charnum == 0:

prevcharnum = 0

else:

prevcharnum = message[charnum ­ 1]

for multiple in getmultiples(256, 0, 256*129, digest[charnum]):

if (multiple ^ prevcharnum) % 129 == 0:

message.append(((multiple ^ prevcharnum) // 129) % 256)

return message

'''

Undercover underground

======================

As you help the rabbits establish more and more resistance groups to fight

against Professor Boolean, you need a way to pass messages back and forth.

Luckily there are abandoned tunnels between the warrens of the rabbits,

and you need to find the best way to use them.

In some cases, Beta Rabbit wants a high level of interconnectedness,

especially when the groups show their loyalty and worthiness.

In other scenarios the groups should be less intertwined,

in case any are compromised by enemy agents or zombits.

Every warren must be connected to every other warren somehow,

and no two warrens should ever have more than one tunnel between them.

Your assignment: count the number of ways to connect the resistance warrens.

For example, with 3 warrens (denoted A, B, C) and 2 tunnels, there are three

distinct ways to connect them:

A­B­C

A­C­B

C­A­B

With 4 warrens and 6 tunnels, the only way to connect them is to connect

each warren to every other warren.

Write a function answer(N, K) which returns the number of ways to connect

N distinctly labelled warrens with exactly K tunnels, so that there is a

path between any two warrens.

The return value must be a string representation of the total number of

ways to do so, in base 10. N will be at least 2 and at most 20.

K will be at least one less than N and at most (N * (N ­ 1)) / 2
'''

"""

solution.py

# used for memoizing binomial coefficient calculation

mem_choose = {}

# used for memoizing total number of possible graphs for n, k

mem_graphs = {}

# used for memoizing recursive relation of counting distinct graphs

mem_counts = {}

def choose(n, k):

"""

Calculates the binomial coefficient for n, k.

This is equivalent to 'n choose k'.

"""

key = (n, k)

if key not in mem_choose:

if k > n:

c = 0

elif k == 0 or n == k:

c = 1

elif k == 1 or k == n ­ 1:

c = n

else:

if k > n / 2:

k = n ­ k

a = 1

b = 1

for t in xrange(1, k + 1):

a *= n

b *= t

n ­= 1

c = a // b

mem_choose[key] = c

return mem_choose[key]

def possible_graphs(n, k):

"""

Returns the total number of graphs with that can be formed using

n nodes and k vertices. This includes graphs that are

identical for undirected labelled graphs, as well as

unconnected graphs.

This function effectively returns the number of ways you can

choose k vertices out of the 'n choose 2' possible choices.

"""

if (n, k) not in mem_graphs:

mem_graphs[(n, k)] = choose(n * (n ­ 1) >> 1, k)

return mem_graphs[(n, k)]

def count(n, k):

"""

Returns the number of distinct, connected, labelled, undirected

graphs that can be formed using 'n' nodes and 'k' vertices

"""

if (n, k) in mem_counts:

# memoized

return mem_counts[(n, k)]

if k == n ­ 1:

# Cayley's formula

c = int(n ** (n ­ 2))

else:

# number of possible vertices

p = n * (n ­ 1) >> 1

if k == p:

# only way is to connect each node to all other nodes,

# therefore only a single distinct graph

c = 1

else:

# initially all possible graphs

c = choose(p, k)

# there can only be duplicates or unconnected components

# if the number of nodes is less than p ­ n + 2.

# equivalent of k < (n ­ 1 choose 2)

if k < p ­ n + 2:

for i in range(1, n):

x = choose(n ­ 1, i ­ 1)

# minimum of possible vertices for 'i' nodes and 'k'

y = min(i * (i ­ 1) >> 1, k)

for j in range(i ­ 1, y + 1):

# exclude invalid graphs from the total

c ­= x * possible_graphs(n ­ i, k ­ j) * count(i, j)

mem_counts[(n, k)] = c

return c

def answer(n, k):

return count(n, k)