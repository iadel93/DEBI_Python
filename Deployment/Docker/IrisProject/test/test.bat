@echo off
setlocal enabledelayedexpansion

for %%f in (test_*.py) do (
    echo Running %%f
    python %%f -v
    if errorlevel 1 (
        echo Failed %%f
        exit /b 1
    )
)

echo Passed unit tests
exit /b 0