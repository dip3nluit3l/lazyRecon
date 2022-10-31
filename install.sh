#!/usr/bin/env bash
echo"     "
echo" ██ ███    ██ ███████ ████████  █████  ██      ██      ███████ ██████  "
echo" ██ ████   ██ ██         ██    ██   ██ ██      ██      ██      ██   ██ "
echo" ██ ██ ██  ██ ███████    ██    ███████ ██      ██      █████   ██████  "
echo" ██ ██  ██ ██      ██    ██    ██   ██ ██      ██      ██      ██   ██ "
echo" ██ ██   ████ ███████    ██    ██   ██ ███████ ███████ ███████ ██   ██ "
echo "                             "

cd lazyHunter
chmod +x *
sudo cp lazyHunter /usr/bin
sudo cp ../lazyHunter /opt
pip3 install -r requirements.txt
cd
echo "Sucessfully installed!!! Now Run, lazyHunter targetDomain.com controller-Key"
echo "Example: lazyHunter dipenluitel30.com.np"


