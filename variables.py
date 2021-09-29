# Proměnné mohou být jakéhokoliv typu a Python nevyžaduje jejich psaní.

x = 5
y = "Hello world!"
print(x)
print(y)

# Pokud ale chceme specifikovat datový typ, můžeme to udělat takhle

c = str(3)
v = int(3)
b = float(3)

# Pokud chceme zjistit s jakým datovým typem pracujeme můžeme použít type()

print(type(x))
print(type(y))
print(type(c))
print(type(v))
print(type(b))

# Proměnné můžeme deklarovat buď "" nebo ''

n = "Jan"
m = 'Michal'

# Python je case-sensitive, a = 4 není to samé jako A = Jan

a = 4
A = 'Jan'

# Více proměnných v proměnné

a, s, d = "Jablko", "Pomeranč", "Třešeň"
print(a)
print(s)
print(d)

# Jedna hodnota pro více proměnných

f = g = h = "Mandarinka"
print(f)
print(g)
print(h)

# Pokud máme kolekci hodnot, Python nám dovolí extrahovat hodnoty do proměnných
fruits = ["Apple", "Banana", "Cherry"]
j, k, l = fruits
print(j)
print(k)
print(l)

# Výsledkové proměnné, pomocí print() můžeme výsledek v proměnné printnout.

q = "UwU"
print("Python je" + q)

# Sčítání proměnných

w = "Python je"
e = "UwU"
r = w + e
print(r)

# Nemůžeme sčítat string s intem
