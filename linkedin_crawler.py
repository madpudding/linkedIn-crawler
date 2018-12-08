#!/usr/bin/env python
# -*- coding:utf-8 -*-
# time 2018-11-(02-17)
# Author fcj
# message 领英数据爬取

import requests
from urllib import parse
from urllib import request
import re
from openpyxl import Workbook
from openpyxl.drawing.image import Image
import time
import random
import urllib
from Include.linkedin import linkedin_cookie
from Include.linkedin import linked_in_redis
import json
from datetime import timedelta
from collections import Counter


def linkedin_scrapy(link, img_url):
    print('in-in-in')
    wb = Workbook()
    ws1 = wb.create_sheet('领英个人信息', index=0)
    title_list = ['名字', '领英链接', '身份/职位', '工作地点', '领英个人简介', '领英经历中文翻译', '个人联系方式', '领英教育经历',
                  '领英工作经历', '个人照片', '个人微信二维码']
    ws1.append(title_list)

    name = ''
    office = ''
    location = ''
    person_summary = ''
    cn_summary = ''
    work_experience = []
    education_experience = []
    link_contact = []
    qr_content = ''

    headers = linkedin_cookie.normal_headers
    headers['user-agent'] = random.choice(linkedin_cookie.user_agent_list)
    headers['Referrer'] = random.choice(linkedin_cookie.referer_list)
    headers['cookie'] = random.choice(linkedin_cookie.normal_list)

    data = requests.get(url=link, headers=headers, verify=False)
    print('第一次linkedInUrl %s' % link)
    print('data.status_code %s' % data.status_code)

    if data.status_code != 200:
        link = link_url_transfer(link)
        data = requests.get(url=link, headers=headers, verify=False)
    r = data.content

    json_id = random.choice(linkedin_cookie.pro_cookie)
    json_re = re.findall('JSESSIONID="(.*?:.*?)"', str(json_id))
    if len(json_re) < 1:
        json_re = re.findall('JSESSIONID=(.*?:.*?);', str(json_id))

    info_headers = linkedin_cookie.pro_headers
    info_headers['path'] = info_url(link).replace('https://www.linkedin.com', '')
    info_headers['cookie'] = json_id
    info_headers['csrf-token'] = json_re[0].replace('JSESSIONID=', '').replace(';', '').replace('"', '')
    info_headers['referer'] = link
    info_headers['user-agent'] = random.choice(linkedin_cookie.user_agent_list)

    contact_data = requests.get(url=info_url(link), headers=info_headers, verify=False)
    print(info_url(link))
    if contact_data.status_code != 200:
        time.sleep(1)
        link = link_url_transfer(link)
        contact_data = requests.get(url=info_url(link), headers=info_headers, verify=False)

        print('link %s' % link)
        print("info_url %s" % info_url(link))
        print("contact status_code %s" % contact_data.status_code)

    info_content = str(contact_data.content, encoding='utf-8')

    content = str(r, encoding='utf-8')

    content_twice = urllib.parse.unquote(content).replace('&quot;', '"').replace('\t', '').replace('\xa0', '') \
        .replace('\u3000', '').replace("\x06", "").replace("\x05", "").replace("\x07", "").replace('&#92;', '') \
        .replace('&amp;', '').replace('O&#39;', '').replace('&#61;', '=').replace('0xff', '')

    info_twice = urllib.parse.unquote(info_content).replace('&quot;', '"').replace('\t', '').replace('\xa0', '') \
        .replace('\u3000', '').replace("\x06", "").replace("\x05", "").replace("\x07", "").replace('&#92;', '') \
        .replace('&amp;', '').replace('O&#39;', '').replace('&#61;', '=')

    profile_txt = ''.join(re.findall('(\{"data":\{"\*profile":.*?Profile"\}\]\})', content_twice))

    first_name = re.findall('"firstName":"(.*?)"', profile_txt)
    last_name = re.findall('"lastName":"(.*?)"', profile_txt)

    if first_name and last_name:
        name = str(first_name[0]) + str(last_name[0])

    summary = re.findall('"summary":"(.*?)"', profile_txt)
    if summary:
        person_summary = str(summary[0])
        cn_summary = translate_content(person_summary)

    occupation = re.findall('"headline":"(.*?)"', profile_txt)
    if occupation:
        office = str(occupation[0])

    location_name = re.findall('"locationName":"(.*?)"', profile_txt)
    if location_name:
        location = str(location_name[0])

    if 'not exist' not in img_url:
        person_image, status_code = get_link_image(img_url)
        if status_code == 200:
            name = name.replace(' ', '').replace('/', '')
            image = open('D:/银行/image/' + name + '.jpg', 'ab')
            image.write(person_image)
            image.close()

            image_png = open('D:/银行/image/' + name + '.png', 'ab')
            image_png.write(person_image)
            image_png.close()

            column_width = 90
            row_height = 90

            ws1.column_dimensions['J'].width = column_width
            ws1.row_dimensions[2].height = row_height

            try:
                img = Image('D:/银行/image/' + name + '.jpg')
                new_size = (90, 90)
                img.width, img.height = new_size
                ws1.add_image(img, 'J' + str(2))
            except Exception as e:
                img = Image('D:/银行/image/' + name + '.png')
                new_size = (90, 90)
                img.width, img.height = new_size
                ws1.add_image(img, 'J' + str(2))

    we_chat_txt = ' '.join(re.findall('"weChatContactInfo":\{.*?\}', info_twice))
    we_chat_image = re.findall('"qrCodeImageUrl":"(http.*?)"', we_chat_txt)
    we_chat_name = re.findall('"name":"(.*?)"', we_chat_txt)

    if we_chat_name:
        link_contact.append('微信昵称:' + we_chat_name[0] + ',')
        qr_content = str(we_chat_image[0].replace('&#61;', ''))
    elif we_chat_image:
        qr_content = str(we_chat_image[0].replace('&#61;', ''))

    if qr_content:
        image = open('D:/银行/wechat/' + name + '.jpg', 'ab')
        image_png = open('D:/银行/wechat/' + name + '.png', 'ab')
        img, sc = get_link_image(qr_content)
        if sc == 200:
            image.write(img)
            image.close()

            image_png.write(img)
            image_png.close()
            column_width = 90
            row_height = 90

            ws1.column_dimensions['K'].width = column_width
            ws1.row_dimensions[2].height = row_height
            try:
                img = Image('D:/法国兴业银行/wechat/' + name + '.jpg')
                new_size = (90, 90)
                img.width, img.height = new_size
                ws1.add_image(img, 'K' + str(2))
            except Exception as e:
                img = Image('D:/银行/wechat/' + name + '.png')
                new_size = (90, 90)
                img.width, img.height = new_size
                ws1.add_image(img, 'K' + str(2))

    website_txt = ' '.join(re.findall('("websites":.*?profile\.ProfileWebsite".*?\})', info_twice))
    website = re.findall('"url":"(.*?)"', website_txt)
    if website:
        for web in website:
            link_contact.append('个人网站:' + ''.join(web))

    educations = re.findall('("timePeriod".*?Education"\})', profile_txt)
    if educations:

        for one in educations:

            school_name = re.findall('"schoolName":"(.*?)",', one)
            field_of_study = re.findall('"fieldOfStudy":"(.*?)"', one)
            degree_name = re.findall('"degreeName":"(.*?)"', one)
            time_period = re.findall('("timePeriod".*?Education"\})', one)
            school_time = ''

            if time_period:

                start_year = re.findall('"startDate":\{.*?"year":(\d+),', one)
                start_month = re.findall('"startDate":{"month":(\d+),', one)
                end_year = re.findall('"endDate":\{.*?"year":(\d+),', one)
                end_month = re.findall('"endDate":{"month":(\d+)', one)
                start_date = ''
                end_date = ''

                if start_year:
                    start_date += '%s' % start_year[0]
                if start_month:
                    start_date += '.%s' % start_month[0]
                    end_date = ''
                if end_year:
                    end_date += '%s' % end_year[0]
                if end_month:
                    end_date += '.%s' % end_month[0]
                if len(start_date) > 0 and len(end_date) == 0:
                    end_date = '现在'
                school_time += '%s ~ %s' % (start_date + '入学', end_date + '毕业')

                if school_name:
                    field_of_study = '%s' % str(' 所学专业：' + field_of_study[0]) if field_of_study else ''
                    degree_name = '%s' % str('学位名称：' + degree_name[0]) if degree_name else ''
                    education_experience.append(str('学校名称：' + school_name[0]) + str(school_time) +
                                                str(field_of_study) + str(degree_name))

    position = re.findall('(\{"\$deletedFields":\[.*?profile\.Position"\},)', profile_txt)
    if position:
        for one in position:

            company_name = re.findall('"companyName":"(.*?)"', one)
            title = re.findall('"title":"(.*?)"', one)
            location_name = re.findall('"locationName":"(.*?)"', one)
            time_period = re.findall('("timePeriod".*?DateRange"\},)', one)
            description = re.findall('"description":"(.*?)"', one)
            position_time = ''

            if time_period:
                start_year = re.findall('"startDate":{.*?"year":(\d+),', one)
                start_month = re.findall('"startDate":{"month":(\d+),', one)
                end_year = re.findall('"endDate":{.*?"year":(\d+),', one)
                end_month = re.findall('"endDate":{(\d+)', one)

                start_date = ''

                if start_year:
                    start_date += '%s' % start_year[0]
                if start_month:
                    start_date += '.%s' % start_month[0]
                end_date = ''
                if end_year:
                    end_date += '%s' % end_year[0]
                if end_month:
                    end_date += '.%s' % end_month[0]
                if len(start_date) > 0 and len(end_date) == 0:
                    end_date = '现在'
                    position_time += '%s ~ %s' % (start_date + '入职', end_date)

                if company_name:
                    title = '%s' % title[0] if title else ''
                    location_name = '   %s' % location_name[0] if location_name else ''
                    work_experience.append(str(company_name[0]) + str(position_time) + str(title) + str(location_name) +
                                           ''.join(description))

    cache[link] = {'name': name, 'url': link, 'office': office, 'location': location, 'person_summary': person_summary,
                   'cn_summary': cn_summary, 'link_contact': ''.join(link_contact),
                   'education_experience': ''.join(education_experience), 'work_experience': ''.join(work_experience)}

    ws1.append([name, link, office, location, person_summary, ''.join(cn_summary), ''.join(link_contact),
                ''.join(education_experience), ''.join(work_experience)])

    wb.save('D:/银行/' + name + '.xlsx')

    # storage = location_choose(location)
    # if storage is True:
    #     ws1.append([name, link, office, location, person_summary, cn_summary, ''.join(link_contact),
    #                 ''.join(education_experience), ''.join(work_experience)])
    #
    #     wb.save('D:/肯锡/' + name + '.xlsx')
    # else:
    #     pass


# def location_choose(location):
#     address_list = ['china', '中国', 'China', '上海', '北京', '广州', '香港', '澳门', '深圳', '天津', '重庆', '苏州', '南京',
#                     '福州', '厦门', '台湾', '成都', '武汉', '杭州', '无锡']
#     res = list(filter(lambda x: x in location, address_list))
#     if len(res) > 0:
#         return True
#     else:
#         return False


def get_link_image(image_url):
    time.sleep(5)
    headers = linkedin_cookie.image_headers
    headers['path'] = str(image_url).replace('https://www.linkedin.com', '')

    headers['cookie'] = random.choice(linkedin_cookie.normal_list)

    if isinstance(image_url, str) is False:
        image_url = image_url.decode('utf-8')
    resp = requests.get(url=image_url, headers=headers, verify=False)
    if resp.status_code != 200:
        print(headers['path'])

    print('图片url状态 %s' % resp.status_code)
    return resp.content, resp.status_code


def info_url(link_url):
    info = 'https://www.linkedin.com/voyager/api/identity/profiles/'
    end_info = 'profileContactInfo'

    mid_url = str(link_url).replace('https://www.linkedin.com/in/', '').replace('https://www.linkedin.com/in', '')\
        .replace('www.linkedin.com', '').replace('https:///pub/', '')\
        .replace('https:///in/', '').replace('http:///in/', '').replace('http:///', '').replace('in/', '')

    if mid_url.endswith('/') is False:
        mid_url = mid_url + '/'
        mid_url = str(re.sub('\s+', '', mid_url))
    url_info = info + mid_url + end_info

    return url_info


def link_url_transfer(link_url):
    links = link_url.split('/')
    num = link_url[0:-11].replace('pub', 'in') + '-' + links[-1] + links[-2] + links[-3] + '/'
    c = Counter(num)
    if c['-'] > 3:
        num = exchange_link_url(num)
    return num


def exchange_link_url(num_url):
    name = num_url.split('-')
    last = ''

    if 'inin' in str(name[-1]):
        last = str(name[-1]).replace('inin/', '')
    elif str(name[-1]).endswith('in/'):
        last = str(name[-1]).replace('in/', '')

    if str(name[-2]) not in last:
        second = str(name[-2]) + '-' + last
        if str(name[-3]) not in second:
            third = str(name[-3]) + '-' + second
            if str(name[-4]) not in third:
                third = str(name[-4]) + '-' + third
        else:
            third = second
    else:
        third = last
    third = ' https://www.linkedin.com/in/'+third
    return third


def translate_content(content):  # 翻译
    form_data = {}

    translate_url = "https://fanyi.so.com/index/search"

    form_data['query'] = content

    form_data['eng'] = '1'

    data = parse.urlencode(form_data).encode('utf-8')

    response = '没有翻译成功'
    try:
        response = request.urlopen(translate_url, data)
    except Exception as e:
        pass

    html = response.read().decode("utf-8")  # 解码方式

    result = json.loads(html)

    if len(result["data"]) > 0:
        translate_result = result["data"]["fanyi"]
    else:
        translate_result = ['']

    return translate_result


def distance_message(dis_url, rf, g):

    cookie = random.choice(linkedin_cookie.dis_cookie)

    json_re = re.findall('JSESSIONID="(.*?:.*?)"', cookie)
    if len(json_re) < 1:
        json_re = re.findall('JSESSIONID=(.*?:.*?);', cookie)

    headers = linkedin_cookie.distance_headers
    headers['referer'] = str(rf)
    headers['user-agent'] = random.choice(linkedin_cookie.user_agent_list)
    headers['cookie'] = cookie
    headers['csrf-token'] = json_re[0].replace('JSESSIONID=', '').replace(';', '').replace('"', '')
    headers['path'] = str(dis_url).replace('https://www.linkedin.com/', '')

    r = requests.get(url=dis_url, headers=headers, verify=False)

    print(r.status_code)

    if r.status_code == 200:

        content = str(r.content, encoding='utf-8')
        content = urllib.parse.unquote(content).replace('&quot;', '"').replace('\t', '').replace('\xa0', '')\
            .replace('\u3000', '').replace("\x06", "").replace("\x05", "").replace("\x07", "").replace('&#92;', '') \
            .replace('&amp;', '').replace('O&#39;', '').replace('&#61;', '=')

        persons = re.findall('"included":\[.*?\}\]\}', content)

        if len(persons) > 0:
            one_person = re.findall('(\{"firstName":.*?"com.linkedin.voyager.identity.shared.MiniProfile"\})',
                                    persons[-1])
        else:
            one_person = re.findall('(\{"firstName":.*?"com.linkedin.voyager.identity.shared.MiniProfile"\})',
                                    ''.join(persons))
        img_list = []
        identity_list = []
        occupation_list = []
        name_list = []

        for one in one_person:
            identity_list.append(re.findall('"publicIdentifier":"(.*?)"', one)[0])
            occupation_list.append(re.findall('"occupation":"(.*?)"', one)[0])
            root_url = re.findall('"rootUrl":"(.*?)"', one)
            first_name = re.findall('"firstName":"(.*?)"', one)
            last_name = re.findall('"lastName":"(.*?)"', one)

            if first_name and last_name:
                name = str(first_name[0]) + str(last_name[0])
                # if len(name) > 5:
                #     name_list.append(name)

            if len(root_url) > 0:
                root_url = root_url[0]
                artifact = re.findall('"picture":\{.*?"fileIdentifyingUrlPathSegment":"(.*?)",.*?\}', one)
                image_url = str(root_url + str(artifact[0]).replace('v=', '&v=').replace('t=', '&t='))
                img_list.append(image_url)
            else:
                img_list.append('not exist')
        search_list = []
        for index, item in enumerate(identity_list):
            it = 'https://www.linkedin.com/in/' + parse.quote(str(item)) + '/'
            c = it + '~' + img_list[index]
            if 'UNKNOWN' not in c:
                search_list.append(c)

        print('len search_list %s' % str(len(search_list)))

        for se in search_list:
            g += 1
            all_url = se.split('~')
            link_u = all_url[0]
            img_url = all_url[1]
            # print('peoples %s' % str(g))
            print('link_u %s' % link_u)
            if cache.client.get(link_u) is None:
                time.sleep(15)
                linkedin_scrapy(link_u, img_url)

    else:
        distance_message(dis_url, rf, g=0)

    return g


if __name__ == '__main__':
    g = 0
    s = 0
    cache = linked_in_redis.RedisCache(expires=timedelta(days=10))

    url = ''
    i = 0
    ref = ''

    while (i<=140):
        url = url + str(int(i/10))

        if i < 10:
            ref = ref + str(2)
            s += distance_message(url, ref, g)
            ref = ''
        else:
            s += distance_message(url, ref, g)
            print(url)
            print('当前页码数 %s' % str(int(i / 10)+1))
            ref = ''
        i += 10
        ref = ref + str(int(i/10))
        url = ''
        print(s)
        time.sleep(20)
