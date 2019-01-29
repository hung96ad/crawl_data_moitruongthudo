# Crawl data from moitruongthudo
Require: pandas

## Run crontab on Sunday
```
0 0 * * 0 cd {path} && python3 crawler.py >> `date +\%y\%m\%d\%H\%M`.log 2>&1

```
