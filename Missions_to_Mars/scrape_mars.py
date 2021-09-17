def scrape():

    from bs4 import BeautifulSoup as soup
    import requests
    from splinter import Browser
    from webdriver_manager.chrome import ChromeDriverManager

    url = 'https://redplanetscience.com/'

    executable_path = {'executable_path': ChromeDriverManager().install()}
    browser = Browser('chrome', **executable_path, headless=False)

    # soup = BeautifulSoup(response.text, 'html.parser')
    # print(soup.prettify())

    browser.visit(url)

    browser.is_element_present_by_css('div.list_text', wait_time=1)
    html = browser.html
    news_soup = soup(html, 'html.parser')


    latest_title = news_soup.find_all('div', class_='content_title')[0].text
    latest_p = news_soup.find_all('div', class_='article_teaser_body')[0].text



    url2 = 'https://spaceimages-mars.com'
    browser.visit(url2)
    html2 = browser.html


    space_soup = soup(html2, 'html.parser')

    feat_image_url = space_soup.find('img', src='image/featured/mars3.jpg')
    featured_image_url = 'https://spaceimages-mars.com/image/featured/mars1.jpg'


    import pandas as pd 

    url3= 'https://galaxyfacts-mars.com'

    galaxy_facts = pd.read_html(url3)
    print(galaxy_facts)

    galaxy_df = pd.DataFrame(galaxy_facts[0])

    galaxy_html = galaxy_df.to_html()
    print(galaxy_html)

    hemispheres_url = 'https://marshemispheres.com/'

    browser.visit(hemispheres_url)

    hemispheres_html = browser.html
    hemispheres = soup(hemispheres_html, 'html.parser')

    hemi_list = hemispheres.find_all('div', class_='item')

    #!/usr/bin/python
    import time

    # setting the list to empty for loop 

    hemisphere_image_urls = []

    for hemi in hemi_list:
        browser.visit(hemispheres_url)
        hemisphere_name = hemi.h3.text
        browser.links.find_by_partial_text(hemisphere_name).click()
        hemispheres_html = browser.html
        hemispheres = soup(hemispheres_html, 'html.parser')
        hemi_soup = hemispheres.find_all('div', class_='downloads')
        hemi_image_url = hemispheres_url + hemi_soup[0].li.a['href']
        hemi_dict= {'title': hemisphere_name, 'img_url':hemi_image_url}
        hemisphere_image_urls.append(hemi_dict)
        time.sleep(1)
        
    print(hemisphere_image_urls)

mars_data = {
    'news title': latest_title,
    'news paragraph': latest_p,
    'featured image url': feat_image_url
    'facts': galaxy_html,
    'hemispheres': hemisphere_image_urls }

    browser.quit()

    return mars_data

