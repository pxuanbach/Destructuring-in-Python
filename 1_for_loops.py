#region Standard for loops 
print("##### Standard for loops #####")
users = [
    ( 1, "Bach", "HCM" ),
    ( 2, "Nam", "HN" ),
    ( 3, "Trung", "NT" )
]

for user in users:
    print(user)
# (1, 'Bach', 'HCM')
# (2, 'Nam', 'HN')
# (3, 'Trung', 'NT')
#endregion

#region Destructuring in for loops
print("##### Destructuring in for loops #####")
users = [
    ( 1, "Bach", "HCM" ),
    ( 2, "Nam", "HN" ),
    ( 3, "Trung", "PR-TC" )
]

for id, name, city in users:
    print("Id:", id, "- Name:", name, "- City:", city)
# Id: 1 - Name: Bach - City: HCM
# Id: 2 - Name: Nam - City: HN
# Id: 3 - Name: Trung - City: PR-TC
#endregion

#region Destructuring with enumerate object
print("##### Destructuring with enumerate object #####")
users = [
    ( 1, "Bach", "HCM" ),
    ( 2, "Nam", "HN" ),
    ( 3, "Trung", "PR-TC" )
]

for index, (id, name, city) in enumerate(users):
    print("Index:", index, "- Id:", id, "- Name:", name, "- City:", city)
# Index: 0 - Id: 1 - Name: Bach - City: HCM
# Index: 1 - Id: 2 - Name: Nam - City: HN
# Index: 2 - Id: 3 - Name: Trung - City: PR-TC
#endregion

#region Combining the use of the ignore syntax and collecting the remaining elements.
print("##### Combining the use of the ignore syntax and collecting the remaining elements #####")
users = [
    [ 1, "Bach", "HCM", "Python" ],
    [ 2, "Nam", "HN", "JavaScript" ],
    [ 3, "Trung", "PR-TC", "TypeScript" ]
]

for id, _, *values in users:
    print("Id:", id, "- Value:", values)
# Id: 1 - Value: ['HCM', 'Python']
# Id: 2 - Value: ['HN', 'JavaScript']
# Id: 3 - Value: ['PR-TC', 'TypeScript']
#endregion
