from fine_linked_list import FineLinkedList


class Person:
    def __init__(self, code_id: str, name: str):
        self.name = name
        self.code_id = code_id
        self.list_fine = FineLinkedList()

    def add_fine(self, fine):
        self.list_fine.append(fine)
    
    def __repr__(self):
        print(f'\n{self.name}\tid: {self.code_id}\n')
        print(f'\tFines:')
        return f'\t{self.list_fine.print_list_fines()}'

    def search_by_type_fine(self, type_fine: str):
        return self.list_fine.search_by_type_fine(type_fine)

    def search_by_city(self, city: str):
        return self.list_fine.search_by_city(city)

    def delete_fine(self, fine):
        result = self.list_fine.delete_fine(fine)
        return result


class PersonNode:
    def __init__(self, key, data):
        self.key = key
        self.data = data
        self.left = None
        self.right = None


class PersonBT:
    def __init__(self):
        self.root = None

    def insert(self, key, data):
        if not self.root:
            self.root = PersonNode(key, data)
        else:
            self.__insert(self.root, key, data)

    def __insert(self, node, key, data):
        if key < node.key:
            if node.left:
                self.__insert(node.left, key, data)
            else:
                node.left = PersonNode(key, data)
        elif key > node.key:
            if node.right:
                self.__insert(node.right, key, data)
            else:
                node.right = PersonNode(key, data)

    def search_by_id(self, key):
        return self.__search_by_id(self.root, key)

    def __search_by_id(self, node, key):
        if not node:
            return None
        if key == node.key:
            return node.data
        elif key < node.key:
            return self.__search_by_id(node.left, key)
        else:
            return self.__search_by_id(node.right, key)

    def search_by_type_fine(self, node, key):
        if not node:
            return None
        return node.data.search_by_type_fine(key)

    def search_by_city(self, node, key):
        if not node:
            return None
        return node.data.search_by_city(key)

    def delete_fine(self, node, key):
        result = node.delete_fine(key)
        print()
        if result:
            print(f'Fine {key} DELETED...')
        else:
            print(f'fine {key} don\'t found...')

    def print_all(self, node=None):
        if node is None:
            node = self.root
        if node is not None:
            print(node.data)
            if node.left or node.right:
                if node.left:
                    self.print_all(node.left)
                if node.right:
                    self.print_all(node.right)
        else:
            print("List of persons is EMPTY")

    def print_by_id_code(self, key):
        search_node = self.search_by_id(key)
        if search_node:
            print(search_node)
        else:
            print('Don\'t found!')

    def print_by_fine(self, key):
        return self.__print_by_fine(self.root, key)

    def __print_by_fine(self, node, key):
        if not node:
            print('List is EMPTY!')
        if node:
            search_node = self.search_by_type_fine(node, key)
            if search_node:
                print(node.data.name, node.data.code_id)
                res = '\n'.join(f'\t{index+1}. {fine}' for index, fine in enumerate(search_node))
                print(res)
            if node.left or node.right:
                if node.left:
                    self.__print_by_city(node.left, key)
                if node.right:
                    self.__print_by_city(node.right, key)

    def print_by_city(self, key):
        return self.__print_by_city(self.root, key)

    def __print_by_city(self, node, key):
        if not node:
            print('List is EMPTY!')
        if node:
            search_node = self.search_by_city(node, key)
            if search_node:
                print(node.data.name, node.data.code_id)
                res = '\n'.join(f'\t{index+1}. {fine}' for index, fine in enumerate(search_node))
                print(res)
            if node.left or node.right:
                if node.left:
                    self.__print_by_fine(node.left, key)
                if node.right:
                    self.__print_by_fine(node.right, key)

    def update(self, code_id, new_name=None, fine=None, new_fine=None):
        found_node = self.search_by_id(code_id)
        if new_name:
            found_node.name = new_name
        if new_fine:
            found_fine = found_node.list_fine.update(fine, new_fine)
        print('update...', found_node)


