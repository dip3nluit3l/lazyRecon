#!/usr/bin/env bash
chmod +x *
pip3 install -r requirements.txt
sudo cp  lazyHunter /usr/bin
cd ..
cp lazyHunter /opt/
cd
echo "Sucessfully installed!!! Now Run, lazyHunter targetDomain.com controller-Key"
echo "Example: lazyHunter dipenluitel30.com.np"


