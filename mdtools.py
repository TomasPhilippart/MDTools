from func_aux import *
from calendarios import *
from teoremas_grafos import *
from percorrer_grafos import *
from FFT import *
from RSA import *
from subprocess import call

######################### MD TOOLS #########################
#                                                          #
# Instituto Superior Técnico - LEIC-A - 1º Ano             #
#                                                          #
# Lançamento original: 07/07/2020                          #
# Versão Atual: 1.3 - Lançada a 01/08/2020                 #
#                                                          #
# Programa criado para auxiliar diversos cálculos em áreas #
# lecionadas na disciplina de Matemática Discreta          #
#                                                          #
# Criado por:                                              #
# David Belchior                                           #
# Gustavo Aguiar                                           #
# Tomás Philippart                                         #
# Tomás Tavares                                            #
############################################################

# ============ MAIN ============
print(f"\n{bcolors.OKBLUE}\t============ MD TOOLS ============\n\nVersao 1.3 - 01/08/2020 - Criado por:\n\nDavid Belchior\nGustavo Aguiar\nTomas Philippart\nTomas Tavares{bcolors.ENDC}")
while True:
    sair1 = ""
    erro = False
    escolha = input(f"""
        --------------{bcolors.BOLD} Menu {bcolors.ENDC}--------------
        {bcolors.BOLD}
        A) Ver algoritmo FFT{bcolors.ENDC}

        {bcolors.BOLD}RSA{bcolors.ENDC}
        B) Descobrir inverso de e mod (p-1)*(q-1)
        C) Fazer congruencias rapidamente
        D) Obter soma em base 2 de numero
        E) Ver algoritmo RSA
        
        {bcolors.BOLD}Congruencias{bcolors.ENDC}
        F) Maximo Divisor Comum
        G) Algoritmo de Saunderson e Coeficientes de Bezout
        H) Equacoes Diofantinas

        {bcolors.BOLD}Calendarios{bcolors.ENDC}
        I) Juliano
        J) Gregoriano
        K) Pascoa Juliana
        L) Pascoa Gregoriana (passo a passo)

        {bcolors.BOLD}Grafos{bcolors.ENDC}
        M) Nocoes Basicas
        N) Teoremas
        O) Algoritmo de Fleury

        X) Sair

{bcolors.BOLD}Escolha:{bcolors.ENDC} """)

    while (sair1.upper() != 'Y'):

        ###### FFT ######

        if escolha.upper() == 'A':
            fft()

        ###### RSA ######

        elif escolha.upper() == 'B':
            e = inputNumber("e = ")
            p = inputNumber("p = ")
            q = inputNumber("q = ")
            phi = (p-1)*(q-1)
            print(f"{bcolors.OKGREEN}d = {multiplicative_inverse(e, phi)}{bcolors.ENDC}")

        elif escolha.upper() == 'C':
            print("a (mod b)")
            a = inputNumber("a = ")
            b = inputNumber("mod = ")
            print(f"{a} ≡ {bcolors.OKGREEN}{a%b}{bcolors.ENDC} (mod {b})")

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

        # ALGORITMO DE SAUNDERSON / COEFICIENTES DE BEZOUT
        elif escolha.upper() == 'G':
            print("ax + by = a ⌢ b")
            a = inputNumber("a = ")
            b = inputNumber("b = ")
            
            mdc, x, y = saunderson(a, b)
            
            print(f"{a}x + {b}y = {mdc} => {bcolors.OKGREEN}x = {x}{bcolors.ENDC} e {bcolors.OKGREEN}y = {y}{bcolors.ENDC}")

        # EQUACOES DIOFANTINAS
        elif escolha.upper() == 'H':
            call(["gcc", "-o", "diofantinas", "diofantinas.c"])
            call(["./diofantinas"])



        ###### CALENDARIO ######

        # DIA DA SEMANA JULIANO
        elif escolha.upper() == 'I':
            D = inputNumber("Dia = ")
            F = inputNumber("Mes = ")
            Y = inputNumber("Ano = ")
            W, FevOuJan = juliano(D, F, Y)

            dias_da_semana = [0, "Domingo", "Segunda-feira", "Terca-feira", "Quarta-feira", "Quinta-feira", "Sexta-feira", "Sabado"]
            print(f"-> {bcolors.OKGREEN}{W}, {dias_da_semana[W]}{bcolors.ENDC}, no calendario Juliano")

            mostrar_passos = input("Mostrar passos? [Y/N]: ")
            if mostrar_passos.upper() == 'Y':
                print(f"{bcolors.OKBLUE}A mostrar passos: {bcolors.ENDC}")
                passos_juliano(D, F, Y, FevOuJan)

        # DIA DA SEMANA GREGORIANO
        elif escolha.upper() == 'J':
            D = inputNumber("Dia = ")
            M = inputNumber("Mes = ")
            Y = inputNumber("Ano = ")

            # ADDGBEGCFADF
            F = escolheMes(M)

            W, FevOuJan = gregoriano(D, F, Y)

            dias_da_semana = [0, "Domingo", "Segunda-feira", "Terca-feira", "Quarta-feira", "Quinta-feira", "Sexta-feira", "Sabado"]
            print(f"-> {bcolors.OKGREEN}{W}, {dias_da_semana[W]}{bcolors.ENDC}, no calendario Gregoriano")

            mostrar_passos = input("Mostrar passos? [Y/N]: ")
            if mostrar_passos.upper() == 'Y':
                print(f"{bcolors.OKBLUE}A mostrar passos: {bcolors.ENDC}")
                passos_gregoriano(D, F, Y, FevOuJan)

        # PASCOA JULIANA
        elif escolha.upper() == 'K':
            Y = inputNumber("Ano = ")
            S = pascoa_juliana(Y)
            if S > 30:
                print(f"A pascoa de {Y} e no dia -> {bcolors.OKGREEN}{S % 31} de Abril, S = {S},{bcolors.ENDC} no calendario Juliano")
            else:
                print(f"A pascoa de {Y} e no dia -> {bcolors.OKGREEN}{S} de Março, S = {S},{bcolors.ENDC} no calendario Juliano")

        # PASCOA GREGORIANA
        elif escolha.upper() == 'L':
            Y = inputNumber("Ano = ")
            S = pascoa_gregoriana(Y)
            if S > 31:
                print(f"A pascoa de {Y} e no dia -> {bcolors.OKGREEN}{S % 31} de Abril, S = {S},{bcolors.ENDC} no calendario Gregoriano")
            else:
                print(f"A pascoa de {Y} e no dia -> {bcolors.OKGREEN}{S} de Março, S = {S},{bcolors.ENDC} no calendario Gregoriano")



        ###### GRAFOS ######

        #NOCOES BASICAS
        elif escolha.upper() == 'M':
            nocoes_grafos()

        #TEOREMAS
        elif escolha.upper() == 'N':
            teoremas_grafos()

        #ALGORITMO DE FLEURY
        elif escolha.upper() == 'O':
            if fleury_apl():
                print("Escolhe uma aresta incidente no vertice em causa, desde que nao seja ponte\n(ou seja, ao ser apagada, nao divide o grafo), apaga-a e repete.")
                print(f"{bcolors.WARNING}Escolhe uma ponte apenas em ultimo recurso!{bcolors.ENDC}")



        ###### SAIDA ######
        elif escolha.upper() == 'X':
            sair()



        ###### ERRO DE INPUT ######
        else:
            erro = True
            print(f"{bcolors.FAIL}Escolha nao valida, tenta de novo!{bcolors.ENDC}")
            sleep(0.5)
            break
        
        sair1 = input("Pretendes sair desta ferramenta? [Y/N]: ")

    ###### SAIR DO PROGRAMA? ######
    if not erro:
        sair2 = ""
        while (sair2.upper() not in ["Y", "N"]):
            sair2 = input("Pretendes sair? [Y/N]: ")
            if (sair2.upper() == "Y"):
                sair()
            elif (sair2.upper() == "N"):
                print(f"{bcolors.OKBLUE}A retornar ao menu...{bcolors.ENDC}")
                sleep(0.5)
                break
            print(f"{bcolors.FAIL}Escolha nao valida, tenta de novo!{bcolors.ENDC}")
            sleep(0.5)