#### Create Dirs
mkdir ~/scripts
mkdir ~/scripts/bin


#### Programming Stuff
curl -LJO https://raw.githubusercontent.com/mttgermano/dotfiles/scripts/mgcc ~/scripts/bin/
chmod u+x ~/scripts/bin/mgcc

curl -LJO https://raw.githubusercontent.com/mttgermano/dotfiles/scripts/template ~/scripts/bin/
chmod u+x ~/scripts/bin/template


#### Configs
curl -LJO https://raw.githubusercontent.com/mttgermano/LP1/main/.bashrc
curl -LJO https://raw.githubusercontent.com/mttgermano/LP1/main/.vimrc


#### Nvim 
curl -LO https://github.com/neovim/neovim/releases/latest/download/nvim.appimage ~/scripts/bin/lvim
chmod u+x ~/scripts/bin/lvim

#### Curl this file!
'
curl -LJO https://raw.githubusercontent.com/mttgermano/LP1/init.sh ~/scripts/bin/init.sh
chmod u+x ~/scripts/bin/init.sh
bash ~/scripts/bin/init.sh
'
