# Write your solution here
def column_correct(sudoku: list, column_no: int):
    
    num = []

    for row in sudoku:

        if row[column_no] == 0:
            num.append(row[column_no])
            continue
        if row[column_no] in num:
            return False
        else:
            num.append(row[column_no])
    return True

    
