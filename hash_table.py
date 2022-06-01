class HashTable:
    def __init__(self, max_size=4096):
        self.data_list = [None] * max_size
    
    def get_valid_index(self, key):
        # Use Python's in-built `hash` function and implement linear probing
        return hash(key) % len(self.data_list) # change this
        
    def __getitem__(self, key):
        # Implement the logic for "find" here
        idx = self.get_valid_index(key)
    
        # 2. Retrieve the data stored at the index
        kv = self.data_list[idx]
        
        # 3. Return the value if found, else return None
        return None if kv is None else kv[1] # change this
    
    def __setitem__(self, key, value):
        # Implement the logic for "insert/update" here
        idx = self.get_valid_index(key)
        
        # 2. Store the key-value pair at the right index
        self.data_list[idx] = key, value # change this
    
    def __iter__(self):
        return (x for x in self.data_list if x is not None)
    
    def __len__(self):
        return len([x for x in self])
    
    def __repr__(self):
        from textwrap import indent
        pairs = [indent("{} : {}".format(repr(kv[0]), repr(kv[1])), '  ') for kv in self]
        return "{\n" + "{}".format(',\n'.join(pairs)) + "\n}"
    
    def __str__(self):
        return repr(self)

x = HashTable()
x[2] = 3
print(x)