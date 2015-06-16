"""The nascent idea behind this project is to have a crawler that can
crawl through https://en.wikipedia.org/wiki/Category:Lists_of_people and
return interesting data based on categories of people.  Example:
which groups of notable people have the highest/lowest rates of articles
mentioning that they were in fraternities or sororoties"""
import requests
import bs4


lists_of_people_page = requests.get("https://en.wikipedia.org/wiki/Category:Lists_of_people")

