#!/bin/bash

function trap_ctrlc()
{
    echo "
    Ctrl-c caught, performing clean up"

    pgrep "main.py" | xargs kill
    echo "Main Killed"

    exit 2
}

trap "trap_ctrlc" INT

echo "Inicializing..."
python3 main.py

echo "main.py running in the backgroud"

echo "Opening the web page..."

python3 -m webbrowser -t localhost:5000

echo "IMPORTANT: PRESS ctrl+c TO TERMIANTE ALL PROCESSES, DO NOT CLOSE THE WINDOW WITHOUT DOING IT"

sleep 1000000