from func_aux import soma_pot_2_aux, multiplicative_inverse, bcolors, inputNumber

def rsa_aux(block, x, N):
    powers = soma_pot_2_aux(x)
    nums_cong = []
    total = 1
    for i in powers:
        num = block ** (2 ** i)
        num_cong = num % N
        nums_cong += [num_cong]
        total *= num_cong
        print(f"{block}^{2 ** i} ≡ {bcolors.OKGREEN}{num_cong}{bcolors.ENDC} (mod {N})")
    display = f"{block}^{x} = "
    for i in powers:
        display += f"{block}^{2**i} * "
    display = display[:-2] + "≡ "
    for i in nums_cong:
        display += f"{i} * "
    display = display[:-2] + f"= {total} ≡ {total % N} (mod {N})"
    print(display)

def rsa():
    p = inputNumber("p = ")
    q = inputNumber("q = ")
    N = p * q
    e = inputNumber("e = ")
    phi = (p-1)*(q-1)
    d = multiplicative_inverse(e, phi)
    print(f"Chave publica: ({N}, {e})\nChave privada: ({N}, {d})")
    action = input("Encriptar ou desencriptar? [E/D] ")
    if action.upper() == 'E':
        block = inputNumber("Bloco a encriptar (em numero): ")
        rsa_aux(block, e, N)
    elif action.upper() == 'D':
        block = inputNumber("Bloco a desencriptar (em numero): ")
        rsa_aux(block, d, N)
        print("Agora, e so pegar neste valor e traduzir com a cifra usada!")
    else:
        print(f"{bcolors.WARNING}Input incorreto, tenta de novo!{bcolors.ENDC}")