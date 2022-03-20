matriz = [[0,0,0,1,0,0,0,0], 
          [0,1,0,1,0,1,1,0], 
          [0,1,0,0,0,1,1,0], 
          [1,1,1,1,0,0,0,0], 
          [0,1,0,1,1,0,1,0]]

class State:
    def __init__(self, matriz, li_a, li_o, co_a, co_o):
        self.m = matriz
        self.l_a = li_a
        self.c_a = co_a
        self.l_o = li_o
        self.c_o = co_o

def showState(s):
    y_a = len(matriz[0])
    for l_a in range (len(matriz)):
        for c_a in range (y_a):
            print(f'[{matriz[l_a][c_a]:^5}]', end = '')
        print()
    print()

    print('l_a: ', str(s.l_a), 'c_a: ', str(s.c_a), 'l_o: ', str(s.l_o), 'c_o: ', str(s.c_o))

def initialState():
    return State(matriz, [0], [4], [0], [5])

def isGoal(s):
    return ((s.l_a == s.l_o) and (s.c_a == s.c_o))

def isValid(s):
    ocupado = []
    testado = []
    if((matriz[s.l_a][s.c_a]) == int(ocupado)):
        return False
    if((matriz[s.l_a][s.c_a]) == int(testado)):
        return False
    if(s.l_a < 0):
        return False
    if(s.c_a < 0):
        return False
    if(s.l_a > len(matriz)):
        return False
    if(s.c_a > len(matriz)):
        return False
    return True

showState(initialState())
print(isGoal(initialState()))
print(isGoal(State(matriz, 4, 4, 5, 5)))
print(isValid(initialState()))



