**MODULES**
Exploits modules uses payloads.
_Auxiliary modules include port scanners, fuzzers, sniffers, and more.

### Payloads, Encoders, Nops
_Payloads_ : consist of code that runs remotely, while _encoders_: ensure that payloads make it to their destination intact.
*Nops*: keep the payload sizes consistent across exploit attempts.

Metsaploit gives you the option to load modules either at runtime or after msfconsole has already been started. If you need additional modules from with msfconsole, use the loadpath command.
*msf > loadpath
Usage: loadpath </path/to/modules>

Loads modules from the given directory which should contain subdirectories for
module types, e.g. /path/to/modules/exploits

msf > loadpath /usr/share/metasploit-framework/modules/
Loaded 399 modules:
    399 payloads*

COMMANDS
>back
>check
>connect: There is a miniature Netcat clone built into the msfconsole that supports SSL, proxies, pivoting, and file transfers. By issuing the **connect** command with an IP address and port number, you can connect to a remote host from within msfconsole the same as you would with Netcat or Telnet.
>edit
>grep
>The **info** command will provide detailed information about a particular module including all options, targets, and other information.
>Running the **irb** command will drop you into a live Ruby interpreter shell where you can issue commands and create Metasploit scripts on the fly. This feature is also very useful for understanding the internals of the Framework.
>Jobs are modules running in the background
>kill
>The **load** command loads a plugin from Metasploit’s **plugin** directory. Arguments are passed as **key=val** on the shell.
>The **loadpath** command will load a third-part module tree for the path so you can point Metasploit at your 0-day exploits, encoders, payloads.
>Conversely, the **unload** command unloads a previously loaded plugin and removes any extended commands.
>Resource: The resource command runs resource (batch) files that can be loaded through msfconsole.
>The **route** command in Metasploit allows you to route sockets through a session or ‘comm’, providing basic pivoting capabilities. To add a route, you pass the target subnet and network mask followed by the session (comm) number.
>search
>name. search name:mysql
>platform: search platform:aix
>type: search type:exploit.
>multiple: search cve:2011 author:jduck platform:linux.
>sessions: The **sessions** command allows you to list, interact with, and kill spawned sessions. The sessions can be shells, Meterpreter sessions, VNC, etc
>set.
>unset
>Setg: In order to save a lot of typing during a pentest, you can set _global variables_ within msfconsole. You can do this with the **setg** command. Once these have been set, you can use them in as many exploits and auxiliary modules as you like. You can also save them for use the next time you start msfconsole. However, the pitfall is forgetting you have saved globals, so always check your options before you **run** or **exploit**. Conversely, you can use the **unsetg** command to unset a global variable. In the examples that follow, variables are entered in all-caps (ie: LHOST), but Metasploit is case-insensitive so it is not necessary to do so.