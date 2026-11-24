# Autoškola DrivePro · uputstvo za sajt

## Šta je u paketu

```
sajt/      ← gotov sajt, ovo ide na hosting (Vercel ili bilo koji statički hosting)
izvor/     ← generator stranica: build.py, tekstovi sadrzaj.py, izgled base.css i extra.css (NE ide na hosting)
```

### Stranice (svaka sa svojim title, description, canonical, breadcrumbs i schema.org podacima)

| URL | Sadržaj |
|---|---|
| `/` | Početna (hero, kategorije, instruktori, kandidati, objave, FAQ, kontakt, traka „Teorija besplatna, obuka u do 5 rata”) |
| `/kategorije/` | Pregled svih kategorija + tabela minimalne starosti |
| `/b-kategorija/` `/a-kategorija/` `/c-kategorija/` `/ce-kategorija/` `/d-kategorija/` | Posebna stranica za svaku kategoriju |
| `/upis/` | Vodič: dokumenti, koraci, ispiti |
| `/teorijska-nastava/` | Besplatna teorija i prva pomoć |
| `/novosti/` | Objave autoškole |
| `/instruktori/` `/o-nama/` `/galerija/` `/pitanja/` `/kontakt/` | Ostali segmenti |
| `/404.html` | Stranica „nije pronađeno” |

`sitemap.xml` sadrži sve stranice. Nakon objave prijavite ga u Google Search Console.

### Boje
* Pozadina je bijela.
* Elementi (dugmad, oznake, kartice, auto): plava `#1D4ED8` i teget `#16257A` (iz znaka DrivePro), svijetloplava `#E8EEFF`.
* Narandžasta za glavnu akciju i sitne akcente: `#C94A0C` (dugmad sa bijelim tekstom), `#F97316` (linije, ivice), `#FDBA74` (tekst na plavom).
* Žuta `#FFCC00` je samo u logotipu, kao na originalnom znaku.
* Boje su u `izvor/extra.css`, u posljednja tri bloka na kraju fajla.

### Kontakti na sajtu
* Glavni broj (dugmad, hero, Google podaci): **Dalibor, 065 803 456**
* Drugi broj: **Vladana, 065 858 411**
* Adresa: **Hasana Bećirevića 3, 76100 Brčko**
* Instagram: **@driveproautoskola**

---

## 1. Galerija kandidata
Dok nema fotografija, na početnoj i na `/galerija/` stoji poziv na Instagram, a `/galerija/` je skrivena od Google pretrage.
Kad stignu fotografije:
1. Pretvorite ih u `.webp`, veličine 560 x 700 px, i stavite u `sajt/img/galerija/`.
2. U `izvor/sadrzaj.py` upišite ih u listu `GAL`, na primjer:
   `('kandidat-polozen-ispit', 'Kandidat Autoškole DrivePro Brčko nakon položenog ispita', 'Položen ispit')`
3. Pokrenite generator (tačka 3). Galerija se tada sama prikazuje, a stranica ulazi u sitemap.

## 2. Objave (`/novosti/`)
**a) Prepisana objava (najbolje za Google).** U `sajt/podaci/objave.js` dodajte na vrh liste:
```js
{ datum: "2026-11-20", naslov: "Upis nove grupe", tekst: "…", slika: "/img/objave/upis.jpg", link: "https://www.instagram.com/p/…" },
```
Slike stavite u `sajt/img/objave/`. Kad unesete prave objave, promijenite `primjer: true` u `primjer: false`.
Dok je `primjer: true`, objave se NE prikazuju na početnoj stranici.

**b) Facebook stranica.** Ako autoškola ima Facebook stranicu (Page), upišite link u `sajt/assets/postavke.js` (`facebookStranica`), pa se na `/novosti/` prikazuju objave sa nje.

**c) Google tabela (opcionalno):** kolone `Datum | Naslov | Tekst | Slika | Link`, objavite kao CSV i link upišite u `objaveCSV`.

## 3. Izmjena tekstova
Tekstovi su u `izvor/sadrzaj.py`, raspored stranice (header, footer, logo) u `izvor/build.py`, a izgled u `izvor/base.css` i `izvor/extra.css`. Nakon izmjene:
```
cd izvor
python3 build.py
```
Generator ponovo napravi sve stranice, `sitemap.xml` i `robots.txt` u folderu `sajt/`.
(Fajlovi `podaci/objave.js`, `assets/main.js`, `assets/podaci.js` i `assets/postavke.js` generator ne dira, mijenjaju se direktno.)

## 4. Objava
Napravite novi GitHub repozitorij, povežite ga sa Vercelom (Framework: Other), a `vercel.json` kaže Vercelu da objavi folder `sajt/`.
Ako ime projekta na Vercelu ne bude `autoskoladrivepro`, ili se kupi vlastiti domen, u `izvor/build.py` i `izvor/sadrzaj.py` promijenite `DOMAIN` i pokrenite generator.
Lokalni pregled: `cd sajt && python3 -m http.server 8000` → http://localhost:8000

## 5. Podaci preuzeti sa Instagrama @driveproautoskola (provjeriti sa Vladanom i Daliborom prije objave)
* Teoretska nastava je besplatna (bio profila).
* Plaćanje do 5 rata; termine praktične obuke i ispita kandidat bira sam (istaknuta priča „Uslovi za upis”).
* B kategorija: u proces obuke 3 mjeseca prije 18. rođendana, teorija 7 radnih dana, prva pomoć 2 dana, 35 časova vožnje.
* C kategorija: 21 godina, potrebna B ili C1; uz B ispit iz propisa i 20 časova vožnje, uz C1 samo praktični dio i 8 časova.
* Radionice za prevazilaženje straha od vožnje (objava „Zašto odabrati nas”).
* Adresa i vlasnica (Vladana Vujadinović): natpis na vozilu za obuku.

Pravne činjenice (starosne granice, mladi vozači, rok ljekarskog uvjerenja, prva pomoć) preuzete su iz Zakona o osnovama bezbjednosti saobraćaja na putevima u BiH (čl. 177, 184, 186, 193), a najava pravila od 1. 1. 2028. od Ministarstva komunikacija i prometa BiH (oktobar 2026).

## 6. Pravilo pisanja tekstova
Obraćamo se sa „ti”, rečenice su kratke, bez nepotrebnih crtica. Brojevi telefona se pišu kao `065 803 456`.
