@echo off
set arg1=%1
ECHO @echo off >> scan.bat
ECHO set arg=%%1 >> scan.bat
ECHO python %CD%\file_scan.py %arg1% %%arg%% >> scan.bat
pip install -r requirements.txt
pause
