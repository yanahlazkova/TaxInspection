

import uuid
from faker import Faker
import json
import random
from db_binary_tree import DBBinaryTree


fake = Faker()


class Fine:
    def __init__(self, fine_type: str, amount: float, city: str):
        self.fine_type = fine_type
        self.amount = amount
        self.city = city

    def __repr__(self):
        return f'Штраф: (type={self.fine_type}, amount={self.amount}, city={self.city})'

    def to_dict(self):
        return {
            'type': self.fine_type,
            'amount': self.amount,
            'city': self.city
        }


class Person:
    def __init__(self, id_code: str, name: str, fines: list = None):
        self._id_code = id_code # uuid.uuid4()
        self.name = name
        self.fines = (fines if fines else [])

    @property
    def id_code(self):
        return str(self._id_code)

    def add_fine(self, fine: Fine):
        self.fines.append(fine)
        # print('Додано штраф')

    def __repr__(self):
        fines_repr = "\n\t\t".join(f'{num+1}. {fine}' for num, fine in enumerate(self.fines))
        return (f'Person name:\t\t{self.name}, id_code={self.id_code},\n'
                f'\tШтрафи:\n\t\t{fines_repr}')

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
        if id_code in self.people:
            print(f'Людина з id {id_code} існує в БД: {self.people[id_code]}')
        else:
            self.people[id_code] = Person(id_code, name)# person
            # print(f'Додано людину: \t{person.id_code}, {person.name}, {person.fines}')
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

    def delete_fine(self, id_code: str, fine: Fine = None, num_fine: int = None):
        person = self.people.get(id_code)
        if person and fine:
            if fine in person.fines:
                person.fines.remove(fine)
                print(f'Штраф видалено для людини з id {id_code}')
            else:
                print(f'Штраф не знайдено')
        elif person and num_fine >= 0:
            if len(person.fines) > num_fine:
                person.fines.pop(num_fine)
                print(f'Штраф видалено для людини з id {id_code}')
            else:
                print(f'Штраф не знайдено')
        else:
            print(f'id {id_code} не існує')


    def print_all(self):
        for number, (id_code, person) in enumerate(self.people.items()):
            print(number+1, person)

    def print_by_id(self, id_code):
        if id_code in self.people:
            print(self.people[id_code])
        else:
            print(f'Людина з id {id_code} не знайдена')

    def print_by_fine(self, fine_type):
        print(f'{fine_type}:\n')
        index = 0
        for person in self.people.values():
            # fines_of_type = '\n\t'.join(f'amount: {fine.amount}, city: {fine.city}' for fine in person.fines if fine.fine_type == fine_type)
            fines_of_type = '\n'.join(f'\t- {fine}' for fine in person.fines if fine.fine_type == fine_type)
            if fines_of_type:
                index += 1
                print(f'{index}. {person.name} - {person.id_code}: \n{fines_of_type}')

    def print_by_city(self, city):
        print(f'City {city}:\n')
        index = 0
        for person in self.people.values():
            fines = '\n'.join(f'\t- {fine}' for fine in person.fines if fine.city == city)
            if fines:
                index += 1
                print(f'{index}. {person.name} - {person.id_code}: \n{fines}')

    def update_person_info(self, id_code, name = None, fine = None):
        person = self.people.get(id_code)
        if person:
            if name:
                person.name = name
            if fine:
                self.add_fine_to_person(id_code, fine)

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


add_random_fines()
add_random_fines()

#
# print(db.to_dict())

# db_json = json.dumps(db.to_dict(), indent=4)
# print(db_json)

# збереження у файл БД
# with open('db.json', 'w', encoding='utf-8') as file:
#     json.dump(db.to_dict(), file, ensure_ascii=False, indent=4)

# Видалення штрафу
# візьмемо рандомний id-код з БД і видалимо рандомний штраф
# list_id_codes = [id_code for id_code in db.people]
# rand_id = random.choice(list_id_codes)
# rand_person = db.people[rand_id]
# print(rand_person)
# person_fine = rand_person.fines
# print(person_fine[0].fine_type)
# db.delete_fine(rand_id, person_fine[0])
# print(rand_person)

# 1. Повний друк бази даних;
# db.print_all()

# 2. Друк даних за конкретним кодом;
# db.print_by_id(rand_id)

# 3. Друк даних за конкретним типом штрафу;
# fine_type = random.choice(list_fine)
# db.print_by_fine(fine_type)

# 4. Друк даних за конкретним містом
# fine_city = random.choice(list_city)
# db.print_by_city(fine_city)

# 5. Додавання нової людини з інформацією про неї
# new_person = fake.name()
# print('new person', new_person)
# id_person = str(uuid.uuid4())
# print('new id:', id_person)
# db.add_person(id_person, new_person)
# db.print_by_id(id_person)

# 6. Додавання нових штрафів для вже існуючого запису;
# rand_fine_type = random.choice(list_fine)
# random_amount = random.uniform(50, 1000)
# rand_city = random.choice(list_city)
# new_fine = Fine(rand_fine_type, random_amount, rand_city)
# db.add_fine_to_person(id_person, new_fine)
# db.print_by_id(id_person)
# db.print_by_city(rand_city)

# 7. Видалення штрафу
# (за вказаним штрафом);
# db.delete_fine(id_person, new_fine)
# db.print_by_id(id_person)

# (за номером у списку)
# db.delete_fine(id_person, num_fine=0)
# db.print_by_id(id_person)

# заміна інформації про людину та її штрафи
# rand_fine_type = random.choice(list_fine)
# print(f'type fine: {rand_fine_type}')
# new_fine = Fine(rand_fine_type, 200, 'Kyiv')
# db.update_person_info(id_person, 'Den', new_fine)
# db.print_by_id(id_person)

""" binary tree """

db_binary = DBBinaryTree()

# загрузка БД з файлу
with open('db.json', 'r', encoding='utf-8') as file:
    data_json = json.load(file)

# додавання даних з файлу у БД
for id_code, data_person in data_json['people'].items():
    person = Person(id_code, data_person['name']) # data_person['fines'])
    if data_person['fines']:
        for fine in data_person['fines']:
            new_fine = Fine(fine['type'], fine['amount'], fine['city'])
            person.add_fine(new_fine)

    db_binary.add_person(person)
    # print(person)

# додавання штрафу
new_fine = Fine('Штраф за використання незареєстрованих РРО', 200, 'Kyiv')
search_person = db_binary.search_person('759e8c3b-7f36-4365-9c2f-b72aedd13dae')
db_binary.add_fine_to_person(search_person, new_fine)
print(search_person)

# видалення штрафу
db_binary.delete_fine('759e8c3b-7f36-4365-9c2f-b72aedd13dae', 1)
print(db_binary.search_person('759e8c3b-7f36-4365-9c2f-b72aedd13dae'))

pers = db_binary.search_person('86b851cb-a819-4ac8-9e81-3ec519a6515d')
print(pers)
db_binary.print_all()

