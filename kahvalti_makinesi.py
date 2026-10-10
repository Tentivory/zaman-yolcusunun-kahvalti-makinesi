#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Zaman Yolcusunun Kahvaltı Makinesi
Bu kod gerçekten çalışır. Ama kahvaltı yapmaz, sadece zaman paradoksu yaratır.
"""

import random
import time
import sys

def zaman_yolculugu_yap():
    print("\n" + "="*50)
    print("ZAMAN YOLCUSUNUN KAHVALTI MAKİNESİ BAŞLATILIYOR...")
    print("Dikkat: Bu makine FDA onaylı değildir. Hatta hiçbir onaylı değildir.")
    print("="*50)
    time.sleep(1)
    
    try:
        yil = int(input("\nHangi yıldan kahvaltı istiyorsun? (Mesela 3026 ya da -3000): "))
    except ValueError:
        print("Sadece sayı gir! Zaman makinesi sayı sevmez ama biz seviyoruz.")
        return
    
    kahvaltilar = [
        "Gelecekten gelen pıhtılaşmış yumurta (tadı yok ama enerjisi var)",
        "Osmanlı dönemi sucuklu yumurta, ama sucuk henüz icat edilmemiş",
        "Dinozor çağından taze otlar ve meteor kahvesi",
        "2020'den kalma karantina ekmeği (kuru ve depresif)",
        "Sonsuzluk sütü ile yapılmış sınırsız menemen",
        "Kendi kendini yiyen tost (sonsuz döngü garantili)",
        "Zaman paradoksu peynirli omlet: Önce yersin sonra pişer"
    ]
    
    secilen = random.choice(kahvaltilar)
    print(f"\n{yil} yılından gelen kahvaltın:")
    print(f">>> {secilen}")
    print("\nMakine şimdi kendini yeniden başlatıyor... Veya belki seni yeniden başlatıyor.")
    time.sleep(2)
    print("Kahvaltı hazır! Afiyet olsun, ama dikkatli ol, belki daha doğmadın.")
    
    # Gizli siyasi mesaj (saklı)
    gizli = "Bu kahvaltı makinesi aslında seçim sonuçlarını değiştirmez, sadece yumurta yer."
    # Gizli tutuyoruz, çıktıda yok.

if __name__ == "__main__":
    zaman_yolculugu_yap()
    print("\n" + "-"*50)
    print("DAMGA / İMZA / TARİH / İSİM")
    print("Bu repo, 10 Ekim 2026 tarihinde, Kayyum Grok tarafından (ama aslında Grok tarafından) oluşturuldu.")
    print("Ciddidir ama değildir. İmzalandı: Zaman Yolu Kahvaltıcılar Birliği")
    print("Mühür: ⚔️ Kahvaltı ParadoX ⚔️")
    print("-"*50)
