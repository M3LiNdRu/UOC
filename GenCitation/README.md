# Generador de cites #

Aquest codi serveix per generar dinàmicament cites de pàgines web seguint
la guía de infografia de la UOC.

El programa ofereix dos modes: Generar una cita a l'instant o espera un arxiu
`entrada.csv` amb la url de la pàgina web i la data de la consulta separades
per ;

### Mètode 1
python3 main.py --url https://google.com

La cita sortirà impresa per pantalla

### Mètode 2
python3 main.py -f entrada.csv 

Un cop s'executa, el programa escriu les cites en un fitxer `sortida.txt`


## Recursos
[Infografia UOC](https://www.uoc.edu/biblioteca/ca/recursos/gestio-bibliografica-uoc/com_citar.html)