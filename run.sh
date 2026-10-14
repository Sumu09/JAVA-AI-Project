#!/usr/bin/env bash
# ==============================================================================
# Butterfly Species Classifier — Launch Script for macOS & Linux
# ==============================================================================
set -e

# Change to project root directory
SCRIPT_DIR="$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)"
cd "$SCRIPT_DIR"

echo "Starting Butterfly Species Classifier App..."

# Auto-detect JAVA_HOME if not already configured
if [ -z "$JAVA_HOME" ]; then
    if [ -d "/Library/Java/JavaVirtualMachines/zulu-17.jdk/Contents/Home" ]; then
        export JAVA_HOME="/Library/Java/JavaVirtualMachines/zulu-17.jdk/Contents/Home"
    elif command -v /usr/libexec/java_home >/dev/null 2>&1; then
        export JAVA_HOME="$(/usr/libexec/java_home 2>/dev/null || true)"
    fi
fi

if [ -n "$JAVA_HOME" ]; then
    export PATH="$JAVA_HOME/bin:$PATH"
fi

# Check for java runtime
if ! command -v java >/dev/null 2>&1; then
    echo "Error: java runtime not found. Please install a JDK/JRE (version 17 or higher) or set JAVA_HOME."
    exit 1
fi

# If compiled classes do not exist, build first
if [ ! -f "target/classes/com/butterfly/classifier/ButterflyClassifierApp.class" ]; then
    echo "Compiled class files not found. Building project first..."
    ./build.sh
fi

echo "Launching ButterflyAI Control Center & Web Server..."
exec java -cp target/classes com.butterfly.classifier.ButterflyClassifierApp "$@"
