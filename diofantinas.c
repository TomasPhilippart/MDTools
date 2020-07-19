#include <stdio.h>

#define SIZE 20
#define FALSE 0
#define TRUE 1

int* Saunderson(int el1, int el2, int* mdc, int* Bx, int* By) {

    int a[SIZE];
    int x[SIZE], y[SIZE], q[SIZE]; 

    if (el1 < 0) {
        el1 = -el1;
    }
    else if (el2 < 0) {
        el2 = -el2;
    }

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
    if (a < 0) {
        bx = -bx;
    } else if (b < 0) {
        by = -by;
    }
    if (c % d != 0) {
        printf("É condição necessária %d ⌢ %d dividir %d, mas %d não divide %d, logo esta equação diofantina não tem solução.", a, b, c, d, c);
        return 0;
    }
    printf("\nDado que %d ⌢ %d = %d, e %d|%d, a equação diofantina tem solução!\n", a, b, d, d, c);
    printf("O máximo divisor comum de %d e %d é %d. Obtém-se assim: \n", a, b, d);
    printf("%d = %d * (%d) + %d * (%d)\n", d, bx, a, by, b);
    printf("\nO que nos dá coeficientes de Bézout %d e %d relativamente a %d e %d, donde:\n", bx, by, a, b);
    printf("x0 = %d * %d/%d = %d    ||    y0 = %d * %d/%d = %d\nDe referir que a expressão acima é uma solução particular.\n", bx, c, d, (bx * (c/d)), by, c, d, (by * (c/d)));
    printf("\nA solução geral, de acordo com o Teorema 43, pág 58, é:\n");
    printf("x = %d + %d/%dt    e    y = %d - %d/%dt, t€Z\n", (bx * (c/d)), b, d, (by * (c/d)), a, d);
    printf("\nOu seja, \nx = %d + (%d)t, t € Z    ||    y = %d + (%d)t, t € Z\n", (bx * (c/d)), b/d, (by * (c/d)), -a/d);

    printf("\n==========/ TRANSLAÇÕES POSSIVEIS /==========\n\n");
    printf("Este passo remete mais aos problemas da vida real, onde os valores a procurar tendem a ser positivos.\n");
    printf("Assim, descobriremos um t € Z que nos aproxime ao máximo de uma solução particular apropriada ao problema.\n");

    int x0 = bx * (c/d);
    int y0 = by * (c/d);
    int x1 = b/d;
    int y1 = -a/d;
    int t = 1;

    /* Solução particular ambos positivos */
    /* Assume-se que os x1 e y1 são negativos */
    if (x0 > 0 && y0 > 0) {
        int t1 = (x0 / (-x1));
        int t2 = (y0 / (-y1));
        if (t1 < t2) {
            t = t1;
        } else { 
            t = t2;
        }
    }

    /* Solução particular ambas negativas */
    /* Assume-se que os x1 e y1 são positivos */
    if (x0 < 0 && y0 < 0) {
        if (x1 < 0 && y1 < 0) {
            int t1 = (x0/(-x1));
            int t2 = (y0/(-y1));
            if (t1 == t2) {
                t = t1 - 1;
            }
            else if (t1 < t2) {
                t = t1;
            } else {
                t = t2;
            }
        }
    }

    /* x0 positivo e y0 negativo */
    if (x0 > 0 && y0 < 0) {
        t = -(x0/x1);
    }

    /* x0 negativo e y0 positivo */
    if (x0 < 0 && y0 > 0) {
        t = -(y0/y1);
    }

    printf("\nDescobrindo o t mais conveniente: %d\n", t);
    printf("Substituindo %d por t na solução geral, temos para x e y:\n\nx = %d + (%d * %d) (C.Aux -> %d * %d = %d) = %d\ny = %d + (%d * %d) (C.Aux -> %d * %d = %d) = %d\n", t,x0, x1, t, x1, t, x1*t, x0 + x1*t, y0, y1, t, y1, t, (y1*t), y0 + (y1*t));
    printf("\nA partir daqui é necessário verificar o enunciado e o que nos pedem!\n");
    printf("Aplicando uma tranlação t <- t + (%d):\n\n", t);
    printf("x = %d + (%d)t, t € Z    ||    y = %d + (%d)t, t € Z\n", x0 + x1*t, x1, y0 + y1*t, y1);

    printf("\nAgora o resto é interpretação! Boa sorte!\n");
    return 0;
}