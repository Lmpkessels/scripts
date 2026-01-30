# A simple script to create filepaths.

import os
myFiles = ['Electrum-4.6.2.tar.gz', 'postman.tar.gz']
for filename in myFiles:
    print(os.path.join('luuk-kessels@luuk-kessels-System-Product-Name:~$', filename))
