from requests import put

# !---Корректный---!
print(put('http://localhost:5000/api/jobs/2',
           json={'title': 'Заголовок',
                 'leader_id': 10,
                 'work_size': 2,
                 'collaborators': '13645',
                 'is_finished': False}).json())

# !---Некорректные---!

# Отсутствует title
print(put('http://localhost:5000/api/jobs',
           json={'leader_id': 10,
                 'work_size': 2,
                 'collaborators': '13645',
                 'is_finished': False}).json())

# title должен быть строкой
print(put('http://localhost:5000/api/jobs',
           json={'title': 123,
                 'leader_id': 10,
                 'work_size': 2,
                 'collaborators': '13645',
                 'is_finished': False}).json())

# leader_id должен быть числом
print(put('http://localhost:5000/api/jobs',
           json={'title': 'Заголовок',
                 'leader_id': 'фыв',
                 'work_size': 2,
                 'collaborators': '13645',
                 'is_finished': False}).json())
