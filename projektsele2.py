import unittest
from selenium import webdriver
from time import sleep
from selenium.webdriver.support.ui import Select
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By

email = "seletest2020@op.pl"
email_firm = "firma@wp.pl"
name = "Anna"
surname = "Marchewka"
login = "seletest"
password = "Testowanie1?"
siedziba_poza_Polska = "Nie"
regon = "787824013"
nip = "5825077517"
nazwa_podmiotu = "Podmiot testowy"
pkd = "5229C"
pkd_nazwa = "DZIAŁALNOŚĆ POZOSTAŁYCH AGENCJI TRANSPORTOWYCH"
krs = "0000253153"
city = "Katowice"
ulica = "Warszawska"
budynek = "12"
lokal = "1"
postcode = "40-006"
telefon = "0327573333"
fax = "0327573333"
data_rozp = "2019-01-01"


class LsiRegistration(unittest.TestCase):

    def setUp(self):
        self.driver = webdriver.Chrome()
        self.driver.get('https://lsi-szkol.slaskie.pl/#/login')
        self.driver.maximize_window()
        # Czekaj max 5 sekund na elementy
        self.driver.implicitly_wait(5)

    def tearDown(self):
        self.driver.quit()

    def test_correct_registration(self):
        driver = self.driver
        logowanie = driver.find_element_by_name("username").send_keys(login)
        password_entry = driver.find_element_by_name("password").send_keys(password)
        signin = driver.find_element_by_id("btn-submit")
        signin.click()
        sleep(5)
        siedziba_poza_Polska = driver.find_element_by_id("nie_poza_pl").click()
        sleep(5)
        nr_regon = driver.find_element_by_id("regon").send_keys(regon)
        nr_nip = WebDriverWait(self.driver, 10).until(EC.element_to_be_clickable((By.XPATH, "//input[@id='nip']")))
        nr_nip.send_keys(nip)
        podmiot = WebDriverWait(self.driver, 10).until(EC.element_to_be_clickable((By.XPATH, "//input[@id='nazwa']")))
        podmiot.send_keys(nazwa_podmiotu)
        nr_pkd = WebDriverWait(self.driver, 10).until(EC.element_to_be_clickable((By.XPATH, "//input[@id='pkd_kod']")))
        nr_pkd.send_keys(pkd)
        nazwa_pkd = WebDriverWait(self.driver, 10).until(EC.element_to_be_clickable((By.XPATH, "//input[@id='pkd']")))
        nazwa_pkd.send_keys(pkd_nazwa)
        nr_krs = WebDriverWait(self.driver, 10).until(EC.element_to_be_clickable((By.XPATH, "//input[@id='krs']")))
        nr_krs.send_keys(krs)
        driver.find_element_by_id("button_lupa").click()
        sleep(5)
        input_city = driver.find_element_by_id("search.nazwa").send_keys(city)
        sleep(5)
        btn_submit_city = driver.find_element_by_xpath("//button[@title='Szukaj w tablicy']")
        btn_submit_city.click()
        sleep(5)
        select_city = driver.find_element_by_xpath("//button[@title='wybierz: Katowice [pow. Katowice / gmi. Katowice]']")
        select_city.click()
        driver.find_element_by_xpath("//div[5]/div/div/div/span/button").click()
        sleep(5)
        input_ulica = driver.find_element_by_id("search.value").send_keys(ulica)
        btn_submit_ulica = driver.find_element_by_xpath("//button[@title='Szukaj w tablicy']")
        btn_submit_ulica.click()
        select_ulica = driver.find_element_by_xpath("//button[@title='wybierz: Warszawska']")
        select_ulica.click()
        nr_budynek = WebDriverWait(self.driver, 10).until(EC.element_to_be_clickable((By.XPATH, "//input[@id='adr_budynek']")))
        nr_budynek.send_keys(budynek)
        nr_lokal = WebDriverWait(self.driver, 10).until(EC.element_to_be_clickable((By.XPATH, "//input[@id='adr_lokal']")))
        nr_lokal.send_keys(lokal)
        nr_kod_pocztowy = WebDriverWait(self.driver, 10).until(EC.element_to_be_clickable((By.XPATH, "//input[@id='adr_kod']")))
        nr_kod_pocztowy.send_keys(postcode)
        nr_telefon = WebDriverWait(self.driver, 10).until(EC.element_to_be_clickable((By.XPATH, "//input[@id='telefon']")))
        nr_telefon.send_keys(telefon)
        nr_fax = WebDriverWait(self.driver, 10).until(EC.element_to_be_clickable((By.XPATH, "//input[@id='fax']")))
        nr_fax.send_keys(fax)
        data_rozp_select = WebDriverWait(self.driver, 10).until(EC.element_to_be_clickable((By.XPATH, "//input[@id='data_rozp']")))
        data_rozp_select.click()
        data_rozp_select.send_keys(data_rozp)
        adres_email_firm = WebDriverWait(self.driver, 10).until(EC.element_to_be_clickable((By.XPATH, "//input[@id='email']")))
        adres_email_firm.send_keys(email_firm)
        forma_prawna_select = Select(driver.find_element_by_id("forma_prawna_id"))
        forma_prawna_select.select_by_visible_text("spółki z ograniczoną odpowiedzialnością - mikroprzedsiębiorstwo")
        forma_wlasnosci_select = Select(driver.find_element_by_id("forma_wlasnosci_id"))
        forma_wlasnosci_select.select_by_visible_text("Pozostałe krajowe jednostki prywatne")
        btn_osw = driver.find_element_by_id("osw_reprezentacja_podm").click()
        #btn_submit_profil = driver.find_element_by_xpath("//button[contains(text(),'Zapisz i wyjdź')]")
        # nie klikam Zapisz i wyjdź
        print ("Nie klikam Zapisz i wyjdź")

    def test_brak_nip(self):
        driver = self.driver
        logowanie = driver.find_element_by_name("username").send_keys(login)
        password_entry = driver.find_element_by_name("password").send_keys(password)
        signin = driver.find_element_by_id("btn-submit")
        signin.click()
        sleep(5)
        siedziba_poza_Polska = driver.find_element_by_id("nie_poza_pl").click()
        sleep(5)
        nr_regon = driver.find_element_by_id("regon").send_keys(regon)
        #nr_nip = WebDriverWait(self.driver, 10).until(EC.element_to_be_clickable((By.XPATH, "//input[@id='nip']")))
        #nr_nip.send_keys(nip)
        podmiot = WebDriverWait(self.driver, 10).until(EC.element_to_be_clickable((By.XPATH, "//input[@id='nazwa']")))
        podmiot.send_keys(nazwa_podmiotu)
        nr_pkd = WebDriverWait(self.driver, 10).until(EC.element_to_be_clickable((By.XPATH, "//input[@id='pkd_kod']")))
        nr_pkd.send_keys(pkd)
        nazwa_pkd = WebDriverWait(self.driver, 10).until(EC.element_to_be_clickable((By.XPATH, "//input[@id='pkd']")))
        nazwa_pkd.send_keys(pkd_nazwa)
        nr_krs = WebDriverWait(self.driver, 10).until(EC.element_to_be_clickable((By.XPATH, "//input[@id='krs']")))
        nr_krs.send_keys(krs)
        driver.find_element_by_id("button_lupa").click()
        sleep(5)
        input_city = driver.find_element_by_id("search.nazwa").send_keys(city)
        sleep(5)
        btn_submit_city = driver.find_element_by_xpath("//button[@title='Szukaj w tablicy']")
        btn_submit_city.click()
        sleep(5)
        select_city = driver.find_element_by_xpath("//button[@title='wybierz: Katowice [pow. Katowice / gmi. Katowice]']")
        select_city.click()
        driver.find_element_by_xpath("//div[5]/div/div/div/span/button").click()
        sleep(5)
        input_ulica = driver.find_element_by_id("search.value").send_keys(ulica)
        btn_submit_ulica = driver.find_element_by_xpath("//button[@title='Szukaj w tablicy']")
        btn_submit_ulica.click()
        select_ulica = driver.find_element_by_xpath("//button[@title='wybierz: Warszawska']")
        select_ulica.click()
        nr_budynek = WebDriverWait(self.driver, 10).until(EC.element_to_be_clickable((By.XPATH, "//input[@id='adr_budynek']")))
        nr_budynek.send_keys(budynek)
        nr_lokal = WebDriverWait(self.driver, 10).until(EC.element_to_be_clickable((By.XPATH, "//input[@id='adr_lokal']")))
        nr_lokal.send_keys(lokal)
        nr_kod_pocztowy = WebDriverWait(self.driver, 10).until(EC.element_to_be_clickable((By.XPATH, "//input[@id='adr_kod']")))
        nr_kod_pocztowy.send_keys(postcode)
        nr_telefon = WebDriverWait(self.driver, 10).until(EC.element_to_be_clickable((By.XPATH, "//input[@id='telefon']")))
        nr_telefon.send_keys(telefon)
        nr_fax = WebDriverWait(self.driver, 10).until(EC.element_to_be_clickable((By.XPATH, "//input[@id='fax']")))
        nr_fax.send_keys(fax)
        data_rozp_select = WebDriverWait(self.driver, 10).until(EC.element_to_be_clickable((By.XPATH, "//input[@id='data_rozp']")))
        data_rozp_select.click()
        data_rozp_select.send_keys(data_rozp)
        adres_email_firm = WebDriverWait(self.driver, 10).until(EC.element_to_be_clickable((By.XPATH, "//input[@id='email']")))
        adres_email_firm.send_keys(email_firm)
        forma_prawna_select = Select(driver.find_element_by_id("forma_prawna_id"))
        forma_prawna_select.select_by_visible_text("spółki z ograniczoną odpowiedzialnością - mikroprzedsiębiorstwo")
        forma_wlasnosci_select = Select(driver.find_element_by_id("forma_wlasnosci_id"))
        forma_wlasnosci_select.select_by_visible_text("Pozostałe krajowe jednostki prywatne")
        btn_osw = driver.find_element_by_id("osw_reprezentacja_podm").click()
        btn_submit_profil = driver.find_element_by_xpath("//button[contains(text(),'Zapisz i wyjdź')]")
        #errors = driver.find_elements_by_xpath("//div[@class='alert alert-dismissible msg-animate ng-scope alert-danger']")
        errors = driver.find_elements_by_xpath("//div[@id='error_msg']")
        visible_errors = []
        for error in errors:
            # Jesli jest widoczny, to dodaj do listy
            if error.is_displayed():
                visible_errors.append(error)
        assert len(visible_errors) == 1
        error_text = visible_errors[0].get_attribute("innerText")
        #assert error_text == "pole nie może być puste"
        assert error_text == "Formularz zawiera błędy - komunikaty znajdują się przy polach lub sekcjach, których dotyczą"

if __name__ == '__main__':
    unittest.main(verbosity=2)
