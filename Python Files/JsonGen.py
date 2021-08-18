import json
import csv

#Write
data = {}

data['Salida 1'] = []
data['Salida 2'] = []
data['Salida 3'] = []
data['Salida 4'] = []
data['Salida 5'] = []
data['VirtualPB 1'] = []
data['VirtualPB 2'] = []
data['VirtualPB 3'] = []
data['INT 1'] = []
data['INT 2'] = []

data['CDTC 301'] = []
data['CDTC 303'] = []
data['CDTC 305-A'] = []
data['CDTC 305-F'] = []
data['CDTC 306'] = []
data['CDTC 307'] = []
data['CDTC 308'] = []
data['CDTC Admisiones'] = []
data['VirtualP2 1'] = []
data['VirtualP2 2'] = []
data['VirtualP2 3'] = []
data['VirtualP2 4'] = []


data['Salida 1'].append({
    'id': 18,
    'coordenadas': (5, 9),
    'usuarios': 25,
    'vecinos': [('INT 1', 16, 0)],
    'activado': True,
    'tipo': 'salida',
    'equivalente': '',
    'piso': 0
})

data['Salida 2'].append({
    'id': 19,
    'coordenadas': (5, 49),
    'usuarios': 0,
    'vecinos': [('VirtualPB 1', 13, 0), ('INT 2', 17, 0)],
    'activado': False,
    'tipo': 'salida',
    'equivalente': '',
    'piso': 0
})

data['Salida 3'].append({
    'id': 20,
    'coordenadas': (40, 49),
    'usuarios': 25,
    'vecinos': [('INT 2', 17, 0)],
    'activado': True,
    'tipo': 'salida',
    'equivalente': '',
    'piso': 0
})

data['Salida 4'].append({
    'id': 21,
    'coordenadas': (46, 26),
    'usuarios': 0,
    'vecinos': [('INT 1', 16, 0), ('INT 2', 17, 0)],
    'activado': True,
    'tipo': 'salida',
    'equivalente': '',
    'piso': 0
})

data['Salida 5'].append({
    'id': 22,
    'coordenadas': (40, 9),
    'usuarios': 0,
    'vecinos': [('VirtualPB 3', 15, 0)],
    'activado': True,
    'tipo': 'salidaPredeterminada',
    'equivalente': '',
    'piso': 0
})

data['VirtualPB 1'].append({
    'id': 13,
    'coordenadas': (17, 46),
    'usuarios': 0,
    'vecinos': [('VirtualP2 1', 9, 0), ('INT 2', 17, 0), ('Salida 2', 19, 0)],
    'activado': True,
    'tipo': 'convencional',
    'equivalente': '',
    'piso': 0
})

data['VirtualPB 2'].append({
    'id': 14,
    'coordenadas': (24, 25),
    'usuarios': 0,
    'vecinos': [('VirtualP2 2', 10, 25), ('Salida 4', 21, 0), ('INT 2', 17, 0), ('VirtualPB 3', 15, 0)],
    'activado': True,
    'tipo': 'convencional',
    'equivalente': '',
    'piso': 0
})

data['VirtualPB 3'].append({
    'id': 15,
    'coordenadas': (29, 13),
    'usuarios': 0,
    'vecinos': [('VirtualP2 3', 11, 0), ('Salida 5', 22, 0), ('Salida 4', 21, 0), ('INT 2', 17, 0), ('VirtualPB 3', 15, 0)],
    'activado': True,
    'tipo': 'convencional',
    'equivalente': '',
    'piso': 0
})

data['INT 1'].append({
    'id': 16,
    'coordenadas': (21, 16),
    'usuarios': 0,
    'vecinos': [('VirtualPB 3', 15, 0), ('VirtualPB 2', 14, 0), ('Salida 1', 18, 25)],
    'activado': False,
    'tipo': 'convencional',
    'equivalente': '',
    'piso': 0
})

data['INT 2'].append({
    'id': 17,
    'coordenadas': (23, 45),
    'usuarios': 0,
    'vecinos': [('VirtualPB 2', 14, 0), ('VirtualPB 1', 13, 0), ('Salida 3', 20, 25)],
    'activado': True,
    'tipo': 'convencional',
    'equivalente': '',
    'piso': 0
})

data['CDTC 301'].append({
    'id': 1,
    'coordenadas': (36, 16),
    'usuarios': 1,
    'vecinos': [('CDTC 303', 2, 1), ('CDTC Admisiones', 8, 1), ('VirtualP2 2', 10, 25), ('VirtualP2 3', 11, 0)],
    'activado': True,
    'tipo': 'convencional',
    'equivalente': '',
    'piso': 2
})

data['CDTC 303'].append({
    'id': 2,
    'coordenadas': (18, 4),
    'usuarios': 1,
    'vecinos': [('VirtualP2 4', 12, 0), ('CDTC 301', 1, 1), ('VirtualP2 2', 10, 25)],
    'activado': True,
    'tipo': 'convencional',
    'equivalente': '',
    'piso': 2
})

data['CDTC 305-A'].append({
    'id': 3,
    'coordenadas': (3, 14),
    'usuarios': 1,
    'vecinos': [('VirtualP2 4', 12, 0), ('CDTC 305-F', 4, 1)],
    'activado': True,
    'tipo': 'convencional',
    'equivalente': '',
    'piso': 2
})

data['CDTC 305-F'].append({
    'id': 4,
    'coordenadas': (3, 44),
    'usuarios': 1,
    'vecinos': [('CDTC 305-A', 3, 1), ('VirtualP2 4', 12, 0)],
    'activado': True,
    'tipo': 'convencional',
    'equivalente': '',
    'piso': 2
})

data['CDTC 306'].append({
    'id': 5,
    'coordenadas': (12, 53),
    'usuarios': 1,
    'vecinos': [('VirtualP2 4', 12, 0), ('VirtualP2 1', 9, 0), ('CDTC 307', 6, 1)],
    'activado': True,
    'tipo': 'convencional',
    'equivalente': '',
    'piso': 2
})

data['CDTC 307'].append({
    'id': 6,
    'coordenadas': (19, 53),
    'usuarios': 1,
    'vecinos': [('CDTC 306', 5, 1), ('CDTC 308', 7, 1)],
    'activado': True,
    'tipo': 'convencional',
    'equivalente': '',
    'piso': 2
})

data['CDTC 308'].append({
    'id': 7,
    'coordenadas': (28, 53),
    'usuarios': 1,
    'vecinos': [('CDTC 307', 6, 1), ('CDTC Admisiones', 8, 1)],
    'activado': True,
    'tipo': 'convencional',
    'equivalente': '',
    'piso': 2
})

data['CDTC Admisiones'].append({
    'id': 8,
    'coordenadas': (34, 39),
    'usuarios': 1,
    'vecinos': [('CDTC 308', 7, 1), ('CDTC 301', 1, 1), ('VirtualP2 3', 11, 0)],
    'activado': True,
    'tipo': 'convencional',
    'equivalente': '',
    'piso': 2
})

data['VirtualP2 1'].append({
    'id': 9,
    'coordenadas': (16, 33),
    'usuarios': 0,
    'vecinos': [('CDTC 306', 5, 1), ('VirtualP2 4', 12, 0)],
    'activado': True,
    'tipo': 'escalera',
    'equivalente': (17, 46),
    'piso': 2
})

data['VirtualP2 2'].append({
    'id': 10,
    'coordenadas': (24, 25),
    'usuarios': 25,
    'vecinos': [('VirtualP2 3', 11, 0),('CDTC Admisiones', 8, 1),('CDTC 301', 1, 1),('VirtualP2 4', 12, 0),('CDTC 303', 2, 1)],
    'activado': True,
    'tipo': 'escalera',
    'equivalente': (24, 26),
    'piso': 2
})

data['VirtualP2 3'].append({
    'id': 11,
    'coordenadas': (29, 24),
    'usuarios': 0,
    'vecinos': [('CDTC 301', 1, 1),('CDTC Admisiones', 8, 1)],
    'activado': True,
    'tipo': 'escalera',
    'equivalente': (29, 13),
    'piso': 2
})

data['VirtualP2 4'].append({
    'id': 12,
    'coordenadas': (14, 29),
    'usuarios': 0,
    'vecinos': [('CDTC 305-F', 4, 1), ('CDTC 303', 2, 1),('CDTC 306', 5, 1),('CDTC 305-A', 3, 1),('VirtualP2 2', 10, 25),('VirtualP2 1', 9, 0)],
    'activado': True,
    'tipo': 'convencional',
    'equivalente': (29, 13),
    'piso': 2
})

#Apertura de mapas
with open('PBenceldas.csv', newline='') as f:
    reader = csv.reader(f)
    pb = list(reader)

with open('P1enceldas.csv', newline='') as f:
    reader = csv.reader(f)
    p1 = list(reader)

with open('P2enceldas.csv', newline='') as f:
    reader = csv.reader(f)
    p2 = list(reader)

maps = {}

maps['Planta Baja'] = []
maps['Primer Piso'] = []
maps['Segundo Piso'] = []

maps['Planta Baja'].append({
    'disposicion': pb
})

maps['Primer Piso'].append({
    'disposicion': p1
})

maps['Segundo Piso'].append({
    'disposicion': p2
})

with open('data.txt', 'w') as outfile:
    json.dump(data, outfile)

with open('mapa.txt', 'w') as outfile:
    json.dump(maps, outfile)




