@echo off
cls
powershell "Set-ExecutionPolicy -ExecutionPolicy RemoteSigned -Scope Process; selfbot\Scripts\activate; py main.py"