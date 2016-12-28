function explain() {
	MYTEXT='\e[0;35m'
	NOCOLOUR='\e[0m' # No Color
	echo -e "\n${MYTEXT} $* ${NOCOLOUR}"
}

explain "Ready to install everything you need."
explain "Lets go!"

#git
explain "add ppa for git"
sudo apt-add-repository ppa:git-core/ppa -y #latest git

#node and npm - I think apt-get works for this (below)
explain "install npm and node"
curl -sL https://deb.nodesource.com/setup_4.x | sudo -E bash -
sudo apt-get install -y nodejs
sudo ln -s /usr/bin/nodejs /usr/bin/node

sudo chown -R `whoami` /usr/lib/node_modules
sudo chown -R `whoami` ~/.npm
sudo chown -R `whoami` /usr/bin/npm
sudo npm install -g npm #sudo considered bad, but it works ¯\_(ツ)_/¯

#install things
explain "update ppa repositories"
# this cleans out the duplicates from the ppas.
# Something to do with the way that the google ppas are set up
# sudo apt-get install python3-apt ## already comes with the distro
git clone https://github.com/davidfoerster/apt-remove-duplicate-source-entries.git
sudo apt-remove-duplicate-source-entries/apt-remove-duplicate-source-entries.py -y
#off we go again
sudo apt-get update
explain "install lots of things"
#I know you can install these things all in one command, but I'm hoping that many commands will be more robust to failure
#this REALLY ought to be in a loop
explain "arduino"
sudo apt-get -y install arduino
explain "build-essential"
sudo apt-get -y install build-essential
explain "bundler"
sudo apt-get -y install bundler
explain "cups"
sudo apt-get -y install cups
explain "curl"
sudo apt-get -y install curl
explain "gdebi-core"
sudo apt-get -y install gdebi-core
explain "git"
sudo apt-get -y install git
explain "imagemagick"
sudo apt-get -y install imagemagick
explain "libapparmor1"
sudo apt-get -y install libapparmor1
explain "ruby2.3 #check version wanted here: https://www.brightbox.com/docs/ruby/ubuntu/"
sudo apt-get -y install ruby2.3
explain "ruby2.3-dev #numbers must match above"
sudo apt-get -y install ruby2.3-dev
explain "rubygems"
sudo apt-get -y install rubygems
explain "samba"
sudo apt-get -y install samba
explain "sl"
sudo apt-get -y install sl
explain "wget"
sudo apt-get -y install wget
explain "xvfb"
sudo apt-get -y install xvfb
explain "unzip"
sudo apt-get -y install unzip

#hyper terminal
explain "install hyper"
sudo apt-get -y install icnsutils graphicsmagick xz-utils rpm libappindicator1 #for hyper
wget "https://hyper-updates.now.sh/download/linux_deb"
sudo dpkg --install linux_deb

#atom
explain "install atom"
sudo apt-get -y install build-essential git libgnome-keyring-dev fakeroot rpm libx11-dev libxkbfile-dev
wget -O atomdeb https://atom.io/download/deb
sudo dpkg --install atomdeb
sudo chown -R `whoami` /home/ben/.atom

#pip
explain "install pip"
sudo apt-get -y install python-pip
sudo -H pip install --upgrade pip #probably not needed, but belt and braces

#python and jupyter
explain "install ipython and jupyter"
sudo apt-get -y install python2.7 python-pip python-dev
sudo apt-get -y install ipython ipython-notebook
sudo apt-get -y install pylint
sudo apt-get -y install python-bs4
sudo apt-get -y install python-html5lib
sudo apt-get -f install -y # does a tidy up, needed for some reason
sudo -H pip install jupyter

#pip
explain "install pip packages"
# sudo pip install **package names**
sudo -H pip install matplotlib numpy scipy requests

#gems
explain "install ruby gems"
# sudo gem install **gem names**

#atom plugins
explain "install atom plugins"
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
explain "set git variables"
source variables #get the variables from a file so that people don't need to come into this file
#git
git config --global user.name $MYNAME
git config --global user.email $MYEMAIL
git config --global credential.helper 'cache --timeout=36000' #cache password for 150 minutes
git config --global color.ui auto #colour the output in git
git config --global core.editor "atom --wait"

#upgrade things if they need it
explain "upgrade things if they need it"
sudo apt-get -f install -y # does a tidy up, needed for some reason
sudo apt-get update -y
sudo apt-get upgrade -y
sudo apt-get clean -y

sudo gem update --system

explain "All done!"
