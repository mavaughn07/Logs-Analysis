# Logs Analysis
This project takes a database and using SQL prints out the responses to 3 questions

## Required Programs
* [Virtual Box](https://www.virtualbox.org/wiki/Downloads)
* [Vagrant](https://www.vagrantup.com/downloads.html)
* [Python3](https://www.python.org/downloads/)

## Setup
Next, download the data [here](https://d17h27t6h515a5.cloudfront.net/topher/2016/August/57b5f748_newsdata/newsdata.zip). You will need to unzip this file after downloading it. The file inside is called newsdata.sql. Put this file into the vagrant directory, which is shared with your virtual machine.
Launch Vagrant with `vagrant up` and login with `vagrant ssh`
To load the data, use the command `psql -d news -f newsdata.sql`

## Running the Program
While logged into vagrant, navigate to the folder that contains the SQL file and python program and run `python3 news.py`
