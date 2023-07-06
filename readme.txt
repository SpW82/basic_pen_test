Interactive pen testing application.
Works best on Linux.
Used for brute forcing ssh/ftp login and multiple hash formats.

Comprised of 4 modules:

1. Scans ssh/ftp(22/21) ports of a given target IP address
	*Requires IP address
2. Brute forces ssh login
	*Requires ssh username, IP address and password file
3. Brute forces ftp login
	*Requires ftp username,  IP address and password file
4. Cracks hashes
	*Requires hash to crack and password file

* c_text.py and f_text.py are for font decoration
* All scripts are required for basic_pt.py to run
* All other scripts can be ran independently


NOTE: I am aware that the ssh/ftp brute forcing scripts are not "fast", this is for two reasons:
	1: To limit the number of logins per second.
	2: Because I haven’t coded a threaded script YET ...
