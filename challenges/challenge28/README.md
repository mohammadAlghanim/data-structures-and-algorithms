# Sorting Object

## Solution
```
def sort_by_year(movies):
return sorted(movies, key=lambda movie: movie['year'], reverse=True)

def sort_by_title(movies):
    def remove_leading_articles(title):
        articles = ['A ', 'An ', 'The ']
        for article in articles:
            if title.startswith(article):
                return title[len(article):]
        return title

    return sorted(movies, key=lambda movie: remove_leading_articles(movie['title']))
``` 
## to run a code 
```
/home/mohammad/data-structures-and-algorithms/.venv/bin/python /home/mohammad/data-structures-and-algorit
hms/challenges/challenge28/Sorting_Comparisons.py
```
## to test a code 
```
pytest
```