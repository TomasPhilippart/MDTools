
print("""
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
""")


def bissexto(year):
    return (( year%400 == 0) or (( year%4 == 0 ) and ( year%100 != 0)))

def gregoriano(D, F, Y):
    C = 1 + ((D + F - 2) % 7)
    N = 7 - (Y - 1 + Y //4 - Y // 100 + Y // 400)%7

    if bissexto(Y):
        FevOuJan = input("Jan/Fev? [y/n]: ")
        if FevOuJan == 'y':
            W = 1 + ((C - N + 6) % 7)
        else:
            W = 1 + ((C - N + 7) % 7)
    else:
        W = 1 + ((C - N + 7) % 7)

    return W

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

    return W
