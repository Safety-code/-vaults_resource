Useful resource:
https://exploit-notes.hdks.org/

**RECONNAISANCE
GOOGLE DORKING**
• site
E.g site:example.com

• inurl
   ◇ E.g inurl:"/course/jumpto.php" site:example.com
• intitle
   ◇ E.g intitle:"index of" site:example.com
• link
   ◇ E.g. link: “https://en.wikipedia.org/wiki.ReDoS”.
• filetype
   ◇ E.g. 

**SCOPE DISCOVERY**
A program’s scope on its policy page specifies which subdomains,products, and applications you’re allowed to attack.

WHOIS AND REVERSE WHOIS
whois example.com
https://viewdns.info/reversewhois/
https://whois.domaintools.com

IP ADDRESS
nslookup
nslookup example.com

REVERSE IP SEARCHES
ViewDNS.info
whois &lt;IP address&gt;

**ASN** 
Another way of finding IP addresses in scope is by looking at autonomous systems, which are routable networks within the public internet. Autonomous system numbers (ASNs) identify the owners of these networks. By checking if two IP addresses share an ASN, you can determine whether the IPs belong to the same owner. To figure out if a company owns a dedicated IP range, run several IP-to-ASN translations to see if the IP addresses map to a single ASN. If many addresses within a range belong to the same ASN, the organization might have a dedicated IP range.
NB: whois.cymru.com is a database that translates IPs to ASNs.

E.g whois -h whois.cymru.com &lt;IP address&gt;
whois -h whois.cymru.com 197.253.67.105

**CERTIFICATE PARSING**
Another way of finding hosts is to take advantage of the Secure Socket Layer Certificates. (SSL) certificates used to encrypt web traffic. An SSL certificate’s lets certificate owners specify additional hostnames that use the same certificate, so you can find those hostnames by parsing this
field. Use online databases like:
1. crt.sh
2. Censys
3. Cert Spotter
to find certificates for domains.

**SUBDOMAIN ENUMERATION**
Tools for automating subdomain enumeration include
• Sublist3r:: Query serach engines and online subdomain databses.
• Amas: Uses a combination of DNS zone transfers, certificate parsing search engines abd subdomain databses to find subdomains.
•SubBrute: A bruteforcing tool that guesses possible subdomains until it finds the right one.
•Gobuster: Is a tool for bruteforcing to discover subdomains, directories and files on target web servers. 
   ◇ E.g gobuster dns -d target_domain -w wordlist
   		-w is to specify wordlist and -d for target when using the dns mode of gobuster.
   		
ome useful tools and resources for finding or building wordlists;
 https://github.com/danielmiessler/SecLists/">https://github.com/danielmiessler/SecLists/</rich_text><rich_text>
 https://github.com/assetnote/commonspeak2"
 https://github.com/assetnote/commonspeak2
 (for generating wordlist)

Use can remove duplicates from items from two set of two wordlists using the command:
sort -u wordlist1.txt wordlist2.txt

• Altdns https://github.com/infosec-au/altdns/"
https://github.com/infosec-au/altdns/
 is a tool for generating patterns in subdomains, which discovers subdomains with names that are permuatations of other subdomain names.

You can find subdomains of subdomains by running the enumeration tools recursively.

**SERVICE ENUMERATION**
Using nmap or Masscan for active scanning of target for open ports.
Combine the information you gather from different databases for the best results.

**DIRECTORY BRUTEFORCING**
You can use Dirsearch or Gobuster for directory bruteforcing.

Dirsearch
E.g python3 dirsearch.py -e php -u scanme.nmap.org --exclude-status 404.

*Gobuster*
NB: A status code of 404 means that the directory or file doesn’t exist, while 403 means it exists but is protected. Examine 403 pages carefully to see if you can bypass the protection to access the content.
Use screenshot tools like EyeWitness https://github.com/FortyNorthSecurity/EyeWitness/" https://github.com/FortyNorthSecurity/EyeWitness/ or Snapper https://github.com/dxa4481/Snapper/" 
https://github.com/dxa4481/Snapper/ to automatically verify that a page is hosted on each location.

NB:Keep an eye out for hidden services, such as developer or admin panels,directory listing pages, analytics pages, and pages that look outdated and ill-maintained. These are all common places for vulnerabilities to manifest.

**BUILDING YOUR OWN RECON SCRIPTS**
*TIPS*
In general, you should use for loops when you already have a list of values to iterate through. You should use while loops when you’re not sure how many values to loop through
but want to specify the condition in which the execution should stop.

*The characters $@ represent the array containing all input arguments, while
$# is the number of command line arguments passed in. "${@:OPTIND:}" slices
the array so that it removes the MODE argument, like nmap-only, making sure
that we iterate through only the domains part of our input*
**Array slicing is a way of extracting a subset of items from an array.**
The -gt, -ge, -lt, and le flags test for greater than, greater than or equal
to, less than, and less than or equal to, respectively:
if [ $3 -gt 1 ]
if [ $3 -ge 1 ]
if [ $3 -lt 1 ]
if [ $3 -le 1 ]

The -z and -n flags test whether a string is empty. These conditions are
both true:
if [ -z "" ]
if [ -n "abc" ]
The -d, -f, -r, -w, and -x flags check for directory and file statuses. You
can use them to check the existence and permissions of a file before your
shell script operates on them. For instance, this command returns true if
/bin is a directory that exists:
if [ -d /bin]
This one returns true if /bin/bash is a file that exists:
if [ -f /bin/bash ]
And this one returns true if /bin/bash is a readable file:
if [ -r /bin/bash ]
or a writable file:
if [ -w /bin/bash ]
or an executable file:
if [ -x /bin/bash ]

You can also use && and || to combine test expressions. This command
returns true if both expressions are true:
if [ $3 -gt 1 ] && [ $3 -lt 3 ]
And this one returns true if at least one of them is true:
if [ $3 -gt 1 ] || [ $3 -lt 0 ]

Here’s the syntax of a **while loop**. As long as the CONDITION is true, the while loop will execute the code between do and done repeatedly:

During your recon, you should be able to get a good idea of what
the company cares about and the sensitive data it’s protecting.

***TOOLS USED SO FAR***
Be sure to learn about how these tools work before you use them!
Understanding the software you use allows you to customize it to fit your workflow.

**Scope Discovery**
WHOIS looks for the owner of a domain or IP.
ViewDNS.info reverse WHOIS (https://viewdns.info/reversewhois/) is a tool that searches for reverse WHOIS data by using a keyword.
nslookup queries internet name servers for IP information about a host.
ViewDNS reverse IP (https://viewdns.info/reverseip/) looks for domains
hosted on the same server, given an IP or domain.
crt.sh (https://crt.sh/), Censys (https://censys.io/), and Cert Spotter (https://
sslmate.com/certspotter/) are platforms you can use to find certificate
information about a domain.
Sublist3r (https://github.com/aboul3la/Sublist3r/), SubBrute (https://github
.com/TheRook/subbrute/), Amass (https://github.com/OWASP/Amass/), and
Gobuster (https://github.com/OJ/gobuster/) enumerate subdomains.
Daniel Miessler’s SecLists (https://github.com/danielmiessler/SecLists/) is a list of keywords that can be used during various phases of recon and hacking. For example, it contains lists that can be used to brute-force subdomains and filepaths.
Commonspeak2 (https://github.com/assetnote/commonspeak2/) generates lists that can be used to brute-force subdomains and filepaths using publicly available data.
Altdns (https://github.com/infosec-au/altdns) brute-forces subdomains by using permutations of common subdomain names.
Nmap (https://nmap.org/) and Masscan (https://github.com/robertdavidgraham/
masscan/) scan the target for open ports.
Shodan (https://www.shodan.io/), Censys (https://censys.io/), and Project Sonar (https://www.rapid7.com/research/project-sonar/) can be used to find services on targets without actively scanning them.
Dirsearch (https://github.com/maurosoria/dirsearch/) and Gobuster (https://github.com/OJ/gobuster) are directory brute-forcers used to find hidden filepaths.
EyeWitness (https://github.com/FortyNorthSecurity/EyeWitness/) and Snapper(https://github.com/dxa4481/Snapper/) grab screenshots of a list of URLs.
They can be used to quickly scan for interesting pages among a list of
enumerated paths.

**Web Hacking Reconnaissance**
OWASP ZAP (https://owasp.org/www-project-zap/) is a security tool that includes a scanner, proxy, and much more. Its web spider can be used to discover content on a web server.
GrayhatWarfare (https://buckets.grayhatwarfare.com/) is an online search engine you can use to find public Amazon S3 buckets.
Lazys3 (https://github.com/nahamsec/lazys3/) and Bucket Stream (https://github.com/eth0izzle/bucket-stream/) brute-force buckets by using keywords.

**OSINT**
The Google Hacking Database (https://www.exploit-db.com/google
-hacking-database/) contains useful Google search terms that fre-
quently reveal vulnerabilities or sensitive files.
KeyHacks (https://github.com/streaak/keyhacks/) helps you determine
whether a set of credentials is valid and learn how to use them to
access the target’s services.
Gitrob (https://github.com/michenriksen/gitrob/) finds potentially sensitive files that are pushed to public repositories on GitHub.
TruffleHog (https://github.com/trufflesecurity/truffleHog/) specializes in
finding secrets in public GitHub repositories by searching for string
patterns and high-entropy strings.
PasteHunter (https://github.com/kevthehermit/PasteHunter/) scans online paste sites for sensitive information.
Wayback Machine (https://archive.org/web/) is a digital archive of internet content. You can use it to find old versions of sites and their files.
Waybackurls (https://github.com/tomnomnom/waybackurls/) fetches URLs from the Wayback Machine.


**Tech Stack Fingerprinting**
The CVE database (https://cve.mitre.org/cve/search_cve_list.html) contains publicly disclosed vulnerabilities. You can use its website to search for vulnerabilities that might affect your target.
Wappalyzer (https://www.wappalyzer.com/) identifies content manage-
ment systems, frameworks, and programming languages used on a site.
BuiltWith (https://builtwith.com/) is a website that shows you which web technologies a website is built with.
StackShare (https://stackshare.io/) is an online platform that allows developers to share the tech they use. You can use it to collect information about your target.
Retire.js (https://retirejs.github.io/retire.js/) detects outdated JavaScript
libraries and Node.js packages.

**Automation**
Git (https://git-scm.com/) is an open sourced version-control system. You can use its git diff command to keep track of file changes.
You should now have a solid understanding of how to conduct reconnaissance on a target. Remember to keep extensive notes throughout your recon process, as the information you collect can really balloon over time. Once you have a solid understanding of how to conduct recon on a target, you can try to leverage recon platforms like Nuclei (https://github.com/projectdiscovery/nuclei/) or Intrigue Core (https://github.com/intrigueio/intrigue-core/) to make your recon process more efficient. But when you’re starting out, I recommend that you do recon manually with individual tools or write your own
automated recon scripts to learn about the process.