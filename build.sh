#!/usr/bin/env bash
# ==============================================================================
# Butterfly Species Classifier — Build Script for macOS & Linux
# ==============================================================================
set -e

# Change to project root directory
SCRIPT_DIR="$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)"
cd "$SCRIPT_DIR"

echo "================================================"
echo " Building Butterfly Species Classifier"
echo "================================================"

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

# Check for javac
if ! command -v javac >/dev/null 2>&1; then
    echo "Error: javac not found. Please install a JDK (version 17 or higher) or set JAVA_HOME."
    exit 1
fi

echo "Using Java compiler: $(javac -version 2>&1)"

# Create target directories
mkdir -p "target/classes"
mkdir -p "target/classes/web"

echo "Compiling Java source files..."
javac -encoding UTF-8 -d target/classes src/main/java/com/butterfly/classifier/*.java

echo "Copying web UI assets to target/classes/web..."
cp -R src/main/resources/web/. target/classes/web/

echo ""
echo "================================================"
echo " Build successful! Run './run.sh' to launch."
echo "================================================"
