@echo off
for /f "delims=" %%i in (announcement.txt) do (
    echo %%i
)
