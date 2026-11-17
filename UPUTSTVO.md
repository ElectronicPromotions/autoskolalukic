# Autoškola Lukić · uputstvo za sajt

## Šta je u paketu

```
sajt/      ← ovo ide na hosting (GitHub Pages ili bilo koji statički hosting), sadržaj foldera u root repozitorija
izvor/     ← generator stranica: build.py, tekstovi sadrzaj.py, izgled base.css i extra.css (NE ide na hosting)
```

### Stranice (svaka sa svojim title, description, canonical, breadcrumbs i schema.org podacima)

| URL | Sadržaj |
|---|---|
| `/` | Početna (hero, kategorije, sljedeća predavanja, cijene, instruktori, galerija, najnovije objave, FAQ, kontakt) |
| `/kategorije/` | Pregled svih kategorija + tabela minimalne starosti |
| `/b-kategorija/` `/a-kategorija/` `/c-kategorija/` `/ce-kategorija/` `/d-kategorija/` | Posebna, detaljna stranica za svaku kategoriju |
| `/upis/` | Vodič: dokumenti, koraci, ispiti |
| `/teorijska-nastava/` | Teorija i prva pomoć |
| `/predavanja/` | **Raspored predavanja po grupama** (termini + spisak kandidata, pretraga po imenu) |
| `/novosti/` | **Violetine objave sa Facebooka** |
| `/instruktori/` `/o-nama/` `/cjenovnik/` `/galerija/` `/pitanja/` `/kontakt/` | Ostali segmenti |
| `/404.html` | Stranica „nije pronađeno” |

`sitemap.xml` sadrži sve stranice i fotografije (image sitemap). Nakon objave prijavite ga u Google Search Console.

---

## 1. Raspored predavanja (`/predavanja/`)

### Način A: fajl `sajt/podaci/predavanja.js`
Otvorite fajl i mijenjajte grupe. Svaka grupa izgleda ovako:

```js
{
  naziv: "Grupa 4",
  kategorija: "B",
  predavac: "Doc. dr Violeta Lukić Vujadinović",
  mjesto: "Učionica, Tina Ujevića 8",
  napomena: "",
  termini: [
    { datum: "2026-12-07", vrijeme: "17:00 do 18:30", tema: "Uvod u saobraćajne propise" },
    { datum: "2026-12-09", vrijeme: "17:00 do 18:30", tema: "Znakovi opasnosti" }
  ],
  kandidati: ["Amar H.", "Lejla M.", "Marko P."]
},
```

- Datum uvijek kao `GGGG-MM-DD`, vrijeme kao `17:00 do 18:30`.
- Sajt sam označava prošle termine (posivljeno), **SLJEDEĆE** i **DANAS**, i sortira grupe.
- **Kad unesete stvarne podatke, promijenite `primjer: true` u `primjer: false`** (inače se prikazuje žuta traka „Primjer rasporeda“).

> **Privatnost:** stranica je javna. Preporuka je upisivati kandidate kao „Ime P.“ (ime + početno slovo prezimena). Ako upišete puna imena, ona su vidljiva svima.

### Način B: Google tabela (najlakše za Violetu, sa telefona)
1. Napravite Google tabelu sa kolonama (prvi red):
   `Grupa | Kategorija | Datum | Vrijeme | Tema | Kandidati | Predavač | Mjesto | Napomena`
2. Svaki red = jedno predavanje. Kandidate upišite u kolonu **Kandidati** (u bilo kojem redu te grupe), razdvojene zarezom.
   Datum može biti `18.11.2026.` ili `2026-11-18`.
3. **Datoteka → Dijeli → Objavi na webu → (list) → CSV → Objavi**. Kopirajte link.
4. U `sajt/assets/postavke.js` zalijepite link u `predavanjaCSV: "..."`.

Od tada se sve mijenja samo u tabeli, a sajt čita tabelu pri svakom otvaranju (Google osvježava objavljeni CSV u roku od nekoliko minuta).

Kandidat može otvoriti i direktan link: `https://autoskolalukic.com/predavanja/?ime=Amar` i stranica odmah pokaže njegovu grupu.

---

## 2. Violetine objave sa Facebooka (`/novosti/`)

Postoje tri načina, koji se mogu kombinovati:

**a) Automatski (Facebook stranica / Page).** U `sajt/assets/postavke.js` upišite link:
`facebookStranica: "https://www.facebook.com/IME-STRANICE"`.
Na `/novosti/` se pojavljuje Facebookov prikaz najnovijih objava, i ažurira se sam.
⚠️ Radi samo za Facebook **stranicu** (Page), ne za lični profil. Ako Violeta objavljuje sa ličnog profila, koristite b) ili c).

**b) Link na pojedinačnu objavu.** U `sajt/podaci/objave.js` dodajte na vrh liste:
```js
{ datum: "2026-11-20", link: "https://www.facebook.com/.../posts/..." },
```
Sajt prikazuje originalnu objavu (objava mora biti **javna**).

**c) Prepisana objava (najbolje za Google).** Tekst objave postaje dio sajta, pa ga Google indeksira:
```js
{ datum: "2026-11-20", naslov: "Upis nove grupe", tekst: "…", slika: "/img/objave/upis.jpg", link: "https://www.facebook.com/…" },
```
Slike stavite u `sajt/img/objave/`. Najnovije objave idu **na vrh**. Promijenite `primjer: true` u `primjer: false`.

**Google tabela za objave (opcionalno):** kolone `Datum | Naslov | Tekst | Slika | Link`, objavite kao CSV (kao gore) i link upišite u `objaveCSV`.

Na početnoj stranici se automatski prikazuju 3 najnovije prepisane objave.

---

## 3. Cijene
U `izvor/sadrzaj.py` na vrhu: `CIJENA_GOTOVINA = None`, `CIJENA_RATE = None`.
Dok su `None`, sajt piše „Na upit” (umjesto ranijeg „___ KM”). Upišite npr. `'1.150 KM'` i pokrenite generator.

## 4. Izmjena tekstova stranica
Tekstovi su u `izvor/sadrzaj.py`, raspored stranice (header, footer) u `izvor/build.py`, a izgled u `izvor/base.css` (originalni dizajn) i `izvor/extra.css` (dodaci za podstranice). Nakon izmjene:
```
cd izvor
python3 build.py
```
Generator ponovo napravi sve stranice, `sitemap.xml` i `robots.txt` u folderu `sajt/`.
(Fajlovi `podaci/*.js`, `assets/main.js`, `assets/podaci.js` i `assets/postavke.js` generator ne dira, mijenjaju se direktno.)

## 5. Objava
Sadržaj foldera `sajt/` ide u root repozitorija/hostinga (tu su i `CNAME`, ikone, `site.webmanifest`, `og-image.jpg`).
Lokalni pregled: `cd sajt && python3 -m http.server 8000` → http://localhost:8000
(Dupli klik na .html neće raditi ispravno jer linkovi počinju sa `/`.)

## 6. Pravne činjenice korištene u tekstovima
Starosne granice po kategorijama, uslovi za CE i D, ograničenja za mlade vozače (70/90/120 km/h), rok ljekarskog uvjerenja (12 mjeseci) i prva pomoć (Crveni krst) preuzeti su iz Zakona o osnovama bezbjednosti saobraćaja na putevima u BiH (čl. 177, 184, 186, 193). Najava novih pravila od 1. 1. 2028. (B kategorija +5 časova, prvih 5 na poligonu): Ministarstvo komunikacija i prometa BiH, oktobar 2026. Prije objave neka Violeta pregleda ove dijelove.

## 7. Pravilo pisanja tekstova
Obraćamo se sa „ti”, kao i do sada, rečenice su kratke, bez nepotrebnih crtica. Brojevi telefona se pišu kao `065 537 043`.
