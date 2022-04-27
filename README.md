# Paralelismo proyecto

- Jean Pierre Mejicanos
- Adriana Mundo
- Pablo Velasquez

## Procesamiento Paralelo Sistemas Operativos


**Descripción:** 
Crear un programa que permita calcular en concurrencia la media, la deviación estándar, el conteo, el valor mínimo y máximo de datos de 1,000 archivos con datadiferente data.




### Tecnologías utilizadas:
- Python
    - Pandas, numpy
- Concurrent.futures
    - ThreadPoolExcecuter
- Docker

## Ejecución del proyecto
#### Docker
```
docker build -t paralelizacion .
docker run --cpus="4" --memory="1g" -it paralelizacion
``` 
El argumento de CPUs es utilizado para indicar la cantidad de CPUs a utilizar. Esto depende de la cantidad de cores que se desee utilizar. 

#### Python
En el código se debe cambiar: *n_hilos_ls = [1,2,4,8]* para poder indicar la cantidad de hilos a usar. Así pues, el código correra los modelos con cada uno de los elementos en la lista.

### Ejecución en terminal
#### 1 core
![image](https://user-images.githubusercontent.com/48104764/165573648-7824ffbf-c8c0-461b-87a7-c2e9cc936de0.png)

#### 2 core
![image](https://user-images.githubusercontent.com/48104764/165573718-983677cd-48d6-47f3-af61-279811334217.png)

#### 4 core
![image](https://user-images.githubusercontent.com/48104764/165573804-8e049eb0-7ef3-467b-8d2b-7c1f196d1d1f.png)

## Gráficas por modelo en cada escenario
#### Por archivos
![image](https://user-images.githubusercontent.com/48104764/165568449-59d647ce-4650-43ee-9509-460257f25b5b.png)

#### Por funciones
![image](https://user-images.githubusercontent.com/48104764/165568934-632915ec-be08-4104-8f0c-b9117cdb19b4.png)

#### Por archivo y funciones
![image](https://user-images.githubusercontent.com/48104764/165569728-e30c3781-f4ee-4f2e-9ed6-a9ce94945235.png)

#### Secuencial
![image](https://user-images.githubusercontent.com/48104764/165569951-897f129e-8ae2-449c-a811-a3f9c49ccad3.png)

#### Comparación de todos los modelos
![image](https://user-images.githubusercontent.com/48104764/165572540-4d9e95da-c5c4-496c-99aa-ef60cfe4cf5f.png)



## Preguntas
1. ¿Cuál es el modelo de paralelismo más rápido en los 6 escenarios?

![image](https://user-images.githubusercontent.com/48104764/165198749-78eccdfd-48b4-4756-b135-496a371b7b56.png)	


2. ¿Cuál opción modelo de paralelismo tomaría y por qué?
![image](https://user-images.githubusercontent.com/48104764/165202161-235f8533-0873-4b18-8e2c-0b86dbf830d0.png)	


3. ¿Recomendaría paralelizar tanto archivos y funciones al mismo tiempo?
![image](https://user-images.githubusercontent.com/48104764/165202101-2f3482e9-49dd-4eec-921f-0b5eb351fa11.png)
							

4. ¿Cuál es el factor de mejora de pasar de 1 Core a 2 Core para el proceso que paraleliza los archivos?
![image](https://user-images.githubusercontent.com/48104764/165202220-ce41a75e-28e9-4a87-badd-0230ac79bd0b.png)
							

5. Determine el factor teórico de mejora para el escenario de 2 Core (amdahl's law) al paralelizar por archivo		
![image](https://user-images.githubusercontent.com/48104764/165202354-90ca60c4-7983-42ee-8180-d05c38650a68.png)
					

6. Determine el factor teórico de mejora para el escenario de 2 Core (amdahl's law) al paralelizar por función estadística	
![image](https://user-images.githubusercontent.com/48104764/165202412-c3f2165b-fa8d-4f6d-8197-970a81661935.png)
				

7. Determine el factor teórico de mejora para el escenario de 2 Core (amdahl's law) al paralelizar por función estadística y archivos		
![image](https://user-images.githubusercontent.com/48104764/165202448-106c4280-9f76-460d-92c7-f08b174afa38.png)
						











