# 📌Görev 2 - İhtiyacınız olan her şeyi içe aktarın
from discord import ui, ButtonStyle
class Question:
    def __init__(self, text, answer_id, *options):
        self.__text = text #sorunun metni
        self.__answer_id = answer_id #cevabın numarası
        self.options = options #tüm olası yanıtları içeren bir liste 
   #📌görev 1
    @property
    def text(self):
        return self.__text 

    def gen_buttons(self):
        # 📌Görev 3 - Dahili klavyeyi oluşturmak için bir metot oluşturun
        buttons = []
        for  i, option in enumerate (self.options):
            if i==self.__answer_id:
                  buttons.append(ui.Button(label=option, style=ButtonStyle.primary, custom_id=f'correct_{i}'))
            else:
                buttons.append(ui.Button(label=option, style=ButtonStyle.primary, custom_id=f'wrong_{i}'))
        return buttons

# 📌Görev 4 - Listeyi sorularınızla doldurun
quiz_questions = [
   Question("Kediler onları kimse görmediğinde ne yapar?", 1, "Uyurlar", "Espri yazarlar"),
   Question("Kediler sevgilerini nasıl ifade ederler?", 0, "Yüksek sesle mırıldanırlar", "Sevimli fotoğraflar", "Havlar"),
   Question("Kediler hangi kitapları okumayı sever?", 3, "Kişisel gelişim kitapları", "Zaman yönetimi: Günde 18 saat nasıl uyunur","Sahibinizden 5 dakika erken uyumanın 101 yolu", "İnsan yönetimi rehberi")
]

