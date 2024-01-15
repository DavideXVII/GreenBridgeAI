import random
import string
import requests
from geopy.geocoders import Nominatim
from random import uniform
from random import randint
from faker import Faker
from datetime import datetime, timedelta

fake=Faker('it_IT')

def generate_cliente():
    data_attuale=datetime.now()

    cliente_data = {
            'nome': fake.first_name(),
            'cognome': fake.last_name(),
            'pwd': fake.password(length=16),
            'data_nascita': fake.date_of_birth(tzinfo=None, minimum_age=18, maximum_age=75),
            'email': fake.email()
    }

    return cliente_data

num_clienti=2

for _ in range(num_clienti):
    cliente_data=generate_cliente()

    print(f"INSERT INTO cliente (nome, cognome, pwd, data_nascita, email) VALUES ('{cliente_data['nome']}', '{cliente_data['cognome']}', '{cliente_data['pwd']}', '{cliente_data['data_nascita'].strftime('%d-%m-%Y')}', '{cliente_data['email']}');")