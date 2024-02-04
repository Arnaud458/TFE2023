source .env/bin/activate

echo '' > tmp.txt
python rn2483.py &
python capture_signal.py
