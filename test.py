from requests import get, post, delete

# !---Корректныйе---!
print(get('http://localhost:5000/api/v2/users').json())
print(post('http://localhost:5000/api/v2/users',
           json={'name': 'виталий',
                 'surname': 'валогда',
                 'age': '25',
                 'position': 'позиция',
                 'speciality': 'специалити',
                 'address': 'марс',
                 'email': '123@rofl.com'}).json())
print(delete('http://localhost:5000/api/v2/users/1').json())

# !---Некорректные---!

# Id не существует
print(get('http://localhost:5000/api/v2/users/213423423').json())

# Отсутствует age
print(post('http://localhost:5000/api/v2/users',
           json={'name': 'виталий',
                 'surname': 'валогда',
                 'position': 'позиция',
                 'speciality': 'специалити',
                 'address': 'марс',
                 'email': '123@rofl.com'}).json())

# Id не существует
print(delete('http://localhost:5000/api/v2/users/152649864684').json())
