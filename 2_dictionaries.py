#region Destructuring dictionary standard concept
print("##### Destructuring dictionary standard concept #####")
customer = {
    "first_name": "John",
    "last_name": "Cena",
    "age": 23,
    "email": "johncena@gmail.com"
}

one, two, three, four = customer
print(f"One '{one}', two '{two}', three '{three}', four '{four}'")
# One 'first_name', two 'last_name', three 'age', four 'email'

one, two, three, four = customer.values()
print(f"One '{one}', two '{two}', three '{three}', four '{four}'")
# One 'John', two 'Cena', three '23', four 'johncena@gmail.com'

print(f"Customer email {customer['email']}, age {customer['age']}")
# Customer email johncena@gmail.com, age 23
#endregion

#region Advanced techniques
print("##### Advanced techniques #####")
from operator import itemgetter

current_user = {
    "id": 1,
    "username": "pxuanbach",
    "email": "pxuanbach@gmail.com",
    "phone": "837281928",
    "full_name": "Bach Pham",
    "gender": "Male",
    "website": "immersedincode.io.vn"
}

id, email, gender, username = itemgetter(
    'id', 'email', 'gender', 'username'
)(current_user)

print("Id:", id, "- Email:", email, "- Gender:", gender, "- Username:", username)
# Id: 1 - Email: pxuanbach@gmail.com - Gender: Male - Username: pxuanbach
#endregion