class HashTable:
    def __init__(self,size=7):
        self.data_map = [None] * size

    def _hash(self,key):
        my_hash = 0
        for letter in key:
            my_hash = (my_hash + ord(letter) * 23) % len(self.data_map)
        return my_hash
    
    def print_table(self):
        for i, val in enumerate(self.data_map):
            print(i,": ",val)
    
    def set_item(self,key,value):
        index = self._hash(key)
        if self.data_map[index] == None:
            self.data_map[index] = []
        self.data_map[index].append([key,value])


    def get_item(self,key):
        index = self._hash(key)
        if self.data_map[index]!=None:
            for i in range(len(self.data_map[index])):
                if self.data_map[index][i][0]==key:
                    return self.data_map[index][i][1]
        return None

my_hash_table = HashTable()
my_hash_table.set_item('nails',1000)
my_hash_table.set_item('pen',1200)
my_hash_table.set_item('tin',2333)
my_hash_table.set_item('hammer',9012)
my_hash_table.set_item('fire',5433)
# my_hash_table.print_table()
print(my_hash_table.get_item('fire'))