# Instructions  

## Instrucciones para un ejercicio de desarrollo web utilizando el hook useEffect y consumiendo la API "https://jsonplaceholder.typicode.com/todos":

```
Objetivo: El objetivo de este ejercicio es que los estudiantes adquieran experiencia práctica en el uso del hook useEffect para realizar peticiones reales a una API externa y mostrar los datos obtenidos en una aplicación web desarrollada con React.
```

## Instrucciones:

Pasos:

Configuración del Entorno:

Asegúrate de tener Node.js y npm instalados en tu sistema.
Crea una nueva aplicación de React utilizando Create React App o tu método preferido.

Crear un Componente Funcional:

Crea un nuevo componente funcional llamado TodoList.
Uso de useEffect:

Importa el hook useEffect en tu componente.
Utiliza useEffect para realizar una petición GET a la API "https://jsonplaceholder.typicode.com/todos" cuando el componente se monta.
Almacenar Datos:

Al recibir la respuesta de la API, almacena los datos en el estado del componente utilizando el hook useState.
Mostrar Datos en el Componente:

Renderiza la lista de tareas (todos) en el componente. Cada elemento de la lista debe mostrar el título de la tarea.
Estilización Opcional:

Aplica estilos CSS al componente TodoList para hacerlo más atractivo visualmente.

Gestión de Errores:

Implementa manejo de errores para tratar posibles fallos en la petición a la API.

Pruebas:

Verifica que los datos de la API se muestren correctamente en el componente TodoList.

Desafíos Adicionales (Opcional):

Filtra y muestra solo las tareas completadas o pendientes.

Notas Adicionales:

Asegúrate de utilizar la función fetch o alguna biblioteca como Axios para realizar la solicitud a la API de manera asíncrona.

```
Puedes explorar otras rutas de la API "https://jsonplaceholder.typicode.com" para obtener diferentes tipos de datos.
```

Este ejercicio proporcionará a los estudiantes experiencia práctica en la gestión de peticiones HTTP a APIs reales y en la presentación de datos en sus aplicaciones de React. También les permitirá comprender cómo useEffect se utiliza para manejar efectos secundarios en componentes React.

  