class Fine:
    def __init__(self, fine: str, amount, city):
        self.fine = fine
        self.amount = amount
        self.city = city

    def __eq__(self, other):
        return other.fine == self.fine and other.amount == self.amount and other.city == self.city

    def __repr__(self):
        return f'{self.fine}: amount {self.amount}, city: {self.city}'


class FineNode:
    def __init__(self, data: Fine):
        self.data = data
        self.next = None


class FineLinkedList:
    def __init__(self):
        self.head = None

    def append(self, data: Fine):
        new_node = FineNode(data)
        if not self.head:
            self.head = new_node
            return
        last_node = self.head
        while last_node.next:
            last_node = last_node.next
        last_node.next = new_node

    def find(self, fine):
        current_node = self.head
        while current_node:
            if current_node.data == fine:
                return current_node
            current_node = current_node.next
        return None

    def print_list_fines(self):
        if not self.head:
            print('List of fines is EMPTY!')
        else:
            current_node = self.head
            index = 0
            while current_node:
                index += 1
                print(f'{index}. {current_node.data}')
                current_node = current_node.next
            return ""

    def search_by_type_fine(self, key):
        current = self.head
        results = []
        while current:
            if current.data.fine == key:
                results.append(current.data)
            current = current.next
        return results

    def search_by_city(self, key):
        current = self.head
        results = []
        while current:
            if current.data.city == key:
                results.append(current.data)
            current = current.next
        return results

    def delete_fine(self, fine):
        if not self.head:
            return False
        current_node = self.head
        if current_node.data == fine:
            self.head = current_node.next
            return True

        while current_node.next:
            if current_node.next == fine:
                found_node = current_node.next
                next_after_found = found_node.next
                current_node.next = next_after_found
                return True
        return False

    def get_list_fines(self):
        list_fines = []
        current_node = self.head
        while current_node:
            list_fines.append(current_node.data)
            current_node = current_node.next
        return list_fines

    def update(self, node, new_node):
        found_node = self.find(node)
        if found_node:
            found_node.data.fine = new_node.fine
            found_node.data.amount = new_node.amount
            found_node.data.city = new_node.city
        else:
            print('Штраф не найден!!!')
