#! /usr/bin/env python
# -*- encoding: utf-8 -*-

def coucou(nom):
    return u"Coucou %s!" % (nom,)
        
if __name__ == '__main__':
    print u"--------------------------------------------------"
    print u"DÉBUT du script"
    print u"--------------------------------------------------"
    nom = raw_input("Quel est votre nom? ")
    print coucou(nom)
    print u"-----------------------------------------------"
    print u"FIN du script"
    print u"-------------------------------------------------"
