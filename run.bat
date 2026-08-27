@echo off
echo Starting Butterfly Species Classifier App...

if not exist "target\classes\com\butterfly\classifier\ButterflyClassifierApp.class" (
    echo Compiled class files not found. Building project first...
    call build.bat
)

start javaw -cp target/classes com.butterfly.classifier.ButterflyClassifierApp
