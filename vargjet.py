# bashkesia fillestare
numList = list(int(num) for num in input(
    "vendos nje seri numrash te ndare vetem me nje hapsire ").strip().split())

t = numList
# t = [4, 23, 66, 145]
# diferenca 1
t1 = [j - u for u, j in zip(t[:-1], t[1:])]
# diferenca 2
t2 = [j - u for u, j in zip(t1[:-1], t1[1:])]
# diferenca 3
t3 = [j - u for u, j in zip(t2[:-1], t2[1:])]
print(t)
print("diferenca 1:", t1)
print("diferenca 2:", t2)
print("diferenca 3:", t3)
# merr nje nga vlerat e bashkesise: diferenca 3
u = t3[0]
b = u / 6

n = [1, 2, 3, 4, 5]

# llogaritja ndodh vetem nese elementet e bashkesise kane vlere te njejte
if all(elem == t3[0] for elem in t3):
    print("b =", b)
else:
    print("Gje qe sbehet")


bn3 = []
for x in n:
    bn3.append(b * x**3)
print("b*n**3: ", bn3)

diferenca_t_bn3 = [a - b for a, b in zip(t, bn3)]
print("t-bn3:", diferenca_t_bn3)

# diferenca 1 midis elemeteve te listes diferenca_t_bn3
D1 = [j - u for u, j in zip(diferenca_t_bn3[:-1], diferenca_t_bn3[1:])]
# diferenca 2 midis elemeteve te listes diferenca_t_bn3
# diferenca 1 midis elemeteve te listes D1
D2 = [j - u for u, j in zip(D1[:-1], D1[1:])]
print("D1:", D1)
print("D2:", D2)
o = D2[0]
c = o / 2

if all(elem == D2[0] for elem in D2):
    print("c =", c)
else:
    print("Gje qe sbehet")

cn2 = []
for x in n:
    cn2.append(c * x**2)
print("c*n**2: ", cn2)

diferenca_t_bn3_cn2 = [a - b for a, b in zip(diferenca_t_bn3, cn2)]
print("D1 - cn2 :", diferenca_t_bn3_cn2)

F1 = [j - u for u, j in zip(diferenca_t_bn3_cn2[:-1], diferenca_t_bn3_cn2[1:])]
print(F1)
d = F1[0]

if all(elem == F1[0] for elem in F1):
    print("d =", d)
else:
    print("Gje qe sbehet")

dn = []
for x in n:
    dn.append(d * x)
print("d * x:", dn)

diferenca_per_e = [a - b for a, b in zip(diferenca_t_bn3_cn2, dn)]
print(diferenca_per_e)

e = diferenca_per_e[0]

if all(elem == diferenca_per_e[0] for elem in diferenca_per_e):
    print("e =", e)
else:
    print("Gje qe sbehet")

print("an =", b, "* n^3 +", c, "* n^2 +", d, "* n+", e)

input("Press enter to exit ;)")
