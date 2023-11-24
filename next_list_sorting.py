
sorted_list = sorted([['1', 'A', 2, 5, 45, 10],
     ['2', 'B', 8, 15, 65, 20],
     ['3', 'C', 32, 35, 25, 140],
     ['4', 'B', 82, 305, 75, 90],
     ['5', 'E', 39, 43, 89, 55]], key=lambda lst: (lst[1], lst[2]))

print(sorted_list)

sorted_list_reverse = sorted([['1', 'A', 2, 5, 45, 10],
     ['2', 'B', 8, 15, 65, 20],
     ['3', 'C', 32, 35, 25, 140],
     ['4', 'B', 82, 305, 75, 90],
     ['5', 'E', 39, 43, 89, 55]], key=lambda lst: (lst[1], lst[2]), reverse=True)
     

print(sorted_list_reverse)
