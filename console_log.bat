@echo off
set logfile=cmd_commands.log
setlocal enabledelayedexpansion

:: Capture the date and time
echo %date% %time% >> %logfile%

:: Capture the commands entered
:loop
set /p command=Enter command: 
if "%command%"=="" goto :loop
echo !command! >> %logfile%
%command%
goto :loop

