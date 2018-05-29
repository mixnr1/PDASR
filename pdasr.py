import time
from selenium import webdriver
browser=webdriver.Chrome()
browser.get('http://www.dvi.gov.lv/pub/pub.php?f=spd')
with open('Personas_datu_aizsardzibas_specialistu_registrs.txt', mode='w', encoding='utf-8') as teksts:
    for i in range(1, 15):
        browser.get('http://www.dvi.gov.lv/pub/pub.php?f=spd')
        time.sleep(2)
        if i != 1:
            browser.find_element_by_link_text(str(i)).click()
        time.sleep(2)
        rows=browser.find_element_by_id('rectable').find_elements_by_tag_name('tr')
        registrs=[]
        for row in range(0, len(rows)):
            adre=rows[row].find_elements_by_tag_name('td')[1].get_attribute('title') #Personas datu apstrādes adreses
            spec=rows[row].find_elements_by_tag_name('td')[0].text #Speciālista vārds, uzvārds
            kont=rows[row].find_elements_by_tag_name('td')[1].text #Kontaktinformācija
            term=rows[row].find_elements_by_tag_name('td')[2].text #Termiņš
            kopa=f'Speciālista vārds, uzvārds:{spec}|Kontaktinformācija:'+kont.replace('\n', ' ')+f'|Termiņš{term}|'+adre.replace('\n', ' ')
            registrs.append(kopa)
            print(kopa)
        for m in range(0, len(registrs)):
            teksts.write(f'{registrs[m]}\n')
browser.close()
