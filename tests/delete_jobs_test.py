from requests import delete


print(delete('http://localhost:8080/api/jobs/999').json())
# новости с id = 999 нет в базе

print(delete('http://localhost:8080/api/jobs/1').json())