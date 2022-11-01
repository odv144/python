#include<stdio.h>
#include<conio.h>
#include<stdlib.h>
#include<string.h>
struct Persona {
 char nombre[50];
 int edad;
 char telefono[15];
}empleado;

typedef struct{
    char nombre[50];
    int edad;
    char telefono[15];
    float sueldo;
}jefe;

int main()
{
    empleado.edad=25;
    strcpy(empleado.nombre,"Omar Dario Virili");
    strcpy(empleado.telefono,"3482558453");
    jefe jefe1;
    jefe1.edad=25;
    jefe1.sueldo=350.53;
    strcpy(jefe1.nombre,"Omar Dario Virili");
    strcpy(jefe1.telefono,"3482558453");

    FILE *arch;
    arch = fopen("archivo1.bin","wb");
    if(arch==NULL)
        exit(1);
    fwrite(&jefe1, sizeof(jefe),1,arch);
    printf("Se creo el archvio");
    fclose(arch);

    FILE *nuevo;
    nuevo = fopen("archivo1.bin","rb");
    if(arch==NULL)
        exit(1);
    jefe jefe2;
    fread(&jefe2,sizeof(jefe),1,nuevo);
    printf("%s %i %s %0.2f",jefe2.nombre, jefe2.edad, jefe2.telefono, jefe2.sueldo);
    fclose(nuevo);
    getch();
    return 0;

}
