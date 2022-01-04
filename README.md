# Epidemia-
Simulador de una epidemia utilizando Python y PovRay 

Se consideran 5 estados para cada habitante en una población de 10,000 habitantes:
  0 Sano   verde
  1 enfermo rojo
  2 recuperado  azul
  3 vacunado  (color segun vacuna)
  4 muerto  negro
  5 inmune amarillo

Al iniciar el programa se coloca una persona contagiada. Las personas se contagian de acuerdo al contacto que tengan con las personas que ya se encuentran contagiadas. 
A partir del día 40 las personas empiezan a recibir las vacunas de forma aleatoria.
Se cuentan con los siguientes tipos de vacunas:
  1 Pfizer blanco
  2 Sputnik gris
  3 Astrazeneca Rosa
  4 Moderna Azul claro

Cuando una persona sea vacunada cambiará el color de la esfera que representa a la persona, de acuerdo a la vacuna que le haya tocado, y después obtendrá inmunidad por 
cierto número de días.
 
Adicional, se agregan gráficos con el número de personas que fueron vacunadas con cada tipo, por ejemplo:

   ![image](https://user-images.githubusercontent.com/79610750/148009331-a7acc14e-a4b8-4fdd-afef-f0b03962a548.png)


Y se muestran otros dos gráficos, uno con el número de contagiaos y el número de enfermos durante toda la simulación.

![image](https://user-images.githubusercontent.com/79610750/148009384-c37ce21b-bb9e-4131-bc4c-33f4197e2275.png)      ![image](https://user-images.githubusercontent.com/79610750/148009403-ba33d458-a04b-48e3-bc05-17b671d3d329.png)




Se generan archivos de formato .pov que deben renderizarse para generar archivos .png y ver como evoluciona la pandemia.

La simulación para este programa dura 200 días

https://user-images.githubusercontent.com/79610750/148009291-28d0ff88-e9ce-43d2-bcda-3b2897610dca.mp4





