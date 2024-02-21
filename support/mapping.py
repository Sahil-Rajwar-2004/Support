class Mapping:
    def __init__(self,key_type,value_type):
        self.__key_type = key_type
        self.__value_type = value_type
        self.__array = []
        self.__current_index = 0
        self.__length = 0

    def __repr__(self):
        return str(self.__array)

    def __getitem__(self,key):
        if type(key) != self.__key_type:
            print("key type doesn't match")
            return
        for index,item in enumerate(self.__array):
            if item[0] == key:
                return item
        return f"{key} not found in linked list!"

    def __len__(self):
        return self.__length
    
    def __iter__(self):
        self.__current_index = 0
        return self

    def __next__(self):
        if self.__current_index < self.__length:
            result = self.__array[self.__current_index]
            self.__current_index += 1
            return result
        else:
            raise StopIteration
        
    def __getitem__(self,key):
        if type(key) != self.__key_type:
            print("key type doesn't match")
            return
        
        for item in self.__array:
            if item[0] == key:
                return item[1]
        raise KeyError(f"key '{key}' not found in the mapping")

    def show(self):
        print(self.__array)
        return

    def add(self,key,value):
        if type(key) != self.__key_type or type(value) != self.__value_type:
            print(f"type mismatch! Desired data types for keys and values are '{self.__key_type.__name__}' and '{self.__value_type.__name__}' respectively.")
            return

        for _,v in enumerate(self.__array):
            if v[0] == key:
                v[1] = value
                return
        self.__array.append([key,value])
        self.__length += 1

    def remove_by_key(self,key):
        if type(key) != self.__key_type:
            print("key type doesn't match")
            return
        
        for index,item in enumerate(self.__array):
            if item[0] == key:
                del self.__array[index]
                self.__length -= 1
                return
    
    def remove_by_value(self,value):
        if type(value) != self.__value_type:
            print("key type doesn't match")
            return
        
        for index,item in enumerate(self.__array):
            if item[1] == value:
                del self.__array[index]
                self.__length -= 1

    def remove_by_index(self,index):
        if 0 <= index < self.__length:
            del self.__array[index]
            self.__length -= 1
            return
        
        print("index out of bound")
        return

    def get_value_by_key(self,key):
        if type(key) != self.__key_type:
            print("key type doesn't match")
            return
        
        answer = []
        for index,item in enumerate(self.__array):
            if item[0] == key:
                answer.append(self.__array[index][1])
        return tuple(answer)
    
    def get_key_by_value(self,value):
        if type(value) != self.__value_type:
            print("value type doesn't match")
            return
        
        answer = []
        for index,item in enumerate(self.__array):
            if item[1] == value:
                answer.append(self.__array[index][0])
        return tuple(answer)
    
    def search_by_key(self,key):
        if type(key) != self.__key_type:
            print("key type doesn't match")
            return
        answer = []
        for index,item in enumerate(self.__array):
            if item[0] == key:
                answer.append(self.__array[index])
        return tuple(answer)
    
    def search_by_value(self,value):
        if type(value) != self.__value_type:
            print("value type doesn't match")
            return
        
        answer = []
        for index,item in enumerate(self.__array):
            if item[1] == value:
                answer.append(self.__array[index])
        return tuple(answer)

    def size(self):
        return self.__length
