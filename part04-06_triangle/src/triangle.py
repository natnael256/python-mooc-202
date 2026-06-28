def line (count, icon):

    if len(icon) > 0:
        print(count * icon[0])

def triangle(size):
    # You should call function line here with proper parameters
    count = size
    wide = 0
    while count > 0:
        wide = wide+1
        line(wide,"#")
        count -= 1

# You can test your function by calling it within the following block
if __name__ == "__main__":
    triangle(5)
