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
### Docker
'''
docker build -t paralelizacion .
docker run --cpus="4" --memory="1g" -it paralelizacion
'''

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
						











