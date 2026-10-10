@echo off
echo ================================================
echo Building Butterfly Species Classifier (Java 21)
echo ================================================

if not exist "target\classes" mkdir "target\classes"

echo Compiling Java source files...
javac -encoding UTF-8 -d target/classes src/main/java/com/butterfly/classifier/*.java

if %ERRORLEVEL% EQU 0 (
    if not exist "target\classes\web" mkdir "target\classes\web"
    echo Copying web UI assets to target/classes/web...
    xcopy /Y /S /I "src\main\resources\web" "target\classes\web" >nul
    echo.
    echo ================================================
    echo Build successful! Run 'run.bat' to launch the app.
    echo ================================================
) else (
    echo.
    echo Compilation failed with error code %ERRORLEVEL%.
)
pause
