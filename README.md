# FSND Project 1 - logsanalysis
This project uses the Linux-based virtual machine, Ubuntu 16.04.5 LTS (GNU/Linux 4.4.0-75-generic x86_64, that was preconfigured and provided as part of Udacity's Full Stack Developer Nanodegree.

The VM includes the PostgreSQL database and support software needed for this project. Put this file into the vagrant directory, which is shared with your virtual machine.

## How it Works
After cloning or forking this repository:

* Download the zip file with data from "https://d17h27t6h515a5.cloudfront.net/topher/2016/August/57b5f748_newsdata/newsdata.zip"
* Put this file into the vagrant directory, which is shared with your virtual machine.
* cd (change directory) into the vagrant folder and run `vagrant up` followed by `vagrant ssh`
* To load the data, run `cd /vagrant` and use the command `psql -d news -f newsdata.sql`
* Finally, click Control+Z to exit psql and run `python newsdb.py` to display the results 

## Created Views
The code in the project on q_three() depend on 3 created views in PostregreSQL:

`create view totalerrors as select extract(Day from time) as Day,`
`extract(Month from time) as Month, extract(Year from time) as Year,`
`count (*) as Errors from log where status = '404 NOT FOUND'`
`group by Day, Month, Year`
`order by Day asc;`

`create view dailyrequests as select extract(Day from time) as Day,`
`extract(Month from time) as Month, extract(Year from time) as Year,`
`count (*) as Requests from log`
`group by Day, Month, Year`
`order by Day asc;`

`create view dailyerrorp as select totalerrors.day, totalerrors.month, totalerrors.year,`
`round(sum(100.0 * totalerrors.errors/dailyrequests.requests), 2) as error_percentage`
`from totalerrors, dailyrequests`
`where totalerrors.day = dailyrequests.day`
`group by totalerrors.day, totalerrors.month, totalerrors.year`
`order by error_percentage desc;`
