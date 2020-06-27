class bcolors:
    HEADER = '\033[95m'
    OKBLUE = '\033[94m'
    OKGREEN = '\033[92m'
    WARNING = '\033[93m'
    FAIL = '\033[91m'
    ENDC = '\033[0m'
    BOLD = '\033[1m'
    UNDERLINE = '\033[4m'

<<<<<<< HEAD
def teoremas_grafos():
    print(f"{bcolors.FAIL}//// TEOREMAS SOBRE GRAFOS ////\n\n{bcolors.ENDC}")

    #Primeiro teorema
    print(f"{bcolors.OKBLUE}-= Primeiro teorema da teoria dos grafos =-{bcolors.ENDC}")
    print("A soma dos graus de um grafo de p vertices e igual a 2 * q (numero de arestas)")
=======
def nocoes_grafos():
    print(f"\n{bcolors.FAIL}//// NOCOES BASICAS SOBRE GRAFOS ////\n{bcolors.ENDC}")
    
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
    print("Um pseudografo e um grafo que pode contar multiplas arestas entre vertices\ne lacos (arestas de um vertice para ele proprio).\n")

    #Grafo planar
    print("Um grafo e planar se e so se nao houver intersecao de arestas (a excecao dos vertices).\n")

def teoremas_grafos():
    print(f"\n{bcolors.FAIL}//// TEOREMAS SOBRE GRAFOS ////\n{bcolors.ENDC}")

    #Primeiro teorema
    print(f"{bcolors.OKBLUE}-= Primeiro teorema da teoria dos grafos =-{bcolors.ENDC}")
    print("A soma dos graus de um grafo de p vertices e igual a 2 * q (numero de arestas).\n")
>>>>>>> MDTools-Funky
    print(f"{bcolors.OKGREEN}(u,v) e (v,u) correspondem a mesma aresta, logo a mesma aresta e contabilizada 2 vezes.\n{bcolors.ENDC}")

    #Numero par de vertices impares
    print(f"{bcolors.OKBLUE}-= Segundo teorema da teoria dos grafos =-{bcolors.ENDC}")
<<<<<<< HEAD
    print("Um grafo possui sempre um numero par de vertices impares")
=======
    print("Um grafo possui sempre um numero par de vertices impares.\n")
>>>>>>> MDTools-Funky
    print(f"{bcolors.OKGREEN}Se a soma dos graus dos vertices e par, e os outros vertices tem grau par (logo a soma e par),\na soma dos vertices de grau impar tem de ser par, e, portanto, tem de existir um numero par de vertices impares.\n{bcolors.ENDC}")

    #Limite de arestas
    print(f"{bcolors.OKBLUE}-= Teorema (limites do numero de arestas) =-{bcolors.ENDC}")
<<<<<<< HEAD
    print("Um grafo de p vertices e k componentes possui um numero de arestas (q) tal que:\np - k <= q <= (p-k+1)(p-k)/2.")
    print(f"{bcolors.OKGREEN}O limite minimo e para k arvores, e o limite maximo e para\numa componente de p-k vertices e k componentes de 1 vertice.\n{bcolors.ENDC}")

    ##Corolarios
    print(f"{bcolors.OKBLUE}-= Corolarios =-{bcolors.ENDC}")
=======
    print("Um grafo de p vertices e k componentes possui um numero de arestas (q) tal que:\np - k <= q <= (p-k+1)(p-k)/2.\n")
    print(f"{bcolors.OKGREEN}O limite minimo e para k arvores, e o limite maximo e para\numa componente de p-k vertices e k componentes de 1 vertice.\n{bcolors.ENDC}")

    ##Corolarios
    print(f"{bcolors.OKGREEN}-= Corolarios =-{bcolors.ENDC}")
>>>>>>> MDTools-Funky
    print("Se o grafo possui mais de (p-1)(p-2)/2 componentes, e conexo (possui uma componente)\nUsa a formula para k = 2 e confirma!\n")
    print("Uma arvore possui o minimo de arestas possivel: p-1 - Usa a formula para k = 1 e confirma!\n")

    #Teoremas de Euler-Hierholzer
<<<<<<< HEAD
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
=======
    print(f"{bcolors.OKBLUE}-= Teoremas de Euler-Hierholzer (Suporte ao algoritmo de Fleury) =-{bcolors.ENDC}")
    print("Um grafo tem circuito euleriano se e so se for conexo e todos os seus vertices forem pares.\n")
    print("Um grafo e atravessavel se e so se for conexo e tiver apenas 2 vertices impares\n(que, ao serem ligados temporariamente, formam um circuito euleriano).\n")
    print(f"{bcolors.OKGREEN}Estes teoremas sao uteis no Algoritmo de Fleury\n(usado, p.ex., no problema das pontes de Konigsberg).\n{bcolors.ENDC}")

    #Teorema de suporte ao algoritmo de Kruskal
    print(f"{bcolors.OKBLUE}-= Teorema (Suporte ao algoritmo de Kruskal) =-{bcolors.ENDC}")
    print("A arvore economica construida numa rede R = <V,E,f> por aplicacao\ndo algoritmo de Kruskal e uma arvore de custo minimo.\n")
    print(f"{bcolors.OKGREEN}Ao alterarmos, aresta a aresta, o grafo obtido pelo algoritmo\nde Kruskal, ate que se torne numa arvore de custo minimo,\nconcluimos que as arestas novas tem de ter custo <= que as anteriores,\npois as arestas da arvore de custo minimo possuem o custo minimo possivel,\ne custo >=, pois, caso contrario, teriam sido escolhidas pelo\nalgoritmo de Kruskal. Portanto, tanto uma como outra tem custo minimo.\n{bcolors.ENDC}")

    #Teorema de suporte ao algoritmo de Ford-Fulkerson
    print(f"{bcolors.OKBLUE}-= Teorema (Suporte ao algoritmo de Ford-Fulkerson) =-{bcolors.ENDC}")
    print("O fluxo numa rede capacitada e maximo se e so se nao existir uma quasitrajetoria de aumento.\n")
    print(f"{bcolors.OKGREEN}Se o fluxo for maximo, nao existe qualquer quasitrajetoria de aumento.\nSe nao existir qualquer quasitrajetoria de aumento, a rede pode ser\ndividida em 2 partes, sendo a divisao (o corte) nas arestas em que\no fluxo nas do sentido 'direto' e igual a sua capacidade e,nas do sentido 'contrario', e igual a 0.\nPortanto, o fluxo na rede em causa e, necessariamente, o maximo possivel.{bcolors.ENDC}\n")

    #Relacao de Euler
    print(f"{bcolors.OKBLUE}-= Teorema (Relacao de Euler) =-{bcolors.ENDC}")
    print("Um grafo planar de p vertices, q arestas e r regioes respeita a relacao:\n p + q = r + 2.\n")

    #Teorema de dimensao de grafos planares
    print(f"{bcolors.OKBLUE}-= Teorema de dimensao de grafos planares =-{bcolors.ENDC}")
    print("Um grafo conexo planar com 3 ou mais vertices possui numero de arestas tal que:\n q <= 3p - 6.\n")
    print("Se o grafo nao possuir triangulos, tem-se que q <= 2p - 4.\n")

    ##Corolarios
    print(f"{bcolors.OKGREEN}-= Corolarios =-{bcolors.ENDC}")
    print("K5 (grafo completo de 5 vertices) nao e planar,\npois p = 5, q = 10 e 10 <= 3 * 5 - 6 = 9 é falso!\n")
    print("K3,3 (grafo bipartido de 3 vertices por parte)\nnao e planar, pois p = 6, q = 9, nao possui triangulos\ne 9 <= 2 * 6 - 4 = 8 é falso!\n")

    print(f"{bcolors.OKBLUE}-= Teorema =-{bcolors.ENDC}")
    print("Num grafo planar conexo, existe sempre um vertice de grau <= 5.\n")

    #Teorema de Kuratowski
    print(f"{bcolors.OKBLUE}-= Teorema de Kuratowski =-{bcolors.ENDC}")
    print("Um grafo e planar se e so se nao possuir\n(se nao for homeomorfico com) um subgrafo nao planar.\n")
    print(f"{bcolors.OKGREEN}Sendo K5 e K3,3 nao planares, se encontrarmos um subgrafo equivalente\na um desses dois, podemos concluir que o grafo em causa nao e planar.{bcolors.ENDC}\n")
>>>>>>> MDTools-Funky
