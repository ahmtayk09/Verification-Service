import yagmail

# E-posta gönderen ve alıcı bilgileri
sender_email = "gönderici adresi"
receiver_email = "alıcı adresi"
subject = "Doğrulama Servis"


def gönder(mesaj):
    # Yagmail ile e-posta gönderme
    try:
        yag = yagmail.SMTP(sender_email, "UYGULAMA ŞİFRESİ")
        yag.send(
            to=receiver_email,
            subject=subject,
            contents= "Doğrulama Kodunuz: " + mesaj
        )
        print("E-posta gönderildi.")
    except Exception as e:
        print("E-posta gönderilirken hata oluştu:", e)
