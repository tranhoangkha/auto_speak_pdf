import pyttsx3
import PyPDF2
import keyboard
import msvcrt
sac = open('se.pdf', 'rb')
pdfReader = PyPDF2.PdfReader(sac)
pages = len(pdfReader.pages)
# print(pages)

bot = pyttsx3.init()
voices = bot.getProperty('voices')
bot.setProperty('voice', voices[1].id)
print('moi nhap trang can speak')
num = int(input())
print('toi trang ')
num_end = int(input())
for num in range(num,num_end):
    page = pdfReader.pages[num]
    text = page.extract_text()
    bot.say(text)

    if msvcrt.kbhit():
        key = msvcrt.getch()
        if key == b'q':
            break
bot.runAndWait()


