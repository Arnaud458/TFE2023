source .env/bin/activate

python rn2483.py &
sleep 4 ; python capture_signal.py
