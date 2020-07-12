# randstring-django
A Django based API that returns a random string of length N, where N is provided by the user.

The API is hosted on Heroku.

URL: http://randstring.herokuapp.com/randstring/42/

### Usage
http://randstring.herokuapp.com/randstring/N/
- Change N (range: 1 to 5000) to get random string of the same length
- Beyond 5000, it returns an error message

### Example run
![alt text](https://github.com/namhsuya/randstring-django/blob/master/randstring.png)

### Cloning this repo
- Update the SECRET_KEY to your own Django secret key 
- Update yourapp.herokuapp.com to the name of your app

in the settings.py file inside randstring subfolder

