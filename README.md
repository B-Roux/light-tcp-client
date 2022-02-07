# Light TCP Client
A (very) light-weight TCP client written in Python and operable from any terminal

## WARNING
This project is in very early development. Please don't put any trust in it without vigorously vetting it yourself (if you *do* do that, let me know how it goes!)
Many things will be changing and you should consider the project unstable for the time being.

## Usage
Please see the help.txt file (for now). I'll have better documentation when the project matures :)

## Installation

* Change the working directory to where you want the file to be located

```zsh
cd /usr/local/bin
```

* Clone the git repository

```zsh
sudo git clone https://github.com/B-Roux/ltcp.git
```

* Because this script was originally written on a Windows machine, we must change to UNIX line endings to make it work

```zsh
cd ltcp && tr -d '\15\32' < client.py > client.py && tr -d '\15\32' < help.txt > help.txt
```

* Give the script permission to run

```zsh
sudo chmod +x ./ltcp/client.py
```

* Create a symbolic link named "ltcp-client"

```zsh
sudo ln ltcp/client.py ltcp-client
```

* Run it!

```zsh
ltcp-client --help
```



### Uninstallation

```zsh
cd /usr/local/bin
```

```zsh
sudo rm -rf ltcp && sudo rm ltcp-client
```
