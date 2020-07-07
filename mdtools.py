from func_aux import *
from calendarios import *
from teoremas_grafos import *
from percorrer_grafos import *
from FFT import *
from RSA import *
from time import sleep
from subprocess import call

# ============ MAIN ============
print(f"\n{bcolors.HEADER}\t============ MD TOOLS ============{bcolors.ENDC}")
while(1):

    escolha = input(f"""
        --------------{bcolors.BOLD} Menu {bcolors.ENDC}--------------
        {bcolors.BOLD}
        A) Ver algoritmo FFT{bcolors.ENDC}

        {bcolors.BOLD}RSA{bcolors.ENDC}
        B) Descobrir inverso de e mod (p-1)*(q-1)
        C) Fazer modulos rapidamente
        D) Obter soma em base 2 de numero
        E) Ver algoritmo RSA
        
        {bcolors.BOLD}Congruencias{bcolors.ENDC}
        F) Maximo Divisor Comum
        G) Simplificar congruencias
        H) Coeficientes de Bezout
        I) Equacoes Diofantinas

        {bcolors.BOLD}Calendarios{bcolors.ENDC}
        J) Juliano
        K) Gregoriano
        L) Pascoa Juliana
        M) Pascoa Gregoriana (passo a passo)

        {bcolors.BOLD}Grafos{bcolors.ENDC}
        N) Nocoes Basicas
        O) Teoremas
        P) Algoritmo de Fleury

        X) Sair

{bcolors.BOLD}Escolha:{bcolors.ENDC} """)

    ###### FFT ######

    if escolha.upper() == 'A':
        fft()

    ###### RSA ######

    if escolha.upper() == 'B':
        e = inputNumber("e = ")
        p = inputNumber("p = ")
        q = inputNumber("q = ")
        phi = (p-1)*(q-1)
        print(f"{bcolors.OKGREEN}d = {multiplicative_inverse(e, phi)}{bcolors.ENDC}")

    elif escolha.upper() == 'C':
        print("a (mod b)")
        b = inputNumber("mod = ")
        sair = ''
        while (sair.upper() != 'Y'):
            a = eval(input("a = "))
            print(f"{a} ≡ {bcolors.OKGREEN}{a%b}{bcolors.ENDC} (mod {b})")
            sair = input("Sair? [Y/N]: ")
    
    elif escolha.upper() == 'D':
        n = inputNumber("Numero a decompor = ")
        print(f"{bcolors.OKGREEN}{soma_pot_2(n)}{bcolors.ENDC}")
    
    # VER ALGORITMO RSA ! TO-DO
    elif escolha.upper() == 'E':
        rsa()

    ###### CONGRUENCIAS ######

    # MAXIMO DIVISOR COMUM
    elif escolha.upper() == 'F':
        a = inputNumber("a = ")
        b = inputNumber("b = ")

        print(f"{bcolors.OKGREEN}a ⌢ b = {gcd(a,b)}{bcolors.ENDC}")
    
    # SIMPLIFICAR CONGRUENCIAS
    elif escolha.upper() == 'G':
        print("ax ≡ b (mod N)")
        a_ini = inputNumber("a = ")
        b_ini = inputNumber("b = ")
        n = inputNumber("mod N = ")

        print(f"{a_ini}x ≡ {b_ini} (mod {n}) <=> {bcolors.OKGREEN}x ≡ {x} (mod {n}) {bcolors.ENDC}")

    # BEZOUT
    elif escolha.upper() == 'H':
        print("ax + by = a ⌢ b")
        a = inputNumber("a = ")
        b = inputNumber("b = ")
        
        mdc, x, y = saunderson(a, b)
        
        print(f"{a}x + {b}y = {mdc} => {bcolors.OKGREEN}x = {x}{bcolors.ENDC} e {bcolors.OKGREEN}y = {y}{bcolors.ENDC}")
    
    # EQUACOES DIOFANTINAS
    elif escolha.upper() == 'I':
        call(["chmod", "+x", "diofantinas"])
        call(["./diofantinas"])



    ###### CALENDARIO ######

    # DIA DA SEMANA JULIANO
    elif escolha.upper() == 'J':
        print("Dia D do mes de letra F do ano Y")
        D = inputNumber("D = ")
        F = inputNumber("F = ")
        Y = inputNumber("Y = ")
        W, FevOuJan = juliano(D, F, Y)

        dias_da_semana = [0, "Domingo", "Segunda-feira", "Terca-feira", "Quarta-feira", "Quinta-feira", "Sexta-feira", "Sabado"]
        print(f"-> {bcolors.OKGREEN}{W}, {dias_da_semana[W]}{bcolors.ENDC}, no calendario Juliano")

        mostrar_passos = input("Mostrar passos? [Y/N]: ")
        if mostrar_passos.upper() == 'Y':
            print(f"{bcolors.OKBLUE}A mostrar passos: {bcolors.ENDC}")
            passos_juliano(D, F, Y, FevOuJan)

    # DIA DA SEMANA GREGORIANO
    elif escolha.upper() == 'K':
        print("Dia D do mes de letra F do ano Y")
        D = inputNumber("D = ")
        F = inputNumber("F = ")
        Y = inputNumber("Y = ")
        W, FevOuJan = gregoriano(D, F, Y)

        dias_da_semana = [0, "Domingo", "Segunda-feira", "Terca-feira", "Quarta-feira", "Quinta-feira", "Sexta-feira", "Sabado"]
        print(f"-> {bcolors.OKGREEN}{W}, {dias_da_semana[W]}{bcolors.ENDC}, no calendario Gregoriano")

        mostrar_passos = input("Mostrar passos? [Y/N]: ")
        if mostrar_passos.upper() == 'Y':
            print(f"{bcolors.OKBLUE}A mostrar passos: {bcolors.ENDC}")
            passos_gregoriano(D, F, Y, FevOuJan)

    # PASCOA JULIANA
    elif escolha.upper() == 'L':
        Y = inputNumber("Y = ")
        S = pascoa_juliana(Y)
        if S > 30:
            print(f"A pascoa de {Y} e no dia -> {bcolors.OKGREEN}{S % 31} de Abril, S = {S},{bcolors.ENDC} no calendario Juliano")
        else:
            print(f"A pascoa de {Y} e no dia -> {bcolors.OKGREEN}{S} de Março, S = {S},{bcolors.ENDC} no calendario Juliano")

    # PASCOA GREGORIANA
    elif escolha.upper() == 'M':
        Y = inputNumber("Y = ")
        S = pascoa_gregoriana(Y)
        if S > 30:
            print(f"A pascoa de {Y} e no dia -> {bcolors.OKGREEN}{S % 31} de Abril, S = {S},{bcolors.ENDC} no calendario Gregoriano")
        else:
            print(f"A pascoa de {Y} e no dia -> {bcolors.OKGREEN}{S} de Março, S = {S},{bcolors.ENDC} no calendario Gregoriano")



    ###### GRAFOS ######

    #NOCOES BASICAS
    elif escolha.upper() == 'N':
        nocoes_grafos()

    #TEOREMAS
    elif escolha.upper() == 'O':
        teoremas_grafos()

    #ALGORITMO DE FLEURY
    elif escolha.upper() == 'P':
        if fleury_apl():
            print("Escolhe uma aresta incidente no vertice em causa, desde que nao seja ponte\n(ou seja, ao ser apagada, nao divide o grafo), apaga-a e repete.")
            print(f"{bcolors.WARNING}Escolhe uma ponte apenas em ultimo recurso!{bcolors.ENDC}")



    ###### SAIDA ######
    elif escolha.upper() == 'X':
        print(f"{bcolors.WARNING}A sair...{bcolors.ENDC}")
        sleep(0.2)
        exit()



    ###### ERRO DE INPUT ######
    else:
        print("Escolha nao valida, tenta de novo!")