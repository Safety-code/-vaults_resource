REFERENCES
https://www.rexegg.com/regex-quickstart.html for more regex usage.
https://stedolan.github.io/jq/manual/

**APPLICATIONS ON LINUX**
	The kernel of the operating system is like an air traffic controller at an airport, and the applications are the airplanes under its control. The kernel decides which program gets which blocks of memory, it starts and kills applications, and it handles displaying text or graphics on a monitor.

Applications make requests to the kernel and in return receive resources, such as memory, CPU, and disk space. If two applications request the same resource, the kernel decides which one gets it, and in some cases, kills off another application to save the rest of the system and prevent a crash.

The kernel also abstracts some complicated details away from the application. For example, the application doesn’t know if a block of disk storage is on a solid-state drive, a spinning metal hard disk, or even a network file share. Applications need only follow the kernel’s Application Programming Interface (API) and therefore don’t have to worry about the implementation details. Each application behaves as if it has a large block of memory on the system; the kernel maintains this illusion by remapping smaller blocks of memory, sharing blocks of memory with other applications, or even swapping out untouched blocks to disk.

The kernel also handles the switching of applications, a process known as multitasking. A computer system has a small number of central processing units (CPUs) and a finite amount of memory. The kernel takes care of unloading one task and loading a new one if there is more demand than resources available. When one task has run for a specified amount of time, the CPU pauses it so that another may run. If the computer is doing several tasks at once, the kernel is deciding when to switch focus between tasks. With the tasks rapidly switching, it appears that the computer is doing many things at once.

When we, as users, think of applications, we tend to think of word processors, web browsers, and email clients, however, there are a large variety of application types. The kernel doesn’t differentiate between a user-facing application, a network service that talks to a remote computer, or an internal task. From this, we get an abstraction called a process. A process is just one task that is loaded and tracked by the kernel. An application may even need multiple processes to function, so the kernel takes care of running the processes, starting and stopping them as requested, and handing out system resources.

**>DNS**
> also holds global information like the address of the MTA for a given domain name. An organization may want to run their own DNS server to host their public-facing names, and also to serve as an internal directory of services. The **Internet Software Consortium** maintains the most popular DNS server, simply called bind after the name of the process that runs the service.

**>LIGHTWEIGTH DIRECTORY ACCESS PROTOCOL:**
>The DNS is focused mainly on computer names and IP addresses and is not easily searchable. Other directories have sprung up to store information such as user accounts and security roles. The **Lightweight Directory Access Protocol (LDAP)** is one common directory system which also powers Microsoft’s Active Directory. In LDAP, an object is stored in a tree, and the position of that object on the tree can be used to derive information about the object and what it stores. For example, a Linux administrator may be stored in a branch of the tree called “IT Department,” which is under a branch called “Operations.” Thus one can find all the technical staff by searching under the “IT Department” branch. **OpenLDAP** is the dominant program used in Linux infrastructure.


**>THE CLOUD:**
>Physically, a cloud can be described as computing resources from one or many off-site data centers which can be accessed over the internet. The cloud builds on the benefits of a data center and provides computing solutions to organizations who need to store and process data, and it allows them to delegate management of IT infrastructure to a third-party. The data and resources that organizations store in the cloud can include data, servers, storage, application hosting, analytics and a myriad of other services.

A cloud deployment model provides a basis for how cloud infrastructure is built, managed, and accessed. There are four primary cloud deployment models:

- **Public Cloud**: A public cloud is a cloud infrastructure deployed by a provider to offer cloud services to the general public and organizations over the Internet. In the public cloud model, there may be multiple tenants (consumers) who share common cloud resources. More than likely, many of us have accessed public cloud resources at some point through providers such as Amazon, Google, and other popular public cloud providers.
    
- **Private Cloud**: A private cloud is a cloud infrastructure that is set up for the sole use of a particular organization. When compared to a public cloud, a private cloud offers organizations a greater degree of privacy, and control over the cloud infrastructure, applications, and data. It can be hosted either on servers managed by the company that is using it or through a managed private cloud provider such as Rackspace or IBM.
    
- **Community Cloud**: A community cloud is a cloud infrastructure that is set up for the sole use by a group of organizations with common goals or requirements. The organizations participating in the community typically share the cost of the community cloud service. This option may be more expensive than the public cloud; however, it may offer a higher level of control and protection against external threats than a public cloud.
    
- **Hybrid Cloud**: A hybrid cloud is composed of two or more individual clouds, each of which can be a private, community, or public cloud. A hybrid cloud may change over time as component clouds join and leave. The use of such technology enables data and application portability. It also allows companies to leverage outside resources while retaining control of sensitive resources.


>
**>FREE AND OPEN SOURCE LICENCES**
FSF licenses, such as GPLv2, are also open source licenses. However, many open source licenses such as BSD and MIT do not contain the copyleft provisions and are thus not acceptable to the FSF. These licenses are called permissive free software licenses because they are permissive in how you can redistribute the software. You can take BSD licensed software and include it in a closed software product as long as you give proper attribution.

**CONTROL STATEMENT**
	The simplest separator is the semicolon (`;`). Using the semicolon between multiple commands allows for them to be executed one right after another, sequentially from left to right.

The `&&` characters create a logical "and" statement. Commands separated by && are conditionally executed. If the command on the left of the `&&` is successful, then the command to the right of the `&&` will also be executed. If the command to the left of the `&&` fails, then the command to the right of the `&&` is not executed.

The `||` characters create a logical "or" statement, which also causes conditional execution. When commands are separated by `||`, then only if the command to the left fails, does the command to the right of the `||` execute. If the command to the left of the `||` succeeds, then the command to the right of the `||` will not execute.

To see how these control statements work, you will be using two special executables: `true` and `false`. The `true` executable always succeeds when it executes, whereas, the `false` executable always fails. While this may not provide you with realistic examples of how `&&` and `||` work, it does provide a means to demonstrate how they work without having to introduce new comman

>**NAVIGATING THE FILESYSTEM:**
>	+ /boot = Contains files to boot the computer.
>	+ + *basename* = Is the portion of the filename not including the directory. <locate -cb passwd>. To limit the serach term for a particular keyword, place a \ character in front of the search term, <locate -b "/passwd">
	+ where = Use to find where a command (or its man page) is located. <whereis passwd>
	+ whatis = Returns what section a man page is stored in.
	+ pwd = Prints the working directory, which is the current location of the user within the file system.
	+ cd = Use to change directory and navigate the filesystem.
	+ absolute path = They are always complete from the root directory to a subdirectory or file. Allows the user to specify the exact location of a directory.
	+ Relative Paths = It starts from the current directory. It gives direction to a file relative to the current location in the filesystem.
	+ ls = Is used to display the contents of  a directory and can provide detailed infoormation about the files.




***BASH SCRIPTS TIPS***
1. You can't use a script's input argument within a function.
2. Bash variables are global except argument such $1, $2 and $3.

**USING REGEX TO FILTER OUTPUT**
grep -E "^\S+\s+\S+\s+\S+$" DIRECTORY/nmap > DIRECTORY/nmap_cleaned.
The *-E* flag tells grep you’re using a regex. A regex consists of two parts:
constants and operators. Constants are sets of strings, while operators are symbols that denote operations over these strings. These two elements together make regex a powerful tool of pattern matching. Here’s a quick overview of regex operators that represent characters:
\d matches any digit.
\w matches any character.
\s matches any whitespace, and 
\S matches any non-whitespace.
. matches with any single character.
\ escapes a special character.
^ matches the start of the string or line.
$ matches the end of the string or line.
Several operators also specify the number of characters to match:
* matches the preceding character zero or more times.
+ matches the preceding character one or more times.
{3} matches the preceding character three times.
{1, 3} matches the preceding character one to three times.
{1, } matches the preceding character one or more times.
[abc] matches one of the characters within the brackets.
[a-z] matches one of the characters within the range of a to z.
(a|b|c) matches either a or b or c.
This regex pattern
specifies that we should extract lines that contain three strings separated by
two whitespaces: "^\S+\s+S+\s+\S+$"


***NETWORK SERVICES***
->**Commands**
>	**SSH(Secure Shell) (OPENSSH)**
>		sudo apt install openssh-server -y
>		systemctl status/stop/start openssh
>		which ssh
>		# Checking for ssh-client
>		apt search openssh-client
>		# Connecting to an ssh-server
>		*ssh root@192.168.225.12 -p 22*
>		ssh connection uses port 22 by default
**Generating ssh key on the client-side**
	ssh-keygen
	**Copying ssh id to the Server**
		ssh-copy-id -i ~/.ssh/id_rsa.pub safety@192.168.8.157

**TO DISABLE ROOT / PASSWORD LOGIN**
1. Open the sshd config file using:
	1. sudo nano /etc/ssh/sshd_config
	Set "PermitRootLogin no"
	Set  "PasswordAuthentication no"





>**NFS** (Network File System)
>	Network File System (`NFS`) is a network protocol that allows us to store and manage files on remote systems as if they were stored on the local system. It enables easy and efficient management of files across networks. For example, administrators use NFS to store and manage files centrally (for Linux and Windows systems) to enable easy collaboration and management of data. For Linux, there are several NFS servers, including NFS-UTILS (`Ubuntu`).

	Creating NFS 
	mkdir nsf_sharing
	Mount NFS Share
		

We can configure NFS via the configuration file `/etc/exports`. This file specifies which directories should be shared and the access rights for users and systems. It is also possible to configure settings such as the transfer speed and the use of encryption. NFS access rights determine which users and systems can access the shared directories and what actions they can perform. Here are some important access rights that can be configured in NFS:

|**Permissions**|**Description**|
|---|---|
|`rw`|Gives users and systems read and write permissions to the shared directory.|
|`ro`|Gives users and systems read-only access to the shared directory.|
|`no_root_squash`|Prevents the root user on the client from being restricted to the rights of a normal user.|
|`root_squash`|Restricts the rights of the root user on the client to the rights of a normal user.|
|`sync`|Synchronizes the transfer of data to ensure that changes are only transferred after they have been saved on the file system.|
|`async`|Transfers data asynchronously, which makes the transfer faster, but may cause inconsistencies in the file system if changes have not been fully committed.|



***WEB SERVER***
we can use a web server to perform phishing attacks by hosting a copy of the target page on our own server and then attempting to steal user credentials. In addition, there is a variety of other possibilities.
1. **APACHE**
	if we want to transfer files to one of our target systems using a web server, we can put the appropriate files in the `/var/www/html` folder and use `wget` or `curl` or other applications to download these files on the target system. It is also possible to customize individual settings at the directory level by using the `.htaccess` file, which we can create in the directory in question. This file allows us to configure certain directory-level settings, such as access controls, without having to customize the Apache configuration file. We can also add modules to get features like `mod_rewrite`, `mod_security`, and `mod_ssl` that help us improve the security of our web application.
	Starting apache2 service
	systemctl start apache2

2. NginX
3. Python Web Server
	**Starting Python & Web Server**
	python3 -m http.server
	python3 -m http.server --directory
	 When we access our Python web server, we can transfer files to the other system by typing the link in our browser and downloading the files. We can also host our Python web server on a port other than the default port by using the `-p` option: python3 -m http.server - 443
1. Ligttpd

***VPN*** (OPENVPN)
Virtual Private Network (`VPN`) is a technology that allows us to connect securely to another network as if we were directly in it. This is done by creating an encrypted tunnel connection between the client and the server, which means that all data transmitted over this connection is encrypted. Some of the most popular VPN servers for Linux servers are OpenVPN, L2TP/IPsec, PPTP, SSTP, and SoftEther. OpenVPN is a popular open-source VPN server available for various operating systems, including Ubuntu, Solaris, and Redhat Linux. OpenVPN is used by administrators for various purposes, including enabling secure remote access to the corporate network, encrypting network traffic, and anonymizing traffic.
	**Installing openvpn**
	sudo apt install openvpn -y
OpenVPN can be customized and configured by editing the configuration file `/etc/openvpn/server.conf`. This file contains the settings for the OpenVPN server. We can change the settings to configure certain features such as encryption, tunneling, traffic shaping, etc.
If we want to connect to an OpenVPN server, we can use the `.ovpn` file we received from the server and save it on our system. We can do this with the following command on the command line:
	**Connecting to VPN**
	sudo openvpn --config internal.ovpn

***WORKING WITH WEB SERVICES***
**CURL**
	`cURL` is a tool that allows us to transfer files from the shell over protocols like `HTTP`, `HTTPS`, `FTP`, `SFTP`, `FTPS`, or `SCP`. This tool gives us the possibility to control and test websites remotely. Besides the remote servers' content, we can also view individual requests to look at the client's and server's communication. Usually, `cURL` is already installed on most Linux systems.
	curl http://localhost: 8080

**Wget**
An alternative to curl is the tool `wget`. With this tool, we can download files from FTP or HTTP servers directly from the terminal, and it serves as a good download manager. If we use wget in the same way, the difference to curl is that the website content is downloaded and stored locally, as shown in the following example.
	wget http://:localhost:8000

**Starting a Web Server using PHP**
	php -S 127.0.0.1:8080
	The server will start in the directory which contains an index.php or index.html file
**Starting a Web Server using npm**
	http-server -p 8080

*LINUX SERVER ADMINISTRATION*
*TIPS*
**Steps For Every New Linux Server Build**
1. apt update
2. apt dist-upgrade(This command downloads updated packages from the repository)
**Adding user**/ **to sudo group**
adduser <username>
usermod -aG sudo <username>

**Changing hostname**
	hostname set-hostname cloud-desktop


pwd, cut, ls, lsof, df, du, tr, sudo, su, grep, file, uname, hostname, chmod, usermod, adduser, useradd, free, fdisk, gpart, Gparted, mount, ps, top, htop, chown, lblk,free, ip a, ifconfig, iwconfig, netstat, ping, traceroute, env, sed, awk, stat, which, whereis, locate, find, head, tail, stat, dpkg, npm, history, date, cal,env, export, unset, echo, type, whoami, clear, whatis,man, copy, apropos, gzip, gunzip, unzip, updatedb, info, 

+ export PATH=/usr/bin/custom:$PATH
+ '!!' = execute the most recent command
+ 'unset' = Removes exported variables back to local variable
+ man -f <command> = whatis = Displays man pages that match,or partially match, a specific name and provide the section number a brief description of each man page.
+ man -k <command> = Searches for both the name and descriptions of the man pages for a keyword = apropos <command>
+ *basename* = Is the portion of the filename not including the directory. <locate -cb passwd>. To limit the serach term for a particular keyword, place a \ character in front of the search term, <locate -b "/passwd">
+ where = Use to find where a command (or its man page) is located. <whereis passwd>
+ whatis = Returns what section a man page is stored in.
+ pwd = Prints the working directory, which is the current location of the user within the file system.
+ cd = Use to change directory and navigate the filesystem.
+ absolute path = They are always complete from the root directory to a subdirectory or file. Allows the user to specify the exact location of a directory.
+ Relative Paths = It starts from the current directory. It gives direction to a file relative to the current location in the filesystem.
+ ls = Is used to display the contents of  a directory and can provide detailed infoormation about the files.
+ ls -lrt /etc/ssh
+ ls -lrS /etc/ssh
+ ls -d
+ ls -d /etc/??? = Execute the following command to display all the files in the /etc directory that are exactly 3 characters long.
+ ls -d /etc/[abcd]* = By using the brackets [] you can specify a single character to match from a set of characters. This displays all the files in the /etc directory that begins with the letters a, b, c, d: