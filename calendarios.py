import math

"""
.----------------.-------.--------.
| Dia da semana  | Letra | Numero |
:----------------+-------+--------:
| Domingo        | A     |      1 |
:----------------+-------+--------:
| Segunda-feira  | B     |      2 |
:----------------+-------+--------:
| Terca-feira    | C     |      3 |
:----------------+-------+--------:
| Quarta-feira   | D     |      4 |
:----------------+-------+--------:
| Quinta-Feira   | E     |      5 |
:----------------+-------+--------:
| Sexta-Feira    | F     |      6 |
:----------------+-------+--------:
| Sabado         | G     |      7 |
'----------------'-------'--------'
"""


def bissexto(year):
    return (( year%400 == 0) or (( year%4 == 0 ) and ( year%100 != 0)))

def gregoriano(D, F, Y):
    C = 1 + ((D + F - 2) % 7)
    N = 7 - (Y - 1 + Y //4 - Y // 100 + Y // 400)%7

    if bissexto(Y):
        FevOuJan = input("Jan/Fev? [y/n]: ")
        if FevOuJan == 'y':
            W = 1 + ((C - N + 6) % 7)
            return (W, FevOuJan)
        else:
            W = 1 + ((C - N + 7) % 7)
            return (W, FevOuJan)
    else:
        W = 1 + ((C - N + 7) % 7)
        return (W, 'n')

def juliano(D, F, Y):
    C = 1 + ((D + F - 2) % 7)
    N = 7 - ((Y + 4 + Y // 4) % 7)

    if bissexto(Y):
        FevOuJan = input("Jan/Fev? [y/n]: ")
        if FevOuJan == 'y':
            W = 1 + ((C - N + 6) % 7)
        else:
            W = 1 + ((C - N + 7) % 7)
    else:
        W = 1 + ((C - N + 7) % 7)

    return (W,FevOuJan)


def passos_gregoriano(D, F, Y, FevOuJan):
    print(f"{Y} // 4 = {Y//4}")
    print(f"{Y} // 100 = {Y//100}")
    print(f"{Y} // 400 = {Y//400}")
    print(f"{Y} - 1 + {Y//4} - {Y//100} + {Y//400} = {Y - 1 + Y//4 - Y//100 + Y//400}")
    print(f"N = 7 - {Y - 1 + Y//4 - Y//100 + Y//400}%7")
    print(f"N = 7 - {(Y - 1 + Y//4 - Y//100 + Y//400)%7} = {7 - (Y - 1 + Y//4 - Y//100 + Y//400)%7}")

    N = 7 - (Y - 1 + Y//4 - Y//100 + Y//400)%7

    print(f"C = 1 + ({D} + {F} - 2)%7 = {1 + (D + F - 2)%7}")
    C = 1 + (D + F - 2)%7


    if bissexto(Y):
        if FevOuJan == 'y':
            W = 1 + ((C - N + 6) % 7)
            print(f"W = 1 + ({C} - {N} + 6)%7 = {W}")
        else:
            W = 1 + ((C - N + 7) % 7)
            print(f"W = 1 + ({C} - {N} + 7)%7 = {W}")      
    else:
        W = 1 + ((C - N + 7) % 7)
        print(f"W = 1 + ({C} - {N} + 7)%7 = {W}")    

def passos_juliano(D, F, Y, FevOuJan):
    print(f"{Y} // 4 = {Y//4}")
    print(f"{Y} + 4 + 2020 // 4 = {Y + 4 + Y//4}")
    print(f"N = 7 - {Y + 4 + Y//4}%7 = 7 - {(Y + 4 + Y//4)%7} = {7 - (Y + 4 + Y//4)%7}")

    N = 7 - ((Y + 4 + Y // 4) % 7)

    print(f"C = 1 + ({D} + {F} - 2)%7 = {1 + (D + F - 2)%7}")
    C = 1 + (D + F - 2)%7

    if bissexto(Y):
        if FevOuJan == 'y':
            W = 1 + ((C - N + 6) % 7)
            print(f"W = 1 + ({C} - {N} + 6)%7 = {W}")
        else:
            W = 1 + ((C - N + 7) % 7)
            print(f"W = 1 + ({C} - {N} + 7)%7 = {W}")      
    else:
        W = 1 + ((C - N + 7) % 7)
        print(f"W = 1 + ({C} - {N} + 7)%7 = {W}")    

def pascoa_juliana(Y):
    
    G = 1 + Y%19
    print(f"G = {G}")

    E = (11*G - 3)%30

    print(f"E = {E}")

    D = 20 + (54 - E)%30
    print(f"D = {D}")

    C = 1 + (D + 2)%7 
    print(f"C = {C}")

    N = 7 - (Y + 4 + Y // 4) % 7
    print(f"N = {N}")

    if C < N:
        S = D + N - C
    else:
        S = D + 7 - (C - N)%7
    
    return S

def pascoa_gregoriana(Y):
    
    G = 1 + Y%19
    print(f"G = {G}")


    Mod1 = 57 + 11 * G
    Mod2 = math.floor(Y/100)
    Mod3 = math.floor(Mod2 / 4)
    ModAux = Mod2 - math.floor((Mod2 - 17) / 25)
    Mod4 = math.floor(ModAux / 3)

    E = (Mod1 - Mod2 + Mod3 + Mod4) % 30
    print(f"E0 = {E}")
    
    V = (E//24 - E//25) + G//12 * (E//25 - E//26)
    print(f"V = {V}")
    E += V
    print(f"E = {E}")

    D = 20 + (54 - E)%30
    print(f"D = {D}")
    C = (D + 2)%7 + 1
    print(f"C = {C}")
    N = 7 - ((Y - 1 + Y // 4 - Y//100 + Y//400) % 7)
    print(f"N = {N}")

    if C < N:
        S = D + N - C
        print(f"S = {S}")
    else:
        S = D + 7 - (C - N)%7
        print(f"S = {S}")
    
    return S



