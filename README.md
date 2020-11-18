# mysub - Name TBA

Freedom is not free, but this software is. Welcome to the source code repository for mysub.

## Purpose

This web application is designed as a way for users to federate their own Subsonic compatible server to smart speakers.

## History

The first speaker supported is Google Home, since it's the first device I own that I could find example code for.  
Though, that code was greatly outdated, it was inspiration for me to build, and thus update the code to work with the 
current iteration of Google Actions.

So, the original point of the project is to use my own web infrastructure that I use for side projects to avoid paying
for a music service when I already have my own music collection, and a Subsonic server, so I can play it on my phone.

Because I don't want Google telling me it's the test version every time, I have decided to expand the scope a bit, and
build a dedicated website where people can register, put in the settings for their own Subsonic (compatible) server, and
use my skill on their device. That way I can "release" my action.

That being said, I also have some history with building and Alexa skill, which I intend to use as a basis to expand this
project there as well.

However, I'm also aware of the privacy concerns with using these third-party cloud services, (and really want to ditch 
my own, or at least relegate them to only being plugged in for testing code) so I also plan to build 
endpoints for Home Assistant, Mycroft, Almond, and anything else I can figure out how to hack out in Python.

## How to help

* Pull Requests for code improvements are definitely welcome.  I know some things are done wrong, and I plan to fix them, but if you can fix them better/faster I'm all for it.
* Documentation for setting up various Subsonic servers, firewall rules, etc.
* Donations for a better droplet (I have a family of 5, and single income... this is sharing a $5 Droplet with my Mail-In-a-Box), dedicated domain name, and Cloudflare setup so I can serve the cover art endpoint behind a CDN.
* Ideas/feature requests - The more ideas on how they might work, the better.

## Feature Status

* Playing a song - working!
* Searching for songs/artists/genres - Working as well as the Subsonic API allows
* Playing more than one song - Sort of works.  You can ask for the next song, and the next song in the directory will be played, but when you ask for songs by an artist or in a genre... only one is currently returned (I plan to fix this soon, to generate random lists based on criteria, artist, album, etc.)
* Linking a Subsonic server to a user account, and interracting with it - Untested, but should work...once I build out the user-facing management options.
* oAuth endpoint for Account Linking workflows - In Progress - I have a server to server Workflow I have used for other projects that I need to expand for end user workflows.
* Website Registration - In Progress / Using django-registration, building out templates, and plan to integrate mfa.
* Website Content Management - In Progress - Using Django CMS, just need to finish building plugins, templates, and writing content.

## Self-hosting

I'm not looking to make money off this project.  Sure, I would love to get a bigger Droplet, and maybe use a Managed Database rather than manage it myself, but that's my only  real motive. (I do want to build a weather service for smart speakers similar to this using CWOP APRS packets, OpenWeatherCloud, and the National Weather Service API.... so that could benefit)

Anyway, to self-host this you need a web server that can serve a Django project.  I'm using Sqlite for local development, but a Postgres database is preferred.  It will probably work with MariaDB as well.

My own server uses
* Ubuntu 18.04 LTS
* Python 3.7 in a VirtualEnv
* Postgres 12
* Nginx
* Let's Encrypt / Certbot
* DNS is managed by my Mail in a Box
    * I have a shell script on my internal/subsonic server that keeps that IP address synced with a sub-domain with the Mail-In-A box API.
    
## Security

Aside from the Subsonic API, which seems to trust anyone who can generate a salted md5 hash, I generally take a 
zero-trust approach to security.  While early versions of the code have some insecure stuff in the repos (yeah, I still 
need to factor out the DJANGO_SECRET_KEY) I intend to have it all fixed before deployment.  I expect contributions to
follow suit.  I don't want anyone getting into my servers, and I'm sure you don't either.

## Subsonic severs

* There are several listed at [AlternativeTo](https://alternativeto.net/software/subsonic/)

## Thanks

* [Subsonic](http://www.subsonic.org/pages/index.jsp) - Thanks for getting it all started
* [ctrlaltca](https://github.com/ctrlaltca/google-home-subsonic) - For the code inspiration
* [DigitalOcean](https://www.digitalocean.com/) - For cheap hosting
* [Mail-in-a-Box](https://mailinabox.email) - For having a DNS API, so I don't need to pay for yet another service to deal with a Dynamic IP address
