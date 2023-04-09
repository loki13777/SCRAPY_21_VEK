import scrapy
from project1.spiders.categories import url_subcategory
from project1.spiders.constants import *

class AptekaSpider(scrapy.Spider):
    name = "21vek"
    # начинаем со страницы подкатегории
    start_urls = [url_subcategory]

    # получаем ссылки на карточки товара с первой и второй страницы и отправляем на них запросы
    def parse(self, response: scrapy.http.Response) -> scrapy.http.Response:
        urls_cards = response.css(css_urls_cards).getall()
        for url_card in urls_cards:
            yield scrapy.Request(url_card, callback=self.parse_data)
        next_page_url = response.css(css_next_page_url).get()
        if next_page_url == response.url+'page:2/':
            yield scrapy.Request(next_page_url, callback=self.parse)

    # получаем интересующую нас информацию из карточки
    @staticmethod
    def get_name(response) -> str:
        return response.css(css_name).get()

    @staticmethod
    def get_price(response: scrapy.http.Response) -> str:
        price = response.css(css_price).get()
        if price == '0.00':
            return 'нет на складе'
        return price

    @staticmethod
    def get_list_feature_name(response: scrapy.http.Response) -> list:
        list_feature_name = [i.strip() for i in response.css(css_list_feature_name).getall()]
        list_feature_name_strip = [i for i in list_feature_name if i]
        return list_feature_name_strip

    @staticmethod
    def get_list_feature_value(response: scrapy.http.Response) -> list:
        list_feature_value = [i.strip() for i in response.css(css_list_feature_value).getall()]
        return list_feature_value

    # собираем информацию с карточки товара и помещаем в словарь для дальнейшей записи в csv формате
    def parse_data(self, response: scrapy.http.Response) -> dict:
        resul_dict = {'Название товара': self.get_name(response), 'Цена': self.get_price(response)}
        list_feature_name = self.get_list_feature_name(response)
        list_feature_value = self.get_list_feature_value(response)
        resul_dict.update(zip(list_feature_name, list_feature_value))
        yield resul_dict
