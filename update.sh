BS="-e \033[1;34m"
#color end
CE="\033[0m"
#red start
RS="\033[0;31m"
C="\033[0m"
#green start
GN="\033[0;32m"
#white start
WHS="\033[0m"

echo -e ""$GN"["$RS"+"$GN"]"$CE" Updating..."$C""

{
  pkg update
  pkg -y install git
  pkg -y install python
  apt-get update
  apt-get -y install git
  apt-get -y install python3
  apk update
  apk add git
  apk add python3
} &> /dev/null

{
git clone https://github.com/entynetproject/ghost.git
} &> /dev/null
echo -e ""$GN"["$RS"+"$GN"]"$CE" Update complete!
