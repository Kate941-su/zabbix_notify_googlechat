# Zabbix Notify Google Chat

# Abstraction

How to send notifications which zabbix server pushed to google chat space.

# Prerequisite

You have to be a google chat user as a **Paid Version User**.
Once you become a paid user, you can use the google chat webhook function.

If you don't have the `httplib2` package, Execute the command below

```
pip install httplib2
```

# Setting

**Zabbix version is 6.4.8 in my environment.**

## Zabbix Server (Application)

1. Go `Notifications > Actions > Media Types`
2. Create Media types
   ! choose type `Script`
   ! Script Parameters will be set as `Shellscript arguments` in order from the top.
3. Please execute `chmod` if you don't gave correct modification to notification.sh.

## Google Chat

You can set up by following the below article.
https://medium.com/@aditichawla2003/decoding-google-chat-webhooks-6d9e27001c3d

## Zabbix Server (Server)

1. You have to confirm your executing script path (my environmet Activescript directory `/usr/lib/zabbix/alertscripts/`.)
2. Set all files in this repository (without README.md)
   ! You have to change URL in `credential.py` to the URL you get from Google Chat.
