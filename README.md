# README #

Sign in [v2ex.com][v2ex] and take the daily award coins for you.
 This script *v2ex_coins.py* reads a cookie's name and value from the json file *v2ex_cookie.json* to log [v2ex.com][v2ex] in.

Note: 

- This Python script only supports **Python3** environment;
- You may need to change the cookie name 'A2' value in the json file to your own v2ex.com cookie;
- Both files *v2ex_coins.py* and *v2ex_cookie.json* would be in same directory.   

```
     Usage:
            v2ex_coins.py --chk         show your balance and the last 20 records   
            v2ex_coins.py --coins       take sign award coins
```

The context of the cookie file *v2ex_cookie.json* looks like following:
```
     {   
     "A2": "2|1:0|10:1432694436|2:A2|56:xxxxx...|uuuuu..."   
     }   
```

On the other hand, you can also use the cookie 'auth' and its value instead of 'A2' in this json file.
 The 'auth' value is one part of 'A2' too. It is encoded by Base64 in this part "|56:xxx...|" of 'A2' behind "|56:".
 The number 56 presents its longth. You would decode it via [Base64](https://www.base64encode.org/) or other Base64 decode tools
 , and then put it in the cookie file.   

For example:     
```
     {
     "auth": "nnn..."
     }
```

The script **v2ex_coins_login.py** which signs in v2ex.com via username and password, not cookies, takes daily award coins or shows up your balance details. The username and password are in the json file **v2ex_user.json**.
```
    Usage:  
            v2ex_coins_login.py --chk        show your balance and the last 20 records  
            v2ex_coins_login.py --coins      take daily sign award  
```

[v2ex]:https://v2ex.com
