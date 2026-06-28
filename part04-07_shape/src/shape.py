# Copy here code of line function from previous exercise and use it in your solutio
def line (count, icon):

    if len(icon) > 0:
        print(count * icon[0])

def shape (h1, char1 , h2, char2):
    count = h1
    wide = 0
    while count > 0:
        wide = wide+1
        line(wide,char1)
        count -= 1
    while h2 > 0:
        line(h1, char2)
        h2 -= 1
    
# You can test your function by calling it within the following block
if __name__ == "__main__":
    shape(5, "x", 2, "o")