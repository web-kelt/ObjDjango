# Инструкция по запуску

1. установить нужные python-библиотеки from `requirements.txt` with **pip3**

```bash
pip3 install -r requirements.txt
```


2. установить Postgres с использованием имеющегося менеджера пакетов и запустить консоль Postgres под созданным при установке пользователем *postgres*

```bash
sudo apt update
sudo apt install postgresql postgresql-contrib

sudo -u postgres psql
```

3. в консоли Postgres создать пользователя с именем *bob* и произвольным паролем, например, *123*

```sql
CREATE USER bob WITH PASSWORD '123';
```

4. в консоли Postgres создать базу данных с именем **web**

```sql
CREATE DATABASE web OWNER bob;
```

5. создать и загрузить миграции через Pycharm

```bash
python3 manage.py makemigrations && python3 manage.py migrate
```


6. запустить проект, находясь в каталоге `web` репозитория

```bash
python3 manage.py runserver
```


7. подключиться к запущенному серверу в браузере по ссылке http://localhost:8000/


8. для создания суперпользователя введите в Pycharm
```bash
python3 manage.py createsuperuser
```
***
