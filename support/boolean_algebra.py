version = "0.0.1"

def AND(X,Y):
    if X in [0,1,True,False] and Y in [0,1,True,False]:
        return X and Y
    return None

def NAND(X,Y):
    if X in [0,1,True,False] and Y in [0,1,True,False]:
        return not X and not Y
    return None

def OR(X,Y):
    if X in [0,1,True,False] and Y in [0,1,True,False]:
        return X or Y
    return None

def NOR(X,Y):
    if X in [0,1,True,False] and Y in [0,1,True,False]:
        return not X or not Y
    return None

def XOR(X,Y):
    if X in [0,1,True,False] and Y in [0,1,True,False]:
        return X ^ Y
    return None

def XNOR(X,Y):
    if X in [0,1,True,False] and Y in [0,1,True,False]:
        return not (X ^ Y)
    
def NOT(X):
    if X in [0,1,True,False]:
        return not X
    return None

def Buffer(X):
    if X in [0,1,True,False]:
        return X
    return None
