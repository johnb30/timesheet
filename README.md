timesheet
=========

I got tired of keeping track of my time by hand so I made this. This is
probably only useful to me but I'm putting it up here because open source.

###Dependencies

The module requires `pandas` because it makes my life easier.

###Install

1. `git clone` the repo or download the zip file
2. `pip install -e /path/to/repo`

This will install the module with a command-line hook.

###Usage

`timesheet start TASK1`

`timesheet stop TASK1`


This will save the results to `~/Documents/YYYYMMDD.csv` with the format:

```
,type,action
2014-07-16 15:45:00,,
2014-07-16 16:00:00,,
2014-07-16 16:15:00,,
2014-07-16 16:30:00,TASK1,start
2014-07-16 16:45:00,TASK1,stop
2014-07-16 17:00:00,,
2014-07-16 17:15:00,,
2014-07-16 17:30:00,TASK2,start
2014-07-16 17:45:00,TASK2,stop
```
