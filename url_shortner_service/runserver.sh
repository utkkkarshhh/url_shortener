#!/bin/bash

# Prevents __pycache__ creation
export PYTHONDONTWRITEBYTECODE=1

# Start FastAPI server
uvicorn main:app --reload --host 0.0.0.0 --port 9005 &
PID_UVICORN=$!

# Cleanup function
cleanup() {
    echo "🛑 Stopping service..."
    kill $PID_UVICORN
    exit 0
}

trap cleanup SIGINT
 
# Wait for all services
wait $PID_UVICORN
