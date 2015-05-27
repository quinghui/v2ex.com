# README #

Sign in [v2ex.com][v2ex] and take the daily award coins for you.
 This script *v2ex_coins.py* reads cookies from the json file *v2ex_cookie.json* to log [v2ex.com][v2ex] in.  

Note: 

- This Python script only supports **Python3** environment;
- You may need to change the A2 value in the json file to your own v2ex.com cookie;
- Both files *v2ex_coins.py* and *v2ex_cookie.json* would be in same directory.   

```
     Usage:
            v2ex_coins.py --chk         show your balance and the last 20 records   
            v2ex_coins.py --coins       take sign award coins
```
The context of the cookie file *v2ex_cookie.json* looks like following:
```
     {   
     "A2": "2|1:0|10:1432694436|2:A2|56:xxx...|xxxx..."   
     }   
```



[v2ex]:https://v2ex.com
