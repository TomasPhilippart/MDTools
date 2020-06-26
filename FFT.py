class bcolors:
    HEADER = '\033[95m'
    OKBLUE = '\033[94m'
    OKGREEN = '\033[92m'
    WARNING = '\033[93m'
    FAIL = '\033[91m'
    ENDC = '\033[0m'
    BOLD = '\033[1m'
    UNDERLINE = '\033[4m'


class Complexo:
    def __init__(self, p_real, p_complexo):
        self.p_real = p_real
        self.p_complexo = p_complexo

    def __repr__(self):
        # Representacao externa do complexo
        if self.p_complexo == 0:
            return str(self.p_real)
        elif self.p_complexo > 0:
            return "{} + {}i".format(self.p_real, self.p_complexo)
        else:
            return "{} - {}i".format(self.p_real, abs(self.p_complexo))

    def __add__(self, other):
        # Faz a adicao entre dois numeros complexos
        p_real_final = self.p_real + other.p_real
        p_complexo_final = self.p_complexo + other.p_complexo
        
        return Complexo(p_real_final, p_complexo_final)

    def __sub__(self, other):
        # Faz a subtracao entre dois numeros complexos
        p_real_final = self.p_real - other.p_real
        p_complexo_final = self.p_complexo - other.p_complexo
        
        return Complexo(p_real_final, p_complexo_final)

    def __mul__(self, other):
        # Multiplicacao de numeros complexos
        p_real_final = (self.p_real * other.p_real) - (self.p_complexo * other.p_complexo)
        p_complexo_final = (self.p_real * other.p_complexo) + (self.p_complexo * other.p_real)
        
        return Complexo(p_real_final, p_complexo_final)
    def __rmul__(self, other):
        # Multiplicacao de numeros complexos
        p_real_final = (self.p_real * other.p_real) - (self.p_complexo * other.p_complexo)
        p_complexo_final = (self.p_real * other.p_complexo) + (self.p_complexo * other.p_real)
        
        return Complexo(p_real_final, p_complexo_final)

    def conjugado(self):
        return Complexo(self.p_real, (-1 * self.p_complexo))

    def altera(self, real, complexo):
        self.p_real = real
        self.p_complexo = complexo



def obter_vetor():
    x0 = eval(input("       Introduz o termo independente (x^0) : "))
    x1 = eval(input("       Introduz o termo de grau 1 (x^1) : "))
    x2 = eval(input("       Introduz o termo de grau 2 (x^2) : "))
    x3 = eval(input("       Introduz o termo de grau 3 (x^3) : "))

    return [Complexo(x0, 0), Complexo(x1, 0), Complexo(x2, 0), Complexo(x3, 0)]

def rev(vetor):
    vetor[1], vetor[2] = vetor[2], vetor[1]
    return vetor

def conjugado_vetor(vetor):
    for i in range(len(vetor)):
        vetor[i] = vetor[i].conjugado()

    return vetor

def multiplica_vetores(vetor1, vetor2):
    for i in range(len(vetor1)):
        vetor1[i] = vetor1[i] * vetor2[i]

    return vetor1

def processar_vetor(vetor):
    f1_c = [vetor[0] + vetor[1], vetor[0] - vetor[1]]
    print()
    print("\033[94mF1(-1)\033[0m  [ {} ] = [ 1   1 ] [ {} ] = [ \033[92m{}\033[0m ]".format(vetor[0], vetor[0], f1_c[0]))
    print("       [ {} ]   [ 1  -1 ] [ {} ]   [ \033[92m{}\033[0m ]".format(vetor[1], vetor[1], f1_c[1]))

    f1_b = [vetor[2] + vetor[3], vetor[2] - vetor[3]]
    print()
    print("\033[94mF1(-1)\033[0m [ {} ] = [ 1   1 ] [ {} ] = [ \033[92m{}\033[0m ]".format(vetor[2], vetor[2], f1_b[0]))
    print("       [ {} ]   [ 1  -1 ] [ {} ]   [ \033[92m{}\033[0m ]".format(vetor[3], vetor[3], f1_b[1]))

    d1f1_b = [f1_b[0], f1_b[1] * Complexo(0, 1)]
    print()
    print("\033[94mD1F1(-1)\033[0m [ {} ] = [ 1  0 ]  [ 1   1 ] [ {} ] = [ \033[92m{}\033[0m ]".format(vetor[2], vetor[2], d1f1_b[0]))
    print("         [ {} ]   [ 0  i ]  [ 1  -1 ] [ {} ]   [ \033[92m{}\033[0m ]".format(vetor[3], vetor[3], d1f1_b[1]))

    final = [f1_c[0] + d1f1_b[0], f1_c[1] + d1f1_b[1], f1_c[0] - d1f1_b[0], f1_c[1] - d1f1_b[1]]
    print()
    print("[ [ \033[92m{}\033[0m ]  +  [ \033[92m{}\033[0m ] ]  = [ \033[92m{}\033[0m ]".format(f1_c[0], d1f1_b[0], final[0]))
    print("[ [ \033[92m{}\033[0m ]     [ \033[92m{}\033[0m ] ]    [ \033[92m{}\033[0m ]".format(f1_c[1], d1f1_b[1], final[1]))
    print("[                   ]            ")
    print("[ [ \033[92m{}\033[0m ]  -  [ \033[92m{}\033[0m ] ]    [ \033[92m{}\033[0m ]".format(f1_c[0], d1f1_b[0], final[2]))
    print("[ [ \033[92m{}\033[0m ]     [ \033[92m{}\033[0m ] ]    [ \033[92m{}\033[0m ]".format(f1_c[1], d1f1_b[1], final[3]))
    return final

def copia_vetor(vetor):
    novo_vetor = []
    for elemento in vetor:
        novo_vetor.append(elemento)

    return novo_vetor

def dividir_vetor(vetor):
    for i in range(len(vetor)):
        v_real = vetor[i].p_real // 4
        v_complexo = vetor[i].p_complexo // 4
        vetor[i].altera(v_real, v_complexo) 

    return vetor   

def vetor_para_polinomio(vetor):
    polinomio = ""
    for i in range(len(vetor)):
        if vetor[i].p_real > 0: 
            polinomio += " + {}x^{}".format(vetor[i].p_real, i)
        elif vetor[i].p_real < 0:
            polinomio += " - {}x^{}".format(abs(vetor[i].p_real), i)

    return polinomio

def fft():
    print("    - Introduz os valores do \033[94mprimeiro polinomio\033[0m")
    vetor1 = obter_vetor()

    print()
    print("    - Introduz os valores do \033[94msegundo polinomio\033[0m")
    vetor2 = obter_vetor()

    print()
    print("    - Aplicar a funcao \033[94mrev ao vetor {}\033[0m".format(vetor1))
    no_rev = copia_vetor(vetor1)
    vetor1 = rev(vetor1)
    print("       {}  ------------> {}".format(no_rev, vetor1))

    print()
    print("    - Aplicar a funcao \033[94mrev ao vetor {}\033[0m".format(vetor2))
    no_rev = copia_vetor(vetor2)
    vetor2 = rev(vetor2)
    print("       {}  ------------> {}".format(no_rev, vetor2))

    print()
    print("    - \033[94mProcessar o vetor {}\033[0m".format(vetor1))
    vetor1 = processar_vetor(vetor1)

    print()
    print("    - \033[94mProcessar o vetor {}\033[0m".format(vetor2))
    vetor2 = processar_vetor(vetor2)

    print()
    print("    - \033[94mMultiplicar os vetores {} e {}\033[0m".format(vetor1, vetor2))
    resultado = multiplica_vetores(vetor1, vetor2)
    print("       Resultado :  {}".format(resultado))


    print()
    print("    - \033[94mAplicar a funcao rev ao vetor {} e conjugar\033[0m".format(resultado))
    no_rev = copia_vetor(resultado)
    resultado = rev(conjugado_vetor(resultado))
    print("       {}  ------------> {}".format(no_rev, resultado))

    print()
    print("    - \033[94mProcessar o vetor {}\033[0m".format(resultado))
    resultado = processar_vetor(resultado)
    
    print()
    print("    - \033[94mDividir todos os elementos do vetor por 2^2\033[0m")
    resultado = dividir_vetor(resultado)
    print("       Resultado :  {}".format(resultado))

    print()
    print("    - \033[94mO resultado do produto dos polinomios dados e:\033[0m")
    resultado = vetor_para_polinomio(resultado)
    print("       \033[94m{}\033[0m".format(resultado))
    
