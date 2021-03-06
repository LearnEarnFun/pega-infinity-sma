echo Create virtual env
call python -m venv venv
​
echo Make logs directory
call mkdir logs

echo Activate virtual env
call venv\Scripts\activate.bat

echo Update pip
call python -m pip install --upgrade pip
​
echo Install dependences
call python -m pip install -r requirements.txt
​
echo Run migrations
call python manage.py migrate

echo Collect static files
call python manage.py collectstatic
​
echo Create superuser
call python manage.py createsuperuser
​
echo Deactivate virtual env
call venv\Scripts\deactivate.bat
​
@pause
