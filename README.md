# ACI--Create-Config-Rollback

This simple script will create a config rollback point on your APIC

It's an ideal starting module for any APIC automation scripts because it creates a cookie to use in all subsequents POSTS and there's that rollback point if 
your change goes south

It's interactive, start by running APICSnapshot.py and it will ask you for a change ref number and your username

You will need to add the APIC URL and your logon creds in the credntials.py file
