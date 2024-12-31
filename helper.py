

def check_rows(cells:list,symbol:str):
    for row in range(len(cells)):
        count:int=0
        for col in range(len(cells[0])):
            if cells[row][col]==symbol:
                count+=1
        if count==len(cells):
            return True

def check_cols(cells:list,symbol:str):
    for col in range(len(cells[0])):
        count:int=0
        for row in range(len(cells)):
            if cells[row][col]==symbol:
                count+=1
            if count==len(cells[0]):
                return True

def check_left_diagonal(cells:list,symbol:str):
    size = len(cells)
    count:int=0
    for i in range(size):
        if cells[i][i] == symbol:
            count += 1
    if count == size:
        return True

def check_right_diagonal(cells:list,symbol:str):
    size=len(cells)
    count:int=0
    for i in range(size):
        if cells[i][size - 1 - i] == symbol:
            count += 1
        if count == size:
            return True
    return False
