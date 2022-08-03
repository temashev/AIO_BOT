@echo off

call %~dp0C:\Users\Artem\PycharmProjects\bots\venv\Scripts\activate

cd %~dp0bots

set TOKEN=5459494185:AAGuzC4SrqdA88aJWfXl0tAjd4Y7RuakIs4

python bot_telegram.py

pause