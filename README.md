MicroStrategyIServerScripts
====================================

MicroStrategyIServerScripts provide different scripts for the MicroStrategy Intelligence Server:
<ul>
<li>isstate.py:	Script to show the MicroStrategy Intelligence Server's status</li>
<li>isversion.py: Script to show the MicroStrategy Intelligence Server's version</li>
<li>isstart.py:	Script to start the MicroStrategy Intelligence Server and check the state afterwards</li>
<li>isstop.py: Script to stop the MicroStrategy Intelligence Server and check the state afterwards</li>
<li>isterminate.py: Script to terminate the MicroStrategy Intelligence Server (Hardcore-stopping the Intelligence Server)</li>
<li>isrestart.py:	Script to restart the MicroStrategy Intelligence Server</li>
</ul>

The script was written and tested in Python 2.6.8 but runs as well in Python 3.7.4.

[![Build status](https://ci.appveyor.com/api/projects/status/h9n6uochm3mu3o2p?svg=true)](https://ci.appveyor.com/project/SeppPenner/microstrategyiserverscripts)
[![GitHub issues](https://img.shields.io/github/issues/SeppPenner/MicroStrategyIServerScripts.svg)](https://github.com/SeppPenner/MicroStrategyIServerScripts/issues)
[![GitHub forks](https://img.shields.io/github/forks/SeppPenner/MicroStrategyIServerScripts.svg)](https://github.com/SeppPenner/MicroStrategyIServerScripts/network)
[![GitHub stars](https://img.shields.io/github/stars/SeppPenner/MicroStrategyIServerScripts.svg)](https://github.com/SeppPenner/MicroStrategyIServerScripts/stargazers)
[![License: MIT](https://img.shields.io/badge/License-MIT-blue.svg)](https://raw.githubusercontent.com/SeppPenner/MicroStrategyIServerScripts/master/License.txt)
[![Known Vulnerabilities](https://snyk.io/test/github/SeppPenner/MicroStrategyIServerScripts/badge.svg)](https://snyk.io/test/github/SeppPenner/MicroStrategyIServerScripts) 

## Basic usage:
To add those scripts, copy the py-Files to your server under the /root-Folder and change the mode
to be executable via:
```bash
chmod 755 isstate.py
chmod 755 isstart.py
chmod 755 isstop.py
chmod 755 isversion.py
chmod 755 isterminate.py
chmod 755 isrestart.py
```

## To execute the scripts:
```python
python isstate.py
python isstart.py
python isstop.py
python isversion.py
python isterminate.py
python isrestart.py
```

## To define the aliases for the current user:
Create a new file (if it doesn’t already exist) in the /<username> folder (e.g. /root) called .bashrc and add the aliases from [Bash.basrc](https://github.com/SeppPenner/MicroStrategyIServerScripts/blob/master/Bash.bashrc).
Or copy the file [Bash.basrc](https://github.com/SeppPenner/MicroStrategyIServerScripts/blob/master/Bash.bashrc) to the server and rename it to .bashrc.

## Change the paths in the scripts:
You will need to change the paths in the scripts to your MicroStrategy Intelligence Server's installation file.

Change history
--------------

* **Version 1.0.0.3 (2019-09-29)** : Updated python version.
* **Version 1.0.0.2 (2017-12-05)** : Added the script to restart the IServer, added alias to restart tomcat.

* **Version 1.0.0.1 (2016-12-10)** : Added script to terminate IServer. Added function that shows the script's run time (start, stop and terminate).
									 Fixed a bug in the status function to show the "terminated" status, too.
* **Version 1.0.0.0 (2016-12-06)** : 1.0 release.
