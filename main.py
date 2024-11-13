

import uuid
from faker import Faker
import json
import random
# from dataclasses import dataclass, asdict, field


fake = Faker()


class Fine:
    def __init__(self, fine_type: str, amount: float, city: str):
        self.fine_type = fine_type
        self.amount = amount
        self.city = city

    def __repr__(self):
        return f'\t\nFine(type={self.fine_type}, amount={self.amount}, city={self.city})\n'

    def to_dict(self):
        return {
            'type': self.fine_type,
            'amount': self.amount,
            'city': self.city
        }


class Person:
    def __init__(self, id_code: str, name: str):
        self._id_code = id_code # uuid.uuid4()
        self.name = name
        self.fines = []

    @property
    def id_code(self):
        return str(self._id_code)

    def add_fine(self, fine: Fine):
        self.fines.append(fine)
        print('Додано штраф')

    def __repr__(self):
        return f'Person (id_code={self.id_code}, name={self.name}, fines={self.fines})'

    def to_dict(self):
        return {
            'id_code': self.id_code,
            'name': self.name,
            'fines': [fine.to_dict() for fine in self.fines]
        }


class DataBase:
    def __init__(self):
        self.people = {}
        self.fines = []

    def add_person(self, id_code, name: str): # person: Person):
        if person.id_code in self.people:
            print(f'Людина з id {person.id_code} існує в БД: {self.people[person.id_code]}')
        else:
            self.people[person.id_code] = Person(id_code, name)# person
            print(f'Додано людину: \t{person.id_code}, {person.name}, {person.fines}')
            # y = json.dumps(person.to_dict())
            # print('Сериализованный объект Person в JSON:', y)

    def add_fine(self, fine_type):
        """ add fines to database """
        if fine_type in self.fines:
            print(f'Штраф з типом {fine_type} вже існує')
        else:
            self.fines.append(fine_type)

    def add_fine_to_person(self, id_code: str, fine: Fine):
        if id_code in self.people:
            self.people[id_code].add_fine(fine)
        else:
            print(f'Людина з кодом id {id_code} не знайдена')

    def delete_fine(self, id_code: str, fine: Fine):
        # if id_code in self.people:
        #     if fine in self.people[id_code].fines:
        #         pass
        person = self.people.get(id_code)
        if person and fine in person.fines:
            person.fines.remove(fine)
            print(f'Штраф видалено для людини з id {id_code}')

    def to_dict(self):
        """Преобразует объект базы данных в словарь для записи в JSON"""
        # x = list([str(index), person.to_dict()] for index, person in self.people.items())
        # print('x = ', x)
        return {
            'people': {
                id_code: person.to_dict() for id_code, person in self.people.items()
            }
        }


# x_json = json.dumps(x, indent=4)
# with open('fines1.json', 'w') as file:
#     file.write(x_json)

db = DataBase()

# f1 = Fine('main', 200, 'City')
# f2 = Fine('base', 300, 'City')
# f3 = Fine('fine1', 100, 'City')
# p1 = Person(str(uuid.uuid4()), "Alex")
# p2 = Person(str(uuid.uuid4()), 'Deny')
# p3 = Person(str(uuid.uuid4()), 'Filip')

for _ in range(20):
    person = Person(str(uuid.uuid4()), fake.name())
    db.add_person(uuid.uuid4(), fake.name())# (person)

with open('fines1.json') as file:
    fines_dict = json.load(file)

list_fine = list(fine_type['type'] for fine_type in fines_dict['tax_fines'])
# print(f'Список типів штрафів:', list_fine)
list_city = list(city for city in fines_dict['city'])
# print(list_city)

# додамо у БД штрафи

def add_random_fines():
    # додамо кожній людині у базі штрафи
    for people in db.people:
        fine_type = random.choice(list_fine) # randint(0, len(list_fine) - 1)
        random_number_amount = random.uniform(50, 1000)
        fine_city = random.choice(list_city) # (0, len(list_city) - 1)
        fine = Fine(fine_type, random_number_amount, fine_city)
        db.people[people].add_fine(fine)
        # print(db.people[people].fines)


# list_city_json = json.dumps(list_city, indent=4)
# print(list_city)
# print(list_city_json)


# add_random_fines()
# add_random_fines()

# загрузка БД з файлу
with open('db.json', 'r', encoding='utf-8') as file:
    data_json = json.load(file)

print(data_json)

print(db.to_dict())

db_json = json.dumps(db.to_dict())
print(db_json)

# збереження у файл БД
# with open('db.json', 'w', encoding='utf-8') as file:
#     json.dump(db.to_dict(), file, ensure_ascii=False, indent=4)

