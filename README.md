# reviews_api
A Reviews django drf API

# Requirements
1. python 3.x
2. pipenv

# Setup environment
```
git clone https://github.com/lwoites/reviews_api.git
cd reviews_api
pipenv install

python django/manage.py migrate
pythoh django/manage.py createsuperuser
go to http://localhost:8000/admin/users/reviewer/add/ and create some users
```

# Running
```
pipenv shell
python django/manage.py runserver
```

# Coverage
```
pipenv shell
cd django
./coverage.sh
# open htmlcov/index.html with a browser and enjoy
```



# API Doc

The Reviews API allows you to:
- CRUD Companies (any logged user can)
- CRUD Reviews (any logged user can create, users can't get,list, delete, modify other users reviews)

## Authorization
Is made by sending `Token <TOKEN>` in the `Authorization` Header

## Examples

### get authorization token
```
curl -X POST \
  http://localhost:8000/api-token-auth/ \
  -H 'Content-Type: application/json' \
  -d '{
	"username": "<USERNAME>",
	"password": "<PASSWORD>"
}'
```

### Create a Company

```
curl -X POST \
  http://localhost:8000/api/v1/companies/ \
  -H 'Authorization: Token <TOKEN>' \
  -H 'Content-Type: application/json' \
  -d '{
	"name": "company 1",
	"description": "A wonderful company"
}'
```

### Get a Company with id 1

```
curl -X GET   http://localhost:8000/api/v1/companies/1/ -H 'Authorization: Token <TOKEN>'
```

### Get all companies paginated
```
curl -X GET   http://localhost:8000/api/v1/companies/ -H 'Authorization: Token <TOKEN>'
```

### Delete Company with id 1
```
curl -X DELETE   http://localhost:8000/api/v1/companies/1/ -H 'Authorization: Token <TOKEN>'
```

### Update a Company name with id 1

```
curl -X PUT http://localhost:8000/api/v1/companies/1/ \
-H 'Authorization: Token <TOKEN>' \
-H 'Content-Type: application/json' \
-d '{"name": "company 1 modified"}'
```

### Create a Review for a Company with id 2

```
curl -X POST \
  http://localhost:8000/api/v1/reviews/ \
  -H 'Authorization: Token <TOKEN>' \
  -H 'Content-Type: application/json' \
  -d '{
	"title": "review title",
	"summary": "summary of the review",
    "rating": 3,
    "company": 2
}'
```

### Get all reviews paginated
```
curl -X GET   http://localhost:8000/api/v1/reviews/ -H 'Authorization: Token <TOKEN>'
```

### Delete a review with id 1
```
curl -X DELETE   http://localhost:8000/api/v1/reviews/1/ -H 'Authorization: Token <TOKEN>'
```

### Update partially a review name with id 1

```
curl -X PATCH http://localhost:8000/api/v1/reviews/1/ \
-H 'Authorization: Token <TOKEN>' \
-H 'Content-Type: application/json' \
-d '{"title": "review title modified"}'
```
