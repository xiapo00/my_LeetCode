git add .
set /p input=Your commit: 
git commit -m "%input%"
git push
pause