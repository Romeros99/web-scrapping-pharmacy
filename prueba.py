#
# Ejemplo imperativo Web Scraping a www.cruzverde.cl
# Para el proyecto semestral deberá modificar considerando paradigmas solicitados
#

# Librerías
import time
from bs4 import BeautifulSoup
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
import csv

B_VERBOSE_DEBUG = True
B_VERBOSE_RESULT = True
with open('princios_activos.txt', 'r', encoding='utf8') as f:
    L_FIND = [line.strip() for line in f]

# Hacer una pausa en segundos para saltarse sleep de Python (le causa problemas al web driver)
def mySleep(nTimeOut):
    nTimeInit = time.time()
    nTimeDifference = time.time() - nTimeInit 
    while (nTimeDifference < nTimeOut):
        nTimeDifference = time.time() - nTimeInit

# Generar archivo HTML de salida
def outputHtml(sFile, lxmlData):
    fOutputHtml = open (sFile,'w')
    fOutputHtml.write(lxmlData.prettify())
    fOutputHtml.close()

# MAIN
if (__name__ == "__main__"):
    listResult = []
    for S_FIND in L_FIND:
        if (B_VERBOSE_DEBUG):
            print("=" * len("Principio activo: {}".format(S_FIND)))
            print("Principio activo: {}".format(S_FIND))
            print("=" * len("Principio activo: {}".format(S_FIND)))

        # Driver y carga de página
        chrome_options = Options()
        chrome_options.add_argument('--no-sandbox')
        chrome_options.add_argument('--disable-dev-shm-usage')
        driver = webdriver.Chrome(executable_path = r'C:\Users\Federico\Downloads\chromedriver_win32\chromedriver.exe', options = chrome_options)
        driver.get('https://www.cruzverde.cl/search?query={}'.format(S_FIND.replace(' ', '%20')))
        mySleep(5)

        # Dar click ante aparición de comuna
        try:
            sXpath = '/html/body/app-root/app-page/div[1]/div/main/or-modal-location/ml-modal/aside/section/div/div[4]/div/at-button/button'
            btnAccept = driver.find_element(By.XPATH, sXpath)
            btnAccept.click()
            mySleep(5)
        except:
            pass

        # Verificar si hay datos
        bOkExistData = False
        try:
            mySleep(100)
            sXpath = '/html/body/app-root/app-page/div[1]/div/main/tpl-search-result/div/section[2]/tpl-catalog/div/div[3]/div[2]/div[2]/div'
            btnPage1 = driver.find_element(By.XPATH, sXpath)
            bOkExistData = True
            print("Si entró")
        except Exception as e:
            pass

        # Iterar para todas las páginas
        nPage = 1
        while (bOkExistData):
            if (B_VERBOSE_DEBUG):
                print("Página {}".format(nPage))
    
            try:
                sXpath = '/html/body/app-root/app-page/div[1]/div/main/tpl-search-result/div/section[2]/tpl-catalog/div/div[3]/div[2]/div[2]/div'
                contentData = driver.find_element(By.XPATH, sXpath)
                htmlData = contentData.get_attribute('innerHTML')
                lxmlData = BeautifulSoup(htmlData, 'lxml')

                # Generar html
                outputHtml('cruzverde_{}_{}.html'.format(S_FIND, nPage), lxmlData)
                sNames = lxmlData.find_all('a', class_='font-open flex items-center text-green text-16 sm:text-18 leading-20 font-semibold ellipsis hover:text-green-light')
                sPrices = lxmlData.find_all('span', class_='font-bold text-orange')
                for i in range(len(sNames)):
                    listResult.append({'p_activo': S_FIND, 'nombre': sNames[i].span.string, 'precio': sPrices[i].string})
                    if (B_VERBOSE_DEBUG):
                        print(listResult[len(listResult) - 1])
                
                # Siguiente página
                if (nPage == 1):            # Para página 1 el siguiente es 2 
                    nPageDivFullXpathNext = 2
                elif (nPage % 4 == 0):      # Para páginas múltiplo de 4 la sigueinte es 7 
                    nPageDivFullXpathNext = 7
                else:                       # Para el resto se suma 3
                    nPageDivFullXpathNext = nPage % 4 + 3
                # Dar click a la siguiente página
                sXpath = '/html/body/app-root/app-page/div[1]/div/main/tpl-search-result/div/section[2]/tpl-catalog/div/div[3]/div[2]/div[2]/ml-pagination/div/div[{}]'.format(nPageDivFullXpathNext)
                mySleep(2)
                btnButtonNextPage = driver.find_element(By.XPATH, sXpath)
                btnButtonNextPage.click()
                mySleep(4)
            except:
                bOkExistData = False
            
            nPage = nPage + 1

        # Cierre del driver
        driver.close()
        driver.quit()

    # Imprimir capturas de datos
    """if (B_VERBOSE_RESULT):
        print("=" * len("Lista total:"))
        print("Lista total:")       
        print("=" * len("Lista total:"))
        print(*listResult, sep="\n")"""

for i in listResult:
    for key in i:
        print(key, i[key])

with open('ejemplo.csv', 'w') as csv_file:
    fieldnames = ['p_activo', 'nombre', 'precio']
    writer = csv.DictWriter(csv_file, fieldnames=fieldnames) 
    writer.writeheader()
    writer.writerows(listResult)