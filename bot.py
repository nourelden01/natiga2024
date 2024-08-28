from bs4 import BeautifulSoup
import requests
from telethon import TelegramClient, events

# request from emis.gov.eg
cookies = {
    '.AspNetCore.Antiforgery.SMJV7MxZWgE': 'CfDJ8MJ8Hb5aFJ5Glo-6p8ksbpVmpCrSMSA6rZ55-TND1vZ04PVIxLNqVm50-4k6azQDTxRJ6PP18weNTZ0-NVr6B7IZzBg6iXDVWI3A_vPZL1ZTAET6g-RTVRN9LKaihzq8992j5KABZJGO1dP7hg1AtkI',
    'BIGipServerTazalom-Pool': '453836042.47873.0000',
    'TS01b9443d028': '017f87671302b559aa4eea4f1c38e05f21155094751429bf94bb51b6ec4bfe7c9fc958c7dbfa28ceb7506e015a572c85ddaa3c26a3',
    '.AspNetCore.Mvc.CookieTempDataProvider': 'CfDJ8MJ8Hb5aFJ5Glo-6p8ksbpW2L1XPr-erGz9z542ThpUFE_CpmU78DZ9mqjkTqn1_EgjGLaMdrQJ1r_tD8wN4wohfLzSFWEf4f3cWdCTM0OV3GWI74qnwnUd0_DTTcdiP2QyQ9C2o7riBoTI4Nrhb1aM',
    'TS01b9443d': '01fd481861da757bbd69d88428c99f54a8006d7e1890478d573ba3026bd0f7f6c311ac753201ee53bb2c3d61462abdd9f08f966b14fb253a1107ed566915ba79d357a183d4025ef8481552301e51f652caa17763d115d06fb60ec9b0f4314d2cae10872d50',
    'TSe6c21afd027': '08877083daab2000956b56a1294e7ad4e39df56b0f0b1644d7a2a06ec58d2a997083ae38a067801d086366b8d11130004b1fe3b70e2d14a78a135df7e85bb2c0fa5c8828722b134fcf177069187027de321f859f771c3953e31b83f9bb713769',
}

headers = {
    'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7',
    'Accept-Language': 'en-US,en;q=0.9',
    'Cache-Control': 'max-age=0',
    'Connection': 'keep-alive',
    'Content-Type': 'application/x-www-form-urlencoded',
    'Origin': 'https://g12.emis.gov.eg',
    'Referer': 'https://g12.emis.gov.eg/',
    'Sec-Fetch-Dest': 'document',
    'Sec-Fetch-Mode': 'navigate',
    'Sec-Fetch-Site': 'same-origin',
    'Sec-Fetch-User': '?1',
    'Upgrade-Insecure-Requests': '1',
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/127.0.0.0 Safari/537.36',
    'sec-ch-ua': '"Not)A;Brand";v="99", "Google Chrome";v="127", "Chromium";v="127"',
    'sec-ch-ua-mobile': '?0',
    'sec-ch-ua-platform': '"Windows"',
}

params = {
    'csrt': '12199141908310883965',
}

# request from alahram
cookies2 = {
    '__cf_bm': 'v2FQfmRXWkNsuya7jFAjK81U_59o_3Sc.EfVo6fC7cI-1724595769-1.0.1.1-cRhfog55BXS36H6FqDA6uyr1.cdJ_zmgp3N8aCBB2bcBzgBzGZJ0mhChDKsYYVnr_bhRDH8uv2DVxrKgqwynjQ',
    '_ga': 'GA1.1.960193091.1724595770',
    'cf_clearance': 'l_JV6wf_GhLjkVnilgxkMEuWMZNd_U.R5tlDoT0LUew-1724595770-1.2.1.1-o7MyydpkxIeOJrYyt67El4ztScVbqeJS.YqeSAr87hfDbEn9y794xwH_.AMvsHo2CK.GTwGIAtuWxzbvxL.o6DQ9TZzwU7zECjD_cIXmlM1.2nS9Ib5urf7NVQXfViKWUH_fciGXkuk31fndVPRep8P3pQqC69Lx7mCOXL.Lu5QrUosp1.Vb5ZO6.iFpadxdEXspn678HsPfjFfH7WvK.HhceYvNkEUQvbJJPLe5nFigStKhu4rlx4Zi1ZHWDQYZgwLIJyBVjtnSEW7fcYEUFWcn_cGJ8dhRHBDusv2gN3RIs.zldA4Qtn_nXKQzrs0A_BkaS_xT6N5Vc.vU383qpFRanJGfWel6R5NWXbGr94s7fm0shpvTPzOVW_JTCdgA',
    '__gads': 'ID=4541e05987566d45:T=1724595771:RT=1724595771:S=ALNI_MYoGI66MKbvGTzomv8Dmvvne5ozgQ',
    '__gpi': 'UID=00000edc05d38e0a:T=1724595771:RT=1724595771:S=ALNI_MZkX9AwFyP0loZz_a_ms5c7GshzLA',
    '__eoi': 'ID=1b2184bb64e7701a:T=1724595771:RT=1724595771:S=AA-AfjYhUsa45i3GfAGQwOanfrev',
    '_ga_X3WCWTFPLM': 'GS1.1.1724595769.1.1.1724595801.0.0.0',
    '_ga_5LP8VJKL83': 'GS1.1.1724595769.1.1.1724595807.0.0.0',
}

headers2 = {
    'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7',
    'accept-language': 'en-US,en;q=0.9',
    'cache-control': 'max-age=0',
    'content-type': 'application/x-www-form-urlencoded',
    'origin': 'https://natega.ahram.org.eg',
    'priority': 'u=0, i',
    'referer': 'https://natega.ahram.org.eg/',
    'sec-ch-ua': '"Not)A;Brand";v="99", "Google Chrome";v="127", "Chromium";v="127"',
    'sec-ch-ua-mobile': '?0',
    'sec-ch-ua-platform': '"Windows"',
    'sec-fetch-dest': 'document',
    'sec-fetch-mode': 'navigate',
    'sec-fetch-site': 'same-origin',
    'sec-fetch-user': '?1',
    'upgrade-insecure-requests': '1',
    'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/127.0.0.0 Safari/537.36',
}


# settings telegram
api_id = 'YOUR_ID'
api_hash = 'YOUR_HASH'
bot_token = 'YOUR_BOT_TOKEN'

client = TelegramClient('natiga_emis_bot', api_id, api_hash)

@client.on(events.NewMessage(pattern='/start'))
async def start(event):
    await event.respond('مرحبا! استخدم الأمر /natiga ثم أدخل رقم الجلوس للحصول على النتيجة.')

@client.on(events.NewMessage(pattern='/natiga'))
async def natiga_instruction(event):
    await event.respond('يرجى إرسال رقم الجلوس .')

@client.on(events.NewMessage(pattern='/info'))
async def natiga_instruction(event):
    await event.respond("مرحبا بك في بوت نتيجة الثانوية العامة.\n\nلقد تم تطوير البوت من قبل @Nour_El_Den")

@client.on(events.NewMessage)
async def handler(event):
    number = event.message.text.strip()
    
    if number.startswith('/'):
        return  # Skip commands
    
    if not number.isdigit():
        await event.respond('يرجى إرسال رقم جلوس صحيح.')
        return

    # إعداد البيانات مع الرقم المتغير
    data = {
        'SeatingNo': number,
        '__RequestVerificationToken': 'CfDJ8MJ8Hb5aFJ5Glo-6p8ksbpW6y4v-O4yhwVO8_32rEtAQfXK15V4UqC8kBfSmftR7JRnCbiUuWbdBYCO_ExL_qfo5Wb7Ks9Sb-WBbewTAV7J1WatTBuS8TgSmhbSPLEAaJmk649aLlxBWmFPkHR8hk0Q',
    }
    data2 = {
        'seating_no': number,
    }
    
    try:
        response = requests.post('https://g12.emis.gov.eg/', params=params, cookies=cookies, headers=headers, data=data)
        response2 = requests.post('https://natega.ahram.org.eg/Home/Natega', cookies=cookies2, headers=headers2, data=data2)
        response.raise_for_status()
        response2.raise_for_status()
    except requests.RequestException as e:
        await event.respond(f'حدث خطأ في الاتصال: {str(e)}')
        return

    html_content = response.text
    soup = BeautifulSoup(html_content, 'html.parser')
    html_content2 = response2.text
    soup2 = BeautifulSoup(html_content2, 'html.parser')

    # استخراج البيانات الشخصية
    personal_info = soup.find('th')
    status = soup.find_all('h2')
    status_data = status[0].get_text(strip=True) if status else "حالة غير محددة"
    info1 = soup.find_all('td')
    if info1:
        data_list = [element.get_text(strip=True) for element in info1]
        
        # تأكد من أن لديك عدد كافٍ من العناصر
        if len(data_list) >= 8:
            personal_info_text = (
                f"حالة الطــــالب : {status_data}\n"
                f"رقم الجلوس: {data_list[0]}\n"
                f"الاسم: {data_list[1]}\n"
                f"المدرسة: {data_list[2]}\n"
                f"المديرية: {data_list[3]}\n"
                f"الإدارة: {data_list[4]}\n"
                f"اسم اللجنة: {data_list[5]}\n"
                f"عنوان اللجنة: {data_list[6]}\n"
                f"الهاتف: {data_list[7]}"
            )

            # استخراج نتائج الطالب
            res = soup2.find_all('span', class_='formatt2')
            res2 = soup2.find_all('span', class_='formatt4')
            

            results_text = (
                f"{res[0].text} {res2[0].text}\n"
                f"{res[1].text} {res2[1].text}\n"
                f"{res[2].text} {res2[2].text}\n"
                f"{res[3].text} {res2[3].text}\n"
                f"{res[11].text} {res2[11].text}\n"
                f"{res[8].text} {res2[8].text}\n"
                f"{res[12].text} {res2[12].text}\n"
                f"{res[9].text} {res2[9].text}\n"
                f"{res[10].text} {res2[10].text}\n"
                f"{res[4].text} {res2[4].text}\n"
                f"{res[5].text} {res2[5].text}\n"
                f"{res[6].text} {res2[6].text}\n"
                f"{res[7].text} {res2[7].text}\n"
                f"\n{res[13].text} {res2[13].text}\n"
                f"النسبة المئوية: {round((float(res2[13].text) / 410)*100,2)}%"
            )

            # استخراج المواد التي لا تضاف للمجموع
            additional_subjects = soup.find_all('th', class_='degreeFont')
            additional_subjects_data = {}
            for subject in additional_subjects:
                subject_name = subject.find_previous_sibling('th').get_text(strip=True)
                additional_subjects_data[subject_name] = subject.get_text(strip=True)

            additional_subjects_text = (
                f"التربية الدينية: {additional_subjects_data.get('التربية الدينية', 'غير متوفر')}\n"
                f"التربية الوطنية: {additional_subjects_data.get('التربية الوطنية', 'غير متوفر')}\n"
                f"الإقتصاد والإحصاء: {additional_subjects_data.get('الإقتصاد والإحصاء', 'غير متوفر')}\n"
            )

            # تجميع الرسالة النهائية
            final_result = f"{personal_info_text}\n\n{results_text}\n\n{additional_subjects_text}\nBot By @Nour_El_Den"
            await event.respond(final_result)
            print(number)
        else:
            await event.respond("لم يتم العثور على بيانات كافية.")
    else:
        await event.respond("لم يتم العثور على عناصر البيانات.")

if __name__ == '__main__':
    client.start(bot_token=bot_token)
    print("Bot is running...")
    client.run_until_disconnected()
