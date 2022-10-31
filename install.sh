#!/usr/bin/env bash
cd lazyHunter
chmod +x *
pip3 install -r requirements.txt
sudo cp  lazyHunter /usr/bin
cd ..
sudo cp lazyHunter /opt/
cd
echo "Sucessfully installed!!! Now Run, lazyHunter targetDomain.com controller-Key"
echo "Example: lazyHunter dipenluitel30.com.np"


