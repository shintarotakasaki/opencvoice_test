import streamlit as st
from selenium import webdriver
from selenium.webdriver.common.by import By
import time

def click_button():
    driver = webdriver.Ie(executable_path='C:\\Program Files\\path\\IEDriverServer.exe')
    driver.get("http://cvoice.intra.tostem.co.jp/n_copq/koujyou/scripts/KoujyouIdx.asp")
    button = driver.find_element(By.XPATH, "//input[@value='納期回答管理']")
    button.click()
    time.sleep(5)
    driver.quit()

def main():
    st.title('納期回答管理ボタンをクリック')
    if st.button('実行'):
        click_button()
        st.write('ボタンがクリックされました！')

        wb = load_workbook(filename=file)
        sheet = wb.active
        st.write(f"Sheet title: {sheet.title}")

      else:
        st.write("エクセルファイル(.xlsx)をアップロードしてください")
        st.stop()
          
if __name__ == "__main__":
    main()
