@echo off
title Sherlock - Batch Output
cls

git clone https://github.com/sherlock-project/sherlock.git

cd sherlock

py -m pip install -r requirements.txt

goto ask


:ask

cls

set /p opt=Are you inputting more than one username? (Y/N): 
if %opt%==Y goto series
if %opt%==y goto series
if %opt%==N goto single
if %opt%==n goto single


:series

cls

echo Enter multiple usernames to search! Break up usernames by space, not by newlines.
echo.
set /p usernames=

mkdir username

py sherlock --verbose --print-all --folderoutput "../username/" --timeout 10 %usernames%

cd ..
cls
echo Complete! Please check the 'username' folder to see output.

rmdir sherlock


:single

cls

set /p usernames=Enter a single username to search: 

py sherlock --verbose --print-all --output "../username.txt" --timeout 10 %usernames%

cd ..
cls
echo Complete! Please check 'username.txt' to see output.

rmdir sherlock