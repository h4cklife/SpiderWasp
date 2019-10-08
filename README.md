```

  
                      .-.
                     :   \                                      ___...__
                      `.  \      ,                         ,--""        `.
                        `. \    /       \               ,"        ,       \\
                          `.\  |         )            ,"      '            )
                            `\_|,_      /           ,"     '             ,'
                            ,d####""`-./          ,'    '         _,,--""
                        ,  (### ##  *##b.       ,'   '    __,,--""
                        \_  V##_,,-. *##:     ,'  __,,--""
                        / ),--"  __,' *,'--,,'_,-"
                     ,-(_ :..--'' _,,-'/,    `.
                       ,-( `.'`,-,-,_ //_.    `.
                      ' / \ .`/ /,/,/",  \\\\ _. :
                        \  \ .`.-/'/ /,   \\\\ \\\\ `.
                            \ . )\`'"\/    )) \\\\  `.
                             `-"\\\\\\\\ '`--_//,-.))   `.
                                   \\\\    //   //.    `,
                                         '   // `     `,
                                             '  `.     ',
                                                 :      :
                                                 :      :
                                                 `.     :
                                                  ,    ,'
                                                 ,"--"'PG
                                 
..######..########..####.########..########.########.....##......##....###.....######..########.
.##....##.##.....##..##..##.....##.##.......##.....##....##..##..##...##.##...##....##.##.....##
.##.......##.....##..##..##.....##.##.......##.....##....##..##..##..##...##..##.......##.....##
..######..########...##..##.....##.######...########.....##..##..##.##.....##..######..########.
.......##.##.........##..##.....##.##.......##...##......##..##..##.#########.......##.##.......
.##....##.##.........##..##.....##.##.......##....##.....##..##..##.##.....##.##....##.##.......
..######..##........####.########..########.##.....##.....###..###..##.....##..######..##.......  

                Paste Site and Dark Web Data and Identity Monitor v0.5
```

# SpiderWasp v0.5

SpiderWasp will allow you to monitor paste sites and in the future, dark web sites for data dumps containing
client information. 

This code was originally used in an online web service that I have since shutdown and
which used to store all client information, emails, keywords, alerts etc into a database. 

This code has since be converted to database-and-web-less application but coded so that it
could easily be converted into your own web applications and/or application with database support.

This code is open-source, but please give credit where credit is due in order to support 
the original developer, h4cklife.

## Supported Services
    
    1. Slexy
    2. JustPaste - DEAD
    3. Lpaste - DEAD 
    4. Pastefs - Now using JS/JQ to prevent parsing
    5. Pastelink
    6. Pasteonline - DEAD
    7. Paste
    8. Pastie
    
    Pastebin and HaveIBeenPwned APIs will be added back into this public version of the application soon

## Requirements
    
    1. Python3
    2. Pip3
    3. Python3-virtualenv (optional)

## Installation

Depending on your use case, you may wish to use a venv or install the modules globally to make it
easier to run the application from a cronjob without the need to activate the venv.

#####Install with Virtual Environment

    1. git clone https://github.com/h4cklife/SpiderWasp.git
    2. cd spiderwasp
    3. python3 -m virtualenv venv
    4. source venv/bin/activate
    5. pip3 install -r REQUIREMENTS
    
#####Installing globally

    1. git clone https://github.com/h4cklife/SpiderWasp.git
    2. cd spiderwasp
    3. pip3 install -r REQUIREMENTS    

## Configuration

    1. cp config_example.py config.py
    2. vim config.py
    3. Fill in your Twilio and Gmail information if preferred. If you don't want to send
        alerts via email and Twilio text messages, set the SEND_EMAILS and TWILIO_ALERTS alerts to False.
    4. vim libs/Clients.py 
        Add your clients
    5. vim libs/Rules.py
        Add your client keyword rules

## Service Scripts

If you need to run different services at different intervals, you can move the service_scripts/* files
into the root SpiderWasp/ directory and run them from a cronjob at the required intervals. This may be
necessary for services that are update with new posts more or less often than others.

Review the Supported Services section for details on the scripts/services that are still live and working.
    
## Coming Soon

    1. Proxy/Tor support 
    2. Dark web monitoring
       
## Contact
    
    1. Instagram : h4cklife
    2. Twitter : h4cklife
    3. Github : h4cklife
    4. Protonmail : h4cklife_src@protonmail.com

```
-----BEGIN PGP PUBLIC KEY BLOCK-----
Version: OpenPGP.js v4.6.2
Comment: https://openpgpjs.org

xsBNBFwUe9kBCAC5uCRFzkOZvjzs2RSVuE4hljxjKhpl0HLXFT14Hrx1jder
yriBNaIOfreyvky1ShaTF1koHEqS8Wyk+kuCs8ixhY3xySOJAb27tyv0PovX
k6tvChcibN8vZO/78DM+8zWZ/1JbyNOIX4+nX7UWahABLLoeW1tubIs96a2j
3x7MSLhnqB5Vw6MqNuqJXtroZbbFlmf4PivVDa+dtJkM4yxg4sukK0p8oGgY
uCqjG2si31YvEQ2nWvGgNmgh4Ayx7QmTuaZ9QGIhXC4bOZk3S5QqYaEZpJ0n
xWFl9zr6LcptgPV/R4yX6SRqFqqnjmiqwXUEUjA27W3omm3iy4ua97XTABEB
AAHNOyJoNGNrbGlmZV9zcmNAcHJvdG9ubWFpbC5jb20iIDxoNGNrbGlmZV9z
cmNAcHJvdG9ubWFpbC5jb20+wsB/BBABCAApBQJcFHvZBgsJBwgDAgkQZDCj
dv3Zp2sEFQgKAgMWAgECGQECGwMCHgEACgkQZDCjdv3Zp2s4YQf+MCLUuKAJ
vUZG07pnoAHiUbhScbwDdSjU2lXdBqoBXHV6iQnXXUzR0GjarQYTbUPH/6GL
LpYMsP+ZCL9BjypCWm3WgyDnUkFRoq8fvBDRcGatpPbgLAcuZ5hDEComLl9C
YbHirzIKqE6Z8F0KpRVe7D7msHy2uY5Xxykc+d5D3J6etJMOO5fsYeU2cayD
wcP9U9wpXUDWXe5PuCTlKMCAV4cLfzY3/Yt26bXL30dna2zvqTq6YGnLiJEx
/Kysr3IxTb5qtV3BCV7dvPQLvsf5eP0mWFGap2UiAXeVjiDR5moxZ6LU9C1E
zvG4ORnuQz9Qjg7h11VkxuyKg5vfmLVUZc7ATQRcFHvZAQgA4le9DUo7sNJz
6IyA+6E4OAMCUb7iYE9DqLSRQ9CZWWu4u3JTQ+AKbZrkgmupk9fmL5O14NxE
eYmP5+5Oi6oRgpVBohlBUZoKwDHUGPvMq8IdQaIFFj/sqeyH+a/GMTbrrsiH
zpbK9Zp8X+/XLw19Qxu+XPhxHma8x+fpGsL4rwuU8TEK8iKTG4tkuZFu3whd
bzeOhG9MgF0WwNQlQbfscAxcCvF2Akqd4Pu/iW+24gwY8DATaJs/LrW3sIB8
fxGMNgMNE9m7B+T7rGF5DyaJaQBlhN/h7AME1BO9j+fhtXu0yIjZafp9uyjA
6Rqux3/7aUxkhmV3hN5wcsAgXbUPSQARAQABwsBpBBgBCAATBQJcFHvZCRBk
MKN2/dmnawIbDAAKCRBkMKN2/dmna9kdB/0TH6bdTFvVGTIZdDhPlpVU0teS
oMGXNtSeyUb8vVeIXw4GXycb01qBp1QBZOknG15OILjlkPe/vZS2SW9gIt08
xrEj3EYLql/Z51VVyY8XtXabWvMGL0dY7oOf/cn051LKRJ0afaBq4xu4bkXQ
eOIqYRxlrN9D9666raaFND1MH71+5xezHfOZIX+jDaVNkJzZqV7DQ/ABTOFJ
IM7IRPVXnY4QE0rYdyfqqw3QAGP7WYgboQuCFwDCa2WjaissIiE0YOcN6J0a
SyGlE0Dv0tIt4Gbf9sTwylvffwW8eorrGjFXVbZK7nCHEIbCh//C+ZEjW26o
GV71iFJOR0Pcnm3N
=V7Fs
-----END PGP PUBLIC KEY BLOCK-----
```