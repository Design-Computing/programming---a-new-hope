MYTEXT='\e[0;35m'
NOCOLOUR='\e[0m' # No Color


curl -sL https://deb.nodesource.com/setup_6.x | sudo -E bash -
sudo apt-get install -y nodejs

echo -e "\n${MYTEXT}install atom${NOCOLOUR}"
# git clone https://github.com/atom/atom.git
cd atom
script/build
cd ..
