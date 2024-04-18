<h1 align="center">Hi there, I'm <a href="https://github.com/NovaCript/" target="_blank">Gleb</a>
<img src="https://github.com/blackcater/blackcater/raw/main/images/Hi.gif" height="32"/></h1>
<h3 align="center">Template for a menu tree, with an example.</h3>

[![Typing SVG](https://readme-typing-svg.herokuapp.com?color=%2336BCF7&lines=\(\(\(\(\(:++^_^++:\)\)\)\)\))](https://git.io/typing-svg)

><h5> Stack:</h5>Django
<br>

<img width="116" alt="Снимок экрана 2024-02-15 191807" src="https://github.com/NovaCript/UpTrader/assets/114811823/da464410-c06f-49c8-beae-9608d5a64a36">


Зависимости можно установить при помощи pip

```
pip install -r requirements.txt
```
Либо poerty.
```
poetry install
```

Проводим миграции, создаем суперпользователя, запускаем сервер.
```
python manage.py migrate
python manage.py createsuperuser
python manage.py runserver
```

В браузере открываем:
> http://127.0.0.1:8000/

В меню создаем родителя который будет вызываться при помощи включения в файл нашей страницы.

URL генерируется автоматически. 
<img width="68" alt="Снимок экрана 2024-02-16 182524" src="https://github.com/NovaCript/UpTrader/assets/114811823/f6a800d0-f6d2-47f4-9025-df934bd2d0c8">
<img width="150" alt="Снимок экрана 2024-02-16 182515" src="https://github.com/NovaCript/UpTrader/assets/114811823/738601ee-c1a9-4920-aef6-02b135f6393a">


> Не забудте загрузить {% load menu_tags %} на страничке. {% draw_menu 'main_menu' %}


Если нет ни одного созданного меню, вернется пустая строка.


**Для демонстрации было написано представление.**


<img width="213" alt="Снимок экрана 2024-02-15 191351" src="https://github.com/NovaCript/UpTrader/assets/114811823/3daba4d9-edfc-4a4f-a970-a3e4ac56f061">
<br>
Без наведения, содержимое скрыто.<br>
<img width="532" alt="Снимок экрана 2024-02-15 191511" src="https://github.com/NovaCript/UpTrader/assets/114811823/51faa4b2-0ca6-49d2-9c51-2b6056877a01">
<br>
При наведении список раскрываемся.<br>
<img width="539" alt="Снимок экрана 2024-02-15 191517" src="https://github.com/NovaCript/UpTrader/assets/114811823/a44192e2-1bd5-4d6c-bbbc-2f26ef745ab3">
<br>
