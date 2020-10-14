def bubble_sort(s_list):
    for i in range(len(s_list) - 1, 0, -1):
        no_swap = True
        for j in range(0, i):
            if s_list[j + 1] < s_list[j]:
                s_list[j], s_list[j + 1] = s_list[j + 1], s_list[j]
                no_swap = False
        if no_swap:
            return
 
 
s_list = input('Enter the list of numbers: ').split()
s_list = [int(x) for x in s_list]
bubble_sort(s_list)
print('Sorted list: ', end='')
print(s_list)
