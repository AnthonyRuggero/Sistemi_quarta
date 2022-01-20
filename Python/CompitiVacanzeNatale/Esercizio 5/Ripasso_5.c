#include <stdlib.h>
#include <stdio.h>
#include <stdbool.h>

bool isTriangolo(float l1, float l2, float l3){
    return(l1 + l2 > l3 && l1 + l3 > l2 && l2 + l3 > l1);
}

float chiediLato(char frase[]){
    float l;
    do{
        printf("%s", frase);
        scanf("%f", &l);
    }while(l < 0);
    return l;
}

int main(){
    float l1, l2, l3;

    l1 = chiediLato("Inserisci il primo lato: ");
    l2 = chiediLato("Inserisci il secondo lato: ");
    l3 = chiediLato("Inserisci il terzo lato: ");
    if(isTriangolo (l1, l2, l3) == true){
       printf("Puo' essere un triangolo");
    }else{
        printf("Non è un triangolo");
    }
}
