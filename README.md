# Light TCP Client
A (very) light-weight TCP client written in Python and operable from any terminal

This project is in very early development. Please don't put any trust in it without vigorously vetting it yourself (if you *do* do that, let me know how it goes!)
Many things will be changing and you should consider the project unstable for the time being.

## Installation (Linux)

I will be installing this script to my `/usr/local/bin` directory, which means I need `sudo` for read and write permissions. Depending on whether or not you plan on installing to this directory, you may not need to use `sudo`. Avoid using it if you don't.

Since `/usr/local/bin` is on the shell's `$PATH`, installing the scipt here and making a symlink means that we can run it from anywhere in your system by simply typing the name of the symlink, `ltcp-client`. If you choose not to install this script to this directory, you will either need to choose another directory that is a part of `$PATH`, or add the destination directory as a new `$PATH` entry. Alternatively, you can simply run the script by specifying the full path to it every time.

These commands are a guide for you to use when installing this script - review all commands before executing them to ensure they do not harm your system (you should be doing this whenever you get commands online anyway).

* Change the working directory to where you want the file to be located

```zsh
cd /usr/local/bin
```

* Clone the git repository

```zsh
sudo git clone https://github.com/B-Roux/light-tcp-client.git
```

* Since the file was originally made in Windows, we need to change the line endings

```zsh
sudo dos2unix light-tcp-client/client.py
```

* Give the script permission to run

```zsh
sudo chmod +x light-tcp-client/client.py
```

* Create a symbolic link named "ltcp-client"

```zsh
sudo ln light-tcp-client/client.py ltcp-client
```

* Run it!

```zsh
ltcp-client --version
```

Copy-'n-paste (please be careful whenever you copy and paste commands):

`
cd /usr/local/bin && sudo git clone https://github.com/B-Roux/light-tcp-client.git && sudo dos2unix light-tcp-client/client.py && sudo chmod +x light-tcp-client/client.py && sudo ln light-tcp-client/client.py ltcp-client
`

### Uninstallation (Linux)

Ununstallation is quite simple, since this is only a script that doesn't keep logs or modify system variables. We simply have to delete the cloned repository and the symlink. You can also use this to uninstall old versions of the script before re-doing the installation steps to get the latest version.

* Change your directory to where you saved this script

```zsh
cd /usr/local/bin
```

* Delete the directory (recursively) and the symlink

```zsh
sudo rm -rf light-tcp-client && sudo rm ltcp-client
```

### Intsallation & Uninstallation (Windows/Mac)

Unfortunately, I don't have as convenient a guide for these systems (yet?). As of right now, you can download the client.py file and run it with

```console
python /path/to/client.py [args]
```

## Usage

### Syntax:
* Domain: `ltcp-client [domain]:[port]`
  * Example: `ltcp-client www.example.com:80`
* IPV4: `ltcp-client [ip]:[port]`
  * Example: `ltcp-client 192.0.2.199:80`
    
### Options:\n"
* `-v`, `--version` - Show the tool version (pass as only argument)
* `-h`, `--help` - Show this menu (pass as only argument)
* `-s`, `--send` - Prompt custom message to send
* `-l`, `--listen` [size] - Listen for [size] bytes (if unset, 4096)
* `-d`, `--details` - Print the initial message and details
