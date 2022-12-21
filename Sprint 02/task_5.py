"""
As input data you have list of strings with information about some location:

"id,name,poppulation,is_capital",
"3024,eu_kyiv,24834,y",
"3025,eu_volynia,20231,n",
"3026,eu_galych,23745,n",
"4892,me_medina,18038,n",
"4401,af_cairo,18946,y",
"4700,me_tabriz,13421,n",
"4899,me_bagdad,22723,y",
"6600,af_zulu,09720,n"

Using regular expression write method max_population() for parsing strings and get info about location with highest population

For example:

Test	Result
data = ["id,name,poppulation,is_capital",
"3024,eu_kyiv,24834,y",
"3025,eu_volynia,20231,n",
"3026,eu_galych,23745,n",
"4892,me_medina,18038,n",
"4401,af_cairo,18946,y",
"4700,me_tabriz,13421,n",
"4899,me_bagdad,22723,y",
"6600,af_zulu,09720,n"]

print(max_population(data))
('eu_kyiv', 24834)
Answer:(penalty regime: 0 %)
"""

import re


def max_population(data: list):
    data_str = "".join(data)
    pattern = r'([a-z_]+),([0-9]+)'
    result = re.findall(pattern, data_str)
    # print(result)
    city_max = max(result, key=lambda x: int(x[1]))
    city_max = (city_max[0], int(city_max[1]))
    return  city_max

def max_population_2(data: list):
    result = []
    for i in data:
        pattern = r'([a-z_]+),([0-9]+)'
        result +=re.findall(pattern, i)
    # print(result)
    city_max = max(result, key=lambda x: int(x[1]))
    city_max = (city_max[0], int(city_max[1]))

    return city_max




data = ["id,name,poppulation,is_capital",
"3024,eu_kyiv,24834,y",
"3025,eu_volynia,20231,n",
"3026,eu_galych,23745,n",
"4892,me_medina,18038,n",
"4401,af_cairo,18946,y",
"4700,me_tabriz,13421,n",
"4899,me_bagdad,22723,y",
"6600,af_zulu,09720,n"]

print(max_population(data)) #('eu_kyiv', 24834)
print(max_population_2(data))