import os 
import sqlite3 as sql
from colorama import * # Importamos Colorama.
init() # Inicializamos Colorama

def clean(): # Function to clean console.
    if os.name == 'nt' or os.name == 'msdos':
        os.system('cls');
        pass
    else:
        os.system('clear');
        pass
    pass

conexion = sql.connect('wifi.db'); # Nombre de la base de datos
conexion.commit(); #Creamos el archivo.
cursor = conexion.cursor(); # Creamos el cursor
cursor.execute('''
    CREATE TABLE IF NOT EXISTS datos(
        red_name VARCHAR(800) NOT NULL,
        red_password VARCHAR(800) NOT NULL
    );
''') # Creamos la tabla si no existe
conexion.close();

Error_Message = str('\n! No Hay redes guardadas en la base de datos.\n'); # Error Red Message.


def main(): # Main Function Ok??!
    autor = 'Axel Ezequiel Kampmann'
    version = '[1.0]'
    menu = f'''# Wifi Save Tool

###> By : {autor}
 
###> Version : {version}
 
###> Elige una opcion
'''
    Options = '''
[a] - Guardar una red wifi.

[b] - Ver Redes Wifi Guardadas.

[c] - Borrar todas las redes.

[d] - Exportar todas las redes en un ".txt".

[xx] - Salir de la app.
'''
    clean();
    print(Fore.LIGHTGREEN_EX + menu);
    print(Fore.LIGHTYELLOW_EX + Options);
    optc = str(input(Fore.LIGHTBLUE_EX + '\n###> Elige una Opcion >> ')).lower();

    if optc == 'a':
        generate();

    elif optc == 'b':
        view();
    elif optc == 'c':
        delete();

    elif optc == 'd':
        export();

    elif optc == 'xx':
        exit();
    else:
        print(f'\n\nOpcion "{optc}" invalida, saliendo de la app.\n\n');
        exit();

def generate(): # Save Wifi Connections Into of the Database. 
    name = str(input(Fore.LIGHTMAGENTA_EX  + '\n> Ingresa el nombre de la red wifi >> '));
    password = str(input(Fore.LIGHTRED_EX +'\n> Ingresa la password de la red wifi >> '));

    conexion = sql.connect('wifi.db');
    cursor = conexion.cursor();
    cursor.execute(f'''INSERT INTO datos(red_name , red_password) VALUES ('{name}' , '{password}');''')
    conexion.commit();
    conexion.close();
    print(Fore.LIGHTYELLOW_EX + '\n> Red añadida a la base de datos.\n')
    exit();

def view(): # View Wifi's Connections Function
    conexion = sql.connect('wifi.db');
    cursor = conexion.cursor();
    cursor.execute('''SELECT * FROM datos;''');
    red = cursor.fetchall();
    conexion.commit();
    conexion.close();

    if red == []: # Detectamos las redes wifi.
        print(Fore.LIGHTRED_EX + Error_Message); # Error Red Message
        exit();

    else: # De lo contrario mostramos las redes wifi
        print(Fore.LIGHTMAGENTA_EX + '\n> Redes Wifi Guardadas en la base de datos.\n');
        for i in red:
            print(Fore.LIGHTCYAN_EX + '> Nombre , Contraseña.');
            print(Fore.LIGHTYELLOW_EX + '> {}\n'.format(i));

def delete(): # Delete Function.
    conexion = sql.connect('wifi.db');
    cursor = conexion.cursor();
    cursor.execute('''DROP TABLE IF EXISTS datos''');
    conexion.commit(); # Cometemos los cambios.
    conexion.close(); # Cerramos la conexion.
    print(Fore.LIGHTYELLOW_EX + '\n\n> Tabla borrada correctamente.\n');
    exit();

def export(): # Export Function
    # Fetch or Get Data.
    conexion = sql.connect('wifi.db');
    cursor = conexion.cursor();
    cursor.execute('SELECT * FROM datos;');
    information = cursor.fetchall();
    conexion.commit();
    conexion.close();

    if information == []: # Detectamos las redes wifi.
        print(Fore.LIGHTRED_EX + Error_Message); # Error Red Message.
        exit();

    else: # De lo contrario exportamos los datos.
        name_file = 'exportado.txt'
        file = open(name_file , 'w');
        file.write('Las redes se guardan en formato (name , password) #\n\n');

        for x in information:
            file.write('Red : ' + str(x) + '.\n'); # Write Data.

        file.close();
        print(Fore.LIGHTYELLOW_EX + '\n> Exportado Correctamente en "{}"\n'.format(name_file));
        exit();
    pass

main(); # Run the main Function.
