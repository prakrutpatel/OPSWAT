#install package requirements
pip3 install -r requirements.txt

#add file_scan.py along with your personal api key as an alias
CWD=$(pwd)
var1="python3 ${CWD}/file_scan.py $1"
echo alias scan="\"${var1}\"" >> ~/.bash_aliases

source ~/.bashrc