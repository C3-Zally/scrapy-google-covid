import scrapy


class SpiderGoogle(scrapy.Spider):
    name = 'spider_google'
    allowed_domains = ['https://news.google.com/covid19/map?hl=en-US&gl=US&ceid=US%3Aen']
    start_urls = [
        # 'http://https://news.google.com/covid19/map/', 
        'https://news.google.com/covid19/map?hl=en-US&gl=US&ceid=US%3Aen'
    ]
    custom_settings = {
        'FEED_URI': './dist/response.json',
        'FEED_FORMAT': 'json',
        'CURRENT_REQUESTS': 24,
        'MEMUSAGE_LIMIT_MB': 2048,
        'MEMUSAGE_NOTIFY_MAIL': ['ingeniero.miguelvargas@gmail.com'],
        'ROBOTSTXT_OBEY': True,
        'USER_AGENT': 'Pepito Perez',
        'FEED_EXPORT_ENCODING': 'utf-8'
    }


    def parse(self, response):
        header = self.get_head(response)
        content = self.get_content(response)
        yield {'header': header, 'content': content}


    ## Complements (General)
    def get_head(self, response):
        title = self.get_title(response)
        title_complements = self.get_title_complements(response)
        title_date = self.get_title_date(response)
        return {
            'title': title,
            'date': title_date,
            'values': title_complements
        }


    def get_content(self, response):
        # Content
        table_header = self.get_table_header(response)
        table_location = self.get_table_location(response)
        table_data = self.get_table_data(response)
        filter_data = self.filter_data(table_header, table_location, table_data)
        return filter_data
        # return {
        #     'tempData': {
        #         'header': table_header, 'location': table_location,'data':  table_data
        #     }
        # }


    def filter_data(self, table_header, table_location, table_data):
        del table_header[0] # Remove Name Country
        del table_header[2] # Remove Image Col
        new_table_data = self.split_list(table_data, 4)
        data_table_complement = list()
        for item in new_table_data:
            data = {}
            for value_one, value_two in zip(table_header, item):
                data.update({value_one: value_two})
            data_table_complement.append(data)
            # data_table_complement.append(({value_one: value_two}) for value_one, value_two in zip(header, new_table_data))
        response = {}
        for value_one, value_two in zip(table_location, data_table_complement):
            response.update({value_one: value_two})
        return response


    # Header
    def get_title(self, response):
        return response.xpath('//h3[@class="wH7mg"]/text()').get()


    def get_title_complements(self, response):
        get_title_complements_subtitle = self.get_title_complements_subtitle(response)
        get_title_complements_value = self.get_title_complements_value(response)
        return [({'title':value_one, 'value': value_two}) for value_one, value_two in zip(get_title_complements_subtitle, get_title_complements_value)]


    def get_title_complements_subtitle(self, response):
        return  response.xpath('//div[contains(@class,"fNm5wd")]/div[contains(@class,"RbBDcc")]/text()').getall()


    def get_title_complements_value(self, response):
        return  response.xpath('//div[contains(@class,"fNm5wd")]/div[contains(@class,"UvMayb")]/text()').getall()


    def get_title_date(self, response):
        return  response.xpath('//div[@class="mvmWx"]//time/@datetime').get()


    # Table
    def get_table_header(self, response):
        return response.xpath('//table[@class="pH8O4c"]/thead/tr//th//text()').getall()


    def get_table_location(self, response):
        return response.xpath('//table[@class="pH8O4c"]/tbody/tr//th//text()').getall()


    def get_table_data(self, response):
        return response.xpath('//table[@class="pH8O4c"]//tr//td//text()').getall()


    # Complements and Functions
    def split_list(self, arr, size):
        # length = len(alist)
        # return [ alist[i*length // wanted_parts: (i+1)*length // wanted_parts] 
        #         for i in range(wanted_parts) ]
        arrs = []
        while len(arr) > size:
            pice = arr[:size]
            arrs.append(pice)
            arr   = arr[size:]
        arrs.append(arr)
        return arrs


