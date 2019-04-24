        # encoding=utf-8

import scrapy
from scrapy.exporters import XmlItemExporter
from ..items import HrforecastspiderItem
import re
import datetime

class HRForecast(scrapy.Spider):
    name = 'HRForecast'

    start_urls =[
        'https://www.hrforecast.de/company/career/'
    ]

    def parse(self, response):


        all_jobs_blocks = response.css('.grid-content').css('.grid-entry-title a')

        vacancies_links = all_jobs_blocks.xpath('@href').getall()

        for link in vacancies_links:
            yield response.follow(link, callback=self.parse_page)

    def parse_page(self, response):

        items = HrforecastspiderItem()

        # block with info
        info = response.css('#av_section_1 .avia-builder-el-first').css('p')

        # has no company name, so write default
        items['company_name'] = 'HRForecast'

        # make crawled date
        items['crawled_date'] = datetime.datetime.now().date()

        # has no posted date, so it will empty
        items['posted_date'] = []
        # take a name
        items['job_title'] = info.css('::text').get()

        # take desription and delete title and part-time
        tmp = info.css('::text')[2:].getall()
        # я понимаю что будут доваблены слова такие как Tasks
        # их можно было удалить
        # и затем из обновленных данных создать словарь
        # но т.к. паук запускается только раз, и не работает "онлайн"
        # я решил не загружать его подобным
        # в дальнейшем, в идеале я предпологаю что стоит с помощью pandas
        # почистить базу

        # add '\n' for good base view
        for idx, item in enumerate(tmp):
            if item[0] is not '\n':
                tmp[idx] = '\n' + item

        # join full data in one string
        items['job_description'] = ''.join(tmp)

        return items