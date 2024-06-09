#region Standard concept
print("##### Standard concept - List #####")
first, second, third = [3, 6, 8]  
print(first)    # 3
print(second)   # 6
print(third)    # 8

print("##### Standard concept - Tuple #####")
one, two, three = (1, 2, 3) 
print(one)      # 1
print(two)      # 2
print(three)    # 3
#endregion

#region Standard concept exception
print("##### Standard concept exception #####")
try:
    first, second, third, four = [3, 6, 8]  
except ValueError as e:
    print("ValueError -", str(e))
#endregion

#region Ignoring values
print("##### Ignoring values #####")
one, _, three, _, _ = (1, 2, 3, 4, 5)
print(one, three)   # 1 3
#endregion

#region Using * operator to assign the remaining values
print("##### Using * operator to assign the remaining values #####")
a, b, *re = ["a", "b", "c", "d", "e"]
print(a)    # a
print(b)    # b
print(re) # ['c', 'd', 'e']

*start, end = ("dog", "cat", "frog", "crab")
print(start)    # ['dog', 'cat', 'frog']
print(end)      # crab
#endregion

#region Ignoring remaining values
print("##### Ignoring remaining values #####")
a, *_ = ["a", "b", "c", "d", "e"]
print(a)    # a

a, *_, e = ["a", "b", "c", "d", "e"]
print(a)    # a
print(e)    # e
#endregion
