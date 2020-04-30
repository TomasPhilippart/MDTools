from func_aux import *
from time import sleep


# ============ MAIN ============
print(f"\n{bcolors.HEADER}\t============ RSA TOOL ============{bcolors.ENDC}")
while(1):
    escolha = input(f"""
        --------------{bcolors.BOLD} Menu {bcolors.ENDC}--------------
        A: Descobrir inverso de e mod (p-1)*(q-1)
        B: Fazer modulos rapidamente
        C: Obter soma em base 2 de numero
        D: Ver algoritmo RSA 
        E: Maximo Divisor Comum
        X: Sair

Escolha: """)


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
    else:
        print("Escolha nao valida, tenta de novo!")

