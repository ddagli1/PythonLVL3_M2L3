class Superhero:
    def __init__(self, real_name, superhero_name):
        self.__real_name = real_name  # private özellik (dışarıdan erişime kapalı)
        self.superhero_name = superhero_name  # public özellik

    # Gerçek isme (gizli kimliğe) erişim için bir getter metodu    
    @property
    def get_real_name(self):
        return self.__real_name

    # Gerçek ismi (gizli kimliği) değiştirmek için bir setter metodu
    @get_real_name.setter
    def set_real_name(self, new_real_name):
        if len(new_real_name) > 3:  # Uzunluk kontrolünün eklenmesi
            self.__real_name = new_real_name
        else:
            print("Gerçek adınızda en az 4 adet karakter bulunmalıdır.")

    def reveal_identity(self):
        print(f"Ben - {self.superhero_name}, Ben aslında- {self.__real_name}.")

# superhero nesnesi oluşturma
hulk = Superhero("Bruce Banner", "Hulk")

# public özelliğe erişim
print(hulk.superhero_name)

# private özelliğe (gizli kimliğe) doğrudan erişmeye çalışmak hata ile sonuçlanacaktır
#print(hulk.__real_name)

# Getter metoduyla private özelliğe erişim
#### Görev 1. Hulk nesnesinin private özelliğine erişmek için getter metodunu kullanın
print(hulk.get_real_name)

#### Görev 2. Hulk nesnesinin gerçek adını "Doktor Bruce Banner" olarak değiştirmek için setter metodunu kullanın
hulk.set_real_name = "Doktor Bruce Banner"
hulk.reveal_identity()
