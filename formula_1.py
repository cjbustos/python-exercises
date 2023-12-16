import json
import pickle as pkl

# function example
def what_type_it_is(sub_info):
    if isinstance(sub_info, str):
        print(f"{sub_info} is a string value!")
    elif isinstance(sub_info, (int, float, complex)):
        print(f"{sub_info} is a number value!")
    elif isinstance(sub_info, bool):
        print(f"{sub_info} is a boolean value!")
    elif isinstance(sub_info, (list, tuple)):
        for index, element in enumerate(sub_info):
            print(f"In {index} found {element} ")
#    return print(type(sub_info))
    return print(sub_info)

# guarda
def save_data(out_of_data):
    with open("file_txt.txt", mode="w") as io_object:
        io_object.write(str(out_of_data))

# lee
def read_data():
    with open("file_txt.txt", mode="r") as io_object:
        data_from_file = io_object.read()
    return data_from_file

# guarda en json
def save_data_to_json(out_of_data):
    with open("file_json.json", mode="w") as io_object:
        json.dump(out_of_data, io_object, indent=4)

# guarda en json generico
def save_to_json(file_name, mode="w", **dic_type):
    with open(f"{file_name}.json", mode=mode, encoding='utf-8') as obj_json:
        json.dump(dic_type, obj_json, ensure_ascii=False, indent=4)

def read_from_json():
    with open("file_json.json", mode="r") as io_object:
        employee = json.load(io_object)
    return employee

# guarda en pkl - binario
def save_data_to_pkl(out_of_data):
    with open("file_pkl.pkl", mode="wb") as io_object:
        pkl.dump(out_of_data, io_object)

# lee en pkl - binario
def read_from_pkl():
    with open("file_pkl.pkl", mode="rb") as io_object:
        employee = pkl.load(io_object)
    return employee

matriz = [
            [1,2,"tres", True],
            [5, 6, "siete", False],
            [[1, 2, 3, 4, 5], "once"]
]

for data in matriz:
    for sub_data in data:
        what_type_it_is(sub_data)

save_data(matriz)
print(read_data())

print("#"*100)

pilotos = ["Yuki Tsunoda",
            "Sergio Pérez",
            "Carlos Sainz",
            "Max Verstappen",
            "Lando Norris",
            "George Russell",
            "Esteban Ocon",
            "Charles Leclerc",
            "Yuki Tsunoda",
            "Oscar Piastri",
            "Fernando Alonso",
            "Lewis Hamilton",
            "Pierre Gasly",
            "Lance Stroll",
            "Nyck de Vries",
            "Kevin Magnussen",
            "Valtteri Bottas",
            "Guanyu Zhou",
            "Alexander Albon",
            "Logan Sargeant",
            "Nico Hulkenberg"]

aux =  "tiempo_Total en pista", "vuelta Mas Rapida", "total de vueltas"

tiempos = [ [3610, 115, 30],
            [6150, 115, 52],
            [6153, 116, 52],
            [6140, 116, 52],
            [6141, 116, 52],
            [6160, 115, 52],
            [6165, 114, 52],
            [6172, 112, 52],
            [6175, 115, 52],
            [6177, 114, 52],
            [4720, 111, 40],
            [6111, 114, 52],
            [ 700, 119,  5],
            [6201, 118, 52],
            [6133, 114, 52],
            [1205, 118, 10],
            [6272, 122, 52],
            [6375, 135, 52],
            [6475, 144, 52],
            [5720, 151, 30],
            [6130,  11, 52] ]


pilotos_escuderias=["George Russell","MERCEDES",
                    "Lewis Hamilton","MERCEDES",
                    "Pierre Gasly","ALPINE",
                    "Esteban Ocon","ALPINE",
                    "Nico Hulkenberg","HAAS",
                    "Kevin Magnussen","HAAS",
                    "Oscar Piastri","MCLAREN",
                    "Lando Norris","MCLAREN",
                    "Sergio Pérez","RED BULL",
                    "Max Verstappen","RED BULL",
                    "Fernando Alonso","ASTON MARTIN",
                    "Lance Stroll","ASTON MARTIN",
                    "Nyck de Vries","ALPHATAURI",
                    "Yuki Tsunoda","ALPHATAURI",
                    "Carlos Sainz","FERRARI",
                    "Charles Leclerc","FERRARI",
                    "Valtteri Bottas","ALFA ROMEO",
                    "Guanyu Zhou","ALFA ROMEO",
                    "Alexander Albon","WILLIAMS",
                    "Logan Sargeant","WILLIAMS"]

dic_tiempos = {}

# el zip() toma un dato de una lista y otro dato de la otra lista
for index, [cada_piloto, cada_valor] in enumerate (zip(pilotos, tiempos)):
    print (f"El dato está ubicado en el index: {index}")
    print (f"El nombre del piloto es: {cada_piloto}")
    print (f"Las estadísticas del piloto son: {cada_valor}")
    
print("#"*100)

# se puede unificar el dato al principio para después desempaquetar
for index, data in enumerate (zip(pilotos, tiempos)):
    [cada_piloto, cada_valor] = data
#    dic_tiempos[cada_piloto] = cada_valor
    dic_tiempos[cada_piloto] = {}
    for nombre_campo, cada_valor in zip(aux, cada_valor):
        dic_tiempos[cada_piloto][nombre_campo] = cada_valor
#    print (f"El dato está ubicado en el index: {index}")
#    print (f"El nombre del piloto es: {cada_piloto}")
#    print (f"Las estadísticas del piloto son: {dic_tiempos[cada_piloto]}")

dic_escuderias = {}

for piloto, escuderia in zip(pilotos_escuderias[0:len(pilotos_escuderias):2], pilotos_escuderias[1:len(pilotos_escuderias):2]):
    dic_escuderias[piloto] = escuderia

print(dic_escuderias)

"""        
for piloto in pilotos_escuderias[0:len(pilotos_escuderias):2]:
    print(f"El piloto es: {piloto} ")

for escuderia in pilotos_escuderias[1:len(pilotos_escuderias):2]:
    print(f"La escudería es: {escuderia} ")
"""

totales_vueltas=[]

for piloto in dic_tiempos.keys():
    totales_vueltas.append(dic_tiempos[piloto]['total de vueltas'])   
#print(max(totales_vueltas))

max_vueltas=max([dic_tiempos[piloto]['total de vueltas'] for piloto in dic_tiempos.keys()])
max_tiempo_pista=max([dic_tiempos[piloto]['tiempo_Total en pista'] for piloto in dic_tiempos.keys()])


print(max_vueltas)
print(max_tiempo_pista)

for piloto in dic_tiempos.keys():
    if dic_tiempos[piloto]['tiempo_Total en pista'] < max_tiempo_pista and dic_tiempos[piloto]['total de vueltas'] == max_vueltas:
            ganador = piloto
            ganador_valores = dic_tiempos[piloto]
            max_tiempo_pista = dic_tiempos[piloto]['tiempo_Total en pista']
            
print(f'El piloto ganador es {ganador}\n con {ganador_valores}')

#tener en cuenta que con dos asteriscos estoy pasando como argumento un diccionario, con un asterisco es una tupla
save_to_json("test",mode="w", **dic_tiempos)
