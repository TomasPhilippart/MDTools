from func_aux import *
from calendarios import *
from time import sleep



# ============ MAIN ============
print(f"\n{bcolors.HEADER}\t============ RSA TOOL ============{bcolors.ENDC}")
while(1):
    escolha = input(f"""
        --------------{bcolors.BOLD} Menu {bcolors.ENDC}--------------
        A) Descobrir inverso de e mod (p-1)*(q-1)
        B) Fazer modulos rapidamente
        C) Obter soma em base 2 de numero
        D) Ver algoritmo RSA 
        E) Maximo Divisor Comum

        {bcolors.BOLD}Calendarios{bcolors.ENDC}
        F) Juliano
        G) Gregoriano
        H) Pascoa Juliana
        I) Pascoa Gregoriana

        X) Sair

{bcolors.BOLD}Escolha:{bcolors.ENDC} """)


    if escolha == 'A':
        e = inputNumber("e = ")
        p = inputNumber("p = ")
        q = inputNumber("q = ")
        phi = (p-1)*(q-1)

        print(f"{bcolors.OKGREEN}d = {multiplicative_inverse(e, phi)}{bcolors.ENDC}")

    elif escolha == 'B':
        print("a (mod b)")
        b = inputNumber("mod = ")
        sair = ''
        while (sair != 'y'):
            a = inputNumber("a = ")
            print(f"{a} ≡ {bcolors.OKGREEN}{a%b}{bcolors.ENDC} (mod {b})")
            sair = input("Sair? [y]: ")
    
    elif escolha == 'C':
        n = inputNumber("Numero a decompor = ")
        print(f"{bcolors.OKGREEN}{soma_pot_2(n)}{bcolors.ENDC}")

    elif escolha == 'X':
        print(f"{bcolors.WARNING}A sair...{bcolors.ENDC}")
        sleep(0.2)
        exit()
    
    elif escolha == 'D':
        continue

    elif escolha == 'E':
        a = inputNumber("a = ")
        b = inputNumber("b = ")

        print(f"{bcolors.OKGREEN}a ⌢ b = {gcd(a,b)}{bcolors.ENDC}")

    elif escolha == 'F':
        print("Dia D do mes de letra F do ano Y")
        D = inputNumber("D = ")
        F = inputNumber("F = ")
        Y = inputNumber("Y = ")
        W, FevOuJan = juliano(D, F, Y)

        dias_da_semana = [0, "Domingo", "Segunda-feira", "Terca-feira", "Quarta-feira", "Quinta-feira", "Sexta-feira", "Sabado"]
        print(f"-> {bcolors.OKGREEN}{W}, {dias_da_semana[W]}{bcolors.ENDC}, no calendario Juliano")

        mostrar_passos = input("Mostar passos? [y/n]: ")
        if mostrar_passos == 'y':
            print("\n")
            print(f"{bcolors.OKBLUE}A mostrar passos: {bcolors.ENDC}")
            passos_juliano(D, F, Y, FevOuJan)


    elif escolha == 'G':
        print("Dia D do mes de letra F do ano Y")
        D = inputNumber("D = ")
        F = inputNumber("F = ")
        Y = inputNumber("Y = ")
        W, FevOuJan = gregoriano(D, F, Y)

        dias_da_semana = [0, "Domingo", "Segunda-feira", "Terca-feira", "Quarta-feira", "Quinta-feira", "Sexta-feira", "Sabado"]
        print(f"-> {bcolors.OKGREEN}{W}, {dias_da_semana[W]}{bcolors.ENDC}, no calendario Gregoriano")

        mostrar_passos = input("Mostar passos? [y/n]: ")
        if mostrar_passos == 'y':
            print("\n")
            print(f"{bcolors.OKBLUE}A mostrar passos: {bcolors.ENDC}")
            passos_gregoriano(D, F, Y, FevOuJan)

    elif escolha == 'H':
        Y = inputNumber("Y = ")
        S = pascoa_juliana(Y)
        print(f"A pascoa de {Y} e no dia -> {bcolors.OKGREEN}{S},{bcolors.ENDC} no calendario Juliano")

    elif escolha == 'I':
        Y = inputNumber("Y = ")
        S = pascoa_gregoriana(Y)
        print(f"A pascoa de {Y} e no dia -> {bcolors.OKGREEN}{S},{bcolors.ENDC} no calendario Gregoriana")

    else:
        print("Escolha nao valida, tenta de novo!")

