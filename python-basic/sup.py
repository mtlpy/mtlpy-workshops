#! /usr/bin/env python
# -*- encoding: utf-8 -*-

def sup(name):
    return u"What's up, %s!" % (name)

if __name__ == '__main__':
    print u"--------------------------------------------------"
    print u"START the script"
    print u"--------------------------------------------------"
    name = raw_input("What is your name? ")
    print sup(name)
    print u"-----------------------------------------------"
    print u"END the script"
    print u"-------------------------------------------------"
