import time
import pandas as pd
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
import signal
import sys

# Captura interrupção manual
def interromper_selenium(sig, frame):
    print("\nAutomação interrompida pelo usuário.")
    sys.exit(0)

signal.signal(signal.SIGINT, interromper_selenium)

# Carregar dados da planilha Excel
def carregar_dados(caminho):
    df = pd.read_excel(caminho)
    return df

# Inicializar o navegador
def iniciar_navegador():
    servico = Service(ChromeDriverManager().install())
    driver = webdriver.Chrome(service=servico)
    return driver

# Função para preencher o formulário
def preencher_formulario(driver, linha):
    driver.get("https://docs.google.com/forms/d/e/1FAIpQLSe3Ermjt4oEp009wPxRMlpKUTxU1TNROtbpPhKFcyeSea8lGA/viewform")
    time.sleep(2)  # Espera a página carregar
    
    try:
        driver.find_element(By.XPATH, "//*[@id='mG61Hd']/div[2]/div/div[2]/div[1]/div/div/div[2]/div/div[1]/div/div[1]/input").send_keys(linha["nome"])
        driver.find_element(By.XPATH, "//*[@id='mG61Hd']/div[2]/div/div[2]/div[2]/div/div/div[2]/div/div[1]/div/div[1]/input").send_keys(linha["email"])
        driver.find_element(By.XPATH, "//*[@id='mG61Hd']/div[2]/div/div[2]/div[3]/div/div/div[2]/div/div[1]/div/div[1]/input").send_keys(str(linha["telefone"]))
        driver.find_element(By.XPATH, "//*[@id='mG61Hd']/div[2]/div/div[2]/div[4]/div/div/div[2]/div/div[1]/div/div[1]/input").send_keys(linha["endereço"])
        driver.find_element(By.XPATH, "//*[@id='mG61Hd']/div[2]/div/div[2]/div[5]/div/div/div[2]/div/div[1]/div/div[1]/input").send_keys(str(linha["idade"]))
        
        # Seleção do sexo
        if linha["sexo"].strip().lower() == "feminino":
            driver.find_element(By.XPATH, "//*[@id='mG61Hd']/div[2]/div/div[2]/div[6]/div/div/div[2]/div[1]/div/span/div/div[2]/label").click()
        elif linha["sexo"].strip().lower() == "masculino":
            driver.find_element(By.XPATH, "//*[@id='mG61Hd']/div[2]/div/div[2]/div[6]/div/div/div[2]/div[1]/div/span/div/div[1]/label").click()
        
        # Enviar formulário
        driver.find_element(By.XPATH, "//*[@id='mG61Hd']/div[2]/div/div[3]/div[1]/div[1]/div/span").click()
        time.sleep(3)  # Espera a submissão
        
    except Exception as e:
        print(f"Erro ao cadastrar: {linha['nome']}. Erro: {e}")

# Executar o script
def main():
    caminho_planilha =("/home/enzo-nunes/Downloads/AUTOMAÇÃO.xlsx")
    dados = carregar_dados(caminho_planilha)
    
    for _, linha in dados.iterrows():
        driver = iniciar_navegador()
        preencher_formulario(driver, linha)
        driver.quit()
        time.sleep(2)  # Pequeno intervalo entre cada envio

if __name__ == "__main__":
    main()


  # "/home/enzo-nunes/Downloads/AUTOMAÇÃO.xlsx