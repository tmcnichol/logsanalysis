# FSND Project 1 - logsanalysis
## Created Views
The code in the project on q_three() depend on 3 created views:

``` create view totalerrors as select extract(Day from time) as Day,
    extract(Month from time) as Month, extract(Year from time) as Year,
    count (*) as Errors from log where status = '404 NOT FOUND'
    group by Day, Month, Year
    order by Day asc;

    create view dailyrequests as select extract(Day from time) as Day,
    extract(Month from time) as Month, extract(Year from time) as Year,
    count (*) as Requests from log
    group by Day, Month, Year
    order by Day asc;

    create view dailyerrorp as select totalerrors.day, totalerrors.month, totalerrors.year,
    round(sum(100.0 * totalerrors.errors/dailyrequests.requests), 2) as error_percentage
    from totalerrors, dailyrequests
    where totalerrors.day = dailyrequests.day
    group by totalerrors.day, totalerrors.month, totalerrors.year
    order by error_percentage desc;```
