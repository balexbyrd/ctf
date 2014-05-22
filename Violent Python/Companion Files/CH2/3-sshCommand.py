#!/usr/bin/python
# -*- coding: utf-8 -*-
import pexpect

#we inclue the pexpect.TIMEOUT in here incase we don't get a prompt
PROMPT = [pexpect.TIMEOUT,'# ', '>>> ', '> ','\$ ']

def send_command(child, cmd):
    child.sendline(cmd)
    child.expect(PROMPT)
    print child.before

def connect(user, host, password):
    ssh_newkey = 'Are you sure you want to continue connecting'
    connStr = 'ssh ' + user + '@' + host
    child = pexpect.spawn(connStr)
    ret = child.expect([pexpect.TIMEOUT, ssh_newkey,\
                        '[P|p]assword:'])
    
    print 'ret = '+str(ret)
    if ret == 0:
        print '[-] Error Connecting'
        return
    
    if ret == 1:
        child.sendline('yes')
        ret = child.expect([pexpect.TIMEOUT, \
                            '[P|p]assword:'])
        if ret == 0:
            print '[-] Error Connecting'
            return


    #ret == 2, we send the password
    child.sendline(password)

    #check for prompt
    ret2 = child.expect(PROMPT)
    while ret2 == 0:
        print 'NO PROMPT ret2 = '+str(ret2)
        child.sendline(" ")
        ret2 = child.expect(PROMPT)

    print 'PROMPT FOUND'
    return child


def main():
    #host = 'localhost'
    #user = 'root'
    #password = 'toor'
    host = 'sdf.org'
    user = 'lawmicha'
    password = 'compsex'
    
    child = connect(user, host, password)
    send_command(child, 'cat /etc/shadow | grep root')

if __name__ == '__main__':
    main()

