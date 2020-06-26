class bcolors:
    HEADER = '\033[95m'
    OKBLUE = '\033[94m'
    OKGREEN = '\033[92m'
    WARNING = '\033[93m'
    FAIL = '\033[91m'
    ENDC = '\033[0m'
    BOLD = '\033[1m'
    UNDERLINE = '\033[4m'

def fleury_apl():
    Conexo = input("O grafo e conexo? [y/n] ")
    if Conexo == 'y':
        Euleriano = input("Todos os vertices do grafo tem grau par? [y/n] ")
        if Euleriano == 'y':
            print(f"O grafo e {bcolors.OKGREEN}euleriano{bcolors.ENDC}.")
            print(f"{bcolors.OKGREEN}Algoritmo de Fleury aplicavel, comecando em qualquer vertice e acabando nele proprio.{bcolors.ENDC}")
            return True;
        elif Euleriano == 'n':
            print(f"{bcolors.WARNING}O grafo nao e euleriano.{bcolors.ENDC}")
            Atravessavel = input("O grafo possui apenas 2 vertices de grau impar? [y/n] ")
            if Atravessavel == 'y':
                print(f"O grafo e {bcolors.OKGREEN}atravessavel{bcolors.ENDC}.")
                print(f"{bcolors.OKGREEN}Algoritmo de Fleury aplicavel, comecando num dos vertices de grau impar e acabando no outro.{bcolors.ENDC}")
                return True;
            else:
                print(f"{bcolors.FAIL}Algoritmo de Fleury nao aplicavel.{bcolors.ENDC}")
                return False;
        else:
            print(f"{bcolors.WARNING}Input incorreto, tenta de novo!{bcolors.ENDC}")
            return False;
    elif Conexo == 'n':
        print(f"{bcolors.FAIL}Algoritmo de Fleury nao aplicavel.{bcolors.ENDC}")
        return False;
    else:
        print(f"{bcolors.WARNING}Input incorreto, tenta de novo!{bcolors.ENDC}")
        return False;

