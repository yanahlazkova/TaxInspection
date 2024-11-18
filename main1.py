import json
import uuid

from person_binary_tree import PersonBT, Person
from fine_linked_list import Fine

db_persons = PersonBT()
db_persons.print_all()

# загрузка БД з файлу
with open('db.json', 'r', encoding='utf-8') as file:
    data_json = json.load(file)

for id_code, person in data_json['people'].items():
    new_person = Person(id_code, person['name'])
    db_persons.insert(id_code, new_person)
    if person['fines']:
        for fine in person['fines']:
            new_fine = Fine(fine['type'], fine['amount'], fine['city'])
            new_person.add_fine(new_fine)


# # 1. Повний друк бази даних
# db_persons.print_all()
#
# # 2. Друк даних за конкретним кодом
# print('Find by id code')
# db_persons.print_by_id_code('d7d1aa54-4bde-47a6-b108-bc85e91da0bb')
#
# # 3. Друк даних за конкретним типом штрафу
# print('Find by type of fine')
# db_persons.print_by_fine('Штраф за несплату податків')
#
# # 4. Друк даних за конкретним містом
# print('Find by city')
# db_persons.print_by_city('Dorseymouth')

# 5. Додавання нової людини з інформацією про неї
new_person = Person(str(uuid.uuid4()), 'Alex Culture')
db_persons.insert(new_person.code_id, new_person)

# 6. Додавання нових штрафів для вже існуючого запису
# new_fine = Fine('Adminfine', 2000, 'Kyiv')
# db_persons.add_fine_to_list(new_person.code_id, new_fine)
# db_persons.print_all()

# 7. Видалення штрафу
# person = db_persons.search_by_id('a84c50cb-a56f-4aec-86aa-63c7fd7beaf7')
# print(person)
# current_fine = Fine('Штраф за використання незареєстрованих РРО', 107.28915636152847,
#                     'South Lindaview')
# db_persons.delete_fine(person, current_fine)
# print(person)

# 8. заміна інформації про людину та її штрафи
person = db_persons.search_by_id('a84c50cb-a56f-4aec-86aa-63c7fd7beaf7')
print(person)
list_fines: list = person.list_fines.get_list_fines()
print(list_fines[0])
update_fine = Fine('New fine', 200, 'Kyiv')
db_persons.update(person, 'new Name')
db_persons.update(person, fine=list_fines[0], new_fine=update_fine)
