from .char import char

version = "0.0.1"

def string(text):
    return String(text)

class String:
    def __init__(self,text):
        self.__text = text
        self.__length = len(self)

    @property
    def size(self):
        return self.__length

    def __repr__(self):
        return self.__text

    def __len__(self):
        return len(list(self.__text))

    def __getitem__(self,index):
        if not 0 <= index < len(self):
            raise IndexError(f"index out of range! from {0} to {len(self) - 1}")
        str_list = list(self.__text)
        return char(str_list[index])

    def __setitem__(self,index,text):
        if not 0 <= index < len(self):
            raise IndexError(f"index out of range! from {0} to {len(self) - 1}")
        str_list = list(self.__text)
        str_list[index] = text
        self.__text = ""
        for char in str_list:
            self.__text += char

    def __add__(self,other):
        if isinstance(other,int):
            str_list = list(self.__text)
            result = ""
            for x in str_list:
                result += chr(ord(x) + 1)
            return String(result)
        elif isinstance(other,str):
            result = self.__text + other
            return String(result)
        elif isinstance(other,String):
            result = self.__text + other.__text
            return String(result)
        raise TypeError(f"'{type(self).__name__}' type isn't compatible with '{type(other).__name__}' type!")

    def __sub__(self,other):
        if isinstance(other,int):
            str_list = list(self.__text)
            result = ""
            for x in str_list:
                result += chr(ord(x) - 1)
            return String(result)
        raise TypeError(f"'{type(self).__name__}' type isn't compatible with '{type(other).__name__}' type!")

    def lower_case(self):
        str_list = list(self.__text)
        self.__text = ""
        for char in str_list:
            ascii_value = ord(char)
            if 65 <= ascii_value <= 90:
                self.__text += chr(ascii_value + 32)
            else:
                self.__text += char
        return String(self.__text)
    
    def upper_case(self):
        str_list = list(self.__text)
        self.__text = ""
        for char in str_list:
            ascii_value = ord(char)
            if 97 <= ascii_value <= 122:
                self.__text += chr(ascii_value - 32)
            else:
                self.__text += char
        return String(self.__text)

    def substring(self,start,end,endpoint = False):
        if not 0 <= start < len(self) or not 0 <= end <= len(self) and start < end:
            raise ValueError(f"start or end index out of index!")
        if endpoint:
            end += 1
        new_string = ""
        for x in range(start,end):
            new_string += self.__text[x]
        return String(new_string)

    def update(self,text):
        self.__text = text
        self.__length = len(self)

    def at(self,index):
        if not 0 <= index < len(self):
            raise IndexError(f"index out of range! from {0} to {len(self) - 1}")
        str_list = list(self.__text)
        return char(str_list[index])

