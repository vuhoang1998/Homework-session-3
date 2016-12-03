# Homework-session-3
def even_list(n):
    m = []
    for i in range(len(n)):
        if i%2==1:
            m.append(n[i])
    return m

new_list = even_list([1,2,5,-10,9,6])
print(new_list)
if set(new_list) == set([6, -10, 2]):
    print("Your function is correct")
else:
    print("Oops, bugs detected")
