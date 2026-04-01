# Download articles

## SZ

Run:

```
python3 download_sz_archive_safari.py \
  --username tum_username \
  --password tum_password \
  --keyword Gaza \
  --ad-hoc-inspect \
--page-from 96 --page-to 92
````

Notes: 
- One needs to introduce the TUM username and password, so this only works if you have TUM credentials. 
- It only works for Safari (but should be easy to adapt). 
- "Allow remote automation" must be clicked. 
- The script opens a safari browser with the SZ TUM archive link, logs in with the TUM credential, set up the date search given as default (this can be changed in the input), gives the given --keyword, and downloads all articles from page --page-from to  --page-to. 

# Article analysis. 
Run `analyze_article.py`:

````
python analyze_article.py articles_data_clean/2023_10_08_israel-erlebt-einen-9-11-moment-wie-konnte-es-dazu-kommen.txt --source-kind text-file > analysis_outputs/2023_10_08_israel-erlebt-einen-9-11-moment-wie-konnte-es-dazu-kommen.json
```

Notes: 
- The output is a JSON file with fields given in rubric.md. 
- It required codex. 