echo "Installing dependencies for trav..."

cd ..

touch /tmp/tree_out.txt
apt install python3
apt install xclip
pip3 install pynput
pip install .

currentPath=$(pwd)

travPath="$currentPath/trav"

pathString="export PATH=\$PATH:$travPath"
if grep -qF "$pathString" ~/.bashrc; then
  :
else
  echo "export PATH=\$PATH:$travPath" >> ~/.bashrc
fi

aliasString="alias trav=\". trav.sh\""
if grep -qF "$aliasString" ~/.bashrc; then
  :
else
  echo "alias trav=\". trav.sh\"" >> ~/.bashrc
fi

#echo "export PATH=\$PATH:$travPath" >> ~/.bashrc
#echo "alias trav=\". trav.sh\"" >> ~/.bashrc