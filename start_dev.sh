#!/bin/bash

cleanup() {
    echo "Stopping all servers..."
    if [ ! -z "$BACKEND_PID" ]; then
        kill $BACKEND_PID
    fi
    if [ ! -z "$FRONTEND_PID" ]; then
        kill $FRONTEND_PID
    fi
    echo "All servers stopped."
    exit
}

trap cleanup SIGINT

echo "--- Starting Backend (FastAPI) ---"
cd backend
source .venv/bin/activate
uvicorn main:app --reload &
BACKEND_PID=$!
cd ..
echo "Backend started with PID: $BACKEND_PID"
echo ""


echo "--- Starting Frontend (Angular) ---"
cd frontend
ng serve &
FRONTEND_PID=$!
cd ..
echo "Frontend started with PID: $FRONTEND_PID"
echo ""

echo "=========================================="
echo "Both servers are running in the background."
echo "Backend: http://127.0.0.1:8000"
echo "Frontend: http://localhost:4200"
echo ""
echo "Press Ctrl+C in this terminal to stop ALL servers."
echo "=========================================="

wait $BACKEND_PID
wait $FRONTEND_PID