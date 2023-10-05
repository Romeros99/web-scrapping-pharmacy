# Librerías
from calendar import c
import time
from bs4 import BeautifulSoup
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By



B_VERBOSE_DEBUG = True
B_VERBOSE_RESULT = True
with open('princios_activos.txt', 'r', encoding='utf8') as f:
    L_FIND = [line.strip() for line in f]
print(L_FIND)

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
        driver = webdriver.Chrome(options = chrome_options)
        driver.get('https://www.farmaciasahumada.cl/catalogsearch/result/?q={}'.format(S_FIND.replace(' ', '+')))
        mySleep(2)
        
        # Dar click ante aparición de comuna

        # Verificar si hay datos
        bOkExistData = False
        try:
            sXpath = '/html/body/div[1]/main/div/div[1]/div[5]/div[2]/ol'
            btnPage1 = driver.find_element(By.XPATH, sXpath)
            bOkExistData = True
            numero = driver.find_element(By.XPATH, '/html/body/div[1]/main/div/div[1]/div[4]/span[3]')
            numero = int(numero.text.split(" ")[0])
            if(numero >24 and numero <=36): #3 paginas
                formato = 5
            elif(numero >36 and numero <=48): #4 paginas
                formato = 6
            elif(numero >48): #5 o mas paginas
                formato = 7   
        except:
            pass
        # Iterar para todas las páginas}
        print("FORMATO:{}, tipo: {} ".format(formato, type(formato)))
        x = 1
        while (bOkExistData):
            print(x)
            if (B_VERBOSE_DEBUG):
                print("Página {}".format(x))
    
            try:
                sXpath = '/html/body/div[1]/main/div/div[1]/div[5]/div[2]/ol'
                contentData = driver.find_element(By.XPATH, sXpath)
                htmlData = contentData.get_attribute('innerHTML')
                lxmlData = BeautifulSoup(htmlData, 'lxml')

                # Generar html
                outputHtml('farmacias_ahumada_{}_{}.html'.format(S_FIND, x), lxmlData)

                sNames = lxmlData.find_all('a', class_='product-item-link')
                sPrices = lxmlData.find_all('span', class_='price')

                for i in range(len(sNames)):
                    listResult.append({'p_activo': S_FIND, 'nombre': sNames[i].string.replace("\n",'').strip(), 'precio': sPrices[i].string})
                    if (B_VERBOSE_DEBUG):
                        print(listResult[len(listResult) - 1])
                if(x == 1):
                    sXpath = "/html/body/div[1]/main/div/div[1]/div[5]/div[3]/div[2]/ul/li[2]/a"
                else:
                    sXpath ="/html/body/div[1]/main/div/div[1]/div[5]/div[3]/div[2]/ul/li[{}]/a".format(formato)
                print(sXpath)
                mySleep(3)
                btnButtonNextPage = driver.find_element(By.XPATH, sXpath)
                btnButtonNextPage.click()
                mySleep(5)
            except Exception as ex:
                bOkExistData = False
            x +=1

        # Cierre del driver
        driver.close()
        driver.quit()

    # Imprimir capturas de datos
    if (B_VERBOSE_RESULT):
        print("=" * len("Lista total:"))
        print("Lista total:")       
        print("=" * len("Lista total:"))
        print(*listResult, sep="\n")
