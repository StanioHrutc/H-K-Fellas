from django.shortcuts import render
from urllib.request import urlopen
from urllib.error import HTTPError
from bs4 import BeautifulSoup
from .models import Hackathon

import re


class HackScrapper(object):

    @staticmethod
    def create_soup(url):
        try:
            work_html = urlopen(url)
            return BeautifulSoup(work_html, features='html.parser')
        except HTTPError as e:
            print('No such url', e)
            return None

    def __init__(self, main_page_url, *args, **kwargs):
        self._bs_object = HackScrapper.create_soup(main_page_url)

    def __str__(self):
        return 'It is a super class for scrapping purposes'


class DouScrapper(HackScrapper):

    def __init__(self, dou_url, represent_title):
        super().__init__(dou_url)
        self.__dou_url       = dou_url
        self.represent_title = represent_title
        self.articles        = self._bs_object.findAll('article', {'class': 'b-postcard'})

    @staticmethod
    def hackathon_article(article):
        categories = article.find('div', {'class': 'more'}).findChildren()

        result_categories = []
        for category in categories:
            result_categories.append(category.get_text())

        if 'хакатон' in result_categories:
            return result_categories
        else:
            return None

    @staticmethod
    def hackathon_place_price(article):
        place_price_info = article.find('div', {'class': 'when-and-where'}).findChildren()

        result_info = []

        for place in place_price_info:
            result_info.append(place.get_text().strip())
        return result_info

    @staticmethod
    def filter_inner_links(links):
        result_links = []

        for link in links:
            working_link = link.get('href') if link.get('href') is not None else ''
            result       = re.match('https://dou.ua/', working_link)

            if result is None:
                result_links.append(working_link)

        return result_links

    def set_bs_object(self, new_url):

        working_soup = HackScrapper.create_soup(new_url)

        if working_soup is not None:
            self._bs_object = working_soup
            self.articles   = self._bs_object.findAll('article', {'class': 'b-postcard'})

    def scrap_articles(self, new_page_url):

        self.set_bs_object(new_page_url)

        for article in self.articles:
            categories = DouScrapper.hackathon_article(article)
            title      = re.sub('\xa0', ' ', article.find('h2').get_text().strip())
            if categories is None or Hackathon.objects.filter(title=title).exists():
                 continue  
                 '''
                    if category of article isn't hackathon continue iterating over articles
                    if article with such title already exists
                 '''

            
            place_price_info   = DouScrapper.hackathon_place_price(article)
            brief_info         = article.find('p', {'class': 'b-typo'}).get_text().strip()
            article_body       = article.find('a', {'href': re.compile(r'https://dou.ua/calendar/')})['href']

            inner_content      = HackScrapper.create_soup(article_body)
            inner_body_section = inner_content.find('div', {'class': 'cell g-right-shadowed mobtab-maincol'})
            inner_img_src      = inner_content.find('img', {'class': 'event-info-logo'})['src']
            inner_links        = DouScrapper.filter_inner_links(inner_body_section.findAll('a', {'target': '_blank'}))

            
            article_info  = {
                'when': place_price_info[0],
                'price': place_price_info[1],
                'brief_info': re.sub('\xa0', ' ', brief_info),
                'img_src': inner_img_src,
                'inner_links': inner_links
            }
            new_hack = Hackathon(
                title=title,
                info=re.sub('\xa0', ' ', brief_info),
                when=place_price_info[0],
                price=place_price_info[1],
                img=inner_img_src,
                links=inner_links
            )

            new_hack.save()
            print('new hackathon added')


    def general_scrap(self):
        result_hackathons = []

        counter = 1

        test_url = self.__dou_url + 'page-'

        try:
            current_page_url = urlopen(test_url + str(counter))
        except HTTPError:
            current_page_url = None

        while current_page_url is not None:
            scraped_articles = self.scrap_articles(test_url + str(counter))
            counter += 1

            try:
                current_page_url = urlopen(test_url + str(counter))
            except HTTPError:
                current_page_url = None
            
          

    def __str__(self):
        return self.represent_title



def hacks(request):

    dou = DouScrapper('https://dou.ua/calendar/', 'DOU - Developers of Ukraine')

    dou.general_scrap()

    return render(request=request,
                  template_name='hackathons/hacks.html',
                  context={})




