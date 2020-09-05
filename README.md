# test-django-saas
following https://blog.nicolasmesa.co/posts/2018/10/saas-like-isolation-in-django-rest-framework/

##Steps after installation:

Run in virtual environment:
```
python manage.py migrate
python manage.py createsuperuser
```

##Description

This project uses  ```django-rest-framework``` to create accounts system for User and Company model.

Every new User have the Company tied to his account 



The project also has the ```user_messages``` app by which users can transfer messages among other users 

Every logging in user may see only his messages


###Endpoints:
```
api/v1/accounts/ - to create a new account
api/v1/accounts/users/ - to see the list of the users(every created user - seems like a bug)
api/v1/accounts/company - logged in user may see only his company
api/v1/user-messages/ - to send a message or see existing messages of the the current logged in user
```

###Endpoints use cases:
Go to http://127.0.0.1:8000/api/v1/accounts/ to create a new account

![api/v1/accounts](https://github.com/SergSm/test-django-saas/blob/master/images/accounts.png?raw=true)

Go to http://127.0.0.1:8000/api/v1/accounts/users/  to see every user but only if you are logged in

![api/v1/accounts/users](https://github.com/SergSm/test-django-saas/blob/master/images/user-list.png?raw=true)

Go to http://127.0.0.1:8000/api/v1/accounts/company to see the current user company 

![/api/v1/accounts/company](https://github.com/SergSm/test-django-saas/blob/master/images/company-detail.png?raw=true)
  
  
Go to http://127.0.0.1:8000/api/v1/user-messages/ to send a message to other users(logged in user sees only his messages)

![/api/v1/user-messages](https://github.com/SergSm/test-django-saas/blob/master/images/usermessage-list.png?raw=true)

  
  
  
  
##Additional info

The project also uses the one fixture to create 'non existent company' in the Company model

it loads on first ```python manage.py migrate``` run


