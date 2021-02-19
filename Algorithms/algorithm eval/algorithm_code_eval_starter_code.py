#Question 3
def foo(some_array, b):
    a = 0
    while a < b:
        print(some_array)
        some_array[a], some_array[b] = some_array[b], some_array[a]
        a += 1
        b -= 1



def bar(some_array, n):
    m = 0
    for x in range(0, n):
        if some_array[x] > some_array[m]:
            m = x
    return m



def sort_list(some_array):
    n = len(some_array)

    for x in range(n, 0, -1):
        m = bar(some_array, x)
        if m != x - 1:
            foo(some_array, m)
            
            foo(some_array, x - 1)



##Question 6
def some_function(a_list, value):
    n = len(a_list)

    for i in range(n):
        if a_list[i] == value:
            return a_list[:i] + a_list[i+1:]

    return a_list


