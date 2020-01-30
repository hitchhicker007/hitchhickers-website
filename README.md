# hitchhicker's website
Source code of my personal website.
link of my website https://hitchhicker.pythonanywhere.com/

### REQUIREMENTS:
- python3
- django framework
- mysql database (Recommendation : xampp)

### CONNECT DATABASE:
1. Create new database in phpmyadmin.
2. Open blog/settings.py
3. Edit DATABASE details with your databse.
4. Save file and close.

### USAGE:
```
git clone https://github.com/hitchhicker007/hitchhickers-website.git
cd hitchhickers-website
pip install -r requirements.txt
python manage.py makemigrations
python manage.py migrate
python manage.py runserver
```

### ADMIN ACCESS:
To create new admin user open cmd in project dir.
```
python manage.py createsuperuser
```
Add **/admin** in url to go to Admin Panel
