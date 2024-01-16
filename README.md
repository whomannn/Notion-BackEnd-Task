# Notion BackEnd Task
 

## Descriptions:

Django Rest Framework simple blog app .

### API Endpoints:

1. Create a Post :
- Create a new post(you must authenticate first)
- URL: '/posts/create/'
- Method: POST

2. List Posts : 
- Show List of posts
- URL: '/posts/list/'
- Method: GET

3. Retrieve Post :
- Show single post with id
- URL: '/posts/detail/<int:pk>/'
- Method: GET

4. Update Post:
- Update exist post with pk(you must be author or admin)
- URL: '/posts/update/<int:pk>/'
- Method: PUT

4. Delete Post:
- Delete exist post with pk(you must be author or admin)
- URL: '/posts/delete/<int:pk>/'
- Method: DELETE


## Installation

1. Clone the repository:


git clone https://github.com/whomannn/Notion-BackEnd-Task

2. Install dependencies:

pip install -r requirements.txt

3. Run server:

python3 manage.py runserver



## For Test

python3 manage.py test tests

