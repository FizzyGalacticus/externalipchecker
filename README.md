# External IP Checker
This is a script that runs indefinitely and monitors your external IP address.

If your external IP changes, it will use your provided email and SMS gateway address to send you a text message.

You can lookup your SMS gateway address by using [Free Carrier Lookup](http://www.freecarrierlookup.com).

I created this script so that I don't have to setup a static IP with my ISP and I can SSH into my Raspberry Pi from anywhere without the issue of my external IP changing to hinder that process.

## Disclaimer:
I highly recommend creating an email address to use only with this or similar scripts, since it hard-codes your password. I know there are other ways to go about this, but this was the quickest/easiest way to get going on with what I needed to do.
