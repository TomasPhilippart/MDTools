class bcolors:
    HEADER = '\033[95m'
    OKBLUE = '\033[94m'
    OKGREEN = '\033[92m'
    WARNING = '\033[93m'
    FAIL = '\033[91m'
    ENDC = '\033[0m'
    BOLD = '\033[1m'
    UNDERLINE = '\033[4m'

def teoremas_grafos():
    print(f"{bcolors.FAIL}//// TEOREMAS SOBRE GRAFOS ////\n\n{bcolors.ENDC}")

    #Primeiro teorema
    print(f"{bcolors.OKBLUE}-= Primeiro teorema da teoria dos grafos =-{bcolors.ENDC}")
    print("A soma dos graus de um grafo de p vertices e igual a 2 * q (numero de arestas)")
    print(f"{bcolors.OKGREEN}(u,v) e (v,u) correspondem a mesma aresta, logo a mesma aresta e contabilizada 2 vezes.\n{bcolors.ENDC}")

    #Numero par de vertices impares
    print(f"{bcolors.OKBLUE}-= Segundo teorema da teoria dos grafos =-{bcolors.ENDC}")
    print("Um grafo possui sempre um numero par de vertices impares")
    print(f"{bcolors.OKGREEN}Se a soma dos graus dos vertices e par, e os outros vertices tem grau par (logo a soma e par),\na soma dos vertices de grau impar tem de ser par, e, portanto, tem de existir um numero par de vertices impares.\n{bcolors.ENDC}")

    #Limite de arestas
    print(f"{bcolors.OKBLUE}-= Teorema (limites do numero de arestas) =-{bcolors.ENDC}")
    print("Um grafo de p vertices e k componentes possui um numero de arestas (q) tal que:\np - k <= q <= (p-k+1)(p-k)/2.")
    print(f"{bcolors.OKGREEN}O limite minimo e para k arvores, e o limite maximo e para\numa componente de p-k vertices e k componentes de 1 vertice.\n{bcolors.ENDC}")

    ##Corolarios
    print(f"{bcolors.OKBLUE}-= Corolarios =-{bcolors.ENDC}")
    print("Se o grafo possui mais de (p-1)(p-2)/2 componentes, e conexo (possui uma componente)\nUsa a formula para k = 2 e confirma!\n")
    print("Uma arvore possui o minimo de arestas possivel: p-1 - Usa a formula para k = 1 e confirma!\n")

    #Teoremas de Euler-Hierholzer
    print(f"{bcolors.OKBLUE}-= Teoremas de Euler-Hierholzer =-{bcolors.ENDC}")
    print("Um grafo tem circuito euleriano se e so se for conexo e todos os seus vertices forem pares.\n")
    print("Um grafo e atravessavel se e so se for conexo e tiver apenas 2 vertices impares\n(que, ao serem ligados temporariamente, formam um circuito euleriano).\n")
    print(f"{bcolors.OKGREEN}Estes teoremas sao uteis no Algoritmo de Fleury\n(usado, p.ex., no problema das pontes de Konigsberg).\n\n{bcolors.ENDC}")


def nocoes_grafos():
    print(f"{bcolors.FAIL}//// NOCOES BASICAS SOBRE GRAFOS ////\n\n{bcolors.ENDC}")
    
    #Grafo
    print("Um grafo e um par ordenado <V,E> em que V sao os vertices e E sao as arestas\n(pares ordenados de vertices diferentes - (x,x) nao e aresta!)")
    print(f"{bcolors.OKGREEN}Em grafos normais, as arestas sao simetricas, ou seja, (x,y) e (y,x) sao arestas.\n{bcolors.ENDC}")
    
    #Grau de um vertice
    print("O grau de um vertice e o numero de arestas que nele incidem - pode ser par ou impar.\n")
    
    #Digrafo
    print("Um grafo orientado (ou digrafo) e um grafo em que as arestas nao sao necessariamente simetricas.")
    print(f"{bcolors.OKGREEN}(x,y) existir nao implica que (y,x) tambem exista.\n{bcolors.ENDC}")

    #Rede
    print("Uma rede e um terno ordenado <V,E,f> em que <V,E> e um grafo e f e uma funcao de E para IR.\n")

    #Pseudografo
    print("Um pseudografo e um grafo que pode contar multiplas arestas entre vertices\ne lacos (arestas de um vertice para ele proprio).\n\n")
