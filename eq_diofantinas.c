#include <stdio.h>

#define SIZE 20
#define FALSE 0
#define TRUE 1

int* Saunderson(int el1, int el2, int* mdc, int* Bx, int* By) {

    int a[SIZE];
    int x[SIZE], y[SIZE], q[SIZE]; 

    x[0] = 1; x[1] = 0;
    y[0] = 0; y[1] = 1;

    a[0] = el1; a[1] = el2; 

    int i = 1; 

    while((a[i - 1] % a[i]) != 0) {
        q[i] = a[i - 1] / a[i];
        a[i + 1] = a[i - 1] - (q[i] * a[i]);
        x[i + 1] = x[i - 1] - (q[i] * x[i]);
        y[i + 1] = y[i - 1] - (q[i] * y[i]);
        i++;
    }
    *mdc = a[i];
    *Bx = x[i];
    *By = y[i]; 
    return 0;
}

int main() 
{
    int a, b, c;
    int d, bx, by; /* mdc; coeficiente bezout para x; coeficiente bezout para y */

    printf("=================/ INÍCIO /=================\n\n");
    printf("\nax + by = c\n");
    printf("\nInsira o coeficiente de x: \n");
    scanf("%d", &a);
    printf("Insira o coeficiente de y: \n");
    scanf("%d", &b);
    printf("Insira o termo independente: \n");
    scanf("%d", &c);
    printf("\n%dX + %dY = %d\n", a, b, c);

    printf("\n===============/ SAUNDERSON /===============\n\n");
    Saunderson(a, b, &d, &bx, &by);
    printf("\nO máximo divisor comum de %d e %d é %d. Obtém-se assim: \n", a, b, d);
    printf("%d = %d * (%d) + %d * (%d)\n", d, bx, a, by, b);
    printf("\nO que nos dá coeficientes de Bézout %d e %d relativamente a %d e %d, donde:\n", bx, by, a, b);
    printf("x = %d * %d/%d = %d, t € Z    ||    y = %d * %d/%d = %d, t € Z\nDe referir que a expressão acima é uma solução particular.\n", bx, c, d, (bx * (c/d)), by, c, d, (by * (c/d)));
    printf("\nA solução geral, de acordo com o Teorema 43, pág 58, é:\n");
    printf("x = %d + %d/%dt    e    y = %d - %d/%dt, t€Z\n", (bx * (c/d)), b, d, (by * (c/d)), a, d);
    printf("\nOu seja, \nx = %d + (%d)t, t € Z    ||    y = %d + (%d)t, t € Z\n", (bx * (c/d)), b/d, (by * (c/d)), -a/d);

    printf("\n==========/ TRANSLAÇÕES POSSIVEIS /==========\n\n");
    printf("Este passo remete mais aos problemas da vida real, onde os valores a procurar tendem a ser positivos.\n");
    printf("Assim, descobriremos um t € z que nos aproxime ao máximo dos coeficientes positivos\n");

    int x0 = bx * (c/d);
    int y0 = by * (c/d);
    int t, one_neg;

    if (x0 < 0 && (b/d) <0) 
    {
        one_neg = TRUE;
        t = -((x0 / (b/d)) + 1);
        printf("\nDescobrindo o t mais conveniente: %d\n",t);
        printf("Substituindo %d por t na solução geral, temos para x e y:\n\nx = %d + (%d * %d) (C.Aux -> %d * %d = %d) = %d\ny = %d + (%d * %d) (C.Aux -> %d * %d = %d) = %d\n", t, x0, b/d, t, b/d, t, (b/d)*t, x0 + (b/d)*t, y0, -a/d, t, -a/d, t, ((-a/d)*t), y0 + (-a/d)*t);
    } else if (y0 < 0 && (-a/d) < 0)
    {
        one_neg = TRUE;
        t = -((y0 / (-a/d)) + 1);
        printf("\nDescobrindo o t mais conveniente: %d\n", t);
        printf("Substituindo %d por t na solução geral, temos para x e y:\n\nx = %d + (%d * %d) (C.Aux -> %d * %d = %d) = %d\ny = %d + (%d * %d) (C.Aux -> %d * %d = %d) = %d\n", t, x0, b/d, t, b/d, t, (b/d)*t, x0 + (b/d)*t, y0, -a/d, t, -a/d, t, ((-a/d)*t), y0 + (-a/d)*t);
    } else if ((x0 > 0 && (b/d) < 0) || (x0 < 0 && (b/d) > 0))
    {
        one_neg = TRUE;
        t = ((-x0 / (b/d)) + 1);
        printf("\nDescobrindo um t conveniente: %d\n", t);
        printf("Substituindo %d por t na solução geral, temos para x e y:\n\nx = %d + (%d * %d) (C.Aux -> %d * %d = %d) = %d\ny = %d + (%d * %d) (C.Aux -> %d * %d = %d) = %d\n", t, x0, b/d, t, b/d, t, (b/d)*t, x0 + (b/d)*t, y0, -a/d, t, -a/d, t, ((-a/d)*t), y0 + (-a/d)*t);
    } else if ((y0 > 0 && (-a/d) < 0) || (y0 < 0 && (-a/d) > 0))
    {
        one_neg = TRUE;
        t = ((-y0 / (-a/d)) + 1);
        printf("\nDescobrindo o t mais conveniente: %d\n", t);
        printf("Substituindo %d por t na solução geral, temos para x e y:\n\nx = %d + (%d * %d) (C.Aux -> %d * %d = %d) = %d\ny = %d + (%d * %d) (C.Aux -> %d * %d = %d) = %d\n", t,x0, b/d, t, b/d, t, (b/d)*t, x0 + (b/d)*t, y0, -a/d, t, -a/d, t, ((-a/d)*t), y0 + (-a/d)*t);
    }
    printf("\nA partir daqui é necessário verificar o enunciado e o que nos pedem!\n");
    printf("Aplicando uma tranlação t <- t + (%d):\n\n", t);

    if (one_neg == TRUE) {
        printf("x = %d + (%d)t, t € Z    ||    y = %d + (%d)t, t € Z\n", x0 + (b/d)*t, b/d, y0 + (-a/d)*t, -a/d);
    } else {
        printf("x = %d + (%d)t, t € Z    ||    y = %d + (%d)t, t € Z\n", x0, b/d, y0, -a/d);
    }

    printf("\nAgora o resto é interpretação! Boa sorte!\n");
    return 0;
}