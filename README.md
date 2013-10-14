# mtlpy-workshops

Montréal-Python workshops (presentations, exercises... all the needed material).

These IPython notebooks are compatible with IPython 1.0.0

## Workshops

Each workshop has its own directory, with translations marked with a filename suffix 
of the appropriate language code.

### Published workshops

For convenience, here are the published workshops :

* Supported Technical Setup
    * English [mtlpy-workshop-supported-technical-setup.ipynb](http://bit.ly/18eiMIO)
    * French : [mtlpy-workshop-supported-technical-setup-fr.ipynb](http://bit.ly/1697xMF)
* Virtualenv
    * English
    * French
* Python Basic
    * English
    * French : [mtlpy-workshop-python-basic-fr.ipynb](http://bit.ly/16eEckF)
        * Exercise solution : [mtlpy-workshop-python-basic-solution-fr.ipynb](http://bit.ly/1bnRClq)
        * Example txt file : [texte.txt](http://bit.ly/1btMYSW)
        * Example script file : [script.py](http://bit.ly/16iNg7h)
* Django Basic
    * English
    * French : [mtlpy-workshop-django-basic-fr.ipynb](http://bit.ly/1c2mDcq)
        * Technical setup : [setup-fr.ipynb](http://bit.ly/1bCp099)
        * Final source : [ligue_rugby_mp.tar.gz](http://bit.ly/1g3mfj4)
        * Image web development : [web-development.jpg](http://bit.ly/1cAIcDP)
* Kivy
* OpenStreetMap
* Debian Development Environment

## Publishing

The .ipynb files are published via http://nbviewer.ipython.org.
We give the raw version of the file to the nbviewer service.
It returns the .ipynb file rendered behind a long URL...
... so we shorten them via a service of URL shortener like bit.ly
then we communicate this shortened URL.

Be careful of the branch your on when you choose the raw .ipynb file to publish :
every commit updating this file in this branch will automatically update the 
published version in the nbviewer. (Use master for the latest official version.)

Also, moving around the .ipynb files in the repo will break the links in your 
previous publications.

### Full example

File : 
/mtlpy-workshop-supported-technical-setup-fr.ipynb

Github URL :
https://github.com/mtlpy/mtlpy-workshops/blob/master/mtlpy-workshop-supported-technical-setup-fr.ipynb

RAW Github URL :
https://raw.github.com/mtlpy/mtlpy-workshops/master/mtlpy-workshop-supported-technical-setup-fr.ipynb

Nbviewer URL :
http://nbviewer.ipython.org/urls/raw.github.com/mtlpy/mtlpy-workshops/master/mtlpy-workshop-supported-technical-setup-fr.ipynb

So, we end with the diffusion of something like this :
http://bit.ly/1697xMF

