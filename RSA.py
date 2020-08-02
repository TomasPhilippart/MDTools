from func_aux import soma_pot_2, soma_pot_2_aux, multiplicative_inverse, bcolors, inputNumber

def rsa_aux(block, x, N):
    
    """Esta funcao recebe o bloco a (des)encriptar, o expoente e o modulo,
    mostra as potencias de base 2 que compoem o expoente, efetua o algoritmo
    passo a passo, e no fim exibe o bloco (des)encriptado."""

    print(soma_pot_2(x))
    powers = soma_pot_2_aux(x)
    max_power = powers[0]
    nums_cong = [block]
    num_cong_ant = block
    total = block

    for i in range(1, max_power + 1):
        num = num_cong_ant ** 2
        num_cong = num % N
        if i in powers:
            nums_cong = [num_cong] + nums_cong
            total *= num_cong
        if i == 1:
            print(f"{block}^{2 ** i} = {num} ≡ {bcolors.OKGREEN}{num_cong}{bcolors.ENDC} (mod {N})")
        else:
            print(f"{block}^{2 ** i} ≡ {num_cong_ant} ^ 2 = {num} ≡ {bcolors.OKGREEN}{num_cong}{bcolors.ENDC} (mod {N})")
        num_cong_ant = num_cong

    display = f"{block}^{x} = "

    for i in powers:
        display += f"{block}^{2**i} * "

    display = display[:-2] + "≡ "

    for i in nums_cong:
        display += f"{i} * "

    display = display[:-2] + f"= {total} ≡ {bcolors.FAIL}{total % N}{bcolors.ENDC} (mod {N})"
    print(display)

def rsa():

    p = inputNumber("p = ")
    q = inputNumber("q = ")
    N = p * q
    e = inputNumber("e = ") # Chave de encriptacao
    phi = (p-1)*(q-1)
    d = multiplicative_inverse(e, phi) # Chave de desencriptacao (e * d ≡ 1 mod (p-1) * (q-1))

    print(f"(p-1) * (q-1) = {p-1} * {q-1} = {phi}\n{bcolors.FAIL}Chave publica: ({N}, {e}){bcolors.ENDC}\nO expoente d e tal que {bcolors.OKGREEN}{e} * d ≡ 1 mod {phi} <=> d = {d}{bcolors.ENDC}\n{bcolors.FAIL}Chave privada: ({N}, {d}){bcolors.ENDC}")

    while True:
        action = input("Encriptar ou desencriptar? [E/D] ")

        if action.upper() == 'E': # Encriptacao
            block = inputNumber("Bloco a encriptar (em numero): ")
            rsa_aux(block, e, N)
            break

        elif action.upper() == 'D': # Desencriptacao
            block = inputNumber("Bloco a desencriptar: ")
            rsa_aux(block, d, N)
            print(f"{bcolors.OKBLUE}Agora, e so pegar neste valor e traduzir com a cifra usada!{bcolors.ENDC}")
            break

        else: #Input incorreto
            print(f"{bcolors.WARNING}Input incorreto, tenta de novo!{bcolors.ENDC}")
