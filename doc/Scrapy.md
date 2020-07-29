```
response.xpath('//h3[@class="wH7mg"]/text()').get()
'Worldwide'

 response.xpath('//div[contains(@class,"fNm5wd")]/div/text()').getall()

['Confirmed', '16,660,138', 'Recovered', '9,699,116', 'Deaths', '658,813']
```


```
response.xpath('//div[@class="mvmWx"]//time/@datetime').get()
'2020-07-29T04:08:37Z'

response.xpath('//div[@class="mvmWx"]//time/text()').get()
'Updated less than 1 hour ago'
```


```
response.xpath('//table[@class="pH8O4c"]//tr//td//text()').getall()
['16,660,138', '2,143', '9,699,116', '658,813', '4,426,281', '13,431', '2,151,219', 
'151,374', '2,484,649', '11,757', '1,721,560', '88,634', '1,483,156', '1,090', '952,743', '33,425', '823,515', '5,612', '612,217', '13,504', '459,761', '7,822', '287,313', '7,257', '402,697', '3,181', '261,457', '44,876', '395,005', '12,293', '276,452', '18,612', '349,800', '18,307', '322,332', '9,240', '300,692', '4,526', 'No data', 
'45,878', '296,273', '3,555', '257,019', '16,147', '280,610', '5,958', '150,376', '28,436', '275,225', '1,256', '242,436', '5,865', '270,831', '7,915', '225,624', '2,789', '267,385', '5,413', '136,690', '9,074', '246,488', '4,092', '198,756', '35,123', '229,185', '1,361', '127,414', '3,000', '227,982', '2,742', '211,561', '5,645', '207,950', '2,501', '190,796', '9,202', '183,804', '2,740', '81,311', '30,223', '173,342', '3,857', '75,070', '3,179', '115,332', '2,948', '81,062', '4,535', '114,994', '3,028', '100,134', '8,912', '109,880', '39,996', '106,603', '167', '102,051', '382', 
'60,539', '4,901', '92,947', '928', '35,959', '4,691', '84,648', '4,533', '54,404', 
'793', '84,060', '60', '78,944', '4,634', '83,673', '771', '26,617', '1,947', '82,279', '4,713', '5,900', '5,584', '79,494', '7,693', 'No data', '5,702', '77,904', '16,700', '58,587', '402', '71,181', '6,206', '21,478', '2,647', '67,366', '7,156', '60,669', '543', '66,575', '1,590', '36,744', '1,629', '66,428', '5,764', '18,132', '9,822', '66,293', '7,221', '32,182', '486', '65,149', '14,739', '55,681', '442', '64,690', '6,245', '32,014', '1,101', '62,223', '14,749', '36,181', '1,349', '59,546', '6,021', '52,905', '347']

>>> response.xpath('//table[@class="pH8O4c"]//tr//th//text()').getall()
['Location', 'Confirmed', 'New cases (last 60 days)', 'Cases per 1M people', 'Recovered', 'Deaths', 'Worldwide', 'United States', 'Brazil', 'India', 'Russia', 'South Africa', 'Mexico', 'Peru', 'Chile', 'United Kingdom', 'Iran', 'Spain', 'Pakistan', 'Saudi Arabia', 'Colombia', 'Italy', 'Bangladesh', 'Turkey', 'Germany', 'France', 'Argentina', 'Iraq', 'Canada', 'Qatar', 'Indonesia', 'Egypt', 'Kazakhstan', 'China (Mainland)', 'Philippines', 'Ecuador', 'Sweden', 'Oman', 'Bolivia', 'Belarus', 'Ukraine', 
'Belgium', 'Israel', 'Kuwait', 'Dominican Republic', 'Panama', 'United Arab Emirates']

>>> response.xpath('//table[@class="pH8O4c"]/tbody/tr//th//text()').getall()
['Worldwide', 'United States', 'Brazil', 'India', 'Russia', 'South Africa', 'Mexico', 'Peru', 'Chile', 'United Kingdom', 'Iran', 'Spain', 'Pakistan', 'Saudi Arabia', 'Colombia', 'Italy', 'Bangladesh', 'Turkey', 'Germany', 'France', 'Argentina', 'Iraq', 'Canada', 'Qatar', 'Indonesia', 'Egypt', 'Kazakhstan', 'China (Mainland)', 'Philippines', 'Ecuador', 'Sweden', 'Oman', 'Bolivia', 'Belarus', 'Ukraine', 'Belgium', 'Israel', 'Kuwait', 'Dominican Republic', 'Panama', 'United Arab Emirates']
>>> response.xpath('//table[@class="pH8O4c"]/thead/tr//th//text()').getall()
['Location', 'Confirmed', 'New cases (last 60 days)', 'Cases per 1M people', 'Recovered', 'Deaths']
```

