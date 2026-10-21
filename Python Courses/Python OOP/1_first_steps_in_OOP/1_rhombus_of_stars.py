def print_line(size, stars):
    print(" " * (size - stars) + "* " * stars)

def print_lines_up(size):
    for i in range(1, size):
        print_line(size, i)

def print_lines_down(size):
    for i in range(size, 0, -1):
        print_line(size, i)

def print_rhombus(size):
    print_lines_up(size)
    print_lines_down(size)


n = int(input())

print_rhombus(n)