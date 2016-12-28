MYTEXT='\e[0;35m'
NOCOLOUR='\e[0m' # No Color
echo -e "${MYTEXT}Ready to install everything you need.${NOCOLOUR}"
echo -e "${MYTEXT}Lets go!${NOCOLOUR}"

#git
echo -e "\n${MYTEXT}add ppa for git${NOCOLOUR}"
sudo apt-add-repository ppa:git-core/ppa -y #latest git

#node and npm - I think apt-get works for this (below)
echo -e "\n${MYTEXT}install npm and node${NOCOLOUR}"
curl -sL https://deb.nodesource.com/setup_6.x | sudo -E bash -
sudo apt-get install -y nodejs

#install things
echo -e "\n${MYTEXT}update ppa repositories${NOCOLOUR}"
# this cleans out the duplicates from the ppas.
# Something to do with the way that the google ppas are set up
# sudo apt-get install python3-apt ## already comes with the distro
git clone https://github.com/davidfoerster/apt-remove-duplicate-source-entries.git
sudo apt-remove-duplicate-source-entries/apt-remove-duplicate-source-entries.py -y
#off we go again
sudo apt-get update
echo -e "\n${MYTEXT}install lots of things${NOCOLOUR}"
#I know you can install these things all in one command, but I'm hoping that many commands will be more robust to failure
#this REALLY ought to be in a loop
echo -e "\n${MYTEXT}arduino${NOCOLOUR}"
sudo apt-get -y install arduino
echo -e "\n${MYTEXT}build-essential${NOCOLOUR}"
sudo apt-get -y install build-essential
echo -e "\n${MYTEXT}bundler${NOCOLOUR}"
sudo apt-get -y install bundler
echo -e "\n${MYTEXT}cups${NOCOLOUR}"
sudo apt-get -y install cups
echo -e "\n${MYTEXT}curl${NOCOLOUR}"
sudo apt-get -y install curl
echo -e "\n${MYTEXT}gdebi-core${NOCOLOUR}"
sudo apt-get -y install gdebi-core
echo -e "\n${MYTEXT}git${NOCOLOUR}"
sudo apt-get -y install git
echo -e "\n${MYTEXT}imagemagick${NOCOLOUR}"
sudo apt-get -y install imagemagick
echo -e "\n${MYTEXT}libapparmor1${NOCOLOUR}"
sudo apt-get -y install libapparmor1
echo -e "\n${MYTEXT}ruby2.3${NOCOLOUR}" #check version wanted here: https://www.brightbox.com/docs/ruby/ubuntu/
sudo apt-get -y install ruby2.3
echo -e "\n${MYTEXT}ruby2.3-dev${NOCOLOUR}" #numbers must match above
sudo apt-get -y install ruby2.3-dev
echo -e "\n${MYTEXT}rubygems${NOCOLOUR}"
sudo apt-get -y install rubygems
echo -e "\n${MYTEXT}samba${NOCOLOUR}"
sudo apt-get -y install samba
echo -e "\n${MYTEXT}sl${NOCOLOUR}"
sudo apt-get -y install sl
echo -e "\n${MYTEXT}wget${NOCOLOUR}"
sudo apt-get -y install wget
echo -e "\n${MYTEXT}xvfb${NOCOLOUR}"
sudo apt-get -y install xvfb
echo -e "\n${MYTEXT}unzip${NOCOLOUR}"
sudo apt-get -y install unzip

#hyper terminal
echo -e "\n${MYTEXT}install hyper${NOCOLOUR}"
sudo apt-get -y install icnsutils graphicsmagick xz-utils rpm libappindicator1 #for hyper
wget "https://hyper-updates.now.sh/download/linux_deb"
sudo dpkg --install linux_deb

#atom
echo -e "\n${MYTEXT}install atom${NOCOLOUR}"
git clone https://github.com/atom/atom.git
cd atom
script/build
cd ..

#pip
echo -e "\n${MYTEXT}install pip${NOCOLOUR}"
sudo apt-get -y install python-pip
sudo -H pip install --upgrade pip #probably not needed, but belt and braces

#python and jupyter
echo -e "\n${MYTEXT}install ipython and jupyter${NOCOLOUR}"
sudo apt-get -y install python2.7 python-pip python-dev
sudo apt-get -y install ipython ipython-notebook
sudo apt-get -y install pylint
sudo apt-get -y install python-bs4
sudo apt-get -y install python-html5lib
sudo -H pip install jupyter

#pip
echo -e "\n${MYTEXT}install pip packages${NOCOLOUR}"
# sudo pip install **package names**
sudo -H pip install matplotlib numpy scipy requests

#gems
echo -e "\n${MYTEXT}install ruby gems${NOCOLOUR}"
# sudo gem install **gem names**

#atom plugins
echo -e "\n${MYTEXT}install atom plugins${NOCOLOUR}"
apm install linter
apm install linter-pylint
apm install script
apm install seti-ui
apm install monokai-seti
apm install open-recent
apm install todo-show
apm install minimap
apm install highlight-selected
apm install minimap-highlight-selected
apm install pigments

#settings
echo -e "\n${MYTEXT}set git variables${NOCOLOUR}"
source variables #get the variables from a file so that people don't need to come into this file
#git
git config --global user.name $MYNAME
git config --global user.email $MYEMAIL
git config --global credential.helper 'cache --timeout=36000' #cache password for 150 minutes
git config --global color.ui auto #colour the output in git
git config --global core.editor "atom --wait"

#upgrade things if they need it
sudo apt-get update -y
sudo apt-get upgrade -y
sudo apt-get clean -y

sudo gem update --system

echo -e "\n${MYTEXT}All done!${NOCOLOUR}"
