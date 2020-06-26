from func_aux import *
from calendarios import *
from grafos import *
from teoremas_grafos import *
from FFT import *
from time import sleep



# ============ MAIN ============
print(f"\n{bcolors.HEADER}\t============ MD TOOLS ============{bcolors.ENDC}")
while(1):

    escolha = input(f"""
        --------------{bcolors.BOLD} Menu {bcolors.ENDC}--------------

        N) {bcolors.BOLD}FFT{bcolors.ENDC}

        {bcolors.BOLD}RSA{bcolors.ENDC}
        A) Descobrir inverso de e mod (p-1)*(q-1)
        B) Fazer modulos rapidamente
        C) Obter soma em base 2 de numero
        D) Ver algoritmo RSA
        
        {bcolors.BOLD}Congruencias{bcolors.ENDC}
        E) Maximo Divisor Comum
        J) Simplificar congruências
        K) Coeficientes de Bezout
        L) Equacoes Diofantinas

        {bcolors.BOLD}Calendarios{bcolors.ENDC}
        F) Juliano
        G) Gregoriano
        H) Pascoa Juliana
        I) Pascoa Gregoriana (step by step)

        {bcolors.BOLD}Grafos{bcolors.ENDC}
        M) Algoritmo de Fleury
        O) Nocoes de Grafos
        P) Teoremas de Grafos

        X) Sair

{bcolors.BOLD}Escolha:{bcolors.ENDC} """)

    if escolha.upper() == 'A':
        e = inputNumber("e = ")
        p = inputNumber("p = ")
        q = inputNumber("q = ")
        phi = (p-1)*(q-1)

        print(f"{bcolors.OKGREEN}d = {multiplicative_inverse(e, phi)}{bcolors.ENDC}")

    elif escolha.upper() == 'B':
        print("a (mod b)")
        b = inputNumber("mod = ")
        sair = ''
        while (sair != 'y'):
            a = eval(input("a = "))
            print(f"{a} ≡ {bcolors.OKGREEN}{a%b}{bcolors.ENDC} (mod {b})")
            sair = input("Sair? [y]: ")
    
    elif escolha.upper() == 'C':
        n = inputNumber("Numero a decompor = ")
        print(f"{bcolors.OKGREEN}{soma_pot_2(n)}{bcolors.ENDC}")

    elif escolha.upper() == 'X':
        print(f"{bcolors.WARNING}A sair...{bcolors.ENDC}")
        sleep(0.2)
        exit()
    
    # VER ALGORITMO RSA ! TO-DO
    elif escolha.upper() == 'D':
        continue

    # MAXIMO DIVISOR COMUM
    elif escolha.upper() == 'E':
        a = inputNumber("a = ")
        b = inputNumber("b = ")

        print(f"{bcolors.OKGREEN}a ⌢ b = {gcd(a,b)}{bcolors.ENDC}")
    

    # DIA DA SEMANA JULIANO
    elif escolha.upper() == 'F':
        print("Dia D do mes de letra F do ano Y")
        D = inputNumber("D = ")
        F = inputNumber("F = ")
        Y = inputNumber("Y = ")
        W, FevOuJan = juliano(D, F, Y)

        dias_da_semana = [0, "Domingo", "Segunda-feira", "Terca-feira", "Quarta-feira", "Quinta-feira", "Sexta-feira", "Sabado"]
        print(f"-> {bcolors.OKGREEN}{W}, {dias_da_semana[W]}{bcolors.ENDC}, no calendario Juliano")

        mostrar_passos = input("Mostar passos? [y/n]: ")
        if mostrar_passos == 'y':
            print(f"{bcolors.OKBLUE}A mostrar passos: {bcolors.ENDC}")
            passos_juliano(D, F, Y, FevOuJan)

    # DIA DA SEMANA GREGORIANO
    elif escolha.upper() == 'G':
        print("Dia D do mes de letra F do ano Y")
        D = inputNumber("D = ")
        F = inputNumber("F = ")
        Y = inputNumber("Y = ")
        W, FevOuJan = gregoriano(D, F, Y)

        dias_da_semana = [0, "Domingo", "Segunda-feira", "Terca-feira", "Quarta-feira", "Quinta-feira", "Sexta-feira", "Sabado"]
        print(f"-> {bcolors.OKGREEN}{W}, {dias_da_semana[W]}{bcolors.ENDC}, no calendario Gregoriano")

        mostrar_passos = input("Mostar passos? [y/n]: ")
        if mostrar_passos == 'y':
            print(f"{bcolors.OKBLUE}A mostrar passos: {bcolors.ENDC}")
            passos_gregoriano(D, F, Y, FevOuJan)

    # PASCOA JULIANA
    elif escolha.upper() == 'H':
        Y = inputNumber("Y = ")
        S = pascoa_juliana(Y)
        if S > 30:
            print(f"A pascoa de {Y} e no dia -> {bcolors.OKGREEN}{S % 31} de Abril, S = {S},{bcolors.ENDC} no calendario Juliano")
        else:
            print(f"A pascoa de {Y} e no dia -> {bcolors.OKGREEN}{S} de Março, S = {S},{bcolors.ENDC} no calendario Juliano")

    # PASCOA GREGORIANA
    elif escolha.upper() == 'I':
        Y = inputNumber("Y = ")
        S = pascoa_gregoriana(Y)
        if S > 30:
            print(f"A pascoa de {Y} e no dia -> {bcolors.OKGREEN}{S % 31} de Abril, S = {S},{bcolors.ENDC} no calendario Gregoriano")
        else:
            print(f"A pascoa de {Y} e no dia -> {bcolors.OKGREEN}{S} de Março, S = {S},{bcolors.ENDC} no calendario Gregoriano")

    # SIMPLIFICAR CONGRUENCIAS
    elif escolha.upper() == 'J':
        print("ax ≡ b (mod N)")
        a_ini = inputNumber("a = ")
        b_ini = inputNumber("b = ")
        n = inputNumber("mod N = ")

        # to do 

        print(f"{a_ini}x ≡ {b_ini} (mod {n}) <=> {bcolors.OKGREEN}x ≡ {x} (mod {n}) {bcolors.ENDC}")

    # BEZOUT
    elif escolha.upper() == 'K':
        print("ax + by = a ⌢ b")
        a = inputNumber("a = ")
        b = inputNumber("b = ")
        
        mdc, x, y = saunderson(a, b)
        
        print(f"{a}x + {b}y = {mdc} => {bcolors.OKGREEN}x = {x}{bcolors.ENDC} e {bcolors.OKGREEN}y = {y}{bcolors.ENDC}")
    
    # DIOFANTINAS
    elif escolha.upper() == 'L':
        print("ax + by = c")
        a = inputNumber("a = ")
        b = inputNumber("b = ")
        c = inputNumber("c = ")
        
        x, y = diofantina(a,b,c)
        print(f"{a}x + {b}y = {c} => {bcolors.OKGREEN}x = {x}{bcolors.ENDC} e {bcolors.OKGREEN}y = {y}{bcolors.ENDC}.")

    elif escolha.upper() == 'M':
        fleury_apl()

    elif escolha.upper() == 'N':
        fft()

    elif escolha.upper() == 'O':
        nocoes_grafos()

    elif escolha.upper() == 'P':
        teoremas_grafos()

    else:
        print("Escolha nao valida, tenta de novo!")


    

