"""
Napište program porovnávající jednotlivé třídící algoritmy, porovnejte jejich rychlosti a zdůvodněte,
proč se chovají tak, jak se chovají. Implementujte Quicksort a 2 "pomalé" třídící algoritmy.
Změřte rychlost běhu jednotlivých algoritmů a standardního třídění (list.sort()) na datech velikostí 4^k,
kde k=3,...,10. Změřte na následujících typech dat:

náhodné integery
stříděné integery
setříděné integery, které mají 1% dvojic prvků náhodně prohozených
Výsledky vyneste do grafů a odůvodněte.

Vstup
Program si vstupní data generuje sám, od uživatele nebere vstup.

Výstup
Program průběžně vypisuje, za jak dlouho setřídil daný seznam.
Přesný formát není dán, ale měl by být takový, aby se naměřená data dala dále snadno zpracovávat
a neztrácela se v debugovacích výpisech.

Dále z naměřených dat vytvoříte zprávu v PDF s popisy iomplementovaných algoritmů, grafy, zdůvodněními a použitou
metodikou měření (kolikrát jste měřili jaká data, jak jste generovali data, ...).
"""


# implementace 1. pomalého select sort
def select_sort(x):
    for i in range(0, len(x) - 1):
        imin = i
        for j in range(i, len(x)):
            if x[j] < x[imin]:
                imin = j
        temp = x[i]
        x[i] = x[imin]
        x[imin] = temp


# implementace 2. pomalého merge sort
def merge_sort(c, l, mid, r):
    a = c[l:mid + 1]
    b = c[mid + 1, r+1]
    n = len(a)
    m = len(b)
    i = 0
    j = 0
    for k in range(l, r+1):
        if i == n:
            c[k] = b[j]
            j = j + 1
            continue
        if j == m:
            c[k] = a[i]
            i = i + 1
            continue
        if a[i] < b[j]:
            c[k] = a[i]
            i = i + 1
        else:
            c[k] = b[j]
            j = j + 1


# implementace rychlého quick sort
def quick_sort(x, l, r):
    i = l
    j = r
    p = x[(l + r) // 2]
    while i <= j:
        while x[i] < p:
            i = i + 1
        while p < x[j]:
            j = j - 1
        if i <= j:
            temp = x[i]
            x[i] = x[j]
            x[j] = temp
            i = i + 1
            j = j - 1
        if l < j:
            quick_sort(x, l, j)
        if p > i:
            quick_sort(x, i, p)


# generování vstupních dat
    # náhodné integery
    # stříděné integery
    # setříděné integery, které mají 1% dvojic prvků náhodně prohozených

# output pdf
