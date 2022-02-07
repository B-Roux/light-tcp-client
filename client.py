#!/usr/bin/python3

import socket
import re
import sys
import getopt

#spell checking instructions (you can ignore this)
#cSpell:ignore chdir inet

version_number = 'ltcp-client 0.1.0 (early alpha)'

def print_txt_file(filename):
    with open(filename, 'r') as file:
        print(file.read())
def exit_with_error(message):
    print(message)
    print('Please see -h or --help for more information.')

def main(target, argv):

    #Check if the argument is a help or version request
    if target in ('-h', '--help'):
        print(
            """Usage:
                Domain:  ltcp-client [domain]:[port]
                Example: ltcp-client www.example.com:80

                IPV4:    ltcp-client [ip]:[port]
                Example: ltcp-client 192.0.2.199:80

                Help:    ltcp-client -h

            Options:
                -v, --version     Show the tool version (pass as only argument)
                -h, --help               Show this menu (pass as only argument)
                -s, --send                        Prompt custom message to send
                -l, --listen [size]    Listen for [size] bytes (if unset, 4096)
                -d, --details             Print the initial message and details""")
        exit(0)
        
    if target in ('-v', '--version'):
        print(version_number), exit(0)

    target_host = None
    target_port = None

    #Regex filters for validation
    ip_filter = r'''(
        ^                                                   # Beginning of text
        (25[0-5]|2[0-4][0-9]|[01]?[0-9][0-9]?)                          # 0-255
        (\.(25[0-5]|2[0-4][0-9]|[01]?[0-9][0-9]?)){3}               # .0-255 x3
        :[0-9]+                                               # The port number
        $                                                         # End of text
    )'''
    domain_filter = r'''(
        ^                                                   # Beginning of text
        ((?=[a-z0-9-]{1,63}\.)(xn--)?[a-z0-9]+(-[a-z0-9]+)*\.)  #(Sub)Domain(s)
        +[a-z]{2,63}                                                      # TLD
        :[0-9]+                                               # The port number
        $                                                         # End of text
    )'''

    #validate the url/IP(v4) before processing
    if re.fullmatch(
        re.compile(ip_filter+'|'+domain_filter, re.VERBOSE), 
        target
    ):
        try:
            target_host, target_port = target.split(':')
        except:
            exit_with_error('Could not parse host and port.'), exit(1)
    else:
        exit_with_error('Could not parse host and port.'), exit(1)

    #parse CLI opts
    try:
        opts, args = getopt.getopt(argv,
        'sld', 
        ["send", "listen", "details"])
    except getopt.GetoptError:
        exit_with_error('Could not parse options.'), exit(1)

    #set options
    options = {
        'listen': False,
        'listen.size': 0,
        'send': False,
        'send.message': "",
        'details': False,
    }

    for opt, arg in opts:
        if opt in ('-s', '--send'):
            options['send'] = True
        elif opt in ('-l', '--listen'):
            try:
                options['listen'] = True
                options['listen.size'] = int(arg)
            except:
                exit_with_error('Could not understand "listen" arg.'), exit(1)
        elif opt in('-d', '--details'):
            options['details'] = True


    #set the initial message (either user specified or default)
    if options['send']: #use user-entered
        print('Enter the message to be sent:\r\n>>> ', end='')
        textblock = ""       
        while True:         
            textblock += input() + '\r\n'
            if textblock[-4:] == '\r\n\r\n':
                break
            else:
                print('... ', end='')
        options['send.message'] = textblock
    else: #use default
        options['send.message'] = \
            f'GET / HTTP/1.1\r\nHost: {target_host}\r\n\r\n'

    #set the response size
    if not options['listen']:
        options['listen.size'] = 4096

    #print (mainly for debug reasons) the verbose sent info
    if options['details']:
        print('Sending:')
        print()
        print(f'Host:            {target_host}')
        print(f'Port:            {target_port}')
        print(f'Response Length: {options["listen.size"]}')
        print(f'Sent Message:\n{options["send.message"]}')
        print('-'*79)
        print()
        print('Received:')
        print()

    #connect
    client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    client.connect((target_host, int(target_port)))
    #send
    client.send(bytes(options['send.message'], 'utf-8'))
    print(client.recv(options['listen.size']).decode())
    #close
    client.close()

if __name__ == "__main__":
    #QOL arg handling :)
    if len(sys.argv) == 1:
        main('-h', [])
    elif len(sys.argv) == 2:
        main(sys.argv[1], [])
    else: #if arg length 3+
        main(sys.argv[1], sys.argv[2:])
