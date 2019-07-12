from string import ascii_lowercase as string
a = """
    A
   A A
  A   A
 A  A  A
A       A
"""
b = """
BBBBBB
B     B
BBBBBB
B     B
BBBBBB
"""
c = """
 CCCCCC
C
C
C
 CCCCCC
"""
d = """
DDDDDD
D     D
D     D
D     D
DDDDDD
"""
e = """
EEEEEEE
E
EEEEEEE
E
EEEEEEE
"""
f = """
FFFFFFF
F
FFFFFFF
F
F
"""
g = """
GGGGGGG
G
G   GGG
G     G
GGGGGGG
"""
h = """
H     H
H     H
HHHHHHH
H     H
H     H
"""
i = """
IIIIIII
   I
   I
   I
IIIIIII
"""
j = """
   JJJJ
     J
     J
JJ   J
JJJJJJ
"""
k = """
K    K
K  K
KK
K  K
K    K
"""
l = """
L
L
L
L
LLLLLLL
"""
m = """
MM   MM
M M M M
M  M  M
M     M
M     M
"""
n = """
N      N
NN     N
N  N   N
N    N N
N      N
"""
o = """
  OOOO
O      O
O      O
O      O
  OOOO
"""
p = """
PPPPPPP
P      P
PPPPPPP
P
P
"""
q = """
 QQQQQQ
Q      Q
Q   Q  Q
Q    Q Q
 QQQQQQQ
"""
r = """
RRRRRRR
R      R
RRRRRRR
R  R
R     R
"""
s = """
  SSSSSS
S
 SSSSSS
       S
SSSSSSS
"""
t = """
TTTTTTT
   T
   T
   T
   T
"""
u = """
U      U
U      U
U      U
U      U
 UUUUUU
"""
v = """
V       V
 V     V
  V   V
   V V
    V
"""
w = """
W       W
W   W   W
W W   W W
W       W
"""
x = """
X       X
  X   X
    X
  X   X
X       X
"""
y = """
Y     Y
 Y   Y
   Y
   Y
   Y
"""
z = """
ZZZZZZZ
      Z
   Z
Z
ZZZZZZZ
"""

dicionário = dict(zip(string, [eval(temp) for temp in string]))


def main():
    print(dicionário[input('Letra: ').lower()])


if __name__ == '__main__':
    main()
