import discord
from discord.ext import commands
from logic import quiz_questions  # Quiz sorularını içeren modül
# Görev 7 - defaultdict komutunu içe aktarın
from config import token  # Bot token'ını içeren dosya

# Bot için gerekli izinleri ayarlıyoruz
intents = discord.Intents.default()
intents.message_content = True

# Komut ön eki "!" olan botu oluşturuyoruz
bot = commands.Bot(command_prefix="!", intents=intents)

# Kullanıcıların cevaplarını ve hangi soruda olduklarını saklamak için sözlük
user_responses = {}
# Görev 8 - Kullanıcı puanlarını kaydetmek için puan sözlüğünü oluşturun


# Kullanıcıya soru gönderen fonksiyon
async def send_question(ctx_or_interaction, user_id):
    question = quiz_questions[user_responses[user_id]]  # Kullanıcının mevcut sorusu
    buttons = question.gen_buttons()  # Soru için butonları oluştur
    view = discord.ui.View()  # Butonları göstermek için View oluştur
    for button in buttons:
        view.add_item(button)

    # Eğer komutla çağrıldıysa farklı, etkileşimle çağrıldıysa farklı şekilde gönder
    if isinstance(ctx_or_interaction, commands.Context):
        await ctx_or_interaction.send(question.text, view=view)
    else:
        await ctx_or_interaction.followup.send(question.text, view=view)

# Bot hazır olduğunda çalışacak event
@bot.event
async def on_ready():
    print(f'Yeni giriş: {bot.user}!')  # Konsola botun giriş yaptığını yazdır

# Kullanıcı etkileşimlerini dinleyen event
@bot.event
async def on_interaction(interaction):
    user_id = interaction.user.id
    if user_id not in user_responses:
        # Eğer kullanıcı teste başlamadıysa uyar
        await interaction.response.send_message("Lütfen !start komutunu yazarak testi başlatın")
        return

    custom_id = interaction.data["custom_id"]  # Buton ID'sini al
    if custom_id.startswith("correct"):
        await interaction.response.send_message("Doğru cevap!")
       # Görev 9 - Doğru cevap için kullanıcıya puan ekleyin
    elif custom_id.startswith("wrong"):
        await interaction.response.send_message("Yanlış cevap!")

    # 📌Görev 5 - Kullanıcının soru sayacını artır
    user_responses[user_id] += 1

    # 📌Görev 6 - Kullanıcı tüm soruları yanıtladı mı kontrol et
    if user_responses[user_id] > len(quiz_questions) - 1:
        await interaction.followup.send("Sınav bitti!")  # Tüm sorular cevaplandı
    else:
        await send_question(interaction, user_id)  # Sıradaki soruyu gönder

# Kullanıcının testi başlatması için komut
@bot.command()
async def start(ctx):
    user_id = ctx.author.id
    if user_id not in user_responses:
        user_responses[user_id] = 0  # Kullanıcının soru sayacını başlat
        await send_question(ctx, user_id)  # İlk soruyu gönder

# Botu çalıştır
bot.run(token)
