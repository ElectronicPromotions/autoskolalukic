# -*- coding: utf-8 -*-
"""Sadržaj svih stranica sajta Autoškole Lukić (Brčko)."""
import os, re

HERE = os.path.dirname(os.path.abspath(__file__))
CARSYM = open(os.path.join(HERE, 'carsym.svg'), encoding='utf-8').read()
DOMAIN = 'https://autoskolalukic.vercel.app'
ORG = {"@id": DOMAIN + '/#autoskola'}

# Cijene: upišite iznos (npr. '1.150 KM') ili ostavite None, pa se prikazuje "Na upit"
CIJENA_GOTOVINA = None
CIJENA_RATE = None

TV = '<a href="tel:+38765537043">065 537 043</a>'
TD = '<a href="tel:+38765803456">065 803 456</a>'
MAPS = 'https://www.google.com/maps/search/?api=1&amp;query=Tina+Ujevi%C4%87a+8+Br%C4%8Dko+76100'
ZAKON = 'Zakon o osnovama bezbjednosti saobraćaja na putevima u BiH'


def strip_tags(s):
    return re.sub(r'\s+', ' ', re.sub(r'<[^>]+>', '', s)).replace('&amp;', '&').strip()


# ---------------------------------------------------------------- helpers
def side(path, title='Kategorije', links=None):
    if links is None:
        links = [('/b-kategorija/', 'B kategorija, automobil'), ('/a-kategorija/', 'A kategorija, motocikl'),
                 ('/c-kategorija/', 'C1 i C, kamion'), ('/ce-kategorija/', 'CE, kamion s prikolicom'),
                 ('/d-kategorija/', 'D, autobus')]
    ac = ' aria-current="page"'
    ls = ''.join(f'<a href="{p}"{ac if p == path else ""}>{n}</a>' for p, n in links)
    return f'''<aside class="side">
  <div class="scard"><h3>Upis i informacije</h3><p>Tina Ujevića 8, Brčko. Pozovi i dogovori termin upisa, cijenu i rate.</p>
    <a href="tel:+38765537043" class="btn btn-y">📞 Violeta 065 537 043</a>
    <a href="tel:+38765803456" class="btn btn-g">📞 Dalibor 065 803 456</a></div>
  <nav class="sl" aria-label="{title}"><h3>{title}</h3>{ls}</nav>
  <nav class="sl" aria-label="Korisno"><h3>Korisno</h3><a href="/upis/">Kako do vozačke dozvole</a><a href="/predavanja/">Raspored predavanja</a><a href="/cjenovnik/">Cijene i rate</a><a href="/pitanja/">Česta pitanja</a></nav>
</aside>'''


def art(prose, aside, alt=False):
    return f'<section class="sec{" alt" if alt else ""}"><div class="wrap art"><article class="prose">{prose}</article>{aside}</div></section>'


def related(title, items, alt=True):
    cards = ''.join(f'<a class="card tilt" href="{p}"><i class="gl"></i><span class="lt2">{b}</span><h3>{h}</h3><p>{t}</p><span class="more">Saznaj više →</span></a>' for p, b, h, t in items)
    k4 = ' k4' if len(items) == 4 else ''
    return f'<section class="sec{" alt" if alt else ""}"><div class="wrap"><h2 class="t rvl">{title}</h2><div class="hub{k4} rvl">{cards}</div></div></section>'


def faq_block(qa, title='Česta pitanja', alt=False):
    out = []
    for i, (q, a) in enumerate(qa):
        out.append(f'<details class="fq"{" open" if i == 0 else ""}><summary><span class="fn">{i+1:02d}</span><span>{q}</span></summary><p>{a}</p></details>')
    return f'''<section class="sec{" alt" if alt else ""}"><div class="wrap faqw">
<aside class="faqa rvl"><div class="qm" aria-hidden="true">?</div><h2>{title}</h2><p>Ako nešto nije jasno, nazovi nas. Odgovaramo na sva pitanja prije upisa.</p><a href="tel:+38765537043" class="btn btn-y">📞 065 537 043</a></aside>
<div class="faq rvl">{"".join(out)}</div></div></section>'''


def svc(name, path, desc):
    return {"@type": "Service", "@id": DOMAIN + path + '#usluga', "name": name, "serviceType": "Obuka vozača",
            "description": desc, "provider": ORG, "areaServed": [{"@type": "City", "name": "Brčko"}, {"@type": "AdministrativeArea", "name": "Brčko distrikt BiH"}],
            "url": DOMAIN + path,
            "offers": {"@type": "Offer", "availability": "https://schema.org/InStock", "url": DOMAIN + "/cjenovnik/",
                       "seller": ORG, "description": "Gotovinsko plaćanje ili plaćanje na rate"}}


ALL_KAT = [('/b-kategorija/', 'B', 'B kategorija', 'Putnički automobil. Najtraženija kategorija, od 18 godina.'),
           ('/a-kategorija/', 'A', 'A kategorija', 'Motocikli. Obuka na poligonu i u saobraćaju, od 18 godina.'),
           ('/c-kategorija/', 'C1·C', 'C1 i C kategorija', 'Teretna vozila. C1 od 18, C od 21 godine.'),
           ('/ce-kategorija/', 'CE', 'CE kategorija', 'Kamion s prikolicom, za vozače koji već imaju C.'),
           ('/d-kategorija/', 'D', 'D kategorija', 'Autobusi, od 24 godine, uz prethodnu B, C ili D1.')]


def other_kat(path):
    return [k for k in ALL_KAT if k[0] != path]


# ---------------------------------------------------------------- HOME
def home_ld(D, org_id):
    return [
        {"@type": "DrivingSchool", "@id": org_id, "name": "Autoškola Lukić",
         "alternateName": ["Autoskola Lukic", "Autoškola Lukić Brčko", "Auto škola Lukić"],
         "url": D + "/", "image": [D + "/og-image.jpg", D + "/img/galerija/teoretska-nastava-ucionica.webp"], "logo": D + "/android-chrome-512x512.png",
         "description": "Autoškola Lukić u Brčkom: 25 godina iskustva, obuka za A, B, C1, C, CE i D kategoriju, plaćanje na rate, teoriju drži doktor nauka iz saobraćaja.",
         "slogan": "Vozi sigurno. 25 godina sa vama.", "telephone": "+387 65 537 043",
         "contactPoint": [
             {"@type": "ContactPoint", "contactType": "upis i informacije", "telephone": "+387 65 537 043", "name": "Violeta", "availableLanguage": ["bs", "hr", "sr"]},
             {"@type": "ContactPoint", "contactType": "časovi vožnje", "telephone": "+387 65 803 456", "name": "Dalibor", "availableLanguage": ["bs", "hr", "sr"]}],
         "address": {"@type": "PostalAddress", "streetAddress": "Tina Ujevića 8", "addressLocality": "Brčko", "postalCode": "76100", "addressRegion": "Brčko distrikt", "addressCountry": "BA"},
         "hasMap": "https://www.google.com/maps/search/?api=1&query=Tina+Ujevi%C4%87a+8+Br%C4%8Dko+76100",
         "areaServed": [{"@type": "City", "name": "Brčko"}, {"@type": "AdministrativeArea", "name": "Brčko distrikt BiH"},
                        {"@type": "Place", "name": "Bijela"}, {"@type": "Place", "name": "Brka"}, {"@type": "Place", "name": "Gornji Rahić"}, {"@type": "Place", "name": "Maoča"}],
         "sameAs": ["https://www.instagram.com/autoskolalukic"],
         "paymentAccepted": "Gotovina, plaćanje na rate", "currenciesAccepted": "BAM", "knowsLanguage": "bs",
         "employee": [{"@type": "Person", "@id": D + "/instruktori/#violeta", "name": "Violeta Lukić Vujadinović", "honorificPrefix": "Doc. dr", "jobTitle": "Predavač teorijske nastave"},
                      {"@type": "Person", "@id": D + "/instruktori/#dalibor", "name": "Dalibor Vujadinović", "jobTitle": "Instruktor vožnje"}],
         "hasOfferCatalog": {"@type": "OfferCatalog", "name": "Obuka vozača", "itemListElement": [
             {"@type": "Offer", "itemOffered": {"@id": D + p + "#usluga", "@type": "Service", "name": "Obuka za " + n + " u Brčkom", "url": D + p}} for p, b, n, t in ALL_KAT]}},
        {"@type": "WebSite", "@id": D + "/#website", "url": D + "/", "name": "Autoškola Lukić Brčko", "inLanguage": "bs", "publisher": {"@id": org_id}},
        {"@type": "WebPage", "@id": D + "/#stranica", "url": D + "/", "name": "Autoškola Brčko | Lukić, vozačka dozvola B kategorije i plaćanje na rate",
         "isPartOf": {"@id": D + "/#website"}, "about": {"@id": org_id}, "inLanguage": "bs", "dateModified": "2026-11-17"},
        {"@type": "FAQPage", "@id": D + "/#pitanja", "inLanguage": "bs", "mainEntity": [
            {"@type": "Question", "name": q, "acceptedAnswer": {"@type": "Answer", "text": strip_tags(a)}} for q, a in HOME_FAQ]}]


HOME_FAQ = [
    ('Gdje se nalazi Autoškola Lukić u Brčkom?', 'Autoškola Lukić nalazi se u ulici Tina Ujevića 8, 76100 Brčko. Primamo kandidate iz cijelog Brčko distrikta i okoline.'),
    ('Koje kategorije vozačke dozvole nudite?', 'U Autoškoli Lukić možeš se obučiti za A, B, C1, C, CE i D kategoriju. B kategorija je najtraženija.'),
    ('Koliko košta autoškola u Brčkom?', 'Cijena zavisi od kategorije i načina plaćanja, gotovinski ili na rate. Paket obuhvata teorijsku nastavu, fond časova vožnje te prijavu i polaganje ispita. Nazovi nas i dobit ćeš tačnu ponudu.'),
    ('Mogu li autoškolu platiti na rate?', 'Možeš. Pored gotovinskog plaćanja nudimo i plaćanje na rate, a uslove dogovaramo prilikom upisa.'),
    ('Kako se upisati i koji su dokumenti potrebni?', 'Dovoljno je da nazoveš 065 537 043 ili dođeš na adresu Tina Ujevića 8. Obično su potrebni važeća lična karta, prijava boravka i ljekarsko uvjerenje o zdravstvenoj sposobnosti za vozača, a za B kategoriju najmanje 18 godina. Tačan spisak potvrđujemo pri upisu.'),
    ('Ko predaje teoriju, a ko vodi vožnju?', 'Teoriju predaje Doc. dr Violeta Lukić Vujadinović, doktor nauka iz oblasti saobraćaja i licencirani predavač. Časove vožnje vodi instruktor Dalibor Vujadinović, strpljivo i bez pritiska.'),
]

GAL = [('kandidati-ispred-skolskog-automobila', 'Kandidati autoškole Lukić Brčko ispred školskog automobila', 'Novi vozači ispred školskog auta'),
       ('kandidat-polozen-vozacki-ispit', 'Kandidat autoškole Lukić Brčko nakon položenog ispita', 'Položen ispit, vozačka u rukama'),
       ('kandidat-ispred-automobila-za-obuku', 'Kandidat ispred automobila za obuku vožnje u Brčkom', 'Spreman za samostalnu vožnju'),
       ('kandidatkinja-palac-gore', 'Kandidatkinja autoškole Lukić pokazuje palac gore', 'Palac gore za položen ispit'),
       ('teoretska-nastava-ucionica', 'Teoretska nastava u učionici Autoškole Lukić Brčko', 'Predavanje u našoj učionici'),
       ('kandidat-podignuti-palcevi', 'Kandidat sa podignutim palcima ispred auta za obuku vožnje', 'Još jedan novi vozač')]


def gal_html(items):
    return ''.join(f'<a class="gi" href="/img/galerija/{f}.webp" data-lb><img src="/img/galerija/{f}.webp" alt="{a}" width="560" height="700" loading="lazy" decoding="async"><span class="cap">{c}</span></a>' for f, a, c in items)


def price(v):
    return v if v else 'Na upit'


def home():
    faq = ''.join(f'<details class="fq"{" open" if i == 0 else ""}><summary><span class="fn">{i+1:02d}</span><span>{q}</span></summary><p>{a}</p></details>' for i, (q, a) in enumerate(HOME_FAQ))
    tag = '<span class="tag">NAJTRAŽENIJA</span>'
    kat_cards = ''.join(f'<a class="card tilt{" hot" if b == "B" else ""}" href="{p}"><i class="gl"></i>{tag if b == "B" else ""}<span class="lt2">{b}</span><h3>{n} u Brčkom</h3><p>{t}</p><span class="more">Detalji obuke →</span></a>' for p, b, n, t in ALL_KAT)
    kat_cards += '<a class="card tilt" href="/teorijska-nastava/" style="background:linear-gradient(145deg,#DC2626,var(--blue-d));color:#fff;border:0"><i class="gl"></i><span class="lt2">Dr</span><h3>Teoretska nastava</h3><p style="color:#F6E7E1">Moderna učionica i predavač sa doktoratom iz oblasti saobraćaja. Gradivo učiš s razumijevanjem, ne napamet.</p><span class="more" style="color:var(--yel)">O predavanjima →</span></a>'
    hero = f'''<section id="pocetna" class="hero">
  <div class="orb o1"></div><div class="orb o2"></div>
  <div class="wrap hg">
    <div>
      <span class="chip">🚦 Vozi sigurno</span>
      <h1>Autoškola Lukić u Brčkom<br><span>25 godina sa vama.</span></h1>
      <p class="l">Vozačka dozvola A, B, C1, C, CE i D kategorije u Brčkom. Iskusni instruktori, strpljiv pristup i obuka koja te priprema za stvarni saobraćaj, a ne samo za ispit.</p>
      <div class="cta">
        <a href="/kontakt/" class="btn btn-y">Zakaži obuku →</a>
        <a href="tel:+38765537043" class="btn btn-g">📞 065 537 043</a>
      </div>
    </div>
    <div class="stage" id="stage">
      <div class="coin-wrap"><div class="coin" id="coin"></div><div class="coin-shadow"></div></div>
      <div class="chips">
        <div class="fs"><b>25</b><span>godina iskustva</span></div>
        <div class="fs fs2"><b>Dr</b><span>predavač teorije</span></div>
        <div class="fs fs3"><b>0</b><span>pritiska na vožnji</span></div>
      </div>
      <svg class="car" id="car" viewBox="0 0 600 250" role="img" aria-label="Školski automobil Autoškole Lukić Brčko, tel. 065 537 043"><use href="#carsym"/></svg>
    </div>
  </div>
  <div class="road"></div>
  <div class="curb"></div>
</section>
<div class="mq"><div class="mqm"><div id="mq" aria-live="off"></div></div></div>'''
    body = f'''<section id="o-nama" class="sec">
  <div class="wrap">
    <h2 class="t rvl">Zašto izabrati <em>Autoškolu Lukić</em> u Brčkom?</h2>
    <ul class="facts rvl">
      <li><b>A, B, C1, C, CE, D</b><span>Teorija, vožnja i prijava ispita</span></li>
      <li><b>Plaćanje na rate</b><span>Dogovor na upisu</span></li>
      <li><b>Dr predavač</b><span>Teoriju drži doktor nauka iz saobraćaja</span></li>
      <li><b>Tina Ujevića 8</b><span>Brčko, 065 537 043</span></li>
    </ul>
    <div class="g4 rvl">
      <div class="card tilt"><i class="gl"></i><div class="ico">🤝</div><h3>Podrška umjesto pritiska</h3><p>Učiš strpljivo, bez stresa i u opuštenoj atmosferi. Svaka greška dobije objašnjenje, a ne ukor.</p></div>
      <div class="card tilt"><i class="gl"></i><div class="ico">🎓</div><h3>Stručni kadar</h3><p>Predavanja vodi Doc. dr Violeta Lukić Vujadinović, doktor nauka iz oblasti saobraćaja, licencirani predavač teoretske nastave i NLP Master.</p></div>
      <div class="card tilt"><i class="gl"></i><div class="ico">🏆</div><h3>25 godina tradicije</h3><p>Već četvrt vijeka osposobljavamo vozače u Brčkom i tačno znamo šta je potrebno za siguran početak.</p></div>
      <div class="card tilt"><i class="gl"></i><div class="ico">🚗</div><h3>Realna vožnja</h3><p>Pripremamo te za stvarni saobraćaj, a ne samo za poligon, da voziš sigurno i kad dobiješ dozvolu.</p></div>
    </div>
    <p class="ctr"><a class="more-link" href="/o-nama/">Više o Autoškoli Lukić →</a></p>
    <div class="quick rvl">
      <div><h3>Brzi upis, javi nam se danas</h3><p>Tina Ujevića 8, Brčko. Pozovi i dogovori termin upisa, cijenu i rate.</p></div>
      <a href="tel:+38765537043" class="btn btn-y">📞 Violeta</a>
      <a href="tel:+38765803456" class="btn btn-y">📞 Dalibor</a>
      <a target="_blank" rel="noopener" href="{MAPS}" class="btn btn-g">🧭 Navigacija</a>
    </div>
  </div>
</section>

<section class="sec alt">
  <div class="wrap">
    <h2 class="t rvl">Put do <em>vozačke dozvole</em></h2>
    <p class="sub mut rvl">Jednostavno, korak po korak, uz podršku na svakom koraku.</p>
    <div class="steps rvl" style="perspective:1200px">
      <div class="card step tilt"><i class="gl"></i><h3>Upis</h3><p>Nazovi i dogovori termin upisa.</p></div>
      <div class="card step tilt"><i class="gl"></i><h3>Teorija</h3><p>Moderna učionica i jasna objašnjenja.</p></div>
      <div class="card step tilt"><i class="gl"></i><h3>Vožnja</h3><p>Časovi sa strpljivim instruktorom.</p></div>
      <div class="card step tilt"><i class="gl"></i><h3>Ispit</h3><p>Podrška sve do polaganja.</p></div>
      <div class="card step tilt"><i class="gl"></i><h3>Dozvola 🎉</h3><p>Položen ispit i vozačka u rukama. Spreman si za samostalnu i sigurnu vožnju.</p></div>
    </div>
    <p class="ctr"><a class="more-link" href="/upis/">Detaljan vodič: dokumenti, ispiti i rokovi →</a></p>
  </div>
</section>

<section id="kategorije" class="sec">
  <div class="wrap">
    <h2 class="t rvl">Kategorije vozačke dozvole <em>u Brčkom</em></h2>
    <p class="sub mut rvl">Odaberi kategoriju i pročitaj sve o uslovima, obuci i ispitu.</p>
    <div class="hub cat rvl">{kat_cards}</div>
  </div>
</section>

<section class="sec alt">
  <div class="wrap">
    <h2 class="t rvl">Raspored <em>predavanja</em></h2>
    <p class="sub mut rvl">Sljedeći termini teorijske nastave po grupama. Pronađi svoju grupu i provjeri kad dolaziš.</p>
    <div class="nx rvl" id="home-pv"><div class="card" style="padding:24px;grid-column:1/-1;text-align:center"><h3>Učitavam raspored…</h3></div></div>
    <p class="ctr"><a class="more-link" href="/predavanja/">Kompletan raspored i spiskovi grupa →</a></p>
  </div>
</section>

<section class="sec">
  <div class="wrap">
    <h2 class="t rvl">Cijene obuke i <em>plaćanje na rate</em></h2>
    <p class="sub mut rvl">Jasne cijene i način plaćanja koji ti odgovara.</p>
    <div class="pr rvl">
      <div class="card tilt"><i class="gl"></i><h3>Gotovinsko plaćanje</h3><div class="price">{price(CIJENA_GOTOVINA)}</div>
        <ul><li>Teorijska nastava</li><li>Fond časova vožnje</li><li>Prijava i polaganje ispita</li></ul><a href="/cjenovnik/" class="btn btn-y">Detalji cijena</a></div>
      <div class="card tilt hot"><i class="gl"></i><span class="tag">POVOLJNO</span><h3>Plaćanje na rate</h3><div class="price">{price(CIJENA_RATE)}</div>
        <ul><li>Teorijska nastava</li><li>Fond časova vožnje</li><li>Prijava i polaganje ispita</li><li>Mogućnost plaćanja na rate</li></ul><a href="/cjenovnik/" class="btn btn-y">Kako funkcionišu rate</a></div>
    </div>
  </div>
</section>

<section class="sec alt">
  <div class="wrap">
    <h2 class="t rvl">Instruktori <em>autoškole Lukić</em></h2>
    <p class="sub mut rvl">Ljudi koji te uče, a ne samo ispituju.</p>
    <div class="team rvl">
      <a class="card tilt" href="/instruktori/#violeta"><i class="gl"></i><div class="av y">VL</div><div><h3>Doc. dr Violeta Lukić Vujadinović</h3><p class="mut" style="font-size:.9rem">Doktor nauka iz oblasti saobraćaja, licencirani predavač, NLP Master.</p><span class="ph">Upoznaj predavača →</span></div></a>
      <a class="card tilt" href="/instruktori/#dalibor"><i class="gl"></i><div class="av b">DV</div><div><h3>Dalibor Vujadinović</h3><p class="mut" style="font-size:.9rem">Instruktor vožnje. Praktična obuka i organizacija časova vožnje.</p><span class="ph">Upoznaj instruktora →</span></div></a>
    </div>
  </div>
</section>

<section class="sec">
  <div class="wrap">
    <h2 class="t rvl">Položili su! <em>Naši kandidati</em></h2>
    <p class="sub mut rvl">Vozačka u ruke, osmijeh na licu.</p>
    <div class="gal rvl">{gal_html(GAL)}</div>
    <p class="ctr"><a class="more-link" href="/galerija/">Cijela galerija →</a></p>
  </div>
</section>

<section class="sec alt">
  <div class="wrap">
    <h2 class="t rvl">Najnovije <em>objave</em></h2>
    <p class="sub mut rvl">Obavještenja o upisu, terminima i čestitke kandidatima, direktno od Violete.</p>
    <div class="nwp rvl" id="home-nw"></div>
    <p class="ctr"><a class="more-link" href="/novosti/">Sve objave →</a></p>
  </div>
</section>

<section id="pitanja" class="sec">
  <div class="wrap faqw">
    <aside class="faqa rvl">
      <div class="qm" aria-hidden="true">?</div>
      <h2>Česta pitanja o <em>autoškoli u Brčkom</em></h2>
      <p>Sve što kandidati najčešće pitaju prije upisa. Ako je nešto ostalo nejasno, nazovi nas.</p>
      <a href="/pitanja/" class="btn btn-y">Sva pitanja i odgovori</a>
    </aside>
    <div class="faq rvl">{faq}</div>
  </div>
</section>

<section id="kontakt" class="sec alt">
  <div class="wrap">
    <h2 class="t rvl">Autoškola Brčko: <em>kontakt i lokacija</em></h2>
    <div class="ct rvl">
      <div class="card tilt"><i class="gl"></i>
        <div class="row"><div class="ico">📍</div><div><small>Adresa</small><b>Tina Ujevića 8, 76100 Brčko</b></div></div>
        <div class="row"><div class="ico">📞</div><div><small>Violeta, upis i informacije</small><a href="tel:+38765537043"><b>065 537 043</b></a></div></div>
        <div class="row"><div class="ico">📞</div><div><small>Dalibor, časovi vožnje</small><a href="tel:+38765803456"><b>065 803 456</b></a></div></div>
        <div class="row"><div class="ico">📸</div><div><small>Instagram</small><a href="https://www.instagram.com/autoskolalukic" target="_blank" rel="noopener"><b>@autoskolalukic</b></a></div></div>
      </div>
      <div class="map">
        <iframe title="Mapa: Autoškola Lukić, Tina Ujevića 8, Brčko" loading="lazy" referrerpolicy="no-referrer-when-downgrade" src="https://www.google.com/maps?q=Tina+Ujevi%C4%87a+8+Br%C4%8Dko+76100&amp;output=embed"></iframe>
        <a target="_blank" rel="noopener" href="{MAPS}">Otvori navigaciju →</a>
      </div>
    </div>
  </div>
</section>'''
    return dict(path='/', home=True, prio='1.0', freq='weekly',
                title='Autoškola Brčko | Lukić, vozačka dozvola B kategorije i plaćanje na rate',
                desc='Autoškola Lukić u Brčkom: 25 godina iskustva, obuka za A, B, C1, C, CE i D kategoriju, plaćanje na rate, teoriju drži doktor saobraćaja. Upis: 065 537 043.',
                og_title='Autoškola Lukić Brčko, 25 godina iskustva',
                hero_html=hero, body=body, crumbs=[('/', 'Početna')], images=[f'/img/galerija/{f}.webp' for f, a, c in GAL],
                scripts=['/assets/postavke.js', '/podaci/predavanja.js', '/podaci/objave.js', '/assets/podaci.js'])


# ---------------------------------------------------------------- KATEGORIJE
def kat_page(path, code, title, desc, h1, lead, chip, kv, prose, faq, svc_name, svc_desc):
    kvh = '<div class="kv">' + ''.join(f'<div><b>{a}</b><span>{b}</span></div>' for a, b in kv) + '</div>'
    return dict(path=path, title=title, desc=desc, prio='0.9',
                crumbs=[('/', 'Početna'), ('/kategorije/', 'Kategorije'), (path, strip_tags(h1))],
                hero=dict(chip=chip, h1=h1, lead=lead, big=code),
                body=art(kvh + prose, side(path)) + faq_block(faq, f'Pitanja o <em>{code} kategoriji</em>', alt=True) +
                     related('Ostale <em>kategorije</em>', other_kat(path), alt=False),
                faq=faq, ld=[svc(svc_name, path, svc_desc)])


NOVA_PRAVILA = '''<div class="note blue"><b>Najava: nova pravila za obuku od 2028.</b>Prema najavi Ministarstva komunikacija i prometa BiH iz oktobra 2026. godine, nova pravila za autoškole primjenjivat će se od 1. januara 2028. Za B kategoriju broj časova praktične obuke povećava se za pet, a prvih pet časova obavezno se vozi na poligonu.</div>'''

MLADI = f'''<h2>Prve dvije godine: pravila za <em>mlade vozače</em></h2>
<p>Prema Zakonu o osnovama bezbjednosti saobraćaja na putevima u BiH, vozač koji je dobio vozačku dozvolu za kategoriju A1, A, B ili C1 prve dvije godine od izdavanja dozvole:</p>
<ul><li>ne smije voziti brže od <strong>70 km/h</strong> na putu, <strong>90 km/h</strong> na brzom putu i <strong>120 km/h</strong> na autoputu,</li><li>ne smije tim vozilom vući priključno vozilo,</li><li>ne smije organizovano prevoziti djecu.</li></ul>
<p>Na predavanjima prolazimo i ova pravila, da od prvog dana samostalne vožnje znaš šta smiješ, a šta ne.</p>'''


def b_kat():
    prose = f'''
<h2>Vozačka dozvola B kategorije u <em>Brčkom</em></h2>
<p class="lead">B kategorija je prva vozačka dozvola za većinu kandidata i najtraženija obuka u Autoškoli Lukić. Već 25 godina pripremamo kandidate iz Brčkog i okoline da polože ispit, ali i da nakon ispita voze sigurno i samouvjereno u stvarnom saobraćaju.</p>
<p>Teorijsku nastavu drži <a href="/instruktori/#violeta">Doc. dr Violeta Lukić Vujadinović</a>, doktor nauka iz oblasti saobraćaja, a časove vožnje vodi instruktor <a href="/instruktori/#dalibor">Dalibor Vujadinović</a>. Obuku možeš platiti odjednom ili <a href="/cjenovnik/">na rate</a>.</p>

<h2>Šta smiješ voziti sa <em>B kategorijom</em>?</h2>
<p>Vozačka dozvola B kategorije daje pravo upravljanja putničkim automobilima i drugim motornim vozilima čija najveća dozvoljena masa nije veća od 3.500 kg i koja, osim sjedišta za vozača, nemaju više od osam sjedišta. Uz takvo vozilo smiješ vući i laku prikolicu, najveće dozvoljene mase do 750 kg.</p>
<p>To znači lični automobil, kombi za porodicu ili posao i manje dostavno vozilo. Sve ono što se svakodnevno vozi po Brčkom i okolini.</p>

<h2>Uslovi za upis <em>B kategorije</em></h2>
<ul>
<li><strong>Najmanje 18 godina.</strong> To je minimalna starost za B kategoriju propisana Zakonom o osnovama bezbjednosti saobraćaja na putevima u BiH.</li>
<li><strong>Važeća lična karta</strong> i prijava boravka.</li>
<li><strong>Ljekarsko uvjerenje</strong> o zdravstvenoj sposobnosti za vozača. Pribavlja se prije početka obuke i važi 12 mjeseci od dana izdavanja.</li>
</ul>
<p>Tačan spisak dokumenata potvrđujemo pri upisu. Nazovi Violetu na {TV} i sve dogovaramo u jednom razgovoru.</p>

<h2>Kako izgleda obuka u <em>Autoškoli Lukić</em></h2>
<ol>
<li><strong>Upis i dogovor.</strong> Dogovaramo termin, način plaćanja i grupu za teoriju.</li>
<li><strong>Prva pomoć.</strong> Predavanja i ispit iz prve pomoći, koje prema zakonu sprovodi Crveni krst.</li>
<li><strong>Teorijska nastava.</strong> Saobraćajni propisi, znakovi i pravila u modernoj učionici. Termin svoje grupe nađeš u <a href="/predavanja/">rasporedu predavanja</a>.</li>
<li><strong>Teorijski ispit.</strong> Test iz poznavanja propisa o bezbjednosti saobraćaja.</li>
<li><strong>Časovi vožnje.</strong> Prvo osnovne radnje vozilom, zatim vožnja kroz grad, raskrsnice, kružni tokovi, parkiranje i vožnja van naselja.</li>
<li><strong>Praktični ispit.</strong> Vožnja pred ispitnom komisijom koju imenuju nadležni organi Brčko distrikta.</li>
</ol>

<h2>Koliko traje obuka za <em>B kategoriju</em>?</h2>
<p>Trajanje zavisi od termina teorijske grupe, slobodnih termina za vožnju i ispitnih rokova. Kandidati koji redovno dolaze na predavanja i časove vožnje prolaze kroz obuku najbrže. Na upisu ti kažemo kada počinje sljedeća grupa i kako da uklopiš vožnju sa školom ili poslom.</p>
{NOVA_PRAVILA}

<h2>Zašto kandidati biraju <em>Lukić</em> za B kategoriju</h2>
<ul>
<li><strong>Teorija s razumijevanjem.</strong> Predavač sa doktoratom iz saobraćaja objašnjava zašto pravilo postoji, pa se gradivo pamti, a ne buba.</li>
<li><strong>Vožnja bez pritiska.</strong> Instruktor objašnjava svaku grešku mirno i strpljivo.</li>
<li><strong>Priprema za stvarni saobraćaj.</strong> Vozimo tamo gdje ćeš poslije i voziti: gradske ulice Brčkog, raskrsnice, parking i magistralni put.</li>
<li><strong>Plaćanje na rate.</strong> Obuka koja se uklapa u kućni budžet.</li>
<li><strong>25 godina iskustva.</strong> Generacije vozača iz Brčkog počele su upravo kod nas.</li>
</ul>

<h2>Savjeti za polaganje <em>iz prve</em></h2>
<ul>
<li>Ne propuštaj predavanja. Propise koje razumiješ ne zaboravljaš na testu.</li>
<li>Rješavaj probne testove redovno, ne samo sedmicu pred ispit.</li>
<li>Na vožnji pitaj sve što ti nije jasno. Zato je instruktor tu.</li>
<li>Prije ispita se naspavaj i dođi ranije. Mirna glava je pola položenog ispita.</li>
</ul>
{MLADI}
<p><a class="btn btn-y" href="/kontakt/">Upiši B kategoriju →</a></p>'''
    faq = [
        ('Sa koliko godina mogu upisati B kategoriju?', 'Vozačku dozvolu B kategorije možeš dobiti sa navršenih 18 godina, kako propisuje Zakon o osnovama bezbjednosti saobraćaja na putevima u BiH. Za tačne uslove upisa nazovi 065 537 043.'),
        ('Mogu li platiti obuku za B kategoriju na rate?', 'Možeš. Pored gotovinskog plaćanja nudimo i plaćanje na rate, a uslove dogovaramo pri upisu. Više na stranici <a href="/cjenovnik/">Cijene i rate</a>.'),
        ('Gdje se održavaju predavanja za B kategoriju?', 'U učionici Autoškole Lukić, Tina Ujevića 8, Brčko. Raspored po grupama objavljujemo na stranici <a href="/predavanja/">Predavanja</a>.'),
        ('Koliko dugo važi ljekarsko uvjerenje?', 'Ljekarsko uvjerenje o zdravstvenoj sposobnosti za vozača važi 12 mjeseci od dana izdavanja, pa ga je najbolje uraditi neposredno prije početka obuke.'),
        ('Šta ako ne položim ispit iz prvog pokušaja?', 'Ništa strašno. Dogovaramo dodatne časove i pripremu za novi termin. Cilj nam je da položiš i da voziš sigurno, a ne da žurimo.'),
    ]
    return kat_page('/b-kategorija/', 'B', 'Vozačka dozvola B kategorije u Brčkom | Autoškola Lukić',
                    'Obuka za B kategoriju u Brčkom: uslovi (18 godina), dokumenti, teorija kod doktora saobraćaja, časovi vožnje i plaćanje na rate. Autoškola Lukić, 065 537 043.',
                    'B kategorija <span>u Brčkom</span>', 'Vozačka dozvola za automobil, od upisa do položenog ispita, uz strpljive instruktore, predavača sa doktoratom iz saobraćaja i mogućnost plaćanja na rate.',
                    '🚗 Najtraženija kategorija',
                    [('18', 'godina, minimalna starost'), ('3.500 kg', 'najveća dozvoljena masa vozila'), ('Rate', 'plaćanje u dogovoru'), ('25 god.', 'iskustva u Brčkom')],
                    prose, faq, 'Obuka za B kategoriju u Brčkom', 'Teorijska nastava, prva pomoć, časovi vožnje i priprema za vozački ispit B kategorije u Autoškoli Lukić, Brčko.')


def a_kat():
    prose = f'''
<h2>Vozačka dozvola za <em>motocikl</em> u Brčkom</h2>
<p class="lead">A kategorija je za one kojima je motocikl način života ili najpraktičniji način da stignu na posao. U Autoškoli Lukić obuka za motocikl kombinuje teoriju, vježbe na poligonu i vožnju u saobraćaju, sa naglaskom na ono što motoristu najviše čuva: predviđanje opasnosti.</p>

<h2>Uslovi za <em>A kategoriju</em></h2>
<ul>
<li><strong>Najmanje 18 godina</strong> za kategoriju A, prema Zakonu o osnovama bezbjednosti saobraćaja na putevima u BiH.</li>
<li>Za potkategoriju <strong>A1</strong>, odnosno lake motocikle, zakon propisuje najmanje 16 godina. Ako te zanima A1, pitaj nas pri upisu.</li>
<li>Važeća lična karta, prijava boravka i ljekarsko uvjerenje, koje važi 12 mjeseci.</li>
</ul>

<h2>Šta učiš na obuci za <em>motocikl</em></h2>
<ol>
<li><strong>Teorija i prva pomoć.</strong> Isti propisi kao za ostale kategorije, uz posebna pravila za vozače motocikla. <a href="/teorijska-nastava/">Više o teorijskoj nastavi</a>.</li>
<li><strong>Poligon.</strong> Balans, polazak i zaustavljanje, vožnja u sporom hodu, slalom, kočenje i izbjegavanje prepreke.</li>
<li><strong>Vožnja u saobraćaju.</strong> Položaj u traci, vidljivost, raskrsnice, preticanje i vožnja kroz krivine.</li>
<li><strong>Ispit.</strong> Teorijski test, zatim praktični ispit pred komisijom.</li>
</ol>

<h2>Zaštitna oprema</h2>
<p>Za vožnju motocikla obavezna je zaštitna kaciga. Na obuku dođi u čvrstoj obući koja štiti zglob, dugim pantalonama i jakni, a preporučujemo i rukavice. Na prvom času ti pokažemo šta je od opreme važno i kako se pravilno podešava.</p>

<h2>Zašto <em>Autoškola Lukić</em> za A kategoriju</h2>
<ul>
<li>Strpljiv pristup, jer se na motociklu samopouzdanje gradi korak po korak.</li>
<li>Teorija kod predavača sa doktoratom iz oblasti saobraćaja.</li>
<li>Mogućnost <a href="/cjenovnik/">plaćanja na rate</a>.</li>
<li>Već imaš B kategoriju? Teoriju i termine prilagođavamo tvom predznanju, pitaj nas.</li>
</ul>
{MLADI}
<p><a class="btn btn-y" href="/kontakt/">Upiši A kategoriju →</a></p>'''
    faq = [
        ('Sa koliko godina mogu upisati obuku za motocikl?', 'Za kategoriju A zakon u BiH propisuje najmanje 18 godina, a za potkategoriju A1, lake motocikle, najmanje 16 godina.'),
        ('Moram li imati svoju opremu?', 'Kaciga je obavezna, a preporučujemo i rukavice, jaknu, duge pantalone i obuću koja štiti zglob. Detalje dogovaramo pri upisu.'),
        ('Imam B kategoriju. Moram li ponovo slušati cijelu teoriju?', 'Obim teorije zavisi od toga koje kategorije već imaš. Nazovi 065 537 043 i reći ćemo ti tačno šta te čeka.'),
    ]
    return kat_page('/a-kategorija/', 'A', 'A kategorija Brčko, obuka za motocikl | Autoškola Lukić',
                    'Vozačka dozvola za motocikl (A kategorija) u Brčkom: uslovi od 18 godina, poligon, vožnja u saobraćaju, oprema i plaćanje na rate. Autoškola Lukić.',
                    'A kategorija, <span>motocikli</span>', 'Obuka za motocikl u Brčkom: poligon, vožnja u saobraćaju i teorija kod doktora nauka iz saobraćaja. Sigurno, strpljivo i bez pritiska.',
                    '🏍️ Motocikli',
                    [('18', 'godina za kategoriju A'), ('16', 'godina za potkategoriju A1'), ('Poligon', 'i vožnja u saobraćaju'), ('Rate', 'plaćanje u dogovoru')],
                    prose, faq, 'Obuka za A kategoriju (motocikl) u Brčkom', 'Teorija, poligon i vožnja u saobraćaju za vozačku dozvolu A kategorije u Autoškoli Lukić, Brčko.')


def c_kat():
    prose = f'''
<h2>Vozačka dozvola za <em>kamion</em> u Brčkom</h2>
<p class="lead">C1 i C kategorija otvaraju vrata poslu u transportu, građevini, dostavi i logistici. U Autoškoli Lukić kandidate za teretna vozila pripremamo za ispit, ali i za realne situacije: manevrisanje velikim vozilom, mrtve uglove, opterećenje i vožnju u gradu.</p>

<h2>Razlika između <em>C1 i C</em></h2>
<div class="tw"><table class="tbl">
<thead><tr><th>Kategorija</th><th>Vozila</th><th>Minimalna starost</th></tr></thead>
<tbody>
<tr><td>C1</td><td>Teretna vozila srednje mase, iznad 3.500 kg, a najviše do 7.500 kg</td><td>18 godina</td></tr>
<tr><td>C</td><td>Teretna vozila čija najveća dozvoljena masa prelazi 3.500 kg</td><td>21 godina</td></tr>
</tbody></table></div>
<p>Starosne granice za C1 (18 godina) i C (21 godina) propisuje {ZAKON}. Ako želiš voziti kamion s prikolicom, nakon C kategorije slijedi <a href="/ce-kategorija/">CE kategorija</a>.</p>

<h2>Uslovi za upis</h2>
<ul>
<li>Potrebne godine: 18 za C1, odnosno 21 za C.</li>
<li>Važeća lična karta i prijava boravka.</li>
<li>Ljekarsko uvjerenje o zdravstvenoj sposobnosti za vozača odgovarajuće kategorije, koje važi 12 mjeseci.</li>
<li>Većina kandidata C kategoriju upisuje nakon B kategorije. Tačne uslove za tvoj slučaj provjeravamo pri upisu.</li>
</ul>

<h2>Šta obuhvata obuka</h2>
<ol>
<li><strong>Teorija.</strong> Propisi s naglaskom na teretna vozila: dimenzije, mase i osovinsko opterećenje, osiguranje tereta i pravila za teška vozila.</li>
<li><strong>Upoznavanje vozila.</strong> Kontrolni pregled prije vožnje, ogledala, mrtvi uglovi i dimenzije vozila.</li>
<li><strong>Vožnja na poligonu.</strong> Manevrisanje, vožnja unazad i parkiranje velikog vozila.</li>
<li><strong>Vožnja u saobraćaju.</strong> Raskrsnice, skretanje velikim vozilom, vožnja kroz grad i van naselja.</li>
<li><strong>Ispit.</strong> Teorijski i praktični dio pred ispitnom komisijom.</li>
</ol>

<div class="note"><b>Za profesionalne vozače</b>Za rad u prevozu robe, posebno u međunarodnom prevozu, pored vozačke dozvole traže se i dodatno stručno osposobljavanje i kvalifikacijska kartica vozača. To se organizuje odvojeno od autoškole, a rado ćemo te uputiti šta je sljedeći korak.</div>

<h2>Zašto <em>Lukić</em> za kamion</h2>
<ul>
<li>25 godina iskustva u obuci vozača svih kategorija u Brčkom.</li>
<li>Teorija kod predavača sa doktoratom iz oblasti saobraćaja.</li>
<li>Mogućnost <a href="/cjenovnik/">plaćanja na rate</a>, što je posebno važno kod obimnije obuke.</li>
</ul>
<p><a class="btn btn-y" href="/kontakt/">Upiši C1 ili C kategoriju →</a></p>'''
    faq = [
        ('Sa koliko godina mogu voziti kamion?', 'Prema zakonu u BiH, potkategoriju C1 možeš dobiti sa 18, a kategoriju C sa 21 godinom.'),
        ('Treba li mi B kategorija prije C?', 'Većina kandidata C kategoriju upisuje nakon B kategorije. Tačne uslove za tvoj slučaj provjeravamo pri upisu, nazovi 065 537 043.'),
        ('Mogu li obuku za kamion platiti na rate?', 'Možeš. Plaćanje na rate dogovaramo pri upisu za sve kategorije.'),
    ]
    return kat_page('/c-kategorija/', 'C', 'C1 i C kategorija Brčko, vozačka za kamion | Autoškola Lukić',
                    'Obuka za C1 i C kategoriju (kamion) u Brčkom: C1 od 18, C od 21 godine. Teorija, poligon, vožnja u saobraćaju i plaćanje na rate. Autoškola Lukić.',
                    'C1 i C kategorija, <span>teretna vozila</span>', 'Vozačka dozvola za kamion u Brčkom: teorija s naglaskom na teretna vozila, poligon i vožnja u saobraćaju, uz mogućnost plaćanja na rate.',
                    '🚚 Teretna vozila',
                    [('18', 'godina za C1'), ('21', 'godina za C'), ('3.500 kg+', 'teretna vozila'), ('Rate', 'plaćanje u dogovoru')],
                    prose, faq, 'Obuka za C1 i C kategoriju (kamion) u Brčkom', 'Teorija, poligon i vožnja za vozačku dozvolu C1 i C kategorije u Autoškoli Lukić, Brčko.')


def ce_kat():
    prose = f'''
<h2>CE kategorija, kamion <em>s prikolicom</em></h2>
<p class="lead">CE kategorija je sljedeći korak za vozače kamiona: skup vozila sastavljen od vučnog vozila C kategorije i priključnog vozila, prikolice ili poluprikolice. Prevoznici je traže, pa je CE često ključ za bolje plaćen posao u transportu.</p>

<h2>Uslovi za <em>CE kategoriju</em></h2>
<ul>
<li><strong>Vozačka dozvola C kategorije.</strong> Zakon u BiH propisuje da CE mogu dobiti samo vozači koji već imaju C kategoriju.</li>
<li><strong>Najmanje 21 godina</strong> života.</li>
<li>Ljekarsko uvjerenje o zdravstvenoj sposobnosti, koje važi 12 mjeseci, i lična dokumenta.</li>
</ul>

<h2>Šta se uči na obuci</h2>
<ol>
<li><strong>Spajanje i razdvajanje</strong> vučnog i priključnog vozila, uz provjeru kočionog sistema, svjetala i spojnica.</li>
<li><strong>Manevrisanje skupom vozila.</strong> Vožnja unazad s prikolicom, okretanje i parkiranje.</li>
<li><strong>Vožnja u saobraćaju.</strong> Skretanje, kružni tokovi, kočenje i rastojanje sa teškim skupom vozila.</li>
<li><strong>Propisi</strong> o dimenzijama, masama i osiguranju tereta, kroz <a href="/teorijska-nastava/">teorijsku nastavu</a>.</li>
<li><strong>Praktični ispit</strong> pred ispitnom komisijom.</li>
</ol>

<div class="note"><b>Planiraš rad u međunarodnom prevozu?</b>Za profesionalni prevoz robe potrebna je i kvalifikacijska kartica vozača, koja se stiče posebnim stručnim osposobljavanjem. Pitaj nas i reći ćemo ti redoslijed koraka.</div>

<h2>Zašto <em>Autoškola Lukić</em></h2>
<ul>
<li>Iskustvo u obuci vozača teretnih vozila i skupova vozila.</li>
<li>Obuka prilagođena vozačima koji već rade. Termine vožnje dogovaraš s instruktorom Daliborom na {TD}.</li>
<li><a href="/cjenovnik/">Plaćanje na rate</a>.</li>
</ul>
<p><a class="btn btn-y" href="/kontakt/">Upiši CE kategoriju →</a></p>'''
    faq = [
        ('Mogu li upisati CE ako još nemam C kategoriju?', 'Ne možeš. Prema zakonu u BiH, vozačku dozvolu za CE kategoriju mogu dobiti samo vozači koji već imaju C kategoriju. Možemo te voditi kroz C, pa onda CE.'),
        ('Koliko godina moram imati za CE?', 'Zakon propisuje najmanje 21 godinu za kategorije C i CE.'),
        ('Mogu li vožnju uklopiti uz posao?', 'Možeš. Termine časova vožnje dogovaraš direktno s instruktorom Daliborom na 065 803 456.'),
    ]
    return kat_page('/ce-kategorija/', 'CE', 'CE kategorija Brčko, kamion s prikolicom | Autoškola Lukić',
                    'Obuka za CE kategoriju u Brčkom: uslov je C kategorija i 21 godina. Spajanje prikolice, manevrisanje, ispit i plaćanje na rate. Autoškola Lukić.',
                    'CE kategorija, <span>kamion s prikolicom</span>', 'Za vozače koji već imaju C kategoriju: obuka za skup vozila u Brčkom, od spajanja prikolice do položenog ispita.',
                    '🚛 Skup vozila',
                    [('C', 'kategorija je preduslov'), ('21', 'godina minimalno'), ('Rate', 'plaćanje u dogovoru'), ('Uz posao', 'fleksibilni termini vožnje')],
                    prose, faq, 'Obuka za CE kategoriju (kamion s prikolicom) u Brčkom', 'Obuka za vozačku dozvolu CE kategorije, skup vozila, u Autoškoli Lukić, Brčko.')


def d_kat():
    prose = f'''
<h2>Vozačka dozvola za <em>autobus</em> u Brčkom</h2>
<p class="lead">D kategorija je za vozače autobusa: gradskog, međugradskog, školskog ili turističkog. To je kategorija s najvećom odgovornošću, jer vozač prevozi putnike, pa obuka u Autoškoli Lukić stavlja poseban naglasak na sigurnost, predviđanje i miran stil vožnje.</p>

<h2>Uslovi za <em>D kategoriju</em></h2>
<ul>
<li><strong>Najmanje 24 godine.</strong> To je minimalna starost za kategoriju D prema zakonu u BiH, a za potkategoriju D1 je 21 godina.</li>
<li><strong>Prethodna vozačka dozvola.</strong> D kategoriju mogu dobiti vozači koji već najmanje dvije godine imaju vozačku dozvolu kategorije B, C ili potkategorije D1.</li>
<li>Ljekarsko uvjerenje o zdravstvenoj sposobnosti, koje važi 12 mjeseci, i lična dokumenta.</li>
</ul>
<div class="note"><b>Dobro je znati</b>Vozači kategorija D, DE, D1 i D1E prema zakonu obavljaju zdravstveni pregled prilikom svakog produženja vozačke dozvole.</div>

<h2>Šta obuhvata obuka</h2>
<ol>
<li><strong>Teorija.</strong> Propisi o prevozu putnika, dimenzije i mase vozila, ponašanje na stajalištima i u posebnim situacijama.</li>
<li><strong>Upoznavanje autobusa.</strong> Kontrolni pregled, ogledala, vrata, mrtvi uglovi i gabariti.</li>
<li><strong>Manevrisanje.</strong> Vožnja unazad, prilazak stajalištu i okretanje.</li>
<li><strong>Vožnja u saobraćaju.</strong> Glatko kočenje i ubrzavanje zbog udobnosti putnika, skretanje dugim vozilom i vožnja van naselja.</li>
<li><strong>Ispit</strong> pred ispitnom komisijom.</li>
</ol>

<div class="note"><b>Profesionalni prevoz putnika</b>Za rad vozača u javnom prevozu putnika, pored vozačke dozvole, potrebna je i kvalifikacijska kartica vozača, koja se stiče posebnim osposobljavanjem. Javi nam se i objasnit ćemo ti cijeli put.</div>

<h2>Zašto <em>Lukić</em> za D kategoriju</h2>
<ul>
<li>25 godina iskustva u obuci vozača svih kategorija u Brčkom.</li>
<li>Teorija kod doktora nauka iz oblasti saobraćaja: razumijevanje, a ne bubanje.</li>
<li><a href="/cjenovnik/">Plaćanje na rate</a>.</li>
</ul>
<p><a class="btn btn-y" href="/kontakt/">Upiši D kategoriju →</a></p>'''
    faq = [
        ('Sa koliko godina mogu voziti autobus?', 'Prema zakonu u BiH, kategoriju D možeš dobiti sa najmanje 24 godine, a potkategoriju D1 sa 21 godinom.'),
        ('Koju dozvolu moram imati prije D kategorije?', 'D kategoriju mogu dobiti vozači koji najmanje dvije godine imaju vozačku dozvolu kategorije B, C ili potkategorije D1.'),
        ('Treba li vozačima autobusa češći ljekarski pregled?', 'Treba. Vozači kategorija D, DE, D1 i D1E prema zakonu obavljaju zdravstveni pregled prilikom svakog produženja vozačke dozvole.'),
    ]
    return kat_page('/d-kategorija/', 'D', 'D kategorija Brčko, vozačka za autobus | Autoškola Lukić',
                    'Obuka za D kategoriju (autobus) u Brčkom: uslovi su 24 godine i dvije godine B, C ili D1. Teorija, vožnja, ispit i plaćanje na rate. Autoškola Lukić.',
                    'D kategorija, <span>autobusi</span>', 'Vozačka dozvola za autobus u Brčkom: obuka sa naglaskom na sigurnost putnika, od teorije do ispita, uz mogućnost plaćanja na rate.',
                    '🚌 Prevoz putnika',
                    [('24', 'godine za kategoriju D'), ('2 god.', 'prethodno B, C ili D1'), ('21', 'godina za D1'), ('Rate', 'plaćanje u dogovoru')],
                    prose, faq, 'Obuka za D kategoriju (autobus) u Brčkom', 'Obuka za vozačku dozvolu D kategorije u Autoškoli Lukić, Brčko.')


def kategorije():
    body = '''<section class="sec"><div class="wrap">
<h2 class="t rvl">Odaberi <em>kategoriju</em></h2>
<p class="sub mut rvl">Za svaku kategoriju imaš posebnu stranicu sa uslovima, tokom obuke i odgovorima na česta pitanja.</p>
<div class="hub rvl">''' + ''.join(f'<a class="card tilt" href="{p}"><i class="gl"></i><span class="lt2">{b}</span><h3>{n}</h3><p>{t}</p><span class="more">Saznaj više →</span></a>' for p, b, n, t in ALL_KAT) + '''
<a class="card tilt" href="/teorijska-nastava/"><i class="gl"></i><span class="lt2">Dr</span><h3>Teorijska nastava</h3><p>Zajednička za sve kategorije, u modernoj učionici, kod doktora nauka iz saobraćaja.</p><span class="more">Saznaj više →</span></a>
</div></div></section>''' + art('''
<h2>Minimalna starost po <em>kategorijama</em></h2>
<p>Prema članu 184. Zakona o osnovama bezbjednosti saobraćaja na putevima u BiH, vozačka dozvola se može dobiti sa navršenih:</p>
<div class="tw"><table class="tbl">
<thead><tr><th>Kategorija</th><th>Vozila</th><th>Godine</th><th>Napomena</th></tr></thead>
<tbody>
<tr><td>A1</td><td>Laki motocikli</td><td>16</td><td>Potkategorija</td></tr>
<tr><td>A</td><td>Motocikli</td><td>18</td><td></td></tr>
<tr><td>B</td><td>Putnički automobili do 3.500 kg</td><td>18</td><td>Najtraženija</td></tr>
<tr><td>C1</td><td>Teretna vozila do 7.500 kg</td><td>18</td><td>Potkategorija</td></tr>
<tr><td>C</td><td>Teretna vozila preko 3.500 kg</td><td>21</td><td></td></tr>
<tr><td>CE</td><td>Kamion s prikolicom</td><td>21</td><td>Potrebna C kategorija</td></tr>
<tr><td>D1</td><td>Manji autobusi</td><td>21</td><td>Potkategorija</td></tr>
<tr><td>D</td><td>Autobusi</td><td>24</td><td>Najmanje 2 godine B, C ili D1</td></tr>
</tbody></table></div>
<p>U Autoškoli Lukić obučavamo kandidate za kategorije <strong>A, B, C1, C, CE i D</strong>. Za potkategorije i posebne slučajeve, na primjer ako već imaš neku kategoriju, nazovi nas na ''' + TV + '''. Reći ćemo ti tačno koji je tvoj sljedeći korak.</p>
<h2>Šta je zajedničko za <em>sve kategorije</em></h2>
<ul>
<li><strong>Ljekarsko uvjerenje</strong> prije početka obuke, koje važi 12 mjeseci.</li>
<li><strong>Obuka iz prve pomoći</strong> i ispit, za kandidate koji ga još nisu položili.</li>
<li><strong>Teorijska nastava</strong> i teorijski ispit iz poznavanja propisa.</li>
<li><strong>Časovi vožnje</strong> sa instruktorom i praktični ispit pred komisijom.</li>
</ul>
<p>Detaljan redoslijed koraka pročitaj u vodiču <a href="/upis/">Kako do vozačke dozvole u Brčkom</a>.</p>''', side('/kategorije/'), alt=True)
    return dict(path='/kategorije/', title='Kategorije A, B, C1, C, CE i D u Brčkom | Autoškola Lukić',
                desc='Sve kategorije vozačke dozvole u Autoškoli Lukić Brčko: A, B, C1, C, CE i D. Minimalna starost, uslovi i obuka za svaku kategoriju na jednom mjestu.',
                crumbs=[('/', 'Početna'), ('/kategorije/', 'Kategorije')], prio='0.9', page_type='CollectionPage',
                hero=dict(chip='🚦 A · B · C1 · C · CE · D', h1='Kategorije vozačke dozvole <span>u Brčkom</span>',
                          lead='Od motocikla do autobusa. U Autoškoli Lukić obučavamo kandidate za šest kategorija. Pogledaj uslove i odaberi svoju.', big='ABC'),
                body=body)


# ---------------------------------------------------------------- O NAMA
def o_nama():
    prose = f'''
<h2>Autoškola Lukić, <em>25 godina</em> u Brčkom</h2>
<p class="lead">Autoškola Lukić već četvrt vijeka osposobljava vozače u Brčkom. Generacije kandidata iz grada i okolnih mjesta, Bijele, Brke, Gornjeg Rahića, Maoče i cijelog Brčko distrikta, svoju prvu vožnju odvezle su upravo s nama.</p>
<p>Za 25 godina mijenjali su se propisi, vozila i ispiti, ali naš pristup je ostao isti: kandidat treba da razumije saobraćaj i da se u njemu osjeća sigurno, a ne samo da prođe ispit.</p>

<h2>Naš pristup: <em>podrška umjesto pritiska</em></h2>
<p>Mnogi kandidati dolaze s tremom. Neki nikad nisu sjeli za volan, a neki su loše iskustvo ponijeli iz druge autoškole. Zato kod nas vrijedi jednostavno pravilo: svaka greška dobije objašnjenje, a ne ukor. Mirna atmosfera nije luksuz, nego najbrži put do sigurnog vozača.</p>
<ul>
<li><strong>Strpljivi instruktori.</strong> Vožnja bez vike i bez stresa.</li>
<li><strong>Stručna teorija.</strong> Predavanja drži doktor nauka iz oblasti saobraćaja.</li>
<li><strong>Realna vožnja.</strong> Pripremamo te za stvarni saobraćaj Brčkog, ne samo za poligon.</li>
<li><strong>Fleksibilno plaćanje.</strong> Gotovina ili <a href="/cjenovnik/">plaćanje na rate</a>.</li>
</ul>

<h2>Stručnost koja se <em>vidi u učionici</em></h2>
<p>Teorijsku nastavu vodi <a href="/instruktori/#violeta">Doc. dr Violeta Lukić Vujadinović</a>, doktor nauka iz oblasti saobraćaja, licencirani predavač teoretske nastave i NLP Master. Bavi se i naučnim radom iz oblasti bezbjednosti saobraćaja, između ostalog stavovima mladih vozača i uticajem medija na bezbjednost u saobraćaju. To znanje direktno ulazi u predavanja: gradivo se uči s razumijevanjem, kroz primjere iz stvarnog saobraćaja.</p>
<p>Praktičnu obuku vodi instruktor <a href="/instruktori/#dalibor">Dalibor Vujadinović</a>, koji organizuje časove vožnje tako da se uklope u školu ili posao.</p>

<h2>Šta nudimo</h2>
<ul>
<li>Obuku za kategorije <a href="/a-kategorija/">A</a>, <a href="/b-kategorija/">B</a>, <a href="/c-kategorija/">C1 i C</a>, <a href="/ce-kategorija/">CE</a> i <a href="/d-kategorija/">D</a>.</li>
<li><a href="/teorijska-nastava/">Teorijsku nastavu</a> u modernoj učionici, po grupama. <a href="/predavanja/">Raspored predavanja</a> objavljujemo na sajtu.</li>
<li>Časove vožnje i pripremu za praktični ispit.</li>
<li>Prijavu i polaganje ispita.</li>
</ul>

<h2>Gdje smo</h2>
<p>Nalazimo se u ulici <strong>Tina Ujevića 8, 76100 Brčko</strong>. Za upis i informacije zovi Violetu na {TV}, a za časove vožnje Dalibora na {TD}. Sve kontakt informacije i mapa su na stranici <a href="/kontakt/">Kontakt</a>.</p>
<p><a class="btn btn-y" href="/kontakt/">Dogovori upis →</a></p>'''
    return dict(path='/o-nama/', title='O nama | Autoškola Lukić Brčko, 25 godina obuke vozača',
                desc='Autoškola Lukić u Brčkom 25 godina osposobljava vozače. Strpljiv pristup, teorija kod doktora nauka iz saobraćaja, kategorije A, B, C1, C, CE i D.',
                crumbs=[('/', 'Početna'), ('/o-nama/', 'O nama')], page_type='AboutPage',
                hero=dict(chip='🏆 25 godina sa vama', h1='O Autoškoli Lukić: <span>25 godina sa vama</span>',
                          lead='Četvrt vijeka iskustva, strpljivi instruktori i predavač sa doktoratom iz saobraćaja. Upoznaj autoškolu u kojoj su generacije Brčaka naučile da voze.', big='25'),
                body=art(prose, side('/o-nama/', 'Autoškola', [('/o-nama/', 'O nama'), ('/instruktori/', 'Instruktori'), ('/teorijska-nastava/', 'Teorijska nastava'), ('/galerija/', 'Galerija'), ('/novosti/', 'Novosti')])))


# ---------------------------------------------------------------- INSTRUKTORI
def instruktori():
    body = '''<section class="sec"><div class="wrap">
<div class="team rvl" style="margin-top:0">
<div class="card tilt" id="violeta"><i class="gl"></i><div class="av y">VL</div><div><h2 style="font-weight:800;font-size:1.15rem">Doc. dr Violeta Lukić Vujadinović</h2><p class="mut" style="font-size:.9rem">Predavač teorijske nastave · upis i informacije</p><a class="ph" href="tel:+38765537043">📞 065 537 043</a></div></div>
<div class="card tilt" id="dalibor"><i class="gl"></i><div class="av b">DV</div><div><h2 style="font-weight:800;font-size:1.15rem">Dalibor Vujadinović</h2><p class="mut" style="font-size:.9rem">Instruktor vožnje · časovi vožnje</p><a class="ph" href="tel:+38765803456">📞 065 803 456</a></div></div>
</div></div></section>''' + art(f'''
<h2>Doc. dr Violeta <em>Lukić Vujadinović</em></h2>
<p class="lead">Predavač teorijske nastave u Autoškoli Lukić. Doktor nauka iz oblasti saobraćaja, licencirani predavač teoretske nastave i NLP Master.</p>
<p>Violeta je osoba koju ćeš prvu upoznati. Kod nje se obavlja upis, dogovara plaćanje i formiraju grupe za predavanja. U učionici predaje saobraćajne propise na način koji je kandidatima razumljiv: kroz primjere, crteže i situacije iz stvarnog saobraćaja u Brčkom.</p>
<ul>
<li><strong>Doktorat iz oblasti saobraćaja.</strong> Akademsko znanje pretočeno u jasna predavanja.</li>
<li><strong>Licencirani predavač</strong> teoretske nastave za kandidate za vozače.</li>
<li><strong>NLP Master.</strong> Pomaže kandidatima da savladaju tremu i uče bez stresa.</li>
<li><strong>Naučni rad</strong> iz bezbjednosti saobraćaja, između ostalog „Istraživanje stavova mladih vozača o uticajnim faktorima bezbjednosti saobraćaja” (NIR, časopis za nauku, istraživanje i razvoj, 2022) i „Uticaj mas medija na bezbjednost drumskog saobraćaja” (Evropska revija, 2022).</li>
</ul>
<p>Termine predavanja po grupama Violeta objavljuje na stranici <a href="/predavanja/">Predavanja</a>, a obavještenja i novosti na <a href="/novosti/">Novostima</a>. Kontakt: {TV}.</p>

<h2>Dalibor <em>Vujadinović</em></h2>
<p class="lead">Instruktor vožnje u Autoškoli Lukić. Vodi praktičnu obuku i organizaciju časova vožnje.</p>
<p>Kod Dalibora počinje dio obuke koji kandidati najviše iščekuju, vožnja. Prvi časovi su posvećeni osnovama: podešavanju sjedišta i ogledala, polasku, mijenjanju brzina i kočenju. Zatim slijedi vožnja kroz grad, raskrsnice, kružni tokovi, parkiranje i vožnja van naselja, sve dok kandidat ne bude spreman za ispit i, još važnije, za samostalnu vožnju.</p>
<ul>
<li><strong>Strpljivo i bez pritiska.</strong> Greške se objašnjavaju, ne kažnjavaju.</li>
<li><strong>Fleksibilni termini.</strong> Časove vožnje dogovaraš direktno s Daliborom.</li>
<li><strong>Vožnja kao u stvarnom životu.</strong> Ulice Brčkog, raskrsnice i magistralni put.</li>
</ul>
<p>Za termine časova vožnje zovi Dalibora: {TD}.</p>
<p><a class="btn btn-y" href="/kontakt/">Upiši se kod nas →</a></p>''', side('/instruktori/', 'Autoškola', [('/o-nama/', 'O nama'), ('/instruktori/', 'Instruktori'), ('/teorijska-nastava/', 'Teorijska nastava'), ('/predavanja/', 'Raspored predavanja')]), alt=True)
    ld = [{"@type": "Person", "@id": DOMAIN + "/instruktori/#violeta", "name": "Violeta Lukić Vujadinović", "honorificPrefix": "Doc. dr",
           "jobTitle": "Predavač teoretske nastave", "telephone": "+387 65 537 043", "worksFor": ORG, "knowsAbout": ["Bezbjednost saobraćaja", "Saobraćajni propisi", "Obuka vozača"], "url": DOMAIN + "/instruktori/#violeta"},
          {"@type": "Person", "@id": DOMAIN + "/instruktori/#dalibor", "name": "Dalibor Vujadinović", "jobTitle": "Instruktor vožnje", "telephone": "+387 65 803 456", "worksFor": ORG, "url": DOMAIN + "/instruktori/#dalibor"}]
    return dict(path='/instruktori/', title='Instruktori Autoškole Lukić Brčko | Doc. dr Violeta i Dalibor',
                desc='Upoznaj instruktore Autoškole Lukić u Brčkom: teoriju predaje Doc. dr Violeta Lukić Vujadinović, doktor nauka iz saobraćaja, a vožnju vodi Dalibor Vujadinović.',
                crumbs=[('/', 'Početna'), ('/instruktori/', 'Instruktori')], ld=ld,
                hero=dict(chip='🎓 Ljudi koji te uče', h1='Instruktori <span>Autoškole Lukić</span>',
                          lead='Ljudi koji te uče, a ne samo ispituju: predavač sa doktoratom iz oblasti saobraćaja i strpljivi instruktor vožnje.', big='VL',
                          cta='<a href="tel:+38765537043" class="btn btn-y">📞 Violeta 065 537 043</a><a href="tel:+38765803456" class="btn btn-g">📞 Dalibor 065 803 456</a>'),
                body=body)


# ---------------------------------------------------------------- TEORIJA
def teorija():
    prose = '''
<h2>Teorija koja se <em>razumije</em>, a ne buba</h2>
<p class="lead">Teorijska nastava je temelj svake vozačke dozvole. U Autoškoli Lukić predavanja drži Doc. dr Violeta Lukić Vujadinović, doktor nauka iz oblasti saobraćaja, pa kandidati ne uče samo šta piše u testu, nego i zašto pravilo postoji.</p>

<h2>Šta se uči na <em>predavanjima</em></h2>
<ul>
<li>Osnovni pojmovi: put, kolovoz, vozač i učesnici u saobraćaju.</li>
<li>Saobraćajni znakovi: znakovi opasnosti, izričitih naredbi i obavještenja, oznake na kolovozu i svjetlosni znakovi.</li>
<li>Pravila saobraćaja: položaj vozila na putu, brzina i rastojanje, preticanje i mimoilaženje.</li>
<li>Raskrsnice i prednost prolaza, oblast u kojoj kandidati najčešće griješe na testu.</li>
<li>Zaustavljanje i parkiranje, vožnja kroz tunel, autoput i brzi put.</li>
<li>Vozač i vozilo: zdravstveno stanje, alkohol i umor, oprema i ispravnost vozila.</li>
<li>Postupak u slučaju saobraćajne nezgode.</li>
<li>Posebna pravila za kategoriju koju polažeš: motocikl, teretna vozila ili autobus.</li>
</ul>

<h2>Kako izgledaju <em>predavanja</em></h2>
<ol>
<li><strong>Grupe.</strong> Nakon upisa ulaziš u grupu za predavanja. Spisak grupa, termine i teme objavljujemo na stranici <a href="/predavanja/">Raspored predavanja</a>.</li>
<li><strong>Moderna učionica</strong> u ulici Tina Ujevića 8, Brčko.</li>
<li><strong>Primjeri iz stvarnog saobraćaja.</strong> Raskrsnice i situacije koje svaki vozač u Brčkom poznaje.</li>
<li><strong>Probni testovi.</strong> Vježbaš pitanja kakva te čekaju na teorijskom ispitu.</li>
<li><strong>Teorijski ispit.</strong> Kada si spreman, prijavljujemo te na ispit.</li>
</ol>

<h2>Prva pomoć</h2>
<p>Svaki kandidat za vozača prolazi i obuku iz prve pomoći te polaže ispit iz prve pomoći. Prema Zakonu o osnovama bezbjednosti saobraćaja na putevima u BiH, osposobljavanje kandidata iz prve pomoći obavlja Crveni krst. Pomoći ćemo ti da obuku iz prve pomoći uklopiš u raspored teorije.</p>

<h2>Učenje bez <em>straha od testa</em></h2>
<p>Kao NLP Master, Violeta pomaže kandidatima koji imaju tremu od ispita ili misle da nisu za učenje. Gradivo se dijeli na male cjeline, ponavlja kroz pitanja i povezuje sa stvarnim situacijama, pa na ispit dolaziš smiren i spreman.</p>
<p><a class="btn btn-y" href="/predavanja/">Pogledaj raspored predavanja →</a></p>'''
    return dict(path='/teorijska-nastava/', title='Teorijska nastava za vozački ispit u Brčkom | Autoškola Lukić',
                desc='Teorijska nastava za vozački ispit u Brčkom: predavanja po grupama kod Doc. dr Violete Lukić Vujadinović, probni testovi, prva pomoć i moderna učionica.',
                crumbs=[('/', 'Početna'), ('/teorijska-nastava/', 'Teorijska nastava')],
                hero=dict(chip='🎓 Predavač sa doktoratom', h1='Teorijska nastava <span>u Brčkom</span>',
                          lead='Saobraćajni propisi u modernoj učionici, kod doktora nauka iz oblasti saobraćaja. Gradivo učiš s razumijevanjem, ne napamet.', big='Dr',
                          cta='<a href="/predavanja/" class="btn btn-y">Raspored predavanja →</a><a href="tel:+38765537043" class="btn btn-g">📞 065 537 043</a>'),
                body=art(prose, side('/teorijska-nastava/')),
                ld=[svc('Teorijska nastava za kandidate za vozače u Brčkom', '/teorijska-nastava/', 'Predavanja iz poznavanja propisa o bezbjednosti saobraćaja po grupama u Autoškoli Lukić, Brčko.')])


# ---------------------------------------------------------------- UPIS
def upis():
    prose = f'''
<h2>Kako do vozačke dozvole u <em>Brčkom</em>, korak po korak</h2>
<p class="lead">Kratak i jasan vodič za kandidate koji žele upisati autoškolu u Brčkom i položiti vozački ispit iz prvog pokušaja. Ako ti bilo šta nije jasno, nazovi Violetu na {TV} i sve objašnjavamo u jednom razgovoru.</p>

<h2>1. Šta je potrebno <em>za upis</em></h2>
<ul>
<li><strong>Važeća lična karta.</strong></li>
<li><strong>Prijava boravka.</strong></li>
<li><strong>Ljekarsko uvjerenje</strong> o zdravstvenoj sposobnosti za vozača. Prema zakonu se pribavlja prije početka obuke i važi 12 mjeseci od dana izdavanja.</li>
<li><strong>Odgovarajuće godine</strong> za kategoriju, na primjer 18 za B kategoriju. Pogledaj tabelu na stranici <a href="/kategorije/">Kategorije</a>.</li>
</ul>
<p>Tačan spisak dokumenata potvrdi pozivom prije upisa.</p>

<h2>2. Upis i <em>dogovor o plaćanju</em></h2>
<p>Dođi u Tina Ujevića 8 ili nas nazovi. Dogovaramo kategoriju, način plaćanja, gotovinski ili na <a href="/cjenovnik/">rate</a>, i grupu za teoriju.</p>

<h2>3. Prva pomoć</h2>
<p>Predavanja i ispit iz prve pomoći. Obuku iz prve pomoći, prema zakonu, sprovodi Crveni krst, a mi ti pomažemo da je uklopiš u raspored.</p>

<h2>4. Teorijska nastava</h2>
<p>Saobraćajni propisi u modernoj učionici, kod <a href="/teorijska-nastava/">predavača sa doktoratom iz saobraćaja</a>. Kada i s kojom grupom dolaziš, provjeri u <a href="/predavanja/">rasporedu predavanja</a>. Dovoljno je da upišeš svoje ime u pretragu.</p>

<h2>5. Teorijski ispit</h2>
<p>Provjera znanja iz propisa i znakova. Kada položiš teoriju, prelaziš na vožnju.</p>

<h2>6. Časovi vožnje</h2>
<p>Vožnja sa strpljivim instruktorom, od osnovnih radnji vozilom do samostalne vožnje kroz grad i van naselja. Termine dogovaraš s instruktorom Daliborom na {TD}.</p>

<h2>7. Praktični ispit i <em>vozačka u rukama</em> 🏁</h2>
<p>Vožnja pred ispitnom komisijom koju imenuju nadležni organi Brčko distrikta. Komisija procjenjuje da li si osposobljen za sigurno upravljanje vozilom. Nakon položenog ispita podnosiš zahtjev za izdavanje vozačke dozvole nadležnom organu.</p>

<div class="note"><b>Autoškola na rate</b>Ako ti odmah ne odgovara plaćanje cijele obuke, u Autoškoli Lukić možeš platiti na rate. Pozovi za uslove i termin upisa u Brčkom.</div>

<h2>Nakon ispita: <em>prve dvije godine</em></h2>
<p>Vozači koji su dobili dozvolu za A1, A, B ili C1 kategoriju prve dvije godine ne smiju voziti brže od 70 km/h na putu, 90 km/h na brzom putu i 120 km/h na autoputu, ne smiju vući priključno vozilo i ne smiju organizovano prevoziti djecu. Tako propisuje {ZAKON}.</p>
{NOVA_PRAVILA}
<p><a class="btn btn-y" href="/kontakt/">Dogovori upis →</a></p>'''
    howto = {"@type": "HowTo", "name": "Kako do vozačke dozvole u Brčkom", "inLanguage": "bs",
             "step": [{"@type": "HowToStep", "position": i + 1, "name": n, "text": t} for i, (n, t) in enumerate([
                 ('Pripremi dokumente', 'Važeća lična karta, prijava boravka i ljekarsko uvjerenje o zdravstvenoj sposobnosti za vozača.'),
                 ('Upis u autoškolu', 'Dogovor o kategoriji, načinu plaćanja (gotovina ili rate) i grupi za teoriju.'),
                 ('Prva pomoć', 'Predavanja i ispit iz prve pomoći.'),
                 ('Teorijska nastava', 'Saobraćajni propisi u učionici po rasporedu grupe.'),
                 ('Teorijski ispit', 'Provjera znanja iz propisa i znakova.'),
                 ('Časovi vožnje', 'Vožnja sa instruktorom do spremnosti za ispit.'),
                 ('Praktični ispit', 'Vožnja pred ispitnom komisijom i izdavanje vozačke dozvole.')])]}
    return dict(path='/upis/', title='Kako do vozačke dozvole u Brčkom: upis i dokumenti | Lukić',
                desc='Vodič za upis u autoškolu u Brčkom: potrebni dokumenti, ljekarsko uvjerenje, prva pomoć, teorijski i praktični ispit, plaćanje na rate. Autoškola Lukić.',
                crumbs=[('/', 'Početna'), ('/upis/', 'Upis')], ld=[howto],
                hero=dict(chip='📋 Vodič za kandidate', h1='Kako do vozačke dozvole <span>u Brčkom</span>',
                          lead='Dokumenti, redoslijed ispita i savjeti. Sve što trebaš znati prije upisa, na jednom mjestu.', big='1·7'),
                body=art(prose, side('/upis/')))


# ---------------------------------------------------------------- CJENOVNIK
def cjenovnik():
    body = f'''<section class="sec"><div class="wrap">
<div class="pr rvl" style="margin-top:0">
  <div class="card tilt"><i class="gl"></i><h2 style="font-weight:900;font-size:1.3rem">Gotovinsko plaćanje</h2><div class="price">{price(CIJENA_GOTOVINA)}</div>
    <ul><li>Teorijska nastava</li><li>Fond časova vožnje</li><li>Prijava i polaganje ispita</li></ul><a href="tel:+38765537043" class="btn btn-y">Zatraži ponudu</a></div>
  <div class="card tilt hot"><i class="gl"></i><span class="tag">POVOLJNO</span><h2 style="font-weight:900;font-size:1.3rem">Plaćanje na rate</h2><div class="price">{price(CIJENA_RATE)}</div>
    <ul><li>Teorijska nastava</li><li>Fond časova vožnje</li><li>Prijava i polaganje ispita</li><li>Mogućnost plaćanja na rate</li></ul><a href="tel:+38765537043" class="btn btn-y">Zatraži ponudu</a></div>
</div></div></section>''' + art(f'''
<h2>Koliko košta <em>autoškola u Brčkom</em>?</h2>
<p class="lead">Cijena obuke zavisi od kategorije i načina plaćanja. Paket u Autoškoli Lukić obuhvata teorijsku nastavu, fond časova vožnje te prijavu i polaganje ispita. Za tačnu ponudu za svoju kategoriju nazovi {TV}.</p>

<h2>Šta je uključeno u <em>paket</em></h2>
<ul>
<li><strong>Teorijska nastava</strong> u učionici, po grupama.</li>
<li><strong>Fond časova vožnje</strong> sa instruktorom.</li>
<li><strong>Prijava i polaganje ispita.</strong></li>
</ul>
<p>Ljekarsko uvjerenje se radi u zdravstvenoj ustanovi i plaća se posebno. Pri upisu ti tačno kažemo šta je uključeno u cijenu, a šta, ako išta, plaćaš odvojeno. Bez skrivenih troškova.</p>

<h2>Kako funkcioniše <em>plaćanje na rate</em></h2>
<ol>
<li>Pri upisu biraš plaćanje na rate.</li>
<li>Zajedno dogovaramo iznos i dinamiku rata koja ti odgovara.</li>
<li>Obuka teče normalno. Učiš i voziš kao i svi ostali kandidati.</li>
</ol>
<p>Uslove rata dogovaraš na upisu. Nazovi i pitaj, bez obaveze.</p>

<h2>Cijene po kategorijama</h2>
<p>Obuka za <a href="/b-kategorija/">B kategoriju</a> je najtraženija, ali nudimo i <a href="/a-kategorija/">A</a>, <a href="/c-kategorija/">C1 i C</a>, <a href="/ce-kategorija/">CE</a> i <a href="/d-kategorija/">D</a> kategoriju. Cijene za ove kategorije razlikuju se zbog vozila i obima obuke, pa se javi za ponudu.</p>

<h2>Dodatni časovi</h2>
<p>Ako ti nakon fonda časova treba još vožnje prije ispita, dogovaramo dodatne časove. Cilj nam je da na ispit izađeš spreman.</p>
<p><a class="btn btn-y" href="tel:+38765537043">📞 Zatraži ponudu: 065 537 043</a></p>''', side('/cjenovnik/'), alt=True)
    faq = [('Koliko košta autoškola u Brčkom?', HOME_FAQ[2][1]), ('Mogu li autoškolu platiti na rate?', HOME_FAQ[3][1])]
    return dict(path='/cjenovnik/', title='Cijena autoškole u Brčkom i plaćanje na rate | Autoškola Lukić',
                desc='Cijene obuke u Autoškoli Lukić Brčko: gotovinsko plaćanje ili plaćanje na rate. Paket uključuje teoriju, fond časova vožnje i polaganje ispita.',
                crumbs=[('/', 'Početna'), ('/cjenovnik/', 'Cjenovnik')], faq=faq,
                hero=dict(chip='💳 Plaćanje na rate', h1='Cijene obuke i <span>plaćanje na rate</span>',
                          lead='Jasne cijene i način plaćanja koji ti odgovara. Odjednom ili na rate, bez skrivenih troškova.', big='KM'),
                body=body)


# ---------------------------------------------------------------- GALERIJA
def galerija():
    body = f'''<section class="sec"><div class="wrap">
<p class="sub mut rvl" style="margin-top:0">Svaka fotografija je jedna položena vozačka. Hvala svim kandidatima koji su nam ukazali povjerenje! Klikni na fotografiju za uvećan prikaz.</p>
<div class="gal rvl">{gal_html(GAL)}</div>
<p class="ctr" style="margin-top:36px">Više fotografija i čestitki objavljujemo na <a class="more-link" style="margin-top:0" href="/novosti/">Novostima</a> i na Instagramu <a class="more-link" style="margin-top:0" href="https://www.instagram.com/autoskolalukic" target="_blank" rel="noopener">@autoskolalukic</a></p>
</div></section>'''
    ld = [{"@type": "ImageGallery", "name": "Galerija Autoškole Lukić Brčko", "image": [
        {"@type": "ImageObject", "contentUrl": DOMAIN + f"/img/galerija/{f}.webp", "caption": a, "width": 560, "height": 700} for f, a, c in GAL]}]
    return dict(path='/galerija/', title='Galerija: položili su! Kandidati Autoškole Lukić Brčko',
                desc='Fotografije kandidata Autoškole Lukić iz Brčkog nakon položenog vozačkog ispita i sa teorijske nastave. Vozačka u ruke, osmijeh na licu.',
                crumbs=[('/', 'Početna'), ('/galerija/', 'Galerija')], ld=ld, prio='0.6', images=[f'/img/galerija/{f}.webp' for f, a, c in GAL],
                hero=dict(chip='📸 Naši kandidati', h1='Položili su! <span>Naši kandidati</span>',
                          lead='Vozačka u ruke, osmijeh na licu. Pogledaj kandidate koji su vozačku dozvolu stekli u Autoškoli Lukić.', big='✓'),
                body=body)


# ---------------------------------------------------------------- PITANJA
PITANJA = [
    ('Upis', [
        HOME_FAQ[0], HOME_FAQ[4],
        ('Sa koliko godina mogu upisati autoškolu?', 'Zavisi od kategorije. Prema zakonu u BiH, B kategoriju možeš dobiti sa 18 godina, A sa 18, C1 sa 18, C i CE sa 21, a D sa 24 godine. Pregled je na stranici <a href="/kategorije/">Kategorije</a>.'),
        ('Koliko važi ljekarsko uvjerenje?', 'Ljekarsko uvjerenje o zdravstvenoj sposobnosti za vozača pribavlja se prije početka obuke i važi 12 mjeseci od dana izdavanja.'),
        ('Primate li kandidate iz okoline Brčkog?', 'Primamo. Kandidati nam dolaze iz cijelog Brčko distrikta i okoline: Bijele, Brke, Gornjeg Rahića, Maoče i drugih mjesta.'),
    ]),
    ('Obuka', [
        HOME_FAQ[1], HOME_FAQ[5],
        ('Kada su predavanja i u kojoj sam grupi?', 'Raspored po grupama objavljujemo na stranici <a href="/predavanja/">Predavanja</a>. Upiši svoje ime u pretragu i odmah vidiš svoju grupu i termine.'),
        ('Kako se dogovaraju časovi vožnje?', 'Termine časova vožnje dogovaraš direktno s instruktorom Daliborom na 065 803 456, tako da se uklope u školu ili posao.'),
        ('Ko sprovodi obuku iz prve pomoći?', 'Prema Zakonu o osnovama bezbjednosti saobraćaja na putevima u BiH, osposobljavanje kandidata iz prve pomoći obavlja Crveni krst. Pomažemo ti da je uklopiš u raspored.'),
    ]),
    ('Plaćanje', [
        HOME_FAQ[2], HOME_FAQ[3],
        ('Da li se ljekarsko uvjerenje plaća posebno?', 'Da. Ljekarsko uvjerenje se radi u zdravstvenoj ustanovi i plaća se posebno. Pri upisu ti kažemo šta je tačno uključeno u cijenu obuke.'),
    ]),
    ('Ispit i nakon ispita', [
        ('Ko organizuje vozački ispit u Brčkom?', 'Vozački ispit se polaže pred komisijom koju imenuju nadležni organi Brčko distrikta. Mi te prijavljujemo i pripremamo za ispit.'),
        ('Šta ako ne položim iz prvog pokušaja?', 'Dogovaramo dodatnu pripremu i novi termin. Cilj nam je da položiš i voziš sigurno.'),
        ('Koja ograničenja imam prve dvije godine?', 'Vozači koji su dobili dozvolu za A1, A, B ili C1 prve dvije godine ne smiju voziti brže od 70 km/h na putu, 90 km/h na brzom putu i 120 km/h na autoputu, ne smiju vući priključno vozilo niti organizovano prevoziti djecu.'),
        ('Mijenjaju li se pravila za obuku?', 'Prema najavi Ministarstva komunikacija i prometa BiH, od 1. januara 2028. za B kategoriju se uvodi pet časova praktične obuke više, a prvih pet časova vozi se na poligonu.'),
    ]),
]


def pitanja():
    flat = [qa for _, l in PITANJA for qa in l]
    blocks, n = [], 1
    for naslov, lst in PITANJA:
        items = []
        for q, a in lst:
            items.append(f'<details class="fq"><summary><span class="fn">{n:02d}</span><span>{q}</span></summary><p>{a}</p></details>')
            n += 1
        blocks.append(f'<h2 class="t" style="text-align:left;font-size:1.5rem;margin:40px 0 16px">{naslov}</h2><div class="faq">{"".join(items)}</div>')
    body = f'<section class="sec"><div class="wrap art"><div class="prose" style="max-width:820px">{"".join(blocks)}</div>{side("/pitanja/")}</div></section>'
    return dict(path='/pitanja/', title='Česta pitanja o autoškoli: upis, cijena, rate i ispit | Lukić',
                desc='Odgovori na najčešća pitanja kandidata: upis, dokumenti, godine po kategorijama, cijena i rate, predavanja, prva pomoć i vozački ispit u Brčkom.',
                crumbs=[('/', 'Početna'), ('/pitanja/', 'Česta pitanja')], faq=flat,
                hero=dict(chip='❓ Pitanja i odgovori', h1='Česta pitanja o <span>autoškoli u Brčkom</span>',
                          lead='Sve što kandidati najčešće pitaju prije upisa, na jednom mjestu. Ako odgovor nije ovdje, nazovi nas.', big='?'),
                body=body)


# ---------------------------------------------------------------- KONTAKT
def kontakt():
    body = f'''<section class="sec"><div class="wrap">
<div class="ct rvl" style="margin-top:0">
  <div class="card tilt"><i class="gl"></i>
    <div class="row"><div class="ico">📍</div><div><small>Adresa</small><b>Tina Ujevića 8, 76100 Brčko</b></div></div>
    <div class="row"><div class="ico">📞</div><div><small>Violeta: upis, cijene, rate, predavanja</small><a href="tel:+38765537043"><b>065 537 043</b></a></div></div>
    <div class="row"><div class="ico">📞</div><div><small>Dalibor: termini časova vožnje</small><a href="tel:+38765803456"><b>065 803 456</b></a></div></div>
    <div class="row"><div class="ico">💬</div><div><small>SMS poruka</small><a href="sms:+38765537043"><b>Pošalji poruku Violeti</b></a></div></div>
    <div class="row"><div class="ico">📸</div><div><small>Instagram</small><a href="https://www.instagram.com/autoskolalukic" target="_blank" rel="noopener"><b>@autoskolalukic</b></a></div></div>
  </div>
  <div class="map">
    <iframe title="Mapa: Autoškola Lukić, Tina Ujevića 8, Brčko" loading="lazy" referrerpolicy="no-referrer-when-downgrade" src="https://www.google.com/maps?q=Tina+Ujevi%C4%87a+8+Br%C4%8Dko+76100&amp;output=embed"></iframe>
    <a target="_blank" rel="noopener" href="{MAPS}">Otvori navigaciju →</a>
  </div>
</div></div></section>''' + art(f'''
<h2>Koga <em>zvati</em>?</h2>
<ul>
<li><strong>Upis, cijene, rate i raspored predavanja:</strong> Violeta, {TV}.</li>
<li><strong>Termini časova vožnje:</strong> Dalibor, {TD}.</li>
</ul>
<h2>Kako do nas</h2>
<p>Autoškola Lukić se nalazi u ulici <strong>Tina Ujevića 8</strong> u Brčkom, poštanski broj 76100. Najlakše je da otvoriš <a href="{MAPS}" target="_blank" rel="noopener">navigaciju na Google mapama</a>, koja te vodi do samih vrata.</p>
<p>Kandidate primamo iz cijelog Brčko distrikta i okoline: Brčko, Bijela, Brka, Gornji Rahić, Maoča i druga mjesta.</p>
<h2>Prije nego što dođeš</h2>
<p>Ponesi ličnu kartu, a ako već imaš ljekarsko uvjerenje, i njega. Spisak potrebnih dokumenata je na stranici <a href="/upis/">Kako do vozačke dozvole</a>.</p>''', side('/kontakt/'), alt=True)
    return dict(path='/kontakt/', title='Kontakt | Autoškola Lukić, Tina Ujevića 8, Brčko, 065 537 043',
                desc='Kontakt Autoškole Lukić: Tina Ujevića 8, 76100 Brčko. Upis i informacije: Violeta, 065 537 043. Časovi vožnje: Dalibor, 065 803 456. Mapa i navigacija.',
                crumbs=[('/', 'Početna'), ('/kontakt/', 'Kontakt')], page_type='ContactPage', prio='0.9',
                hero=dict(chip='📞 Javi nam se', h1='Autoškola Brčko: <span>kontakt i lokacija</span>',
                          lead='Pozovi, pošalji poruku ili svrati u Tina Ujevića 8. Rado odgovaramo na sva pitanja o obuci, ratama i kategorijama.', big='065',
                          cta='<a href="tel:+38765537043" class="btn btn-y">📞 Violeta 065 537 043</a><a href="tel:+38765803456" class="btn btn-g">📞 Dalibor 065 803 456</a>'),
                body=body)


# ---------------------------------------------------------------- PREDAVANJA
def predavanja():
    body = '''<section class="sec"><div class="wrap">
<div class="banner" id="pv-banner" hidden><b>Primjer rasporeda.</b> Ovo su probni podaci. Stvarni raspored grupa bit će objavljen uskoro, a za termine nazovi 065 537 043.</div>
<div class="note" id="pv-note" hidden style="margin-bottom:22px"></div>
<div class="pv-tools">
  <div class="srch"><label for="pv-q" class="sr">Pretraga po imenu</label><input id="pv-q" type="search" placeholder="Upiši svoje ime i pronađi svoju grupu" autocomplete="off"></div>
  <div class="flt" id="pv-flt" role="group" aria-label="Filter po kategoriji"></div>
</div>
<div class="pv-meta" id="pv-meta"></div>
<div id="pv-app"><div class="grp" id="pv-list"><div class="empty"><b>Učitavam raspored…</b></div></div></div>
<noscript><div class="empty"><b>Za prikaz rasporeda uključi JavaScript</b>ili nazovi 065 537 043.</div></noscript>
</div></section>''' + art(f'''
<h2>Kako koristiti <em>raspored</em></h2>
<ol>
<li><strong>Upiši svoje ime</strong> u polje za pretragu i odmah vidiš grupu u kojoj si i sve termine.</li>
<li>Termin označen kao <strong>SLJEDEĆE</strong> je tvoje naredno predavanje, a prošli termini su posivljeni.</li>
<li>Raspored možeš <strong>odštampati</strong> ili sačuvati link na telefonu.</li>
</ol>
<h2>Gdje se održavaju predavanja</h2>
<p>Sva predavanja su u učionici Autoškole Lukić, <strong>Tina Ujevića 8, Brčko</strong>. Predavanja drži <a href="/instruktori/#violeta">Doc. dr Violeta Lukić Vujadinović</a>. Više o tome šta se uči pročitaj na stranici <a href="/teorijska-nastava/">Teorijska nastava</a>.</p>
<h2>Ne možeš doći na termin?</h2>
<p>Javi se Violeti na {TV} što prije, pa ćemo dogovoriti kako da nadoknadiš propušteno gradivo.</p>
<h2>Još nisi upisan?</h2>
<p>Nove grupe se formiraju redovno. Nazovi i saznaj kada počinje sljedeća grupa za tvoju kategoriju ili pročitaj <a href="/upis/">vodič za upis</a>.</p>''', side('/predavanja/'), alt=True)
    return dict(path='/predavanja/', title='Raspored predavanja po grupama | Autoškola Lukić Brčko',
                desc='Raspored teorijske nastave u Autoškoli Lukić Brčko: termini predavanja po grupama i spiskovi kandidata. Upiši svoje ime i pronađi svoju grupu.',
                crumbs=[('/', 'Početna'), ('/predavanja/', 'Predavanja')], freq='daily', prio='0.8',
                hero=dict(chip='🗓️ Ažurira se redovno', h1='Raspored <span>predavanja</span>',
                          lead='Ko, kada i u kojoj grupi dolazi na teorijsku nastavu. Upiši svoje ime i odmah vidi svoje termine.', big='17:00',
                          cta='<a href="#pv-q" class="btn btn-y">🔎 Pronađi svoju grupu</a><a href="tel:+38765537043" class="btn btn-g">📞 065 537 043</a>'),
                body=body, scripts=['/assets/postavke.js', '/podaci/predavanja.js', '/assets/podaci.js'])


# ---------------------------------------------------------------- NOVOSTI
def novosti():
    body = '''<section class="sec"><div class="wrap">
<div class="banner" id="nw-banner" hidden><b>Primjeri objava.</b> Ovdje će se prikazivati Violetine objave sa Facebooka.</div>
<div class="nw" id="nw-app">
  <div class="posts" id="nw-list"><div class="empty"><b>Učitavam objave…</b></div></div>
  <div id="nw-fb"></div>
</div>
<p class="ctr"><a class="more-link" id="nw-fblink" href="#" target="_blank" rel="noopener" hidden>Prati nas na Facebooku →</a></p>
</div></section>'''
    return dict(path='/novosti/', title='Novosti i obavještenja | Autoškola Lukić Brčko',
                desc='Najnovije objave Autoškole Lukić iz Brčkog: upis novih grupa, termini predavanja, obavještenja i čestitke kandidatima koji su položili vozački ispit.',
                crumbs=[('/', 'Početna'), ('/novosti/', 'Novosti')], freq='daily', prio='0.7', page_type='CollectionPage',
                hero=dict(chip='📣 Objave sa Facebooka', h1='Novosti iz <span>Autoškole Lukić</span>',
                          lead='Obavještenja o upisu, terminima i ispitima te čestitke kandidatima. Violetine objave sa Facebooka na jednom mjestu.', big='Novo',
                          cta='<a href="tel:+38765537043" class="btn btn-y">📞 065 537 043</a><a href="https://www.instagram.com/autoskolalukic" target="_blank" rel="noopener" class="btn btn-g">📸 Instagram</a>'),
                body=body, scripts=['/assets/postavke.js', '/podaci/objave.js', '/assets/podaci.js'])


def p404():
    return dict(path='/404.html', title='Stranica nije pronađena | Autoškola Lukić Brčko', desc='Tražena stranica ne postoji.',
                crumbs=[('/', 'Početna'), ('/404.html', 'Stranica nije pronađena')], robots='noindex,follow', sitemap=False,
                hero=dict(chip='🚧 Skretanje', h1='Ups, pogrešno <span>skretanje</span>',
                          lead='Ova stranica ne postoji ili je premještena. Vrati se na početnu ili odaberi neku od stranica ispod.', big='404',
                          cta='<a href="/" class="btn btn-y">← Početna</a><a href="/kontakt/" class="btn btn-g">Kontakt</a>'),
                body=related('Možda tražiš <em>ovo</em>', [('/b-kategorija/', 'B', 'B kategorija', 'Najtraženija obuka.'), ('/predavanja/', '📅', 'Predavanja', 'Raspored po grupama.'), ('/cjenovnik/', 'KM', 'Cjenovnik', 'Cijene i rate.')], alt=False))


def pages():
    return [home(), kategorije(), b_kat(), a_kat(), c_kat(), ce_kat(), d_kat(), o_nama(), instruktori(), teorija(),
            upis(), cjenovnik(), predavanja(), novosti(), galerija(), pitanja(), kontakt(), p404()]
