# HTML y CSS
+ **Instructor**: Gorka Villar
+ [Resolución de ejercios](https://github.com/Open-Bootcamp/ResolucionEjercicios/tree/main/HTMLyCSS)
+ [Repositorio del curso](https://github.com/Open-Bootcamp/HTML-CSS)


## Introducción a HTML, etiquetas y atributos
### Vídeo de la sesión 1 (Introducción a HTML)
+ **Test HTML5 para el navegador**: https://html5test.com
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

### IDE y extensiones
1. Extensiones VSC recomendadas:
    + open in browser
        + TechER
    + HTML End Tag Labels
        + Ante Primorac
    + Auto Rename Tag
        + Jun Han
    + indent-rainbow
        + oderwat
    + Live Server
        + Ritwick Dey
    + Prettier - Code formatter
        + Prettier

### Mi primera páginga web
+ **Contenido**: codificación de una página web simple.

### Etiquetas más utilizadas
+ **Contenido**: sobre las etiquetas más utilizadas:
    + div
    + h1, h2, h3
    + p
    + span
    + a (href)
    + ol, li
    + ul, li
    + img (src, alt)

### Repositorio del curso
+ https://github.com/Open-Bootcamp/HTML-CSS

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

### Ejercicio 
+ Crea un nuevo documento HTML e implementa lo siguiente:
    + Utiliza la etiqueta de título para poner en el título "Ejercicio de Introducción a HTML en OpenBootcamp"
    + Dentro de la etiqueta body pon un comentario de dos líneas
        + Este es mi primer comentario de dos líneas
        + Aprendiendo a documentar mi código con OpenBootcamp
    + Crea una lista desordenada de tus tres vídeos de Youtube favoritos, siguiendo las siguientes pautas:
        + Cada elemento de la lista tiene que ser un enlace
        + El texto del enlace debe ser el título del vídeo
+ **Resolción**:
    ```html
    <!DOCTYPE html>
    <head>
        <title>Ejercicio HTML</title>
    </head>
    <body>
        <h1>Ejercicio de Introducción a HTML en OpenBootcamp</h1>

        <!-- 
            + Este es mi primer comentario de dos líneas
            + Aprendiendo a documentar mi código con OpenBootcamp 
        -->

        <ul>
            <li><a href="https://www.youtube.com/watch?v=ggeQyeyy1Ec">Papillón 3</a></li>
            <li><a href="https://www.youtube.com/watch?v=fetKK8Lr1Pc">Módulo FID en FileMaker</a></li>
            <li><a href="https://www.youtube.com/watch?v=lWFl-rM9R9M">Uso de la App Árbol Genealógico</a></li>
        </ul>
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

### Etiquetas para formularios
1. Código de ejemplos: proyectos\003\formularios

### Botones
1. Código de ejemplos: proyectos\003\botones

### Tablas en HTML
1. Código de ejemplos: proyectos\003\tablas

### Ejercicio 1
+ Crea un nuevo documento HTML que cumpla los siguientes parámetros:
    + El título debe ser "Ejercicio 02 - Formularios en HTML"
    + El body debe contener un formulario que cumpla las siguientes características:
        + El atributo action será "/"
        + Debe contener los siguientes campos:
            + Un campo de texto llamado "nombre"
            + Un campo numérico llamado "edad"
            + Un campo de área de texto llamado "frase-favorita"
            + Un botón de envío
            + Un botón de reset
+ **Resolción**:
    ```html
    <!DOCTYPE html>
    <head>
        <title>Ejercicio 02 - Formularios en HTML</title>
    </head>
    <body>
        <h1>Ejercicio 02 - Formularios en HTML</h1>
        <form action="/">
            <div>
                <label for="nombre">Nombre</label>
                <input type="text" id="nombre" name="nombre">
            </div>
            <br>

            <div>
                <label for="edad">Edad</label>
                <input type="number" id="edad" name="edad" min="0" max="150">
            </div>
            <br>

            <div>
                <label for="frase-favorita">Frase favorita</label>
                <textarea name="frase-favorita" id="frase-favorita"></textarea>
            </div>
            <br>
            
            <button type="submit">Enviar</button>
            <button type="reset">Reset</button>
        </form>
    </body>
    </html>
    ```

## Ejercicio 2
+ Crea un nuevo documento HTML que cumpla los siguientes parámetros:
    + El título debe ser "Ejercicio 02/2 - Tablas en HTML"
    + El body debe contener una tabla que cumpla las siguientes características
        + Las columnas serán las siguientes: "Título", "Autor", "Año de publicación", "Enlace a Amazon"
        + Debe tener tres entradas, que corresponderán a tus tres libros favoritos
+ **Resolción**:
    ```html
    <!DOCTYPE html>
    <head>
        <title>Ejercicio 02/2 - Tablas en HTML</title>
    </head>
    <body>
        <h1>Ejercicio 02/2 - Tablas en HTML</h1>
        <table>
            <tr>
                <th>Título</th>
                <th>Autor</th>
                <th>Año de publicación</th>
                <th>Enlace a Amazon</th>
            </tr>
            <tr>
                <td>Los 7 hábitos de la gente altamente efectiva</td>
                <td>Stephen Covey</td>
                <td>1989</td>
                <td><a href="https://www.amazon.com/-/es/Stephen-R-Covey-ebook/dp/B00T9HU5KK/ref=sr_1_2?crid=12XSS6QZHJ9CU&keywords=los+7+habitos+de+la+gente+altamente+efectiva&qid=1653357491&sprefix=los+7+%2Caps%2C1552&sr=8-2">Ir al libro</a></td>
            </tr>
            <tr>
                <td>Para Salvarte</td>
                <td>Jorge Loring</td>
                <td>1977</td>
                <td><a href="https://www.amazon.com/-/es/Jorge-Loring-Miro/dp/8485662962/ref=sr_1_1?crid=162EWIHGJORWE&keywords=jorge+loring+para+salvarte&qid=1653357690&sprefix=para+salvarte%2Caps%2C186&sr=8-1">Ir al libro</a></td>
            </tr>
            <tr>
                <td>Cómo ganar amigos e influir sobre las personas</td>
                <td>Dale Carnegie</td>
                <td>1936</td>
                <td><a href="https://www.amazon.com/-/es/Dale-Carnegie/dp/164473009X/ref=sr_1_1?crid=3BTEVAZ6NDJVW&keywords=como+ganar+amigos+e+influir+sobre+las+personas&qid=1653357786&sprefix=como+g%2Caps%2C245&sr=8-1">Ir al libro</a></td>
            </tr>
        </table>
    </body>
    </html>
    ```


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

### Imágenes
1. Código de ejemplos: proyectos\003\03multimedia

### Videos y audio
1. Código de ejemplos: proyectos\003\03multimedia

### Ejercicio 1
+ Crea un nuevo documento HTML que cumpla los siguientes parámetros:
    + Debe estar dividido en tres secciones (etiqueta).
    + Condiciones para la primera sección:
        + Debe tener un título (h1) indicando "Aprendiendo a utilizar imágenes".
        + Debes incluir una imagen de tu videojuego favorito.
    + Condiciones para la segunda sección:
        + Debe tener un título (h1) indicando "Aprendiendo a utilizar los vídeos".
        + Descárgate cualquier vídeo de youtube.
        + Debes incluir una etiqueta de vídeo que reproduzca el vídeo que acabas de descargar.
        + El vídeo debe mostrar los controles, reproducirse automáticamente y en bucle, PERO inicialmente debe estar sin sonido.
    + Condiciones para la tercera sección:
        + Debe tener un título (h1) indicando "Aprendiendo a utilizar los audios".
        + Descárgate cualquier audio de una canción de youtube.
        + Debes incluir una etiqueta de audio que reproduzca el audio que acabas de descargar.
        + El audio debe mostrar los controles, reproducirse automáticamente y en bucle.
+ **Resolción**:
    ```html
    <!DOCTYPE html>
    <head>
        <title>Multimedia</title>
    </head>
    <body>
        <!-- sección I -->
        <div>
            <h1>Aprendiendo a utilizar imágenes</h1>
            <img src="videojuego.webp" alt="Imagen de mi video juego favorito" width="300" height="200">
        </div>

        <!-- sección II -->
        <div>
            <h1>Aprendiendo a utilizar los vídeos</h1>
            <video width="300" height="300" controls autoplay muted loop>
                <source src="video.mp4" type="video/mp4">
            </video>
        </div>

        <!-- sección III -->
        <div>
            <h1>Aprendiendo a utilizar los audios</h1>
            <audio controls autoplay muted loop>
                <source src="audio.mp3" type="audio/mp3">
            </audio>
        </div>
    </body>
    </html>
    ```


## Introducción al CSS
### Vídeo de la sesión 4
1. Ejemplo de documento html enlazado con una hoja de estilo:
    + Documento html5:
    ```html
    <!DOCTYPE html>
    <html lang="en">
    <head>
        <meta charset="UTF-8">
        <meta name="viewport" content="width=device-width, initial-scale=1.0">
        <title>Document</title>
        <link href="css/estilos.css" type="text/css" rel="stylesheet" >
        <link rel="preconnect" href="https://fonts.googleapis.com">
        <link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
        <link href="https://fonts.googleapis.com/css2?family=Oswald:wght@300;500;700&display=swap" rel="stylesheet">
        <style>
            h1 {
                color: greenyellow;
            }
        </style>
    </head>
    <body>
        <h1>Encabezado</h1>
        <h2 atributo="hola">Segundo Encabezado</h2>

        <div class="div1"><p>Lorem, ipsum dolor sit amet consectetur adipisicing elit. Rem, suscipit provident maiores id dolor ut exercitationem quaerat molestiae soluta, nam placeat commodi accusantium inventore amet architecto earum sunt vero eius!</p>
            <p>Lorem, ipsum dolor sit amet consectetur adipisicing elit. Rem, suscipit provident maiores id dolor ut exercitationem quaerat molestiae soluta, nam placeat commodi accusantium inventore amet architecto earum sunt vero eius!</p>
        </div>

        <div class="div2">
            <p>Lorem, ipsum dolor sit amet consectetur adipisicing elit. Rem, suscipit provident maiores id dolor ut exercitationem quaerat molestiae soluta, nam placeat commodi accusantium inventore amet architecto earum sunt vero eius!</p>
        </div>

        <input type="text">

        <div class="rosa">
            <p>Hola!</p>
        </div>
        
        <div id="midiv" class="verde">
            <p>Lorem ipsum dolor sit amet, consectetur adipisicing elit. Asperiores voluptate nemo necessitatibus voluptatem expedita et reiciendis dolor quos hic, ullam tenetur provident, corrupti exercitationem eius iusto? Dolore error dolorum iure!</p>
        </div>

        <div id="midiv2" class="midiv2">
            <p class="verde">Lorem ipsum dolor sit amet, consectetur adipisicing elit. Asperiores voluptate nemo necessitatibus voluptatem expedita et reiciendis dolor quos hic, ullam tenetur provident, corrupti exercitationem eius iusto? Dolore error dolorum iure!</p>
        </div>
    </body>
    </html>
    ```
    + Hoja de estilo:
    ```css
    /* estilo universal*/
    * {color: brown;}

    /*selector de elemento*/
    body {
        font-family: 'Oswald', sans-serif;
        font-size: 16px;
        list-style: 20px;
        font-weight:500;
    }

    /*
    p {
        background-color: rgb(36, 14, 114);
        padding: 10px;
    }
    div {
        color: white;
        padding: 20px;
        background-color: chocolate;
        margin-bottom: 20px;
    }
    */

    /* selectores por id*/
    #midiv p {
        color:gray;
        font-style: italic;
    }

    /* selectores de clase*/
    .verde {
        color: green;
    }

    /* Agrupamiento de selectores */
    h2, h1, p {
        color: #741a297c;
    }

    /* Selector por atributo */
    [atributo="hola"] {
        color: #1616cf;    
    }

    input[type="text"] {
        border: 3px solid #000;
    }

    /* selección descendiente */
    .div1 p {
        color: crimson;
        background-color: darkkhaki;
        padding: 20px;
        margin: 30px;
        border: 2px dotted #000;
    }

    /* pseudoclases */
    div p:hover {
        color:blue;
        background-color: cornflowerblue;
        cursor: pointer;
    }

    /*
        selector {
            propiedad:valor;
        }
        selector {
            propiedad:valor;
        }
    */
    ```

### Ejercicios sesión 4
+ Para comenzar a trabajar con CSS, crearéis un documento HTML y otro CSS, en el primero habrá:
    + Un párrafo.
    + Otro párrafo con una class miparrafo.
+ Con CSS deberás hacer que:
    + De manera universal se aplique un color a vuestra elección para el texto.
    + Los elementos que tengan la class miparrafo deberán presentar su texto en cursiva.
+ **Resolción**:
    + Documento html5:
        ```html
        <!DOCTYPE html>
        <html lang="es">
        <head>
            <meta charset="UTF-8">
            <meta name="viewport" content="width=device-width, initial-scale=1.0">
            <title>Introducción al CSS</title>
            <link href="estilos.css" type="text/css" rel="stylesheet" >
        </head>
        <body>
            <p>
                Lorem ipsum dolor, sit amet consectetur adipisicing elit. Fuga minima quod debitis optio soluta recusandae inventore voluptate consequuntur ullam, ipsum quis similique error id temporibus voluptatum, quas sunt. Voluptas, dolorem!
            </p>

            <p class="miparrafo">
                Lorem ipsum dolor sit, amet consectetur adipisicing elit. Aliquam alias minima quam rerum sit non asperiores ab sapiente soluta vero, perferendis excepturi ipsam adipisci in veritatis officia saepe velit? Quia.
            </p>
        </body>
        </html>
        ```
    + Hoja de estilo:
        ```css
        * {
            color: purple;
        }

        .miparrafo {
            font-style: italic;
        }
    ```

### Entrega ejercicio 4
+ **Repositorio GiHub**: 

### Introduccion a las hojas de estilo
1. Código de ejemplos: proyectos\003\04introcss

### Selectores en CSS
1. Código de ejemplos: proyectos\003\04introcss

### Las tres formas de insertar estilos
1. Código de ejemplos: proyectos\003\04introcss

### Colores
1. Código de ejemplos: proyectos\003\04introcss

### Fondos de colores e imágenes
1. Código de ejemplos: proyectos\003\04introcss

### Estilos de altura anchura padding y margin
1. Código de ejemplos: proyectos\003\04introcss

### Fuentes en CSS
1. Código de ejemplos: proyectos\003\04introcss

### Ejercicio
+ Crea un nuevo documento HTML con el título "Ganando precisión con los selectores en CSS".
    + Crea un nuevo fichero CSS e impórtalo en el documento HTML principal
    + Dentro del body crea una sección con los siguientes elementos:
        + Encabezado que contenga el texto "Lista de la compra".
        + Añade en el encabezado un atributo id con el valor "titulo".
        + Añade también un atributo class con el valor "encabezado".
    + Una lista desordenada con cinco elementos que representen artículos de la compra:
        + Cada uno de los elementos debe tener un id como sigue: primer elemento "elemento-1", segundo elemento "elemento-2", etc.
    + Una lista ordenada con cinco elementos que representan los supermercados más cercanos a tu casa:
        + Al igual que en la lista anterior, cada uno de los elementos debe tener un id como sigue: primer elemento "elemento-1", segundo elemento "elemento-2", etc.
    + Modifica el CSS para que el primer elemento de cada lista se muestre de color rojo.
    + A través del encadenamiento de selectores, haz que el primer elemento de la primera lista tenga un tamaño de letra de 2rem.
+ **Resolción**:
    + Documento HTML:
        ```html
        <!DOCTYPE html>
        <html lang="es">
        <head>
            <meta charset="UTF-8">
            <meta http-equiv="X-UA-Compatible" content="IE=edge">
            <meta name="viewport" content="width=device-width, initial-scale=1.0">
            <title>Ganando precisión con los selectores en CSS</title>
            <link rel="stylesheet" href="estilos.css">
        </head>
        <body>
            <div>
                <h1 id="titulo" class="encabezado">Lista de la compra</h1>

                <ul>
                    <li id="elemento-1">Primer Elemento</li>
                    <li id="elemento-2">Segundo Elemento</li>
                    <li id="elemento-3">Tercero Elemento</li>
                    <li id="elemento-4">Cuarto Elemento</li>
                    <li id="elemento-5">Quinto Elemento</li>
                </ul>

                <ol>
                    <li id="elemento-1">Excelsior Gamma</li>
                    <li id="elemento-2">Automercados Plaza</li>
                    <li id="elemento-3">Centralmadeirence</li>
                    <li id="elemento-4">CADA</li>
                    <li id="elemento-5">Unicasa</li>
                </ol>
            </div>
        </body>
        </html>
        ```
    + Hoja de estilos CSS:
        ```css
        #elemento-1 {
            color: red;
        }

        ul #elemento-1 {
            font-size: 2rem;
        }
        ```


## Disposición de elementos y para multimedia
### Vídeo de la sesión 5
1. Ver ejemplos de código html y css en: proyectos\003\ejercicios5\sesion5

### Ejercicio sesión 5
+ Deberéis crear una galería de imágenes, esta galería estará en un contenedor con el borde sólido, en la galería podrás seleccionar la imagen que quieras visualizar entre cuatro, para seleccionar qué imagen ver se hará mediante un input de type radio.
+ **Resolción**:
    + Documento html5:
        ```html
        <!DOCTYPE html>
        <html lang="es">
        <head>
            <meta charset="UTF-8">
            <meta http-equiv="X-UA-Compatible" content="IE=edge">
            <meta name="viewport" content="width=device-width, initial-scale=1.0">
            <title>Sesión 5: Dispositivos de elementos y para multimedia</title>
            <link rel="stylesheet" type="text/css" href="css/estilos.css" />
        </head>
        <body>
            <div class="galeria">
                <input type="radio" name="galeria">
                <input type="radio" name="galeria">
                <input type="radio" name="galeria">
                <input type="radio" name="galeria">

                <img src="img/img1.jpg" alt="Imagen 1" width="314" height="209">
                <img src="img/img2.jpg" alt="Imagen 2" width="314" height="209">
                <img src="img/img3.jpg" alt="Imagen 3" width="314" height="209">
                <img src="img/img4.jpg" alt="Imagen 4" width="314" height="209">
            </div>
        </body>
        </html>
        ```
    + Hoja de estilo:
        ```css
        .galeria {
            width: 314px;
            height: 209px;
            margin:1em auto;
            border: 1px solid blue;
            position: relative;
        }

        .galeria img {
            position: absolute;
            top: 0;
            left: 0;
            opacity: 0;
            transition: opacity .9s;
        }

        .galeria input[type=radio] {
            position: relative;
            top: 220px;
            margin-left: 50px;
        }

        .galeria input[type=radio]:nth-of-type(1):checked ~ img:nth-of-type(1) {
            opacity: 1;
        }

        .galeria input[type=radio]:nth-of-type(2):checked ~ img:nth-of-type(2) {
            opacity: 1;
        }

        .galeria input[type=radio]:nth-of-type(3):checked ~ img:nth-of-type(3) {
            opacity: 1;
        }

        .galeria input[type=radio]:nth-of-type(4):checked ~ img:nth-of-type(4) {
            opacity: 1;
        }
        ```

### Entrega ejercicio 5
+ **Repositorio GiHub**: https://github.com/petrix12/openbootcamp2022/tree/main/proyectos/003/ejercicios5

### Disposiciones y alineaciones
+ proyectos\003\05disposiciones\disposiciones.html

### Posicionamiento
+ proyectos\003\05disposiciones\posicionamiento.html

### FlexBox
+ proyectos\003\05disposiciones\flex.html

### Overflow
+ proyectos\003\05disposiciones\overflow.html

### Trabajando la opacidad y galerías de imágenes
+ proyectos\003\05disposiciones\multimedia.html

### Reproductores de vídeo
+ proyectos\003\05disposiciones\video.html

### Ejercicio
+ Crea un nuevo documento HTML con el título "Disposición de elementos en CSS":
    + Crea un nuevo fichero CSS e impórtalo en el documento HTML principal
    + Utiliza la disposición flex-box para crear una galería de 6 imágenes con los siguientes parámetros:
        + Las imágenes deben tener 300 píxeles de ancho.
        + Deben reagruparse (wrap) cuando el ancho del viewport cambia.
+ **Resolción**:
    + Documento HTML:
        ```html
        <!DOCTYPE html>
        <html lang="es">
        <head>
            <meta charset="UTF-8">
            <meta http-equiv="X-UA-Compatible" content="IE=edge">
            <meta name="viewport" content="width=device-width, initial-scale=1.0">
            <title>Disposición de elementos en CSS</title>
            <link rel="stylesheet" href="ejercicio.css">
        </head>
        <body>
            <div class="galeria">
                <img class="img-galeria" src="../img/imagen1.jpg" alt="imagen1">
                <img class="img-galeria" src="../img/imagen2.jpg" alt="imagen2">
                <img class="img-galeria" src="../img/imagen3.jpg" alt="imagen3">
                <img class="img-galeria" src="../img/imagen4.jpg" alt="imagen4">
                <img class="img-galeria" src="../img/imagen5.jpg" alt="imagen5">
                <img class="img-galeria" src="../img/imagen6.jpg" alt="imagen6">
            </div>  
        </body>
        </html>
        ```
    + Hoja de estilos CSS:
        ```css
        .galeria {
            display: flex;
            flex-wrap: wrap;
        }

        .img-galeria {
            width: 300px;
        }
        ```

## 6. Anidación de selectores
### Anidación de selectores
+ proyectos\003\06selectores\html\selectores.html

### Pseudoclases
+ proyectos\003\06selectores\html\pseudoclases.html

### Pseudoelementos
+ proyectos\003\06selectores\html\pseudoelementos.html

### Especificidad
+ proyectos\003\06selectores\html\especificidad.html

### Ejercicio
+ Crea un nuevo documento HTML con el título "Selectores, pseudo-clases y pseudo-elementos en CSS":
    + Crea un nuevo fichero CSS e impórtalo en el documento HTML principal.
    + Crea un botón con el texto "Pasa por encima" (TIP: Este texto debes agregarlo a través de un pseudo-elemento)
    + Utiliza las pseudo-clases para que cuando se pase el ratón por encima de este botón, el texto se vuelva blanco y el fondo de color verde
    + Utiliza los pseudo-elementos para cambiar el texto del botón a "¡Hecho!"
+ **Resolción**:
    + Documento HTML:
    ```html
    <!DOCTYPE html>
    <html lang="es">
    <head>
        <meta charset="UTF-8">
        <meta http-equiv="X-UA-Compatible" content="IE=edge">
        <meta name="viewport" content="width=device-width, initial-scale=1.0">
        <title>Selectores, pseudo-clases y pseudo-elementos en CSS</title>
        <link rel="stylesheet" href="entrega.css">
    </head>
    <body>
        <button class="texto-boton"></button>
    </body>
    </html>
    ```
    + Hoja de estilos CSS:
    ```css
    .texto-boton::before {
        content: "Pasa por encima";
    }

    .texto-boton:hover {
        color: white;
        background-color: green;
    }

    .texto-boton:hover::before {
        content: "¡Hecho!";
    }
    ```


## 7.Creación de estilos para formularios
### Estilando formularios
+ proyectos\003\07formularios\html\estilosformularios.html

### Creando un formulario moderno - Parte 1
+ proyectos\003\07formularios\html\login.html

### Creando un formulario moderno - Parte 2
+ proyectos\003\07formularios\html\login.html

### Ejercicio
+ Replica el ejercicio del vídeo 3 de esta sesión y realiza el siguiente cambio:
    + Replícalo exactamente igual, pero realiza una nueva versión en modo oscuro.
    + Los colores serán los siguientes:
        + El rosa se queda igual.
        + El fondo blanco será sustituido por el color #161717.
        + El fondo de los inputs tendrá un color #212121.
        + El fondo de los inputs cuando se hace hover será del color #454045.
        + Los textos tendrán un color blanco.
+ **Resolción**:
    + Documento HTML (proyectos\003\07formularios\entrega\entrega.html):
    ```html
    <!DOCTYPE html>
    <html lang="en">
    <head>
        <meta charset="UTF-8">
        <meta http-equiv="X-UA-Compatible" content="IE=edge">
        <meta name="viewport" content="width=device-width, initial-scale=1.0">
        <title>Login Form</title>
        <link rel="stylesheet" href="entrega.css">
    </head>
    <body>
        <div class="container">
            <h3>Regístrate en los formularios</h3>
            <div class="buttons">
                <button class="google-btn">
                    <picture>
                        <img src="https://entredichos.trabajosocial.unlp.edu.ar/wp-content/uploads/sites/6/2016/12/Google_-G-_Logo.svg_.png" alt="logo-google" />
                    </picture>
                    <span>Registrarse con Google</span>
                </button>
                <button class="twitter-btn">
                    <picture>T</picture>
                </button>
            </div>
            <div class="separator">
                <hr>
                <span>O...</span>
                <hr>
            </div>
            <form action="" method="">
                <div class="section-inputs">
                    <label for="name">
                        <span>Name</span>
                        <input id="name" name="name" />
                    </label>
                    <label for="username">
                        <span>Username</span>
                        <input id="username" name="username" />
                    </label>
                </div>
                <label for="email">
                    <span>Email</span>
                    <input id="email" name="email" />
                </label>
                <label for="password">
                    <span>Password</span>
                    <input id="password" name="password" placeholder="6+ caracteres" />
                </label>
                <label for="checkbox" class="checkbox-label">
                    <input type="checkbox" id="checkbox">
                    <span>Acepto las condiciones y el aviso legal</span>
                </label>
                <button type="submit" class="submit-btn">Crear Cuenta</button>
            </form>
        </div>
    </body>
    </html>
    ```
    + Hoja de estilos CSS (proyectos\003\07formularios\entrega\entrega.css):
    ```css
    @import url('https://fonts.googleapis.com/css2?family=Ubuntu:wght@300;400;500;700&display=swap');

    * {
        font-family: 'Ubuntu', sans-serif;
    }

    body {
        background-color: #161717;
    }

    .container {
        margin: auto;
        display: flex;
        flex-direction: column;
        align-items: center;
        justify-content: center;
        gap: 30px;
        width: 450px;
    }

    .buttons {
        align-self: flex-start;
        display: flex;
        gap: 20px;
    }

    .google-btn {
        background-color: #1A73E8;
        border: none;
        border-radius: 5px;
        height: 40px;
        display: flex;
        align-items: center;
        padding: 2px;
        cursor: pointer;
    }

    .google-btn:hover {
        opacity: 0.75;
    }

    .google-btn picture {
        width: 35px;
        height: 35px;
        background-color: white;
        border-radius: 2px;
        display: flex;
        align-items: center;
        justify-content: center;
    }

    .google-btn picture img {
        width: 75%;
    }

    .google-btn span {
        color: white;
        font-weight: 500;
        padding: 15px;
    }

    .twitter-btn {
        color: #bbb;
        background-color: #eee;
        border: none;
        width: 40px;
        border-radius: 5px;
        cursor: pointer;
    }

    .twitter-btn:hover {
        background-color: #ddd;
    }

    .separator {
        display: flex;
        width: 100%;
        gap: 15px;
    }

    .separator hr {
        flex-grow: 1;
        border: none;
        border-top: 1px solid #ccc;
    }

    .separator span {
        color: #8b8b8b;
    }

    .section-inputs {
        display: flex;
        gap: 10px;
        width: 100%;
    }

    form {
        display: flex;
        flex-direction: column;
        align-items: stretch;
        gap: 30px;
    }

    label {
        display: flex;
        flex-direction: column;
        gap: 5px;
    }

    label span {
        font-weight: 700;
        color: white;
    }

    .section-inputs label input {
        width: 80%;
        border: none;
        padding: 10px 20px;
        border-radius: 10px;
        outline: none;
        font-size: 14pt;
    }

    label input {
        width: 90%;
        background-color: #212121;
        color: white;
        border: none;
        padding: 10px 20px;
        border-radius: 10px;
        outline: none;
        font-size: 14pt;
        transition: background-color 0.2s, border 0.2s, box-shadow 0.2s;
    }

    label input:hover {
        background-color: #454045;
        border: solid 1px #f3f3f4;
        box-shadow: 0 0 4px #eb50ff4f;
    }
    label input:focus {
        background-color: #454045;
        border: solid 1px #f3f3f4;
        box-shadow: 0 0 4px #eb50ff4f;
    }

    .checkbox-label {
        display: flex;
        flex-direction: row;
    }

    .checkbox-label input[type="checkbox"] {
        width: 20px;
    }

    .checkbox-label span {
        font-weight: 400;
    }

    .submit-btn {
        background-color: #EA4C89;
        color: white;
        font-weight: 500;
        font-size: 14pt;
        text-align: center;
        padding: 15px;
        border: none;
        border-radius: 10px;
        cursor: pointer;
    }

    .submit-btn:hover {
        opacity: 0.75;
    }
    ```


## 8.Bootstrap
### Incluyendo Bootstrap en nuestro proyecto
+ proyectos\003\08bootstrap\bootstrap.html

### Estilos y animaciones de Bootstrap
+ proyectos\003\08bootstrap\bootstrap.html

### Ejercicio
+ Crea un nuevo documento HTML con el título "Introducción a Bootstrap":
    + Utilizando la página oficial getboostrap.com, añade la última versión de Bootstrap a este documento HTML.
+ **Resolción**:
    + Documento HTML:
    ```html
    <!DOCTYPE html>
    <html lang="es">
    <head>
        <meta charset="UTF-8">
        <meta http-equiv="X-UA-Compatible" content="IE=edge">
        <meta name="viewport" content="width=device-width, initial-scale=1.0">
        <title>Introducción a Bootstrap</title>
        <!-- CSS only -->
        <link href="https://cdn.jsdelivr.net/npm/bootstrap@5.2.0-beta1/dist/css/bootstrap.min.css" rel="stylesheet" integrity="sha384-0evHe/X+R7YkIZDRvuzKMRqM+OrBnVFBL6DOitfPri4tjfHxaWutUpFmBp4vmVor" crossorigin="anonymous">
    </head>
    <body>
        <div class="container">
            <h1>Documento HTML con la última versión de Bootstrap al 10-06-2022</h1>
        </div>
    </body>
    <!-- JavaScript Bundle with Popper -->
    <script src="https://cdn.jsdelivr.net/npm/bootstrap@5.2.0-beta1/dist/js/bootstrap.bundle.min.js" integrity="sha384-pprn3073KE6tl6bjs2QrFaJGz5/SUsLqktiwsUTF55Jfv3qYSDhgCecCxMW52nD2" crossorigin="anonymous"></script>
    </html>
    ```


## 9.Animaciones y transiciones
### Animaciones y Transiciones
+ proyectos\003\09animaciones\animaciones.html

### Tooltips
+ proyectos\003\09animaciones\tooltip.html

### Ejercicio
+ Crea un nuevo documento HTML con el título "Animaciones y transiciones en CSS":
    + Crea un nuevo fichero CSS e impórtalo en el documento HTML principal.
    + En el body crea un botón con el atributo class "btn-modern".
    + Implementa las líneas necesarias en el CSS para que cuando el ratón pase por encima del botón ocurra lo siguiente (hover):
        + El botón se traslade -5px en el eje de las Y.
        + Se añada una sombra.
        + El color de fondo del botón cambie.
        + El color del texto cambie.
        + Todo esto con una transición de 0.4s.
+ **Resolción**:
    + Documento HTML:
    ```html
    <!DOCTYPE html>
    <html lang="es">
    <head>
        <meta charset="UTF-8">
        <meta http-equiv="X-UA-Compatible" content="IE=edge">
        <meta name="viewport" content="width=device-width, initial-scale=1.0">
        <title>Animaciones y transiciones en CSS</title>
        <link rel="stylesheet" href="entrega.css">
    </head>
    <body>
        <button class="btn-modern">Botón</button>
    </body>
    ```
    + Hoja de estilos CSS:
    ```css
    .btn-modern:hover {
        transform: translateX(-5px);
        box-shadow: 0 0 10px gray;
        background-color: purple;
        color: aquamarine;
        transition: all 0.4s
    }
    ```


## 10.Introducción al diseño responsive
### Unidades fijas y relativas
+ proyectos\003\10responsive\unidades.html

### Responsive y unidades em y rem
+ proyectos\003\10responsive\unidades-em.html

### Media Queries
+ proyectos\003\10responsive\mediaqueries.html

### Uso Avanzado de Flex Box
+ proyectos\003\10responsive\flexbox.html

### Viewport, Grid y templates
+ proyectos\003\10responsive\grid.html

### Variables reutilizables en CSS
+ proyectos\003\10responsive\variables.html

### Ejercicio
+ Crea un nuevo documento HTML con el título "Diseño Responsive con CSS":
    + Crea un nuevo fichero CSS e impórtalo en el documento HTML principal
    + Crea las siguientes dos secciones:
        + Una barra lateral izquierda con tres elementos en vertical.
        + Una sección principal a la derecha.
        + (Tip: Utiliza la disposición flex donde la sección principal utilizará flex-grow).
    + Utiliza las media queries para que cuando el ancho del viewport sea menor de 640px ocurra lo siguiente:
        + La barra lateral izquierda se muestre como una navegación en la parte inferior.
        + La disposición de los elementos de la barra lateral se vuelva horizontal.
        + (Tip: Trabaja con la propiedad flex-direction)
+ **Resolción**:
    + Documento HTML:
    ```html
    <!DOCTYPE html>
    <html lang="es">
    <head>
        <meta charset="UTF-8">
        <meta http-equiv="X-UA-Compatible" content="IE=edge">
        <meta name="viewport" content="width=device-width, initial-scale=1.0">
        <title>Diseño Responsive con CSS</title>
        <link rel="stylesheet" href="entrega.css">
    </head>
    <body>
        <div class="contenedor">
            <div class="seccion-1">
                <div class="elemento-1">Elemento 1</div>
                <div class="elemento-2">Elemento 2</div>
                <div class="elemento-3">Elemento 3</div>
            </div>
            <div class="seccion-2">
                <span>CONTENIDO PRINCIPAL</span>
            </div>
        </div>
    </body>
    </html>
    ```
    + Hoja de estilos CSS:
    ```css
    .contenedor {
        display: flex;
        margin: 1rem;
        padding: 1rem;
        background-color: yellow;
    }

    .seccion-1 {
        margin: 1rem;
        padding: 1rem;
        background-color: green;
        display: flex;
        flex-direction: column;
        gap: 0.5rem;
    }

    .seccion-2 {
        margin: 1rem;
        padding: 1rem;
        background-color: blue;
        flex-grow: 1;
    }

    @media (max-width: 640px) {
        .contenedor {
            flex-direction: column-reverse;
        }
        .seccion-1 {
            flex-direction: row;
            justify-content: space-evenly;
        }
    }
    ```


## 11.El sistema grid de Bootstrap
### Sistema grid de Bootstrap
+ proyectos\003\11bootstrap-grid\grid.html

### Ejercicio
+ Crea un nuevo documento HTML con el título "Sistema grid de Bootstrap":
    + Utilizando la página oficial getboostrap.com, añade la última versión de Bootstrap a este documento HTML.
    + Crea 6 div con un texto en su interior
    + Utilizando únicamente el atributo class de cada uno de los div haz lo siguiente:
        + Por defecto, cada elemento ocupará el ancho máximo.
        + Para viewports SM - cada fila contendrá 2 elementos.
        + Para viewports MD - cada fila contendrá 3 elementos.
        + Para viewports LG - cada fila contendrá 4 elementos.
        + Para viewports XL - cada fila contendrá 6 elementos.
+ **Resolción**:
    + Documento HTML:
    ```html
    <!DOCTYPE html>
    <html lang="es">
    <head>
        <meta charset="UTF-8">
        <meta http-equiv="X-UA-Compatible" content="IE=edge">
        <meta name="viewport" content="width=device-width, initial-scale=1.0">
        <title>Sistema grid de Bootstrap</title>
        <!-- CSS only -->
        <link href="https://cdn.jsdelivr.net/npm/bootstrap@5.2.0-beta1/dist/css/bootstrap.min.css" rel="stylesheet" integrity="sha384-0evHe/X+R7YkIZDRvuzKMRqM+OrBnVFBL6DOitfPri4tjfHxaWutUpFmBp4vmVor" crossorigin="anonymous">
    </head>
    <body>
        <div class="row">
            <div class="col-sm-6 col-md-4 col-lg-3 col-xl-2">División 2</div>
            <div class="col-sm-6 col-md-4 col-lg-3 col-xl-2">División 1</div>
            <div class="col-sm-6 col-md-4 col-lg-3 col-xl-2">División 3</div>
            <div class="col-sm-6 col-md-4 col-lg-3 col-xl-2">División 4</div>
            <div class="col-sm-6 col-md-4 col-lg-3 col-xl-2">División 5</div>
            <div class="col-sm-6 col-md-4 col-lg-3 col-xl-2">División 6</div>
        </div>
    </body>
    <!-- JavaScript Bundle with Popper -->
    <script src="https://cdn.jsdelivr.net/npm/bootstrap@5.2.0-beta1/dist/js/bootstrap.bundle.min.js" integrity="sha384-pprn3073KE6tl6bjs2QrFaJGz5/SUsLqktiwsUTF55Jfv3qYSDhgCecCxMW52nD2" crossorigin="anonymous"></script>
    </html>
    ```


## 12.Otros aspectos de interés de Boostrap
### Tablas
+ proyectos\003\12bootstrap-elementos\tablas.html

### Imágenes
+ proyectos\003\12bootstrap-elementos\imagenes.html

### Jumbotron
+ proyectos\003\12bootstrap-elementos\jumbotron.html

### Alertas
+ proyectos\003\12bootstrap-elementos\alertas.html

### Spinners
+ proyectos\003\12bootstrap-elementos\spinners.html

### Tarjetas
+ proyectos\003\12bootstrap-elementos\tarjetas.html

### Listas - Parte 1
+ proyectos\003\12bootstrap-elementos\listas.html

### Listas - Parte 2
+ proyectos\003\12bootstrap-elementos\listas-2.html

### Formularios - Parte 1
+ proyectos\003\12bootstrap-elementos\forms.html

### Formularios - Parte 2
+ proyectos\003\12bootstrap-elementos\forms-2.html

### Formularios - Parte 3
+ proyectos\003\12bootstrap-elementos\forms-3.html

### Modales, popovers y tooltips
+ proyectos\003\12bootstrap-elementos\modales.html

### Iconos
+ proyectos\003\12bootstrap-elementos\iconos.html

### Toasts
+ proyectos\003\12bootstrap-elementos\toasts.html

### Badges
+ proyectos\003\12bootstrap-elementos\badges.html

### Progress
+ proyectos\003\12bootstrap-elementos\progress.html

### Tipografia en Bootstrap
+ proyectos\003\12bootstrap-elementos\tipografias.html

### Ejercicio
+ Crea un nuevo documento HTML con el título "Elementos de Interés en Bootstrap":
    + Utilizando la página oficial getboostrap.com, añade la última versión de Bootstrap a este documento HTML.
    + Crea tres secciones.
    + En la primera sección crea un Jumbotron replicando el que realizamos en el vídeo:
        + El botón de llamada a la acción debe abrir una ventana modal.
    + En la segunda sección crea un formulario de contacto con los campos "nombre" (text), "teléfono" (number) y mensaje (textarea)
    + En la tercera sección crea una tarjeta con tu perfil de desarrollador/a que contenga lo siguiente:
        + Tu nombre en el título.
        + Una breve descripción.
        + Tu email en el footer.
+ **Resolción**:
    + Documento HTML:
    ```html
    <!DOCTYPE html>
    <html lang="es">
    <head>
        <meta charset="UTF-8">
        <meta http-equiv="X-UA-Compatible" content="IE=edge">
        <meta name="viewport" content="width=device-width, initial-scale=1.0">
        <title>Elementos de Interés en Bootstrap</title>
        <!-- CSS only -->
        <link href="https://cdn.jsdelivr.net/npm/bootstrap@5.2.0-beta1/dist/css/bootstrap.min.css" rel="stylesheet" integrity="sha384-0evHe/X+R7YkIZDRvuzKMRqM+OrBnVFBL6DOitfPri4tjfHxaWutUpFmBp4vmVor" crossorigin="anonymous">
    </head>
    <body>
        <div class="container my-5">
            <section>
                <div class="bg-light p-3 rounded-3">
                    <div class="container-fluid py-3">
                        <h1 class="display-5 fw-bold">Jumbotron personalizado</h1>
                        <p class="col-md-8 fs-4">
                            Texto de llamado a la acción del Jumbotron personalizado, el cual abre una ventana modal.
                        </p>
                        <button 
                            class="btn btn-primary btn-lg"
                            type="button"
                            data-bs-toggle="modal" 
                            data-bs-target="#exampleModal"
                        >Abrir ventana modal</button>
                        <!-- Modal -->
                        <div class="modal fade" id="exampleModal" tabindex="-1" aria-labelledby="exampleModalLabel" aria-hidden="true">
                            <div class="modal-dialog">
                                <div class="modal-content">
                                    <div class="modal-header">
                                        <h5 class="modal-title" id="exampleModalLabel">Header de la ventana modal</h5>
                                        <button type="button" class="btn-close" data-bs-dismiss="modal" aria-label="Close"></button>
                                    </div>
                                    <div class="modal-body">
                                        Body de la ventana modal
                                    </div>
                                    <div class="modal-footer">
                                        <button type="button" class="btn btn-secondary" data-bs-dismiss="modal">Cacelar</button>
                                    <button type="button" class="btn btn-primary">Aceptar</button>
                                    </div>
                                </div>
                            </div>
                        </div>
                    </div>
                </div>
            </section>
            <hr />
            <section>
                <form action="#">
                    <div class="row">
                        <div class="mb-3 col-sm-12 col-md-6">
                            <label for="nombre" class="form-label">Nombre</label>
                            <input type="text" class="form-control" id="nombre" placeholder="Escribe tu nombre">
                        </div>
                        <div class="mb-3 col-sm-12 col-md-6">
                            <label for="telefono" class="form-label">Teléfono</label>
                            <input type="number" class="form-control" id="telefono" placeholder="Escribe tu número de teléfono">
                        </div>
                    </div>
                    <div class="mb-3">
                        <label for="mensaje" class="form-label">Mensaje</label>
                        <textarea class="form-control" id="mensaje" rows="3" placeholder="Escribe aquí tu mensaje"></textarea>
                    </div>
                    <button class="btn btn-primary">Enviar</button>
                </form>
            </section>
            <hr />
            <section>
                <div class="card w-50">
                    <div class="card-header text-center">
                        <h4 class="card-title">Pedro Bazó</h4>
                    </div>
                    <div class="card-body">
                        <p class="card-text">
                            Hola, mi nombre es P. J. Bazó, soy escritor y desarrollador de aplicaciones web, 
                            también soy ingeniero químico.
                            Me apasiona tanto escribir, como crear aplicaciones web, en cuanto a mis escritos, 
                            tengo dos obras: La furia de San Julián, y El tiempo de César Augusto Pérez Soles, 
                            la primera es un relato corto de más de 9 mil palabras, ya concluido, 
                            y la segunda es una novela del género fantástico en progreso.
                            También si quieres conocer acerca de mis proyectos web, puedes visitar mi 
                            página: <a href="https://petrix12.github.io/cvpetrix2022">Soluciones++</a>
                        </p>
                    </div>
                    <div class="card-footer text-center">
                        <h5>bazo.pedro@gmail.com</h5>
                    </div>
                </div>
            </section>
        </div>
    </body>
    <!-- JavaScript Bundle with Popper -->
    <script src="https://cdn.jsdelivr.net/npm/bootstrap@5.2.0-beta1/dist/js/bootstrap.bundle.min.js" integrity="sha384-pprn3073KE6tl6bjs2QrFaJGz5/SUsLqktiwsUTF55Jfv3qYSDhgCecCxMW52nD2" crossorigin="anonymous"></script>
    </html>
    ```


## 13.Usando pre-procesadores CSS
### Introducción a SASS
+ Instalar extensión:
    + Live Sass Compiler
        + Glenn Marks
        + Compile Sass or Scss to CSS at realtime.
+ proyectos\003\13sass\introsass.html

### Variables y mixins
+ https://github.com/Open-Bootcamp/HTML-CSS/tree/main/13-Sass

### Importación de extensiones
+ https://github.com/Open-Bootcamp/HTML-CSS/tree/main/13-Sass

### Instalación global SASS y use vs import
+ Instalar SASS de forma global:
    + $ npm install -g sass
+ Para ir compilando SASS:
    + $ sass --watch sass/styles.scss css/styles.css

### Funciones SASS
+ https://sass-lang.com/documentation/modules
+ https://github.com/Open-Bootcamp/HTML-CSS/blob/main/13-Sass/sass/_builtin.scss


## 14.Presentación proyecto final
### Presentación del proyecto final e instalación
+ proyectos\003\14proyecto
+ Para compilar el css:
    + $ sass --watch sass/index.scss css/styles.css


## 15.Finalización proyecto final
### Terminando de crear los componentes
+ proyectos\003\14proyecto\html\proyecto.html

### Menú de navegación
+ proyectos\003\14proyecto\html\proyecto.html

### Sección Home
+ proyectos\003\14proyecto\html\proyecto.html

### Sección Features
+ proyectos\003\14proyecto\html\proyecto.html

### Sección Benefits
+ proyectos\003\14proyecto\html\proyecto.html

### Sección KPIs
### Sección OnBoarding
### Sección Footer
### Responsivizando nuestro proyecto



+ mmmm
+ **Resolción**:
    + Documento HTML:
    ```html
    ≡
    ≡
    ```
    + Hoja de estilos CSS:
    ```css
    ≡
    ≡
    ```



git config --global user.name "Pedro Bazó"
git config --global user.email bazo.pedro@gmail.com