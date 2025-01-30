# **Projeto: Automação de Cadastro em Formulário Google Forms com Selenium**

## **Descrição**
Este projeto foi desenvolvido utilizando para automatizar o preenchimento e envio de um formulário do Google Forms. O objetivo é ler os dados de uma planilha e inseri-los automaticamente no formulário, garantindo que cada cadastro seja feito de forma individual e eficiente.

## **Ferramentas Utilizadas**
- **Python**: Linguagem principal do projeto.
- **Selenium**: Biblioteca utilizada para automação do navegador.
- **Pandas**: Utilizada para ler os dados da planilha Excel.
- **WebDriver Manager**: Gerencia a versão do ChromeDriver automaticamente.
- **Excel**:Utilizado para armazenar os dados dos usuários.

## **Funcionalidades**
✅ **Leitura dos dados** a partir de uma planilha Excel.  
✅ **Abertura do navegador** e navegação automática até o formulário.  
✅ **Preenchimento automático** dos campos (Nome, E-mail, Telefone, Endereço, Idade e Sexo).    
✅ **Envio do formulário e recarregamento** para o próximo cadastro.    
✅ **Possibilidade de interromper a execução manualmente** pressionando `Ctrl + C`.  

## **Fluxo de Execução**
1. O script lê os dados da planilha **AUTOMAÇÃO.xlsx**.
2. Para cada linha da planilha:
   - Abre o navegador.
   - Acessa o formulário.
   - Insere os dados automaticamente nos campos corretos.
   - Seleciona a opção de sexo.
   - Envia o formulário.
   - Fecha o navegador e aguarda antes do próximo cadastro.
3. Repete o processo até que todos os cadastros tenham sido concluídos.

## **Como Executar**
1. Clone este repositório:
   ```bash
   git clone https://github.com/Ebn0511/Automa-o-Web.git
   cd Automa-o-Web
   ```
2. Instale as bibliotecas necessárias:
   ```bash
   pip install selenium pandas openpyxl webdriver-manager
   ```
3. Certifique-se de que a planilha **AUTOMAÇÃO.xlsx** está no diretório correto.
4. Execute o script:
   ```bash
   python test_selenium.py
   ```
5. Para interromper a execução manualmente, pressione `Ctrl + C` no terminal.

## **Observações**
- O script utiliza o **ChromeDriver**, portanto, o Google Chrome precisa estar instalado na máquina.
- O caminho do arquivo **AUTOMAÇÃO.xlsx** deve ser ajustado caso esteja em um diretório diferente.
- Caso o Selenium não esteja funcionando corretamente, verifique se o ChromeDriver está atualizado usando:
  ```bash
  pip install --upgrade webdriver-manager
  ```

---


