@echo off

call %~dp0C:\Users\User\PycharmProjects\name\venv\Scripts\activate

cd %~dp0bots

set TOKEN=/.../

python bot_telegram.py

pause
