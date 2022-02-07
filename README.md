# Light TCP Client
A (very) light-weight TCP client written in Python and operable from any terminal

This project is in very early development. Please don't put any trust in it without vigorously vetting it yourself (if you *do* do that, let me know how it goes!)
Many things will be changing and you should consider the project unstable for the time being.

## Installation

* Change the working directory to where you want the file to be located

```zsh
cd /usr/local/bin
```

* Clone the git repository

```zsh
sudo git clone https://github.com/B-Roux/ltcp.git
```

* Since the file was originally made in Windows, we need to change the line endings

```zsh
sudo dos2unix ltcp/client.py
```

* Give the script permission to run

```zsh
sudo chmod +x ltcp/client.py
```

* Create a symbolic link named "ltcp-client"

```zsh
sudo ln ltcp/client.py ltcp-client
```

* Run it!

```zsh
ltcp-client --help
```

Copy-'n-paste (please be careful whenever you copy and paste commands):

```zsh
cd /usr/local/bin && sudo git clone https://github.com/B-Roux/ltcp.git && sudo dos2unix ltcp/client.py && sudo chmod +x ltcp/client.py && sudo ln ltcp/client.py ltcp-client
```

### Uninstallation

* Change your directory to where you saved this script

```zsh
cd /usr/local/bin
```

* Delete the directory (recursively) and the symlink

```zsh
sudo rm -rf ltcp && sudo rm ltcp-client
```
