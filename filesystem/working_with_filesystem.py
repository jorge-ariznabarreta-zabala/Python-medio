from pathlib import Path

print ( "### INSTANCIAS Path ###")
wave = Path("ocean", "wave.txt")# ruta relativa
print(wave, " *** Path con varios argumentos string, ruta relativa ***")

home = Path.home() #ruta abosoluta = home+ruta relativa
wave_absolute = Path(home, "ocean", "wave.txt") 
print(home, " **** esto es home ****")
print(wave_absolute, " *** esto es la ruta con home ***")
print ("ruta absoluta = home+ruta relativa")
shark = Path(Path.home(), "ocean", "animals", Path("fish", "shark.txt"))
print(shark, " <= *** ruta con varios atributos string y Path")
print ('shark = Path(Path.home(), "ocean", "animals", Path("fish", "shark.txt"))')

print ( "### ATRIBUTOS de los archivos ###")
print ( "### .name .suffix .with_name ###")
wave = Path("ocean", "wave.txt")
print(wave)
print(wave.name , " atributo name")
print(wave.suffix, "atributo suffix")

tides = wave.with_name("tides.txt")
print(wave, " original")
print(tides, 'with_name("tides.txt")')

print ("*** antecesores subir a la carpeta contenedora .parent***")
shark = Path("ocean", "animals", "fish", "shark.txt")
print(shark, '<= shark')
print(shark.parent, '<= parent' )

print('metodo GLOB')
print('└── ocean')
print('    ├── animals')
print('    │   └── fish')
print('    │       └── shark.txt')
print('    ├── tides.txt')
print('    └── wave.txt')

print ('imprime los txt del directorio ocean')
for txt_path in Path("ocean").glob("*.txt"):
    print(txt_path)

print ('imprime los txt del directorio ocean e hijos')
for txt_path in Path("ocean").glob("**/*.txt"):
    print(txt_path)