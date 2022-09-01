
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
