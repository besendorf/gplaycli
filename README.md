# gplaycli2
<!--# gplaycli [![Python package](https://github.com/matlink/gplaycli/workflows/Python%20package/badge.svg)](https://github.com/matlink/gplaycli/actions) ![Debian package](https://github.com/matlink/gplaycli/workflows/Debian%20package/badge.svg)-->
GPlayCli is a command line tool to search, install, update Android applications from the Google Play Store. This is a fork of the unmaintained [matlink/gplaycli](https://github.com/matlink/gplaycli)

	$ usage: gplaycli [-h] [-V] [-v] [-s SEARCH] [-d AppID [AppID ...]] [-y] [-l FOLDER] [-P] [-av] [-a] [-F FILE]
                [-u FOLDER] [-f FOLDER] [-dc DEVICE_CODENAME] [-t] [-tu TOKEN_URL] [-ts TOKEN_STR] [-g GSF_ID]
                [-c CONF_FILE] [-p] [-L]

	A Google Play Store Apk downloader and manager for command line

	optional arguments:
	  -h, --help            show this help message and exit
	  -V, --version         Print version number and exit
	  -v, --verbose         Be verbose
	  -s SEARCH, --search SEARCH
	                        Search the given string in Google Play Store
	  -d AppID [AppID ...], --download AppID [AppID ...]
	                        Download the Apps that map given AppIDs
	  -y, --yes             Say yes to all prompted questions
	  -l FOLDER, --list FOLDER
	                        List APKS in the given folder, with details
	  -P, --paid            Also search for paid apps
	  -av, --append-version
	                        Append versionstring to APKs when downloading
	  -a, --additional-files
	                        Enable the download of additional files
	  -F FILE, --file FILE  Load packages to download from file, one package per line
	  -u FOLDER, --update FOLDER
	                        Update all APKs in a given folder
	  -f FOLDER, --folder FOLDER
	                        Where to put the downloaded Apks, only for -d command
	  -dc DEVICE_CODENAME, --device-codename DEVICE_CODENAME
	                        The device codename to fake
	  -t, --token           Instead of classical credentials, use the tokenize version
	  -tu TOKEN_URL, --token-url TOKEN_URL
	                        Use the given tokendispenser URL to retrieve a token
	  -ts TOKEN_STR, --token-str TOKEN_STR
	                        Supply token string by yourself, need to supply GSF_ID at the same time
	  -g GSF_ID, --gsfid GSF_ID
	                        Supply GSF_ID by yourself, need to supply token string at the same time
	  -c CONF_FILE, --config CONF_FILE
	                        Use a different config file than gplaycli.conf
	  -p, --progress        Prompt a progress bar while downloading packages
	  -L, --log             Enable logging of apps status in separate logging files


Config
===========
GPlayCli searches for the `gplaycli.conf` file in the following places and uses the first file it finds using this priority:
- Current working directory
- ~/.local/etc/gplaycli/
- /usr/local/etc/gplaycli
- /etc/gplaycli

Login
===========
There are 2 ways of authenticating: token (default) or credentials.

Token
-----
GplayCli used to use a token from a token dispenser server located at https://matlink.fr/token/ to login in Google Play. Unfortunatly the server is not recheable and I don't what is needed for such a server so this does not work right now.

Credentials
-----------
If you want to use your own Google credentials, put
	
	token=False

in the config file and type in your credentials in
	
	gmail_address=
	gmail_password=

variables.

Sometimes Google does not accept standard password login and you need to use [App Passwords](https://support.google.com/accounts/answer/185833). For this you need to activate [2-Step Verification](https://support.google.com/accounts/answer/185839)

Changelog
=========
See https://github.com/besendorf/gplaycli/releases for releases and changelogs

Installation
============

Pip
---
`python3 -m pip install gplaycli2` or `python3 -m pip install gplaycli2 --user` if you are non-root (consider using `virtualenv`)

Debian installation
--------------------
Releases are available here https://github.com/besendorf/gplaycli/releases/ as debian packages. <!--Or click this link for automated builds ![Debian package](https://github.com/matlink/gplaycli/workflows/Debian%20package/badge.svg)-->
