# MDTools :unlock:

Pequeno programa em Python para facilitar os cálculos da disciplina de Matemática Discreta.

## Criado por:

#### David Belchior
#### Gustavo Aguiar
#### Tomás Philippart
#### Tomás Tavares

### Instituto Superior Técnico - LEIC-A - 1º Ano

## Lançamento original - 07/07/2020
## Versão Atual: 1.3 - Lançada a 01/08/2020

**Ao terminar o uso de uma ferramenta, o programa perguntará se o utilizador pretende voltar a usá-la: nesse caso, repetirá a execução da ferramenta; caso contrário, perguntará se pretende que o programa seja encerrado, e em caso negativo, retornará ao menu principal.**

Esta alteração permite agilizar o uso repetido da mesma ferramenta, sem que seja necessário retornar sempre ao menu principal. Além disso, permite também encerrar o programa de forma mais rápida.

**Correção de um bug no comando C que não permitia fazer qualquer congruência.**

**Alterações menores no funcionamento e na apresentação global do programa.**

Para mais informações relativamente a versões anteriores do programa, consulta o ficheiro `UPDATE-LOG.md`.

## Utilização

Para correr o programa, escreve `python3 MDTools.py` na linha de comandos do Ubuntu na pasta MDTools, ou abre diretamente, com o Python, o mesmo ficheiro.

## Funcionalidades

#### Algoritmo FFT ####

        A) Ver algortimo FFT

#### Algoritmo RSA ####

        B) Descobrir inverso de e mod (p-1) * (q-1)
        C) Fazer congruências rapidamente
        D) Obter soma em base 2 de número
        E) Ver algoritmo RSA

#### Congruências ####

        F) Simplificar congruências
        G) Algoritmo de Saunderson e Coeficientes de Bézout
        H) Equações Diofantinas

#### Calendários ####

        I) Juliano
        J) Gregoriano
        K) Páscoa Juliana
        L) Páscoa Gregoriana (passo a passo)

#### Grafos ####

        M) Noções Básicas
        N) Teoremas
        O) Algoritmo de Fleury

## RSA (Teoria)

RSA é um algoritmo de criptografia de dados, que deve o seu nome a três professores do Instituto de Tecnologia de Massachusetts (MIT), Ronald Rivest, Adi Shamir e Leonard Adleman, fundadores da actual empresa RSA Data Security, Inc., que inventaram este algoritmo — até a data (2008) a mais bem sucedida implementação de sistemas de chaves assimétricas, e fundamenta-se em teorias clássicas dos números. É considerado dos mais seguros, já que mandou por terra todas as tentativas de quebrá-lo. Foi também o primeiro algoritmo a possibilitar criptografia e assinatura digital, e uma das grandes inovações em criptografia de chave pública.

> _O servidor e o cliente geram as suas chaves públicas e privadas. O servidor envia para o cliente sua_ **_chave pública_**_, e o cliente
> envia para o servidor sua_ **_chave pública_**_._
> 
> _O cliente criptografa seus dados com a_ **_chave pública_** _(do servidor),_  _e envia para o servidor._
> 
> _O servidor descriptografa os dados com a sua_ **_chave privada_**_._
> 
> _O servidor criptografa o que será enviado para o cliente com a_ **_chave pública_** _do cliente, e envia para o cliente._
>
>_O cliente consegue, por fim, descriptografar o retorno do servidor, com sua_ **_chave privada_**_._
