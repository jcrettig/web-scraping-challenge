#Dependencies
#from pip import main
#main(['install', '-U', 'webdriver_manager'])


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
    return browser

#NASA Mars News
def scrape_title():
    # URL of page to scrape
    mng_url = "https://mars.nasa.gov/news/"
    # Retrieve page with the requests module
    response = requests.get(mng_url)
    # Create BeautifulSoup object; parse with 'html.parser'
    soup = bs(response.text, 'html.parser')

    #Scrape NASA website for News Title and assign text to a variable
    news_title = soup.find('div', class_="content_title").text

    return news_title


#Setup scrape for Mars paragraph
def scrape_paragraph(): 

    # URL of page to scrape
    mng_url = "https://mars.nasa.gov/news/"

    browser = init_browser()
    browser.visit(mng_url)

    time.sleep(1)

    # Create BeautifulSoup object; parse with 'html.parser'
    html = browser.html
    soup = bs(html, 'html.parser')

    #Scrape NASA website for News for paragraph and assign text to a variable                              
    news_p = soup.find_all('div', class_="article_teaser_body")[0]
    news_p = news_p.text

        # Close the browser after scraping
    browser.quit()
    return news_p

#JPL Mars Space Images - Featured Image

#Setup scrape
def scrape_image(): 
    browser = init_browser()

    # URL of page to scrape
    jpl_url = "https://data-class-jpl-space.s3.amazonaws.com/JPL_Space/index.html"
    browser.visit(jpl_url)

    time.sleep(1)

    # Create BeautifulSoup object; parse with 'html.parser'
    html = browser.html
    soup = bs(html, 'html.parser')

    #click the "Full Image" button to pull up the feature image                                                 *******
    browser.links.find_by_partial_text("FULL IMAGE").click()

    relative_image_path = soup.find_all('img')[0]["src"]
    featured_image_url = jpl_url + relative_image_path
    featured_image_url = "https://data-class-jpl-space.s3.amazonaws.com/JPL_Space/image/featured/mars2.jpg"

    #Temporary until we figure out above.                                                                       *********
    #featured_image_url = https://data-class-jpl-space.s3.amazonaws.com/JPL_Space/image/featured/mars3.jpg

     # Close the browser after scraping
    browser.quit()
    return featured_image_url

#Mars Facts
    
#Setup scrape
def scrape_facts(): 
    browser = init_browser()

    # URL of page to scrape
    mf_url = 'https://space-facts.com/mars/'
    #browser.visit(mf_url)

    #time.sleep(1)

    # Create BeautifulSoup object; parse with 'html.parser'
    # html = browser.html
    # soup = bs(html, 'html.parser')

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
    return mars_facts_table_html

#Mars Hemispheres
def scrape_hemi():

    #Create a python dictionary of the title and image url                                  
    #string for the full resolution images of the Mars Hemispheres

    hemisphere_image_urls = [
        {'img_url': 'https://astropedia.astrogeology.usgs.gov/download/Mars/Viking/cerberus_enhanced.tif/full.jpg',
            'title': 'Cerberus Hemisphere Enhanced'},
        {'img_url': 'https://astropedia.astrogeology.usgs.gov/download/Mars/Viking/schiaparelli_enhanced.tif/full.jpg',
            'title': 'Schiaparelli Hemisphere Enhanced'},
        {'img_url': 'https://astropedia.astrogeology.usgs.gov/download/Mars/Viking/syrtis_major_enhanced.tif/full.jpg',
            'title': 'Syrtis Major Hemisphere Enhanced'},
        {'img_url': 'https://astropedia.astrogeology.usgs.gov/download/Mars/Viking/valles_marineris_enhanced.tif/full.jpg',
            'title': 'Valles Marineris Hemisphere Enhanced'}
  ]

    return hemisphere_image_urls

        #Store data in a dictionary
def scrape_all():
    Mars_data = {
        "news_title" : scrape_title(),
        "news_p" : scrape_paragraph(), 
        "featured_image_url" : scrape_image(),
        "mars_facts_table_html":scrape_facts(),
        "hemisphere_image_urls" : scrape_hemi()
    }

    return Mars_data
