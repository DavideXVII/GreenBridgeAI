import random
import string
import requests
from geopy.geocoders import Nominatim
from random import uniform
from random import randint
from faker import Faker
from datetime import datetime, timedelta

fake=Faker('it_IT')
certificati=['ISO 14001', 'FairTrade', 'Certificazione bio', 'GlobalG.A.P.', 'Carbon Trust Standard']

def genera_coordinate_italia():
    # Genera casualmente coordinate geografiche in Italia
    lat = uniform(35.5, 47.0)  # Latitudine approssimativa dell'Italia
    lon = uniform(6, 18.5)   # Longitudine approssimativa dell'Italia
    return lat, lon

def coordinate_a_indirizzo(lat, lon):
    # Utilizza Nominatim per ottenere l'indirizzo testuale dalle coordinate
    geolocator = Nominatim(user_agent="database_populator.py")
    location = geolocator.reverse((lat, lon), language='it')

    # Estrai e restituisci l'indirizzo
    address = location.address if location else "Indirizzo non disponibile"
    return address

def genera_indirizzo():
    lat, lon = genera_coordinate_italia()
    indirizzo = coordinate_a_indirizzo(lat, lon)
    return indirizzo

def is_dati_validi(agricoltore_data):
    # Aggiungi qui i tuoi criteri di validazione
    if 'Italia' in agricoltore_data['indirizzo_bottega'] and len(agricoltore_data['indirizzo_bottega']) > len('Italia') and len(agricoltore_data['nome_bottega'])<=30:
        return True
    # Aggiungi altri criteri se necessario

    return False

def genera_mediumlob():
    dati_binari_casuali = bytes(''.join(random.choices(string.ascii_letters + string.digits, k=1024)), 'utf-8')
    return dati_binari_casuali

def generate_portafoglio():
    portafoglio_data = {
        'credito': 0    #se si vuole simulare: random.randint(0, 5000)
    }

    return portafoglio_data

def generate_agricoltore():
    while True:
        agricoltore_data = {
            'nome': fake.first_name(),
            'email': fake.email(),
            'pwd': fake.password(length=16),
            'nome_bottega': fake.company(),
            'indirizzo_bottega': genera_indirizzo()
        }

        if is_dati_validi(agricoltore_data):
            return agricoltore_data

def generate_certificato():
    oggi=datetime.now()
    data_casuale=oggi + timedelta(days=random.randint(0, 365))

    certificato_data = {
        'nome': random.choice(certificati),
        'data_scadenza': data_casuale,
        'scansione': genera_mediumlob()
    }

    return certificato_data

prodotti=['Mele', 'Pere', 'Insalata', 'Melanzane', 'Zucchine', 'Peperoni', 'Pomodori', 'Cipolle', 'Mandarini', 'Limoni', 'Arance', 'Carciofi', 'Uva', 'Fragole', 'Radicchio', 'Kiwi', 'Anguria', 'Cantalupo', 'Cime di rapa']
def generate_prodotto():

    prodotto_data = {
        'nome': random.choice(prodotti),
        'origine': 'Italia',
        'prezzo_kg': random.uniform(1, 10),
        'prezzo_vendita': random.uniform(1, 10),
        'quantita_disp': random.randint(1, 1000),

    }

    return prodotto_data

num_agricoltori=200
id=1

for _ in range(num_agricoltori):
    # portafoglio_data=generate_portafoglio()
    # agricoltore_data=generate_agricoltore()
    certificato_data=generate_certificato()
    # prodotto_data=generate_prodotto()


    # print("INSERT INTO portafoglio (credito) VALUES({});".format(portafoglio_data['credito']))
    # print("""INSERT INTO agricoltore (nome, email, pwd, nome_bottega, indirizzo_bottega, id_portafoglio) VALUES (\""""+agricoltore_data['nome']+"""\", \""""+agricoltore_data['email']+"""\", \""""+agricoltore_data['pwd']+"""\", \""""+agricoltore_data['nome_bottega']+"""\", \""""+agricoltore_data['indirizzo_bottega']+"""\", {});""". format(id_portafoglio))
    print("""INSERT INTO certificato (nome, data_scadenza, scansione, id_agricoltore, id_admin) VALUES (\""""+certificato_data['nome']+"""\", \"{}\", \"{}\", {}, 1);""".format(certificato_data['data_scadenza'].strftime('%Y-%m-%d'), certificato_data['scansione'], id))
    id+=1
    # print("""INSERT INTO prodotto (nome, origine, prezzo_kg, prezzo_vendita, quantita_disp, id_agricoltore) VALUES (\""""+prodotto_data['nome']+"""\", "Italia", {}, {}, {}, @agricoltore_id);""".format(prodotto_data['prezzo_kg'], prodotto_data['prezzo_vendita'], prodotto_data['quantita_disp']))
