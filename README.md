# cheeter
load the Cheat Sheet and show commands, in specify keyword on users interactive input

This script is assist for pentest,

execute with path of file for cheatsheet in first argument.
and enter some info. for example lhost lport rhost rport

follow the terminal show and press the keyword,
after that search and make show the commands, from loading cheat sheet.


Usage:

        python3 cheeter.py <path_of_file>
        
Example:
        
        python3 cheeter.py ~/cheatsheets/cheatsheet.txt
        
        
You can add your own CheatSheet but if you wanna make parse automatically lhost lport and more infos
then you need the follow the rule

Cheat Sheet rule:
        
      origin:  <some command> http://target.com:8080 HOSTandPORTS=10.10.14.11:1337
        
                                |
                                V
        
      rule  :  <some command> http://{rhost}:{rport} HOSTandPORTS={lhost}:{lport}
