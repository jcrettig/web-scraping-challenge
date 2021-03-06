#Dependencies

from bs4 import BeautifulSoup as bs
import pandas as pd
import requests
from splinter import Browser
from webdriver_manager.chrome import ChromeDriverManager
import time

#Setup Splinter
def init_browser():
    executable_path = {'executable_path':ChromeDriverManager().install()}
    browser = Browser('chrome', **executable_path, headless=False)

#NASA Mars News

#Setup scrape
def scrape_info(): 
    browser = init_browser()

    # URL of page to scrape
    mng_url = "https://mars.nasa.gov/news/"
    browser.visit(mng_url)

    time.sleep(1)

    # Create BeautifulSoup object; parse with 'html.parser'
    html = browser.html
    soup = bs(response.text, 'html.parser')

    #Scrape NASA website for News Title and assign text to a variable
    news_title = soup.find('div', class_="content_title").text

    #Scrape NASA website for News for paragraph and assign text to a variable                               *********
    #news_p = soup.find('div', class_="article_teaser_body").text

    #Temporary news_py until we figure out what is wrong below                                              **********
    news_p = "The first trek of the agency’s largest, most advanced rover yet on the Red Planet marks a major milestone before science operations get under way."

    # Close the browser after scraping
    browser.quit()

#JPL Mars Space Images - Featured Image

#Setup scrape
def scrape_info(): 
    browser = init_browser()

    # URL of page to scrape
    jpl_url = "https://data-class-jpl-space.s3.amazonaws.com/JPL_Space/index.html"
    browser.visit(jpl_url)

    time.sleep(1)

    # Create BeautifulSoup object; parse with 'html.parser'
    html = browser.html
    soup = bs(response.text, 'html.parser')

    #click the "Full Image" button to pull up the feature image                                                 *******
    #browser.links.find_by_partial_text("Full Image").click()

    #relative_image_path = soup.find_all('img')[0]["src"]
    #featured_image_url = url + relative_image_path

    #Temporary until we figure out above.                                                                       *********
    featured_image_url = https://data-class-jpl-space.s3.amazonaws.com/JPL_Space/image/featured/mars3.jpg

     # Close the browser after scraping
    browser.quit()

#Mars Facts
    
#Setup scrape
def scrape_info(): 
    browser = init_browser()

    # URL of page to scrape
    mf_url = 'https://space-facts.com/mars/'
    browser.visit(mf_url)

    time.sleep(1)

    # Create BeautifulSoup object; parse with 'html.parser'
    html = browser.html
    soup = bs(response.text, 'html.parser')

    # pull in any potential table data
    tables = pd.read_html(mf_url)

    #identify the correct table data
    df = tables[1]

    #Set the index to the "Mars-Earth Comparison" column
    df = df.set_index("Mars - Earth Comparison")

    #Convert table to an html data string
    mars_facts_table_html =df.to_html()

    #clean up mars_facts_table_html
    mars_facts_table_html = mars_facts_table_html.replace('\n', '')

    # Close the browser after scraping
    browser.quit()

#Mars Hemispheres

    #Create a python dictionary of the title and image url                                  4th bullet point of instructions*******
    #string for the full resolution images of the Mars Hemispheres

    hemisphere_image_urls = [
        {"title": "Valles Marineris Hemisphere", "img_url": "https://astrogeology.usgs.gov/search/map/Mars/Viking/valles_marineris_enhanced"},
        {"title": "Cerberus Hemisphere", "img_url": "https://astrogeology.usgs.gov/search/map/Mars/Viking/cerberus_enhanced"},
        {"title": "Schiaparelli Hemisphere", "img_url": "https://astrogeology.usgs.gov/search/map/Mars/Viking/schiaparelli_enhanced"},
        {"title": "Syrtis Major Hemisphere", "img_url": "https://astrogeology.usgs.gov/search/map/Mars/Viking/syrtis_major_enhanced"},
    ]

    #Append the dictionary with the image url string and the hemisphere title to a list.            not sure what this means *********
    # This list will contain one dictionary for each hemisphere.

    #Store data in a dictionary

    Mars_data = {
        "news_title" : news_title,
        "news_p" : news_p, 
        "featured_image_url" : featured_image_url,
        "hemisphere_image_urls" : hemisphere_image_urls
    }


























    





