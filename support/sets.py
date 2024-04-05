import numpy as np

version = "0.0.1"

def sets(array):
    if isinstance(array,Sets):
        return array
    return Sets(array)

class Sets:
    def __init__(self,data):
        self.__set = self.__remove_duplicates(data)
        self.__size = len(self.__set)

    def __remove_duplicates(self,data):
        new_data = []
        for x in data:
            if x not in new_data:
                new_data.append(x)
        return new_data

    def add(self,data):
        self.__set.append(data)
        self.__size += 1

    def remove(self,data):
        if is_null:
            raise ValueError("null set")
        self.__set.remove(data)
        self.__size -= 1

    @property
    def size(self):
        return self.__size

    def __repr__(self):
        if isinstance(self,Sets):
            return f"<Sets object at {hex(id(self))}, size = {self.__size}>"

    def numpy(self):
        return np.array(self.__set)

    def union(self,other):
        if not isinstance(other,Sets):
            raise TypeError(f"{type(other).__name__} isn't compatible with 'Sets'")
        new_set = self.__set[:]
        for x in other.__set:
            if x not in new_set:
                new_set.append(x)
        return Sets(new_set)

    def intersect(self,other):
        if not isinstance(other,Sets):
            raise TypeError(f"{type(other).__name__} isn't compatible with 'Sets'")
        new_set = []
        for x in self.__set:
            if x in other.__set:
                new_set.append(x)
        return Sets(new_set)
    
    def is_null(self):
        return len(self.__set) == 0
    
    def null(self):
        return Sets([])
        
    def subset(self, other):
        if not isinstance(other, Sets):
            raise TypeError(f"{type(other).__name__} isn't compatible with 'Sets'")
        for x in self.__set:
            if x not in other.__set:
                return False
        return True

    def cartesian_product(self,other):
        if not isinstance(other,Sets):
            raise TypeError(f"'{type(other).__name__}' isn't compatible with 'Sets'")
        new_set = []
        for x in self.__set:
            for y in other.__set:
                new_set.append((x,y))
        return Sets(new_set)
    
    def difference(self, other):
        if not isinstance(other, Sets):
            raise TypeError(f"{type(other).__name__} isn't compatible with 'Sets'")
        new_set = [x for x in self.__set if x not in other.__set]
        return Sets(new_set)

    def to_list(self):
        return self.__set

