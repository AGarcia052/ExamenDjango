# RadioVirgen

### SUPERUSER:
### fran
### 1234

# COMANDOS

1. subir_datos_iniciales. Comando de carga de datos. No recibe parámetros -- Daniel

``` python manage.py 1_subir_datos_iniciales ```
   
2. listar_usuarios. Lista todos los usuarios en la BB.DD. No recibe parámetros -- Alejandro
   
``` python manage.py 2_listar_usuarios ```
   
3. reproducciones_usuario. Comando que liste las reproducciones de un usuario, pasando como parámetro su 
nick. -- Daniel

```python manage.py 3_reproducciones_usuario --nick="(nick del usuario que se quiere listar)"```

4. aniadir_podcast_pendiente. Comando para añadir un podcast a la lista de pendientes de un usuario. Utilizar "" si el nombre del podcast tiene espacios en blanco --Daniel
   
```python manage.py 4_aniadir_podcast_pendiente --nick="(nick del usuario a listar)" --podcast_pendiente="(nombre del podcast)"```

5. like_podcast. Añade un podcast a la lista de podcast con like del usuario.--Alejandro
   
``` python manage.py 5_like_podcast --nick (nick usuario) --id_podcast (id del podcast) ```

6. pendiente_podcast. Añade un podcast a la lista de podcast pendiente del usuario. --Alejandro
   
``` python manage.py 6_pendiente_podcast --nick (nick usuario) --id_podcast (id del podcast)```

drop_database:
 Elimina todos los datos de las tablas y reinicia las secuencias de los ID. --Daniel --Alejandro
