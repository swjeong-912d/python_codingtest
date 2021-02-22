# This is a sample Python script.

# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.
from S18_BinarySearch.L33 import print_test
def print_hi(name):
    # Use a breakpoint in the code line below to debug your script.
    print(f'Hi, {name}')  # Press Ctrl+F8 to toggle the breakpoint.


def get_natural_number():
    n = 0
    while True:
        n += 1
        yield n


def test_syntax():
    g = get_natural_number()
    for _ in range(0, 10):
        print(next(g))
    a = [1, 2, 3, 5]
    for i, v in enumerate(a):
        print(i, v)


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    print_test()
# See PyCharm help at https://www.jetbrains.com/help/pycharm/
