cd
git clone https://github.com/atom/atom.git
sudo apt-get -y install build-essential git libgnome-keyring-dev fakeroot rpm libx11-dev libxkbfile-dev
sudo npm install -g node-gyp
cd atom
# script/build --create-debian-package
wget https://atom.io/download/deb
sudo dpkg --install deb
# cd ..
# cd /media/sf_projects/git/programming---a-new-hope
