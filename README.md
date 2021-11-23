# Twinning-Compiler
Compilador para la clase Diseño de compiladores


Planeación y desarrollo del proyecto

Bitácora 1, 3 de octubre 2021
Se desarrolló un parser y lexer para el lenguaje de programación a desarrollar.
Los tokens y expresiones regulares se basaron principalmente en el lenguaje “patito” que se nos encargó de tarea.
Hay algunos detalles en la gramática que se planean solucionar en los siguientes días antes del segundo avance.

Bitácora 2, 10 de octubre 2021
Agregué las funciones del director de funciones para la tabla de funciones/scopes, la cual tiene un atributo para una lista de variables, con atributos ya definidos (así como en las presentaciones) También se desarrolló un cubo semántico que funciona en base a booleanos, o sea, 0 =/= False.

Bitácora 3, 17 de octubre 2021
Agregué una función para la creación de cubo semántico y los stacks para añadirlos en la lectura del código. Debido a entregas y exámenes, esta entrega es corta, pero espero regularme para la siguiente entrega.

Bitácora 4, 2 de noviembre 2021
Los cuádruplos funcionan, logré implementar las operaciones básicas, pero aún no logro procesar los paréntesis. Las sumas, multiplicaciones, divisiones y restas, ya están funcionando sin problema alguno.

Bitácora 5 9 de noviembre 2021
Logré integrar los cuádruplos de estatutos lógicos, así como los if y whiles, además de que ya encontré una manera de implementar los paréntesis. Hay unos pequeños detalles con los scopes y la memoria virtual, necesitaré ayuda y asesoría de Elda para poder solucionar esto.
Tuve una pequeña asesoría con la maestra Elda Guadalupe, donde ella me guió a los ejercicios y ejemplos para entender el concepto del almacenamiento de la memoria virtual.

Bitácora 6, 15 de noviembre 2021
Comencé a desarrollar la memoria virtual, tuve que rehacer lo que tenía luego de comprender la situación, creo que entendí a lo que se referían con desarrollar clases para el almacenamiento de datos y sus tipos.
Cree una clase para el almacenamiento de memoria, declaró los intervalos de almacenamiento y luego mandó la variable para su definición en memoria
La forma en la que lo estuve desarrollando no me va a funcionar, decidí rehacer el modelo de la memoria y separarlo en dos clases, donde una clase crea los objetos de la otra. Las dos clases son memoriavirtual y valoresmemoria, donde valoresmemoria guarda las variables que se le vayan asignando junto con la memoria base que cada una debería tener, recibe como parametro el número de la memoria base de cada tipo de datos, memoria virtual genera diferentes objetos de tipo valoresmemoria, cada uno se dedica a almacenar un diferente “scope” de memoria. También avancé bastante en mi máquina virtual, pero aún no está terminada.

Bitácora 7, 22 de noviembre 2021
Ya está terminado, solo faltan unas pocas cosas por pulir. En especial una falta de lógica en los goto's. Fuera de eso, las funciones especiales ya están implementadas mediante python Statistics, pienso añadir unas más aún solo quiero resolver lo crítico primero.

Registro de avances/actividad en el proyecto:
Por confusión mía y no excuso mi error, no hice mi repositorio de github sino hasta último momento, pues pensé que solo se iba a entregar eso. Aún así, me gustaría mostrar el registro de actividad de la plataforma que estuve usando para el desarrollo del proyecto.



![image](https://user-images.githubusercontent.com/26450411/142995927-bc866992-24bc-4be3-a30e-060b2b5ae026.png)
![image](https://user-images.githubusercontent.com/26450411/142995947-ce80d767-86f5-403d-91f3-b4d54d46b26b.png)
![image](https://user-images.githubusercontent.com/26450411/142995970-d960a60b-1225-499a-8c4d-d5a84e39113e.png)
![image](https://user-images.githubusercontent.com/26450411/142995997-afb18edd-7dcd-454e-9f93-abb137dd51ad.png)

Pruebas de distintas versiones:

![image](https://user-images.githubusercontent.com/26450411/142996108-563a9bb4-ecea-41d2-9c23-53996b4c2f0c.png)
![image](https://user-images.githubusercontent.com/26450411/142996158-c281490c-450c-4d07-9db9-2a440a720e4d.png)
![image](https://user-images.githubusercontent.com/26450411/142996217-1e6c8393-d5b4-4092-8fef-03852daa207d.png)




