from binary_tree import BinaryTree


class DBBinaryTree:
    def __init__(self):
        self.person = BinaryTree()

    def search_person(self, person_id):
        """ пошук людини по id """
        person = self.person.search(person_id)
        return person

    def add_person(self, person):
        """ додавання нової людини """
        search_person = self.person.search(person.id_code)
        if search_person:
            print(f'Людина з id {person.id_code} існує в БД: {search_person}')
        else:
            self.person.insert(person.id_code, person)

    def add_fine_to_person(self, person, fine):
        """ додавання штрафу """
        search_person = self.person.search(person.id_code)
        if search_person:
            search_person.add_fine(fine)
        else:
            print(f'Людина з кодом id {person.id_code} не знайдена')

    def delete_fine(self, person_id, index_fine):
        search_person = self.search_person(person_id)
        if search_person and index_fine < len(search_person.fines):
            search_person.fines.pop(index_fine)

        else:
            print(f'id {person_id} не існує або штраф не знайдено')

    def print_all(self):
        self.person.print_all()