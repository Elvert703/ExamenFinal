#
# candidatos.py
# Autor: Catedratico Cientifica II
# fecha: julio 2010
#
# Este programa realiza una votacion por los candidatos
# a presidencia de Guatemala
#
#

def pedirNumero(texto):
    """
    pide un dato al usuario y verifica que sea un entero
    parametro: texto indica el mensaje al solicitar el dato
    """
    correcto = False
    while not correcto:
        numero = raw_input(texto)

        #Revisar que sea posible la conversion
        try:
            numero = int(numero)
        except:
            print "--> ERROR: Lo ingresado no es numero entero.\n"
        else:
            correcto = True
    return numero

def votar (candidato, listaNombres,losvotos):
    """
    recibe el nombre del candido por el cual se emite el voto,
    si existe, incrementa en uno la cantidad de votos recibidos
    por ese candidato.
    Parametros: candidato, es el nombre del candidato
                listaNombres, lista de los nombres de todos
                los candidatos
                losvotos, lista con la cantidad de votos por
                        cada candidato.

    OJO: si existen candidatos con el mismo nombre, incrementa
         los votos de todos ellos. Puede usted mejorar esto?
    """
    pos = 0
    existe = False  #suponemos que no existe en la lista
    while pos < len(listaNombres):  #buscamos en toda la lista
        if listaNombres[pos] == candidato: #encontramos al candidato
            existe = True
            losvotos[pos] = losvotos[pos] + 1
        pos = pos + 1
    if not existe:
        print "Ese candidato no esta inscrito en esta votacion "
        

def mostrarCandidatos (listaNombres, listaVotos):
    """
    muestra todos los candidatos y los votos recibos
    Parametros: listaNombres, nombres de los candidatos
                listaVotos, la cantidad de votos por candidato
    """

    for i in range(0,len(listaNombres)):
        print nombres[i], " tiene votos: ", votos[i]


def ganador(listaNombres, listaVotos):
    """
    encuentra el ganador de la votacion, es decir el
    candidato que ha recibido mayor cantidad de votos.

    Parametros: listaNombres, los nombres de los candidatos
                listaVotos, cantidad de votos recibidos por
                    cada candidato

    NOTA: si existe un empate en numero de votos, el primer
          candidato de la lista que tenga mayor numero de 
          votos es declarado ganador.           
    """
    pos = 0
    elMayor = 0
    ganador = 0
    while pos < len(listaVotos):
        if elMayor < listaVotos[pos]:
            ganador = pos
            elMayor = listaVotos[pos]
        pos = pos + 1
    print "\nel ganador es: ",listaNombres[ganador]
    print "tiene ", listaVotos[ganador], " votos"
     

#
#      Inicio del programa de votaciones
#
nombres = []
votos=[]

candidatos = pedirNumero("Cuantos candidatos son: ")

#
#  leer el nombre de cada candidatos y colocar 0 en
#  la cantidad de votos iniciales
#
i = 0
while i < candidatos:
    candidato = raw_input("ingrese el nombre del candidato: ")
    nombres.append(candidato)
    votos.append(0)
    i = i + 1

#
#    efectuar el proceso de votacion
#
seguirVotacion = True
while seguirVotacion:
    elegido = raw_input("ingrese el nombre del candidato por el que vota usted: ")
    votar (elegido, nombres, votos)
    seguir = raw_input("desea seguir con otro voto (si/no)")
    if seguir.upper() == "NO":
        seguirVotacion = False

# mostrar los votos recibidos por cada candidato:

mostrarCandidatos(nombres,votos)
    

#    seleccionar al candidato ganador
#    y mostrar su nombre y cantidad de votos
ganador(nombres,votos)

