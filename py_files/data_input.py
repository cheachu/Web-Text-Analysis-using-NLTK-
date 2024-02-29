import requests
from bs4 import BeautifulSoup
import pandas as pd
import progressbar




# Load input data
input_data = pd.read_excel('Input.xlsx')
bar = progressbar.ProgressBar(
    maxval=len(input_data),
    widgets=[
        ' [', progressbar.Percentage(), '] ',
        progressbar.Bar('#', suffix='%(index)d/%(max_value)d'),
        ' ', progressbar.ETA()
    ]
)
bar.start()
for i, (_, row) in enumerate(input_data.iterrows()):
    url_id = row['URL_ID']
    url = row['URL']

    # Fetch HTML content
    response = requests.get(url)
    soup = BeautifulSoup(response.text, 'html.parser')

    # Extract article title and main text
    title_element = soup.find('title')
    #enter the html class or tags where you need to scrape your data
    main_content_element = soup.find('div', class_=)#type the requreid class type here#

    # If first attempt fails, try alternative class
    if not main_content_element:
        main_content_element = soup.find('div', class_=)

    # Check if elements are found before extracting text
    if title_element and main_content_element:
        article_title = title_element.get_text()
        article_text = main_content_element.get_text()

        # Save extracted text to a text file
        with open(f'{url_id}.txt', 'w', encoding='utf-8') as file:
            file.write(f'{article_title}\n\n{article_text}')
    else:
        with open(f'{url_id}.txt', 'w', encoding='utf-8'):
            pass    
    bar.update(i + 1)        


  
