
#include <stdio.h>
#include <stdlib.h>
#include <string.h>
struct Empleado
{  char nombre[20];
  int edad;
 float sueldo;
};

int escribir ()
{
    int num_emp=0;
    int i=0;
    int j=0;
    FILE *archivo2;
    printf("Ingrese el numero de empleados a capturar\n");
    scanf("%d",&num_emp);
    fflush(stdin);
    struct Empleado **empleados = (struct Empleado **)calloc(num_emp,sizeof(struct Empleado*));

    for(i=0;i<num_emp;i++)
    {
        struct Empleado *emp = (struct Empleado *)malloc(sizeof(struct Empleado));
        printf("Nombre del empleado: ");
        scanf("%s",(emp->nombre));
        fflush(stdin);
        printf("Edad: ");
        scanf("%i",&(emp->edad));
        fflush(stdin);
        printf("Sueldo: ");
        scanf("%f",&(emp->sueldo));
        fflush(stdin);
        empleados[i] = emp;
        printf("\n");
    }
    archivo2=fopen("empleados2.bin","wb");

    if(archivo2 == NULL)
    {
        printf("Error al abrir el archivo");
        return 1;
    }
    else
    {
        for(int i = 0; i < num_emp; i++)
            fwrite(empleados[i], sizeof(struct Empleado), 1, archivo2);

        fclose(archivo2);
    }

    printf("Se ha generado el archivo Binario \n");

    return 0;
}

int leer()
{
    int num_emp = 2;
    FILE *archivo_lectura;
    struct Empleado *emp;
    struct Empleado **empleados = (struct Empleado **)calloc(num_emp,sizeof(struct Empleado*));
    archivo_lectura = fopen("empleados2.bin","rb+");
    if(archivo_lectura == NULL)
    {
        printf("Error al abrir el archivo");
        return 1;
    }
    else
    {
        for(int i = 0; i < num_emp; i++)
        {
            emp = (struct Empleado *) malloc (sizeof(struct Empleado));
            fread(emp, sizeof(struct Empleado), 1, archivo_lectura);
            printf("Nombre: %s\t Edad: %d \t Salario: %f",emp->nombre,emp->edad,emp->sueldo);
            empleados[i] = emp;
        }
        fclose(archivo_lectura);
    }
    for(int i = 0; i != num_emp; ++i)
    {
        emp = empleados[i];
        printf("Nombre: %s\t Edad: %d \t Salario: %f\n", emp->nombre, emp->edad, emp->sueldo);
    }
    for(int i = 0; i != num_emp; ++i)
        free(empleados[i]);
    free(empleados);
}

int main(void)
{
    escribir();
    leer();
    return 0;
}
