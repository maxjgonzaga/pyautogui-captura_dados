# Alertar e pedir informação no PyAutoGUI
import pyautogui
# Mensagem de alerta da automação
pyautogui.alert(text='Iniciando sua automação',title='Automação de Login',button='ok')
# Solcitando usuario digitar email armazenando na variavel email 
email = pyautogui.prompt(text='Digite seu email',title='dados de login')
# Solicitando usuario senha com maskara * armazenando na variavel senha
senha = pyautogui.password(text='digite sua senha',title='dados de login',mask='*')
# Posição do bloco de notas capturada com MouseInfo e clicando dentro do bloco de notas
pyautogui.click(707,217,duration=2)
# Escrevendo email no bloco de notas
pyautogui.typewrite(email)
#Enter para pular de linha 
pyautogui.press('enter')
# Escrevendo senha armazenada no bloco de notas 
pyautogui.typewrite(senha)
