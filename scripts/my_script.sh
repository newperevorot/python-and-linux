#Skript zapuskaetsia iz pod root
#Ustanovka bashrs, vimrc and plugins
apt-get install sudo
git clone https://github.com/ovsergeyev/home.git
cp ~/home/.vimrc ~/.vimrc
cp ~/home/.bashrc ~/.bashrc
git clone https://github.com/VundleVim/Vundle.vim.git
mkdir ~/.vim
mkdir ~/.vim/bundle
cp -R Vundle.vim ~/.vim/bundle
