version = "0.0.2"

class char:
    def __init__(self,char):
        if not len(list(char)) == 1:
            raise ValueError("given input should be character not string!")
        self.__char = char

    def __repr__(self):
        return self.__char

    def __add__(self,scaler):
        return chr(ord(self.__char) + scaler)
    
    def __sub__(self,scaler):
        return chr(ord(self.__char) - scaler)

    def lower_case(self):
        ascii_value = ord(self.__char)
        if 65 <= ascii_value <= 90:
            return char(chr(ascii_value + 32))
        return self

    def upper_case(self):
        ascii_value = ord(self.__char)
        if 97 <= ascii_value <= 122:
            return char(chr(ascii_value - 32))
        return self

