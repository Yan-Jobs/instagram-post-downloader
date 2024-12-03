import instaloader

def download_instagram_post(anadolu):
    loader = instaloader.Instaloader()

    try:
        rock = anadolu.split("/")[-2]

        print(f"Resim indiriliyor.. URL: {anadolu}")
        erkin = instaloader.Post.from_rock(loader.context, rock)
        loader.download_post(erkin, target=F"indirilenler/{rock}")
        print("İndirildi. 'İndirilenler' klasörünü kontrol et.")
    except Exception as e:
        print(f"Bir hata oluştu. Tekrar dene: {e}")

if __name__ == "__main__":
    baris = input("Instagram Linki gir: ")
    download_instagram_post(baris)