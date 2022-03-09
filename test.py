from requests import get, post, delete

# !---Корректныйе---!
print(get('http://localhost:5000/api/v2/jobs').json())
print(post('http://localhost:5000/api/v2/jobs',
           json={'title': '555555555',
                 'leader_id': '555555555',
                 'work_size': '555555555',
                 'collaborators': '555555555',
                 'is_finished': True}).json())
print(delete('http://localhost:5000/api/v2/jobs/1').json())

# !---Некорректные---!

# Id не существует
print(get('http://localhost:5000/api/v2/jobs/213423423').json())

# Отсутствует work_size
print(post('http://localhost:5000/api/v2/jobs',
           json={'title': '555555555',
                 'leader_id': '555555555',
                 'collaborators': '555555555',
                 'is_finished': True}).json())

# Id не существует
print(delete('http://localhost:5000/api/v2/jobs/152649864684').json())
