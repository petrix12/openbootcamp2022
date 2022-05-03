# Python
+ [Resolución de ejercios](https://github.com/Open-Bootcamp/ResolucionEjercicios/tree/main/HTML%20y%20CSS)


## Introducción a HTML, etiquetas y atributos
### Vídeo de la sesión 1
+ **Contenido**: sobre etiquetas, atributos y un poco de historia.
1. Validador html5: https://validator.w3.org
2. Editor html5: https://html5-editor.net
3. Ejemplo de un documento html5:
    ```html
    <!DOCTYPE html>
    <html lang="es">
    <head>
        <meta charset="UTF-8">
        <meta http-equiv="X-UA-Compatible" content="IE=edge">
        <meta name="viewport" content="width=device-width, initial-scale=1.0">
        <title>Lo que Google muestra como título de la búsqueda</title>
        <meta description="Lo que Google muestra como descripción de la búsqueda"></meta>
    </head>
    <body>
        <h2>Hola</h2>
        <ul>
            <li>item1</li>
            <li>item2</li>
            <li>item3</li>
        </ul>
        <!-- Comentarios -->
    </body>
    </html>
    ```

### Ejercicio sesión 1
+ Genera un documento HTML en el que haya dos niveles de encabezados.
    + Después del primer encabezado habrá un párrafo y un enlace.
    + Después del segundo encabezado habrá dos contenedores, a su vez dentro de cada contenedor deberá haber una lista ordenada y otra desordenada, el contenido de estas listas queda a vuestra elección.
+ Como parte final del ejercicio, tendréis que añadir atributos a los contenedores para que tengan un color de fondo.
+ **Resolción**:
    ```html
    <!DOCTYPE html>
    <html lang="es">
    <head>
        <meta charset="UTF-8">
        <meta http-equiv="X-UA-Compatible" content="IE=edge">
        <meta name="viewport" content="width=device-width, initial-scale=1.0">
        <title>Document</title>
    </head>
    <body>
        <h1>Nivel uno de encabezado</h1>
        <p>Párrafo....</p>
        <a href="#">Enlace</a>

        <h2>Nivel dos de encabezado</h2>
        <div style="background-color:purple">
            <ol>
                <li>Elemento 1</li>
                <li>Elemento 2</li>
                <li>Elemento 3</li>
            </ol>
        </div>
        <div style="background-color:blue">
            <ul>
                <li>Elemento A</li>
                <li>Elemento B</li>
                <li>Elemento C</li>
            </ul>
        </div>
    </body>
    </html>
    ```

### Entrega ejercicio 1
+ https://github.com/petrix12/openbootcamp2022/blob/main/proyectos/003/ejercicios1/ejercicio1.html

### Repositorio del curso
+ https://github.com/Open-Bootcamp/HTML-CSS


## Formularios y tablas
### Vídeo de la sesión 2
+ https://codepen.io/pen
+ https://stackblitz.com
1. Ejemplo de documento html5 con formulario y tabla:
    ```html
    <!DOCTYPE html>
    <html lang="es">
    <head>
        <meta charset="UTF-8">
        <meta http-equiv="X-UA-Compatible" content="IE=edge">
        <meta name="viewport" content="width=device-width, initial-scale=1.0">
        <title>Document</title>
    </head>
    <body>
        <h1>Pruebas 2</h1>

        <h2>Pruebas con formulario</h2>
        <form id="form1" action="recibeform.html" method="POST" style="border: 1px #000 solid; margin: 30px; padding: 30px; background-color: #f2f2f2">
            <fieldset>
                <legend>Aquí van tus datos de contacto:</legend>
                <div>
                    <input type="text" name="nombre" id="nombre" value="Petrix" placeholder="Nombre" required pattern="[A-Za-z0-9]+">
                    <p></p>
                    <input type="tel" name="telefono" id="telefono" placeholder="Teléfono">
                    <p></p>
                    <input type="password" name="password" id="password" placeholder="Password">
                    <p></p>
                    <input type="date" name="date" id="date" title="Fecha">
                    <input type="time" name="time" id="time" title="Hora">
                    <p></p>
                    <input type="number" name="number" id="number" placeholder="Número" value="12" min="3" max="24">
                    <p></p>
                    <input type="range" name="range" id="range" placeholder="Rango" value="12" min="3" max="24">
                    <p></p>
                    <input type="radio" name="radio1" id="radio1" value="H"> Radio 1
                    <input type="radio" name="radio2" id="radio2" value="M"> Radio 2
                    <p></p>
                    <input type="checkbox" name="checkbox1" id="checkbox1"> Checkbox 1
                    <input type="checkbox" name="checkbox2" id="checkbox2"> Checkbox 2
                    <input type="checkbox" name="checkbox3" id="checkbox3"> Checkbox 3
                    <p></p>
                    <select name="lista" id="lista" multiple>
                        <optgroup label="Lista básica">
                            <option value="1" label="Opción 1"></option>
                        </optgroup>
                        <optgroup label="Lista avanzada">
                            <option value="2" label="Opción 2"></option>
                            <option value="3" label="Opción 3"></option>
                        </optgroup>
                    </select>
                    <p></p>
                    <textarea name="textarea" id="textarea" cols="30" rows="10" spellcheck="true">Soluciones++</textarea>
                    <input type="hidden" name="hidden" id="hidden">
                </div>
                <p></p>

                <div>
                    <input type="submit" value="Enviar formulario">
                </div>
            </fieldset>
        </form>

        <h2>Pruebas con tabla</h2>
        <table class="default" border="1">
            <caption>Título de la tabla</caption>

            <thead>
                <tr>
                    <th scope="row">Fila</th>
                    <th>Hoy</th>
                    <th>Mañana</th>
                    <th>Martes</th>
                </tr>
            </thead>

            <tbody>
                <tr>
                    <th>Condición</th>
                    <td colspan="2">Soleado</td>
                    <td>Mayormente soleado</td>
                </tr>
                <tr>
                    <th>Temperatura</th>
                    <td rowspan="2">19ºC</td>
                    <td>17ºC</td>
                    <td>12ºC</td>
                </tr>
                <tr>
                    <th>Vientos</th>
                    <td>E 11 Km/h</td>
                    <td>S 16 Km/h</td>
                </tr>
            </tbody>

            <tfoot>
                <tr>
                    <td colspan="3">Pie 1</td>
                    <td>Pie 2</td>
                </tr>
            </tfoot>
        </table>
    </body>
    </html>
    ```

### Ejercicio sesión 2
+ Crea un formulario en el que haya que introducir los siguientes datos:
    + Nombre
    + Apellido
    + e-mail
    + teléfono
    + dirección.
+ Como segunda parte del ejercicio deberás crear una tabla, esta tabla tendrá 4 columnas y 4 filas, en esta tabla deberás hacer que:
    + Una de las celdas ocupe dos columnas.
    + Una de las celdas ocupe dos filas.
+ **Resolción**:
    ```html
    <!DOCTYPE html>
    <html lang="es">
    <head>
        <meta charset="UTF-8">
        <meta http-equiv="X-UA-Compatible" content="IE=edge">
        <meta name="viewport" content="width=device-width, initial-scale=1.0">
        <title>Formularios y tablas</title>
    </head>
    <body>
        <h1>Ejercicio sesion 2</h1>

        <h2>Parte I: formulario</h2>
        <form id="form1" action="recibeform.html" method="POST" style="border: 1px #000 solid; margin: 30px; padding: 30px; background-color: #f2f2f2">
            <fieldset>
                <legend>Datos de contacto:</legend>
                <div>
                    <input type="text" name="nombre" id="nombre" placeholder="Nombre">
                    <p></p>
                    <input type="text" name="apellido" id="apellido" placeholder="Apellido">
                    <p></p>
                    <input type="email" name="email" id="email" placeholder="e-mail">
                    <p></p>
                    <input type="tel" name="telefono" id="telefono" placeholder="Teléfono">
                    <p></p>
                    Dirección: <br>
                    <textarea name="dirección" id="dirección" cols="30" rows="10" spellcheck="true"></textarea>
                </div>
                <p></p>

                <div>
                    <input type="submit" value="Enviar formulario">
                </div>
            </fieldset>
        </form>

        <h2>Parte II: tabla</h2>
        <table class="default" border="1">
            <caption>Tabla de cuatro columnas y cuatro filas</caption>

            <thead>
                <tr>
                    <th>Encabezado 1</th>
                    <th>Encabezado 2</th>
                    <th>Encabezado 3</th>
                    <th>Encabezado 4</th>
                </tr>
            </thead>

            <tbody>
                <tr>
                    <td colspan="2">A y B</td>
                    <td>C</td>
                    <td>D</td>
                </tr>
                <tr>
                    <td rowspan="2">E e I</td>
                    <td>F</td>
                    <td>G</td>
                    <td>H</td>
                </tr>
                <tr>
                    <td>J</td>
                    <td>K</td>
                    <td>L</td>
                </tr>
            </tbody>
        </table>
    </body>
    </html>
    ```

### Entrega ejercicio 2
+ Repositorio GitHub del ejercicio: https://github.com/petrix12/openbootcamp2022/blob/main/proyectos/003/ejercicios2/ejercicio1.html


## Multimedia
### Vídeo de la sesión 3
+ https://fonts.google.com/icons
1. Ejemplo documento html con imagen:
    ```html
    ≡
    <body>
        <h2>Picture</h2>
        <picture>
            <img src="binary-4791836_640.jpg" alt="Es una imagen de un perrito" width="400" height="453" />
        </picture>

        <h2>Imágenes responsive</h2>
        <picture>
            <source media="(min-width: 300px) and (max-width: 600px)" srcset="dog-gc4b1be3a9_1920.webp" />
            <img src="dog-gc4b1be3a9_1920.jpg" alt="HTML5 logo" />
        </picture>
    </body>
    ≡
    ```
2. Ejemplo documento html con video:
    ```html
    ≡
    <body>
        <video autoplay muted src="elephants-dream.webm" poster="dog-gc4b1be3a9_1920.webp" controls></video>
        <video src="Matrix - 47802.mp4" autoplay muted loop controls></video>

        <video width="640" height="480">
            <source src="Matrix - 47802.mp4" type="video/mp4" />
            <source src="elephants-dream.webm" type="video/webm" />
            <source src="video.ogv" type="video/ogg" />
            <img src="imagen.png" alt="Video no soportado" />
            Su navegador no soporta contenido multimedia.
        </video>

        <iframe width="560" height="315" src="https://www.youtube.com/embed/DUjCfXPs2gw" title="YouTube video player" frameborder="0" allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture" allowfullscreen></iframe>
    </body>
    ≡
    ```
3. Ejemplo de documento html con audio:
    ```html
    ≡
    <body>
        <!-- 
            src	            Dirección URL	Audio a reproducir. Obligatoria si actua como etiqueta contenedora.
            preload	        auto | metadata | none	Indica como realizar la precarga del audio.
            mediagroup	    nombre	Establece un nombre para un grupo de contenidos multimedia.
            autoplay		Comienza a reproducir el audio automáticamente.
            loop		    Vuelve a iniciar el audio cuando finaliza su reproducción (bucle).
            muted		    Establece el audio sin sonido (silenciado).
            controls		Muestra los controles de reproducción. Por defecto no se muestran.
        -->
        <h1>Audio</h1>
        <audio src="cinematic-fairy-tale-story-main-8697.mp3" autoplay loop controls preload="none"></audio>

            <!-- 
            Formato	Codec utilizado	Características	¿Recomendado?
            MP3	MPEG Layer-3	Buena calidad.	Sí, buen soporte
            AAC	Advanced Audio Coding	Mejora el MP3. Usado como audio en MP4.	Sí, buen soporte
            OGG	Ogg Vorbis	Buena calidad. Alternativa libre a MP3.	Sí, soporte medio
            Opus	Opus	Buena calidad. Alternativa libre a MP3.	Sí, soporte medio
            FLAC	FLAC Audio Lossless	Compresión sin pérdidas. Alto tamaño.	Sí, buen soporte.
            WAV	Wave sound	Formato de Microsoft. Está soportado.	No, muy pesado
        -->

        <audio>
            <source src="audio.opus" />
            <source src="audio.ogg" />
            <source src="audio.mp3" />
        </audio>
    </body>
    ≡
    ```

### Dudas sesiones 1, 2 y 3
+ **Descripción**: Dudas planteadas por los alumnos de las sesiones 1, 2 y 3 respondidas por el profesor.

### Ejercicio sesión 3
+ Para este ejercicio deberéis introducir una imagen y darle además de un texto alternativo.
+ Aparte, añadiréis un audio y un vídeo a vuestra elección, deben tener algunos de los atributos vistos en las sesiones u otros que os parezcan interesantes.
+ **Resolción**:
    ```html
    <!DOCTYPE html>
    <html lang="es">
    <head>
        <meta charset="UTF-8">
        <meta http-equiv="X-UA-Compatible" content="IE=edge">
        <meta name="viewport" content="width=device-width, initial-scale=1.0">
        <title>Ejercico de la sesión 3</title>
    </head>
    <body>
        <h2>Imagen</h2>
        <picture>
            <img src="hamburguesa.jpg" alt="Es una imagen de una hamburguesa" width="600" height="400" />
        </picture>

        <h2>Audio</h2>
        <audio src="audio.mp3" autoplay loop controls preload="none" title="mi audio"></audio>

        <h2>Video</h2>
        <iframe width="853" height="480" src="https://www.youtube.com/embed/lWFl-rM9R9M" title="YouTube video player" frameborder="0" allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture" allowfullscreen></iframe>
    </body>
    </html>
    ```

### Entrega ejercicio 3
+ **Repositorio GiHub**: 


## Introducción al CSS
### Vídeo de la sesión 4





    ```html
    ≡
    ≡
    ```



### Ejercicios sesión 4
+ mmmm
+ **Resolción**:
    ```html
    ≡
    ≡
    ```
### Entrega ejercicio 4


## Disposición de elementos y para multimedia
### Vídeo de la sesión 5
### Ejercicio sesión 5
+ mmm
+ **Resolción**:
    ```html
    ≡
    ≡
    ```

### Entrega ejercicio 5
+ **Repositorio GiHub**: 


## Anidación de selectores
### Vídeo de la sesión 6
### Ejercicio sesión 6
+ mmm
+ **Resolción**:
    ```html
    ≡
    ≡
    ```

### Entrega ejercicio 6
+ **Repositorio GiHub**: 


## Creación de estilos para formularios
### Vídeo de la sesión 7
### Ejercicio sesión 7
+ mmm
+ **Resolción**:
    ```html
    ≡
    ≡
    ```

### Entrega ejercicio 7
+ **Repositorio GiHub**: 


## Bootstrap
### Vídeo de la sesión 8
### Ejercicio sesión 8
+ mmm
+ **Resolción**:
    ```html
    ≡
    ≡
    ```

### Entrega ejercicio 8
+ **Repositorio GiHub**: 


## Animaciones y transiciones
### Vídeo de la sesión 9
### Ejercicio sesión 9
+ mmm
+ **Resolción**:
    ```html
    ≡
    ≡
    ```
### Entrega ejercicio 9


## Introducción al diseño responsive
### Vídeo de la sesión 10
### Ejercicio sesión 10
+ mmm
+ **Resolción**:
    ```html
    ≡
    ≡
    ```

### Entrega ejercicio 10


## El sistema grid de Bootstrap
### Vídeo de la sesión 11
### Ejercicios sesión 11
+ mmm
+ **Resolción**:
    ```html
    ≡
    ≡
    ```

### Entrega ejercicio 11
+ **Repositorio GiHub**: 


## Otros aspectos de interés de Boostrap
### Vídeo de la sesión 12
### Ejercicios sesión 12
+ mmm
+ **Resolción**:
    ```html
    ≡
    ≡
    ```

### Entrega ejercicios 12
+ **Repositorio GiHub**: 


## Usando pre-procesadores CSS
### Vídeo de la sesión 13


## Presentación proyecto final
### Vídeo de la sesión 14


## Finalización proyecto final
### Vídeo de la sesión 15

