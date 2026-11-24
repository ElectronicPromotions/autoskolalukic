# -*- coding: utf-8 -*-
"""Sadržaj svih stranica sajta Autoškole DrivePro (Brčko)."""
import os, re

HERE = os.path.dirname(os.path.abspath(__file__))
CARSYM = open(os.path.join(HERE, 'carsym.svg'), encoding='utf-8').read()
DOMAIN = 'https://autoskoladrivepro.vercel.app'
ORG = {"@id": DOMAIN + '/#autoskola'}

# Glavni broj je Daliborov. Vladanin broj je drugi kontakt.
TD = '<a href="tel:+38765803456">065 803 456</a>'
TV = '<a href="tel:+38765858411">065 858 411</a>'
ADR = 'Hasana Bećirevića 3'
MAPS = 'https://www.google.com/maps/search/?api=1&amp;query=Hasana+Be%C4%87irevi%C4%87a+3+Br%C4%8Dko+76100'
MAPS_EMBED = 'https://www.google.com/maps?q=Hasana+Be%C4%87irevi%C4%87a+3+Br%C4%8Dko+76100&amp;output=embed'
IG = 'https://www.instagram.com/driveproautoskola'
ZAKON = 'Zakon o osnovama bezbjednosti saobraćaja na putevima u BiH'

# Galerija: fotografije (.webp, 560x700) stavite u sajt/img/galerija/ i upišite ih ovdje:
# ('ime-fajla-bez-ekstenzije', 'alt tekst za Google', 'kratak opis ispod slike')
# Dok je lista prazna, umjesto galerije se prikazuje poziv na Instagram.
GAL = []


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
  <div class="scard"><h3>Upis i informacije</h3><p>{ADR}, Brčko. Pozovi i dogovori upis, termine vožnje i rate.</p>
    <a href="tel:+38765803456" class="btn btn-y">📞 Dalibor 065 803 456</a>
    <a href="tel:+38765858411" class="btn btn-g">📞 Vladana 065 858 411</a></div>
  <nav class="sl" aria-label="{title}"><h3>{title}</h3>{ls}</nav>
  <nav class="sl" aria-label="Korisno"><h3>Korisno</h3><a href="/upis/">Kako do vozačke dozvole</a><a href="/pitanja/">Česta pitanja</a></nav>
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
<aside class="faqa rvl"><div class="qm" aria-hidden="true">?</div><h2>{title}</h2><p>Ako nešto nije jasno, nazovi nas. Odgovaramo na sva pitanja prije upisa.</p><a href="tel:+38765803456" class="btn btn-y">📞 065 803 456</a></aside>
<div class="faq rvl">{"".join(out)}</div></div></section>'''


def svc(name, path, desc):
    return {"@type": "Service", "@id": DOMAIN + path + '#usluga', "name": name, "serviceType": "Obuka vozača",
            "description": desc, "provider": ORG, "areaServed": [{"@type": "City", "name": "Brčko"}, {"@type": "AdministrativeArea", "name": "Brčko distrikt BiH"}],
            "url": DOMAIN + path,
            "offers": {"@type": "Offer", "availability": "https://schema.org/InStock", "url": DOMAIN + "/",
                       "seller": ORG, "description": "Besplatna teoretska nastava, plaćanje odjednom ili u do 5 rata"}}


ALL_KAT = [('/b-kategorija/', 'B', 'B kategorija', 'Putnički automobil. Najtraženija kategorija, od 18 godina.'),
           ('/a-kategorija/', 'A', 'A kategorija', 'Motocikli. Obuka na poligonu i u saobraćaju, od 18 godina.'),
           ('/c-kategorija/', 'C1·C', 'C1 i C kategorija', 'Teretna vozila. C1 od 18, C od 21 godine.'),
           ('/ce-kategorija/', 'CE', 'CE kategorija', 'Kamion s prikolicom, za vozače koji već imaju C.'),
           ('/d-kategorija/', 'D', 'D kategorija', 'Autobusi, od 24 godine, uz prethodnu B, C ili D1.')]


def other_kat(path):
    return [k for k in ALL_KAT if k[0] != path]


def gal_html(items):
    return ''.join(f'<a class="gi" href="/img/galerija/{f}.webp" data-lb><img src="/img/galerija/{f}.webp" alt="{a}" width="560" height="700" loading="lazy" decoding="async"><span class="cap">{c}</span></a>' for f, a, c in items)


def gal_block():
    if GAL:
        return f'<div class="gal rvl">{gal_html(GAL)}</div>'
    return f'''<div class="igcta rvl"><div class="igi" aria-hidden="true">📸</div><div><h3>Naše kandidate objavljujemo na Instagramu</h3><p>Položeni ispiti, čestitke i trenuci sa obuke su na profilu <b>@driveproautoskola</b>.</p></div><a class="btn btn-y" href="{IG}" target="_blank" rel="noopener">Otvori Instagram →</a></div>'''


# ---------------------------------------------------------------- HOME
def home_ld(D, org_id):
    return [
        {"@type": "DrivingSchool", "@id": org_id, "name": "Autoškola DrivePro",
         "alternateName": ["Autoškola Drive Pro", "Autoskola DrivePro", "DrivePro Brčko", "Auto škola DrivePro"],
         "url": D + "/", "image": [D + "/og-image.jpg"], "logo": D + "/android-chrome-512x512.png",
         "description": "Autoškola DrivePro u Brčkom: obuka za A, B, C1, C, CE i D kategoriju, besplatna teoretska nastava, plaćanje do 5 rata i termini vožnje po izboru kandidata.",
         "slogan": "Vaša prva stanica na putu ka sigurnoj vožnji", "telephone": "+387 65 803 456",
         "contactPoint": [
             {"@type": "ContactPoint", "contactType": "upis, informacije i časovi vožnje", "telephone": "+387 65 803 456", "name": "Dalibor", "availableLanguage": ["bs", "hr", "sr"]},
             {"@type": "ContactPoint", "contactType": "informacije i teorijska nastava", "telephone": "+387 65 858 411", "name": "Vladana", "availableLanguage": ["bs", "hr", "sr"]}],
         "address": {"@type": "PostalAddress", "streetAddress": ADR, "addressLocality": "Brčko", "postalCode": "76100", "addressRegion": "Brčko distrikt", "addressCountry": "BA"},
         "hasMap": "https://www.google.com/maps/search/?api=1&query=Hasana+Be%C4%87irevi%C4%87a+3+Br%C4%8Dko+76100",
         "areaServed": [{"@type": "City", "name": "Brčko"}, {"@type": "AdministrativeArea", "name": "Brčko distrikt BiH"}],
         "sameAs": [IG],
         "paymentAccepted": "Plaćanje odjednom ili u do 5 rata", "currenciesAccepted": "BAM", "knowsLanguage": "bs",
         "employee": [{"@type": "Person", "@id": D + "/instruktori/#dalibor", "name": "Dalibor Vujadinović", "jobTitle": "Instruktor vožnje, dipl. inž. saobraćaja"},
                      {"@type": "Person", "@id": D + "/instruktori/#vladana", "name": "Vladana Vujadinović", "jobTitle": "Predavač teorijske nastave i instruktor B kategorije, dipl. inž. saobraćaja"}],
         "hasOfferCatalog": {"@type": "OfferCatalog", "name": "Obuka vozača", "itemListElement": [
             {"@type": "Offer", "itemOffered": {"@id": D + p + "#usluga", "@type": "Service", "name": "Obuka za " + n + " u Brčkom", "url": D + p}} for p, b, n, t in ALL_KAT]}},
        {"@type": "WebSite", "@id": D + "/#website", "url": D + "/", "name": "Autoškola DrivePro Brčko", "inLanguage": "bs", "publisher": {"@id": org_id}},
        {"@type": "WebPage", "@id": D + "/#stranica", "url": D + "/", "name": HOME_TITLE,
         "isPartOf": {"@id": D + "/#website"}, "about": {"@id": org_id}, "inLanguage": "bs", "dateModified": "2026-11-19"},
        {"@type": "FAQPage", "@id": D + "/#pitanja", "inLanguage": "bs", "mainEntity": [
            {"@type": "Question", "name": q, "acceptedAnswer": {"@type": "Answer", "text": strip_tags(a)}} for q, a in HOME_FAQ]}]


HOME_TITLE = 'Autoškola Brčko | DrivePro, besplatna teorija i plaćanje na rate'

HOME_FAQ = [
    ('Gdje se nalazi Autoškola DrivePro u Brčkom?', f'Autoškola DrivePro nalazi se u ulici {ADR}, 76100 Brčko. Kandidati iz cijelog Brčko distrikta i okoline su dobrodošli.'),
    ('Koje kategorije vozačke dozvole nudite?', 'U Autoškoli DrivePro možeš se obučiti za A, B, C1, C, CE i D kategoriju. B kategorija je najtraženija.'),
    ('Koliko košta autoškola u Brčkom?', 'Teoretska nastava je kod nas besplatna. Cijena ostatka obuke zavisi od kategorije i obuhvata časove vožnje te prijavu i polaganje ispita. Nazovi 065 803 456 i dobit ćeš tačnu ponudu.'),
    ('Mogu li autoškolu platiti na rate?', 'Možeš. Obuku možeš platiti odjednom ili u do 5 rata, a uslove dogovaramo pri upisu.'),
    ('Kako se upisati i koji su dokumenti potrebni?', f'Nazovi 065 803 456 ili dođi u ulicu {ADR}. Obično su potrebni važeća lična karta, prijava boravka i ljekarsko uvjerenje o zdravstvenoj sposobnosti za vozača. Za B kategoriju u proces obuke možeš ući tri mjeseca prije 18. rođendana. Tačan spisak dokumenata potvrđujemo pri upisu.'),
    ('Ko predaje teoriju, a ko vodi vožnju?', 'Teorijsku nastavu predaje Vladana Vujadinović, diplomirani inženjer saobraćaja i instruktor B kategorije. Časove vožnje vodi instruktor Dalibor Vujadinović, diplomirani inženjer saobraćaja, strpljivo i bez pritiska.'),
]


def home():
    faq = ''.join(f'<details class="fq"{" open" if i == 0 else ""}><summary><span class="fn">{i+1:02d}</span><span>{q}</span></summary><p>{a}</p></details>' for i, (q, a) in enumerate(HOME_FAQ))
    tag = '<span class="tag">NAJTRAŽENIJA</span>'
    kat_cards = ''.join(f'<a class="card tilt{" hot" if b == "B" else ""}" href="{p}"><i class="gl"></i>{tag if b == "B" else ""}<span class="lt2">{b}</span><h3>{n} u Brčkom</h3><p>{t}</p><span class="more">Detalji obuke →</span></a>' for p, b, n, t in ALL_KAT)
    kat_cards += '<a class="card tilt dk" href="/teorijska-nastava/"><i class="gl"></i><span class="lt2">0 KM</span><h3>Besplatna teoretska nastava</h3><p>Saobraćajne propise učiš kod diplomiranog inženjera saobraćaja, bez naplate. S razumijevanjem, ne napamet.</p><span class="more">O teoretskoj nastavi →</span></a>'
    hero = f'''<section id="pocetna" class="hero">
  <div class="orb o1"></div><div class="orb o2"></div>
  <div class="wrap hg">
    <div>
      <span class="chip">🚦 Prva stanica do vozačke</span>
      <h1>Autoškola DrivePro u Brčkom<br><span>Teorija je besplatna.</span></h1>
      <p class="l">Vozačka dozvola A, B, C1, C, CE i D kategorije u Brčkom. Teoretska nastava bez naplate, plaćanje u do 5 rata, a termine vožnje i ispita biraš sam.</p>
      <div class="cta">
        <a href="/kontakt/" class="btn btn-y">Zakaži obuku →</a>
        <a href="tel:+38765803456" class="btn btn-g">📞 065 803 456</a>
      </div>
    </div>
    <div class="stage" id="stage">
      <div class="hcard">
        <div class="hav" aria-hidden="true"><span class="av b">DV</span><span class="av y">VV</span></div>
        <div class="hx"><span class="hk">Tvoji instruktori</span><p class="hn">Dalibor i Vladana Vujadinović</p><p class="hs">Diplomirani inženjeri saobraćaja</p></div>
        <div class="hr"><span>📍 {ADR}, Brčko</span><a class="hl" href="/instruktori/">Upoznaj instruktore →</a></div>
      </div>
      <div class="car" id="car" role="img" aria-label="Školski automobil Autoškole DrivePro Brčko, tel. 065 803 456"><svg class="carsvg" viewBox="0 58 600 192" aria-hidden="true"><use href="#carsym" x="0" y="0" width="600" height="250"/></svg><i class="whl" style="left:15.167%;top:59.896%;width:9.000%;height:28.125%"><svg viewBox="-27 -27 54 54" aria-hidden="true"><circle r="27" fill="url(#cr)"/><g stroke="#5b6472" stroke-width="6" stroke-linecap="round"><path d="M0 -19V0"/><path d="M0 -19V0" transform="rotate(72)"/><path d="M0 -19V0" transform="rotate(144)"/><path d="M0 -19V0" transform="rotate(216)"/><path d="M0 -19V0" transform="rotate(288)"/></g><circle r="6" fill="#3d4450"/></svg></i><i class="whl" style="left:76.167%;top:59.896%;width:9.000%;height:28.125%"><svg viewBox="-27 -27 54 54" aria-hidden="true"><circle r="27" fill="url(#cr)"/><g stroke="#5b6472" stroke-width="6" stroke-linecap="round"><path d="M0 -19V0"/><path d="M0 -19V0" transform="rotate(72)"/><path d="M0 -19V0" transform="rotate(144)"/><path d="M0 -19V0" transform="rotate(216)"/><path d="M0 -19V0" transform="rotate(288)"/></g><circle r="6" fill="#3d4450"/></svg></i></div>
      <div class="chips">
        <div class="fs"><b>0 KM</b><span>teoretska nastava</span></div>
        <div class="fs fs2"><b>do 5</b><span>rata za plaćanje</span></div>
        <div class="fs fs3"><b>Ti biraš</b><span>termine vožnje</span></div>
      </div>
    </div>
  </div>
  <div class="road"></div>
  <div class="curb"></div>
</section>
<div class="mq"><div class="mqm"><div id="mq" aria-live="off"></div></div></div>'''
    gal_more = '<p class="ctr"><a class="more-link" href="/galerija/">Cijela galerija →</a></p>' if GAL else ''
    body = f'''<section id="o-nama" class="sec">
  <div class="wrap">
    <h2 class="t rvl">Zašto izabrati <em>Autoškolu DrivePro</em> u Brčkom?</h2>
    <ul class="facts rvl">
      <li><b>A, B, C1, C, CE, D</b><span>Teorija, vožnja i prijava ispita</span></li>
      <li><b>Teorija 0 KM</b><span>Teoretska nastava je besplatna</span></li>
      <li><b>Do 5 rata</b><span>Plaćanje obuke na rate</span></li>
      <li><b>{ADR}</b><span>Brčko, 065 803 456</span></li>
    </ul>
    <div class="g4 rvl">
      <div class="card tilt"><i class="gl"></i><div class="ico">🗓️</div><h3>Ti biraš termine</h3><p>Termine časova vožnje i ispita biraš sam, pa se obuka uklapa u školu ili posao.</p></div>
      <div class="card tilt"><i class="gl"></i><div class="ico">🎓</div><h3>Stručni instruktori</h3><p>Obuku vode Dalibor i Vladana Vujadinović, diplomirani inženjeri saobraćaja.</p></div>
      <div class="card tilt"><i class="gl"></i><div class="ico">🤝</div><h3>Bez straha od vožnje</h3><p>Individualan pristup i radionice za prevazilaženje straha od vožnje. Svaka greška dobije objašnjenje, a ne ukor.</p></div>
      <div class="card tilt"><i class="gl"></i><div class="ico">💳</div><h3>Besplatna teorija i rate</h3><p>Teoretska nastava je besplatna, a ostatak obuke možeš platiti u do 5 rata.</p></div>
    </div>
    <p class="ctr"><a class="more-link" href="/o-nama/">Više o Autoškoli DrivePro →</a></p>
    <div class="quick rvl">
      <div><h3>Brzi upis, javi nam se danas</h3><p>{ADR}, Brčko. Pozovi i dogovori upis, termine vožnje i rate.</p></div>
      <a href="tel:+38765803456" class="btn btn-y">📞 Dalibor</a>
      <a href="tel:+38765858411" class="btn btn-y">📞 Vladana</a>
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
      <div class="card step tilt"><i class="gl"></i><h3>Teorija</h3><p>Besplatna teoretska nastava i probni testovi.</p></div>
      <div class="card step tilt"><i class="gl"></i><h3>Vožnja</h3><p>Časovi u terminima koje biraš sam.</p></div>
      <div class="card step tilt"><i class="gl"></i><h3>Ispit</h3><p>Podrška sve do polaganja.</p></div>
      <div class="card step tilt"><i class="gl"></i><h3>Dozvola 🎉</h3><p>Položen ispit i vozačka u rukama. Spreman si za samostalnu i sigurnu vožnju.</p></div>
    </div>
    <p class="ctr"><a class="more-link" href="/upis/">Detaljan vodič: dokumenti, ispiti i časovi →</a></p>
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
    <h2 class="t rvl">Instruktori <em>autoškole DrivePro</em></h2>
    <p class="sub mut rvl">Ljudi koji te uče, a ne samo ispituju.</p>
    <div class="team rvl">
      <a class="card tilt" href="/instruktori/#dalibor"><i class="gl"></i><div class="av b">DV</div><div><h3>Dalibor Vujadinović</h3><p class="mut" style="font-size:.9rem">Dipl. inž. saobraćaja. Instruktor vožnje, praktična obuka i termini časova vožnje.</p><span class="ph">Upoznaj instruktora →</span></div></a>
      <a class="card tilt" href="/instruktori/#vladana"><i class="gl"></i><div class="av y">VV</div><div><h3>Vladana Vujadinović</h3><p class="mut" style="font-size:.9rem">Dipl. inž. saobraćaja. Predavač teorijske nastave i instruktor B kategorije.</p><span class="ph">Upoznaj instruktora →</span></div></a>
    </div>
  </div>
</section>

<section class="sec">
  <div class="wrap">
    <h2 class="t rvl">Položili su! <em>Naši kandidati</em></h2>
    <p class="sub mut rvl">Vozačka u ruke, osmijeh na licu.</p>
    {gal_block()}
    {gal_more}
  </div>
</section>

<section class="sec alt">
  <div class="wrap">
    <h2 class="t rvl">Najnovije <em>objave</em></h2>
    <p class="sub mut rvl">Obavještenja o upisu, terminima i čestitke kandidatima.</p>
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
        <div class="row"><div class="ico">📍</div><div><small>Adresa</small><b>{ADR}, 76100 Brčko</b></div></div>
        <div class="row"><div class="ico">📞</div><div><small>Dalibor: upis, informacije i časovi vožnje</small><a href="tel:+38765803456"><b>065 803 456</b></a></div></div>
        <div class="row"><div class="ico">📞</div><div><small>Vladana: informacije i teorijska nastava</small><a href="tel:+38765858411"><b>065 858 411</b></a></div></div>
        <div class="row"><div class="ico">📸</div><div><small>Instagram</small><a href="{IG}" target="_blank" rel="noopener"><b>@driveproautoskola</b></a></div></div>
      </div>
      <div class="map">
        <iframe title="Mapa: Autoškola DrivePro, {ADR}, Brčko" loading="lazy" referrerpolicy="no-referrer-when-downgrade" src="{MAPS_EMBED}"></iframe>
        <a target="_blank" rel="noopener" href="{MAPS}">Otvori navigaciju →</a>
      </div>
    </div>
  </div>
</section>

<section class="rate-band" aria-label="Besplatna teorija i plaćanje na rate">
  <div class="wrap"><p><b>💳 Teorija besplatna, obuka u do 5 rata.</b> Uslove dogovaramo pri upisu.</p><a href="tel:+38765803456" class="btn btn-y">📞 065 803 456</a></div>
</section>'''
    return dict(path='/', home=True, prio='1.0', freq='weekly',
                title=HOME_TITLE,
                desc='Autoškola DrivePro u Brčkom: kategorije A, B, C1, C, CE i D, besplatna teoretska nastava, plaćanje do 5 rata i termini vožnje po izboru. Tel. 065 803 456.',
                og_title='Autoškola DrivePro Brčko, besplatna teoretska nastava',
                hero_html=hero, body=body, crumbs=[('/', 'Početna')], images=[f'/img/galerija/{f}.webp' for f, a, c in GAL],
                scripts=['/assets/postavke.js', '/podaci/objave.js', '/assets/podaci.js'])


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

MLADI = '''<h2>Prve dvije godine: pravila za <em>mlade vozače</em></h2>
<p>Prema Zakonu o osnovama bezbjednosti saobraćaja na putevima u BiH, vozač koji je dobio vozačku dozvolu za kategoriju A1, A, B ili C1 prve dvije godine od izdavanja dozvole:</p>
<ul><li>ne smije voziti brže od <strong>70 km/h</strong> na putu, <strong>90 km/h</strong> na brzom putu i <strong>120 km/h</strong> na autoputu,</li><li>ne smije tim vozilom vući priključno vozilo,</li><li>ne smije organizovano prevoziti djecu.</li></ul>
<p>Na predavanjima prolazimo i ova pravila, da od prvog dana samostalne vožnje znaš šta smiješ, a šta ne.</p>'''


def b_kat():
    prose = f'''
<h2>Vozačka dozvola B kategorije u <em>Brčkom</em></h2>
<p class="lead">B kategorija je prva vozačka dozvola za većinu kandidata i najtraženija obuka u Autoškoli DrivePro. Pripremamo te da položiš ispit, ali i da poslije ispita voziš sigurno i samouvjereno u stvarnom saobraćaju.</p>
<p>Teoretska nastava je kod nas <strong>besplatna</strong>. Predaje je <a href="/instruktori/#vladana">Vladana Vujadinović</a>, diplomirani inženjer saobraćaja, a časove vožnje vodi instruktor <a href="/instruktori/#dalibor">Dalibor Vujadinović</a>. Ostatak obuke možeš platiti odjednom ili u do 5 rata.</p>

<h2>Šta smiješ voziti sa <em>B kategorijom</em>?</h2>
<p>Vozačka dozvola B kategorije daje pravo upravljanja putničkim automobilima i drugim motornim vozilima čija najveća dozvoljena masa nije veća od 3.500 kg i koja, osim sjedišta za vozača, nemaju više od osam sjedišta. Uz takvo vozilo smiješ vući i laku prikolicu, najveće dozvoljene mase do 750 kg.</p>
<p>To znači lični automobil, kombi za porodicu ili posao i manje dostavno vozilo. Sve ono što se svakodnevno vozi po Brčkom i okolini.</p>

<h2>Uslovi za upis <em>B kategorije</em></h2>
<ul>
<li><strong>Najmanje 18 godina</strong> za vozačku dozvolu, kako propisuje {ZAKON}. U proces obuke možeš ući tri mjeseca prije 18. rođendana, a upisati se možeš i ranije.</li>
<li><strong>Važeća lična karta</strong> i prijava boravka.</li>
<li><strong>Ljekarsko uvjerenje</strong> o zdravstvenoj sposobnosti za vozača. Pribavlja se prije početka obuke i važi 12 mjeseci od dana izdavanja.</li>
</ul>
<p>Tačan spisak dokumenata potvrđujemo pri upisu. Nazovi Dalibora na {TD} i sve dogovaramo u jednom razgovoru.</p>

<h2>Kako izgleda obuka u <em>Autoškoli DrivePro</em></h2>
<ol>
<li><strong>Upis i dogovor.</strong> Dogovaramo početak, način plaćanja i termine teoretske nastave.</li>
<li><strong>Teoretska nastava.</strong> Saobraćajni propisi, znakovi i pravila. Traje sedam radnih dana i besplatna je.</li>
<li><strong>Prva pomoć.</strong> Dva dana obuke iz prve pomoći, koju prema zakonu sprovodi Crveni krst, i ispit iz prve pomoći.</li>
<li><strong>Teorijski ispit.</strong> Test iz poznavanja propisa o bezbjednosti saobraćaja.</li>
<li><strong>35 časova vožnje.</strong> Prvo osnovne radnje vozilom, zatim vožnja kroz grad, raskrsnice, kružni tokovi, parkiranje i vožnja van naselja. Termine časova biraš sam.</li>
<li><strong>Praktični ispit.</strong> Vožnja pred ispitnom komisijom koju imenuju nadležni organi Brčko distrikta.</li>
</ol>

<h2>Koliko traje obuka za <em>B kategoriju</em>?</h2>
<p>Teoretska nastava traje sedam radnih dana, a obuka iz prve pomoći dva. Praktični dio obuhvata 35 časova vožnje. Termine vožnje i ispita biraš sam, pa ukupno trajanje zavisi i od tvog rasporeda i ispitnih rokova.</p>
{NOVA_PRAVILA}

<h2>Zašto kandidati biraju <em>DrivePro</em> za B kategoriju</h2>
<ul>
<li><strong>Besplatna teoretska nastava.</strong> Plaćaš samo ostatak obuke.</li>
<li><strong>Ti biraš termine.</strong> Vožnja i ispit se uklapaju u školu ili posao.</li>
<li><strong>Vožnja bez pritiska.</strong> Instruktor mirno objašnjava svaku grešku.</li>
<li><strong>Pomoć kod straha od vožnje.</strong> Individualan pristup i radionice za prevazilaženje treme.</li>
<li><strong>Plaćanje do 5 rata.</strong> Obuka koja se uklapa u kućni budžet.</li>
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
        ('Sa koliko godina mogu upisati B kategoriju?', 'Vozačku dozvolu B kategorije možeš dobiti sa navršenih 18 godina. U proces obuke možeš ući tri mjeseca prije 18. rođendana, a upisati se možeš i ranije. Za detalje nazovi 065 803 456.'),
        ('Da li je teoretska nastava besplatna?', 'Jeste. Teoretska nastava u Autoškoli DrivePro je besplatna. Cijenu ostatka obuke i šta tačno obuhvata saznaješ pri upisu.'),
        ('Koliko časova vožnje ima obuka za B kategoriju?', 'Praktični dio obuke obuhvata 35 časova vožnje. Termine časova biraš sam.'),
        ('Mogu li platiti obuku za B kategoriju na rate?', 'Možeš. Obuku možeš platiti odjednom ili u do 5 rata, a uslove dogovaramo pri upisu.'),
        ('Koliko dugo važi ljekarsko uvjerenje?', 'Ljekarsko uvjerenje o zdravstvenoj sposobnosti za vozača važi 12 mjeseci od dana izdavanja, pa ga je najbolje uraditi neposredno prije početka obuke.'),
        ('Šta ako ne položim ispit iz prvog pokušaja?', 'Ništa strašno. Dogovaramo dodatne časove i pripremu za novi termin. Cilj nam je da položiš i da voziš sigurno, a ne da žurimo.'),
    ]
    return kat_page('/b-kategorija/', 'B', 'Vozačka dozvola B kategorije u Brčkom | Autoškola DrivePro',
                    'Obuka za B kategoriju u Brčkom: besplatna teoretska nastava, 35 časova vožnje u terminima po tvom izboru i plaćanje do 5 rata. DrivePro, 065 803 456.',
                    'B kategorija <span>u Brčkom</span>', 'Vozačka dozvola za automobil, od upisa do položenog ispita. Besplatna teoretska nastava, 35 časova vožnje i plaćanje u do 5 rata.',
                    '🚗 Najtraženija kategorija',
                    [('18', 'godina, minimalna starost'), ('35', 'časova vožnje'), ('0 KM', 'teoretska nastava'), ('do 5', 'rata za plaćanje')],
                    prose, faq, 'Obuka za B kategoriju u Brčkom', 'Besplatna teoretska nastava, prva pomoć, 35 časova vožnje i priprema za vozački ispit B kategorije u Autoškoli DrivePro, Brčko.')


def a_kat():
    prose = f'''
<h2>Vozačka dozvola za <em>motocikl</em> u Brčkom</h2>
<p class="lead">A kategorija je za one kojima je motocikl način života ili najpraktičniji način da stignu na posao. U Autoškoli DrivePro obuka za motocikl kombinuje teoriju, vježbe na poligonu i vožnju u saobraćaju, sa naglaskom na ono što motoristu najviše čuva: predviđanje opasnosti.</p>

<h2>Uslovi za <em>A kategoriju</em></h2>
<ul>
<li><strong>Najmanje 18 godina</strong> za kategoriju A, prema {ZAKON}.</li>
<li>Za potkategoriju <strong>A1</strong>, odnosno lake motocikle, zakon propisuje najmanje 16 godina. Ako te zanima A1, pitaj nas pri upisu.</li>
<li>Važeća lična karta, prijava boravka i ljekarsko uvjerenje, koje važi 12 mjeseci.</li>
</ul>

<h2>Šta učiš na obuci za <em>motocikl</em></h2>
<ol>
<li><strong>Teorija i prva pomoć.</strong> Isti propisi kao za ostale kategorije, uz posebna pravila za vozače motocikla. Teoretska nastava je besplatna. <a href="/teorijska-nastava/">Više o teoretskoj nastavi</a>.</li>
<li><strong>Poligon.</strong> Balans, polazak i zaustavljanje, vožnja u sporom hodu, slalom, kočenje i izbjegavanje prepreke.</li>
<li><strong>Vožnja u saobraćaju.</strong> Položaj u traci, vidljivost, raskrsnice, preticanje i vožnja kroz krivine.</li>
<li><strong>Ispit.</strong> Teorijski test, zatim praktični ispit pred komisijom.</li>
</ol>

<h2>Zaštitna oprema</h2>
<p>Za vožnju motocikla obavezna je zaštitna kaciga. Na obuku dođi u čvrstoj obući koja štiti zglob, dugim pantalonama i jakni, a preporučujemo i rukavice. Na prvom času ti pokažemo šta je od opreme važno i kako se pravilno podešava.</p>

<h2>Zašto <em>Autoškola DrivePro</em> za A kategoriju</h2>
<ul>
<li>Strpljiv pristup, jer se na motociklu samopouzdanje gradi korak po korak.</li>
<li>Besplatna teoretska nastava kod diplomiranog inženjera saobraćaja.</li>
<li>Termine vožnje biraš sam.</li>
<li>Plaćanje u do 5 rata.</li>
<li>Već imaš B kategoriju? Pitaj nas šta te tačno čeka.</li>
</ul>
{MLADI}
<p><a class="btn btn-y" href="/kontakt/">Upiši A kategoriju →</a></p>'''
    faq = [
        ('Sa koliko godina mogu upisati obuku za motocikl?', 'Za kategoriju A zakon u BiH propisuje najmanje 18 godina, a za potkategoriju A1, lake motocikle, najmanje 16 godina.'),
        ('Moram li imati svoju opremu?', 'Kaciga je obavezna, a preporučujemo i rukavice, jaknu, duge pantalone i obuću koja štiti zglob. Detalje dogovaramo pri upisu.'),
        ('Imam B kategoriju. Moram li ponovo slušati cijelu teoriju?', 'Obim teorije zavisi od toga koje kategorije već imaš. Nazovi 065 803 456 i reći ćemo ti tačno šta te čeka.'),
    ]
    return kat_page('/a-kategorija/', 'A', 'A kategorija Brčko, obuka za motocikl | Autoškola DrivePro',
                    'Vozačka dozvola za motocikl (A kategorija) u Brčkom: uslovi od 18 godina, poligon, vožnja u saobraćaju, besplatna teorija i plaćanje do 5 rata. DrivePro.',
                    'A kategorija, <span>motocikli</span>', 'Obuka za motocikl u Brčkom: poligon, vožnja u saobraćaju i besplatna teoretska nastava. Sigurno, strpljivo i bez pritiska.',
                    '🏍️ Motocikli',
                    [('18', 'godina za kategoriju A'), ('16', 'godina za potkategoriju A1'), ('0 KM', 'teoretska nastava'), ('do 5', 'rata za plaćanje')],
                    prose, faq, 'Obuka za A kategoriju (motocikl) u Brčkom', 'Teorija, poligon i vožnja u saobraćaju za vozačku dozvolu A kategorije u Autoškoli DrivePro, Brčko.')


def c_kat():
    prose = f'''
<h2>Vozačka dozvola za <em>kamion</em> u Brčkom</h2>
<p class="lead">C1 i C kategorija otvaraju vrata poslu u transportu, građevini, dostavi i logistici. U Autoškoli DrivePro kandidate za teretna vozila pripremamo za ispit, ali i za realne situacije: manevrisanje velikim vozilom, mrtve uglove, opterećenje i vožnju u gradu.</p>

<h2>Razlika između <em>C1 i C</em></h2>
<div class="tw"><table class="tbl">
<thead><tr><th>Kategorija</th><th>Vozila</th><th>Minimalna starost</th></tr></thead>
<tbody>
<tr><td>C1</td><td>Teretna vozila srednje mase, iznad 3.500 kg, a najviše do 7.500 kg</td><td>18 godina</td></tr>
<tr><td>C</td><td>Teretna vozila čija najveća dozvoljena masa prelazi 3.500 kg</td><td>21 godina</td></tr>
</tbody></table></div>
<p>Starosne granice za C1 (18 godina) i C (21 godina) propisuje {ZAKON}. Ako želiš voziti kamion s prikolicom, nakon C kategorije slijedi <a href="/ce-kategorija/">CE kategorija</a>.</p>

<h2>Uslovi za upis <em>C kategorije</em></h2>
<ul>
<li><strong>Najmanje 21 godina</strong> za C, odnosno 18 za C1.</li>
<li><strong>Prethodno položena B ili C1 kategorija.</strong></li>
<li>Važeća lična karta, prijava boravka i ljekarsko uvjerenje o zdravstvenoj sposobnosti za vozača odgovarajuće kategorije, koje važi 12 mjeseci.</li>
</ul>

<h2>Koliko obuke te čeka ako već <em>imaš B ili C1</em></h2>
<div class="tw"><table class="tbl">
<thead><tr><th>Već imaš</th><th>Polažeš</th><th>Časova vožnje</th></tr></thead>
<tbody>
<tr><td>B kategoriju</td><td>Ispit iz poznavanja propisa i praktični dio</td><td>20</td></tr>
<tr><td>C1 kategoriju</td><td>Samo praktični dio</td><td>8</td></tr>
</tbody></table></div>

<h2>Šta obuhvata obuka</h2>
<ol>
<li><strong>Teorija.</strong> Propisi s naglaskom na teretna vozila: dimenzije, mase i osovinsko opterećenje, osiguranje tereta i pravila za teška vozila.</li>
<li><strong>Upoznavanje vozila.</strong> Kontrolni pregled prije vožnje, ogledala, mrtvi uglovi i dimenzije vozila.</li>
<li><strong>Vožnja na poligonu.</strong> Manevrisanje, vožnja unazad i parkiranje velikog vozila.</li>
<li><strong>Vožnja u saobraćaju.</strong> Raskrsnice, skretanje velikim vozilom, vožnja kroz grad i van naselja.</li>
<li><strong>Ispit.</strong> Praktični dio, a ako imaš samo B kategoriju i ispit iz propisa, pred ispitnom komisijom.</li>
</ol>

<div class="note"><b>Za profesionalne vozače</b>Za rad u prevozu robe, posebno u međunarodnom prevozu, pored vozačke dozvole traže se i dodatno stručno osposobljavanje i kvalifikacijska kartica vozača. To se organizuje odvojeno od autoškole, a rado ćemo te uputiti šta je sljedeći korak.</div>

<h2>Zašto <em>DrivePro</em> za kamion</h2>
<ul>
<li>Obuku vode diplomirani inženjeri saobraćaja.</li>
<li>Termine vožnje i ispita biraš sam, pa obuku lakše uklopiš uz posao.</li>
<li>Plaćanje u do 5 rata, što je posebno važno kod obimnije obuke.</li>
</ul>
<p><a class="btn btn-y" href="/kontakt/">Upiši C1 ili C kategoriju →</a></p>'''
    faq = [
        ('Sa koliko godina mogu voziti kamion?', 'Prema zakonu u BiH, potkategoriju C1 možeš dobiti sa 18, a kategoriju C sa 21 godinom.'),
        ('Treba li mi B kategorija prije C?', 'Za C kategoriju potrebna je prethodno položena B ili C1 kategorija. Sa B kategorijom polažeš ispit iz propisa i praktični dio, uz 20 časova vožnje. Sa C1 polažeš samo praktični dio, uz 8 časova vožnje.'),
        ('Mogu li obuku za kamion platiti na rate?', 'Možeš. Obuku možeš platiti u do 5 rata, a uslove dogovaramo pri upisu.'),
    ]
    return kat_page('/c-kategorija/', 'C', 'C1 i C kategorija Brčko, vozačka za kamion | Autoškola DrivePro',
                    'Obuka za C1 i C kategoriju (kamion) u Brčkom: C od 21 godine, uz B ili C1. Sa B kategorijom 20 časova vožnje, sa C1 samo 8. Plaćanje do 5 rata.',
                    'C1 i C kategorija, <span>teretna vozila</span>', 'Vozačka dozvola za kamion u Brčkom. Ako već imaš B kategoriju, čeka te 20 časova vožnje, a ako imaš C1, samo 8.',
                    '🚚 Teretna vozila',
                    [('21', 'godina za C'), ('B ili C1', 'potrebna prethodno'), ('20', 'časova vožnje uz B'), ('do 5', 'rata za plaćanje')],
                    prose, faq, 'Obuka za C1 i C kategoriju (kamion) u Brčkom', 'Teorija, poligon i vožnja za vozačku dozvolu C1 i C kategorije u Autoškoli DrivePro, Brčko.')


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

<h2>Zašto <em>Autoškola DrivePro</em></h2>
<ul>
<li>Obuka prilagođena vozačima koji već rade. Termine vožnje biraš sam i dogovaraš ih s instruktorom Daliborom na {TD}.</li>
<li>Obuku vode diplomirani inženjeri saobraćaja.</li>
<li>Plaćanje u do 5 rata.</li>
</ul>
<p><a class="btn btn-y" href="/kontakt/">Upiši CE kategoriju →</a></p>'''
    faq = [
        ('Mogu li upisati CE ako još nemam C kategoriju?', 'Ne možeš. Prema zakonu u BiH, vozačku dozvolu za CE kategoriju mogu dobiti samo vozači koji već imaju C kategoriju. Možemo te voditi kroz C, pa onda CE.'),
        ('Koliko godina moram imati za CE?', 'Zakon propisuje najmanje 21 godinu za kategorije C i CE.'),
        ('Mogu li vožnju uklopiti uz posao?', 'Možeš. Termine časova vožnje biraš sam i dogovaraš ih direktno s instruktorom Daliborom na 065 803 456.'),
    ]
    return kat_page('/ce-kategorija/', 'CE', 'CE kategorija Brčko, kamion s prikolicom | Autoškola DrivePro',
                    'Obuka za CE kategoriju u Brčkom: uslov je C kategorija i 21 godina. Spajanje prikolice, manevrisanje, ispit i plaćanje do 5 rata. Autoškola DrivePro.',
                    'CE kategorija, <span>kamion s prikolicom</span>', 'Za vozače koji već imaju C kategoriju: obuka za skup vozila u Brčkom, od spajanja prikolice do položenog ispita.',
                    '🚛 Skup vozila',
                    [('C', 'kategorija je preduslov'), ('21', 'godina minimalno'), ('do 5', 'rata za plaćanje'), ('Uz posao', 'termine biraš sam')],
                    prose, faq, 'Obuka za CE kategoriju (kamion s prikolicom) u Brčkom', 'Obuka za vozačku dozvolu CE kategorije, skup vozila, u Autoškoli DrivePro, Brčko.')


def d_kat():
    prose = f'''
<h2>Vozačka dozvola za <em>autobus</em> u Brčkom</h2>
<p class="lead">D kategorija je za vozače autobusa: gradskog, međugradskog, školskog ili turističkog. To je kategorija s najvećom odgovornošću, jer vozač prevozi putnike, pa obuka u Autoškoli DrivePro stavlja poseban naglasak na sigurnost, predviđanje i miran stil vožnje.</p>

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

<h2>Zašto <em>DrivePro</em> za D kategoriju</h2>
<ul>
<li>Obuku vode diplomirani inženjeri saobraćaja.</li>
<li>Termine vožnje i ispita biraš sam, pa obuku lakše uklopiš uz posao.</li>
<li>Plaćanje u do 5 rata.</li>
</ul>
<p><a class="btn btn-y" href="/kontakt/">Upiši D kategoriju →</a></p>'''
    faq = [
        ('Sa koliko godina mogu voziti autobus?', 'Prema zakonu u BiH, kategoriju D možeš dobiti sa najmanje 24 godine, a potkategoriju D1 sa 21 godinom.'),
        ('Koju dozvolu moram imati prije D kategorije?', 'D kategoriju mogu dobiti vozači koji najmanje dvije godine imaju vozačku dozvolu kategorije B, C ili potkategorije D1.'),
        ('Treba li vozačima autobusa češći ljekarski pregled?', 'Treba. Vozači kategorija D, DE, D1 i D1E prema zakonu obavljaju zdravstveni pregled prilikom svakog produženja vozačke dozvole.'),
    ]
    return kat_page('/d-kategorija/', 'D', 'D kategorija Brčko, vozačka za autobus | Autoškola DrivePro',
                    'Obuka za D kategoriju (autobus) u Brčkom: uslovi su 24 godine i dvije godine B, C ili D1. Teorija, vožnja, ispit i plaćanje do 5 rata. Autoškola DrivePro.',
                    'D kategorija, <span>autobusi</span>', 'Vozačka dozvola za autobus u Brčkom: obuka sa naglaskom na sigurnost putnika, od teorije do ispita, uz plaćanje u do 5 rata.',
                    '🚌 Prevoz putnika',
                    [('24', 'godine za kategoriju D'), ('2 god.', 'prethodno B, C ili D1'), ('21', 'godina za D1'), ('do 5', 'rata za plaćanje')],
                    prose, faq, 'Obuka za D kategoriju (autobus) u Brčkom', 'Obuka za vozačku dozvolu D kategorije u Autoškoli DrivePro, Brčko.')


def kategorije():
    body = '''<section class="sec"><div class="wrap">
<h2 class="t rvl">Odaberi <em>kategoriju</em></h2>
<p class="sub mut rvl">Za svaku kategoriju imaš posebnu stranicu sa uslovima, tokom obuke i odgovorima na česta pitanja.</p>
<div class="hub rvl">''' + ''.join(f'<a class="card tilt" href="{p}"><i class="gl"></i><span class="lt2">{b}</span><h3>{n}</h3><p>{t}</p><span class="more">Saznaj više →</span></a>' for p, b, n, t in ALL_KAT) + '''
<a class="card tilt" href="/teorijska-nastava/"><i class="gl"></i><span class="lt2">0 KM</span><h3>Teoretska nastava</h3><p>Zajednička za sve kategorije i besplatna, kod diplomiranog inženjera saobraćaja.</p><span class="more">Saznaj više →</span></a>
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
<tr><td>C</td><td>Teretna vozila preko 3.500 kg</td><td>21</td><td>Potrebna B ili C1</td></tr>
<tr><td>CE</td><td>Kamion s prikolicom</td><td>21</td><td>Potrebna C kategorija</td></tr>
<tr><td>D1</td><td>Manji autobusi</td><td>21</td><td>Potkategorija</td></tr>
<tr><td>D</td><td>Autobusi</td><td>24</td><td>Najmanje 2 godine B, C ili D1</td></tr>
</tbody></table></div>
<p>U Autoškoli DrivePro obučavamo kandidate za kategorije <strong>A, B, C1, C, CE i D</strong>. Za potkategorije i posebne slučajeve, na primjer ako već imaš neku kategoriju, nazovi nas na ''' + TD + '''. Reći ćemo ti tačno koji je tvoj sljedeći korak.</p>
<h2>Šta je zajedničko za <em>sve kategorije</em></h2>
<ul>
<li><strong>Ljekarsko uvjerenje</strong> prije početka obuke, koje važi 12 mjeseci.</li>
<li><strong>Obuka iz prve pomoći</strong> i ispit, za kandidate koji ga još nisu položili.</li>
<li><strong>Teoretska nastava</strong>, kod nas besplatna, i teorijski ispit iz poznavanja propisa.</li>
<li><strong>Časovi vožnje</strong> sa instruktorom, u terminima koje biraš sam, i praktični ispit pred komisijom.</li>
<li><strong>Plaćanje</strong> odjednom ili u do 5 rata.</li>
</ul>
<p>Detaljan redoslijed koraka pročitaj u vodiču <a href="/upis/">Kako do vozačke dozvole u Brčkom</a>.</p>''', side('/kategorije/'), alt=True)
    return dict(path='/kategorije/', title='Kategorije A, B, C1, C, CE i D u Brčkom | Autoškola DrivePro',
                desc='Sve kategorije vozačke dozvole u Autoškoli DrivePro Brčko: A, B, C1, C, CE i D. Minimalna starost, uslovi i obuka za svaku kategoriju na jednom mjestu.',
                crumbs=[('/', 'Početna'), ('/kategorije/', 'Kategorije')], prio='0.9', page_type='CollectionPage',
                hero=dict(chip='🚦 A · B · C1 · C · CE · D', h1='Kategorije vozačke dozvole <span>u Brčkom</span>',
                          lead='Od motocikla do autobusa. U Autoškoli DrivePro obučavamo kandidate za šest kategorija. Pogledaj uslove i odaberi svoju.', big='ABC'),
                body=body)


# ---------------------------------------------------------------- O NAMA
def o_nama():
    prose = f'''
<h2>Autoškola DrivePro, <em>prva stanica</em> do vozačke</h2>
<p class="lead">Autoškola DrivePro je autoškola u Brčkom, u ulici {ADR}. Vode je diplomirani inženjeri saobraćaja Vladana i Dalibor Vujadinović, a moto nam je jednostavan: biti tvoja prva stanica na putu ka sigurnoj vožnji.</p>
<p>Obučavamo kandidate za kategorije A, B, C1, C, CE i D. Teoretska nastava je besplatna, obuka se može platiti u do 5 rata, a termine vožnje i ispita biraš sam.</p>

<h2>Naš pristup: <em>individualno i bez pritiska</em></h2>
<p>Mnogi kandidati dolaze s tremom. Neki nikad nisu sjeli za volan, a neki su loše iskustvo ponijeli iz druge autoškole. Zato kod nas svaki kandidat ima individualan pristup, a svaka greška dobije objašnjenje, a ne ukor.</p>
<ul>
<li><strong>Stručni instruktori.</strong> Obuku vode diplomirani inženjeri saobraćaja.</li>
<li><strong>Priprema za teorijski ispit.</strong> Besplatna teoretska nastava i probni testovi.</li>
<li><strong>Radionice za prevazilaženje straha od vožnje.</strong> Trema se može savladati, uz vođenje i vježbu.</li>
<li><strong>Fleksibilni termini.</strong> Termine vožnje i ispita biraš sam.</li>
<li><strong>Plaćanje na rate.</strong> Obuku možeš platiti u do 5 rata.</li>
</ul>

<h2>Ko vodi <em>obuku</em></h2>
<p><a href="/instruktori/#vladana">Vladana Vujadinović</a>, diplomirani inženjer saobraćaja, vlasnica je autoškole, predavač teorijske nastave i instruktor B kategorije.</p>
<p><a href="/instruktori/#dalibor">Dalibor Vujadinović</a>, diplomirani inženjer saobraćaja, instruktor je vožnje. Vodi praktičnu obuku i dogovara termine časova vožnje tako da se uklope u školu ili posao.</p>

<h2>Šta nudimo</h2>
<ul>
<li>Obuku za kategorije <a href="/a-kategorija/">A</a>, <a href="/b-kategorija/">B</a>, <a href="/c-kategorija/">C1 i C</a>, <a href="/ce-kategorija/">CE</a> i <a href="/d-kategorija/">D</a>.</li>
<li><a href="/teorijska-nastava/">Besplatnu teoretsku nastavu</a> i pripremu za teorijski ispit.</li>
<li>Časove vožnje i pripremu za praktični ispit.</li>
<li>Prijavu i polaganje ispita.</li>
</ul>

<h2>Gdje smo</h2>
<p>Nalazimo se u ulici <strong>{ADR}, 76100 Brčko</strong>. Za upis, informacije i časove vožnje zovi Dalibora na {TD}, a Vladanu na {TV}. Sve kontakt informacije i mapa su na stranici <a href="/kontakt/">Kontakt</a>.</p>
<p><a class="btn btn-y" href="/kontakt/">Dogovori upis →</a></p>'''
    return dict(path='/o-nama/', title='O nama | Autoškola DrivePro Brčko, Hasana Bećirevića 3',
                desc='Autoškola DrivePro u Brčkom: diplomirani inženjeri saobraćaja, besplatna teoretska nastava, plaćanje do 5 rata i kategorije A, B, C1, C, CE i D.',
                crumbs=[('/', 'Početna'), ('/o-nama/', 'O nama')], page_type='AboutPage',
                hero=dict(chip='🚗 Prva stanica do vozačke', h1='O Autoškoli DrivePro: <span>prva stanica do vozačke</span>',
                          lead='Diplomirani inženjeri saobraćaja, besplatna teoretska nastava i termini vožnje po tvom izboru. Upoznaj Autoškolu DrivePro iz Brčkog.', big='DP'),
                body=art(prose, side('/o-nama/', 'Autoškola', [('/o-nama/', 'O nama'), ('/instruktori/', 'Instruktori'), ('/teorijska-nastava/', 'Teorijska nastava'), ('/galerija/', 'Galerija'), ('/novosti/', 'Novosti')])))


# ---------------------------------------------------------------- INSTRUKTORI
def instruktori():
    body = '''<section class="sec"><div class="wrap">
<div class="team rvl" style="margin-top:0">
<div class="card tilt" id="dalibor"><i class="gl"></i><div class="av b">DV</div><div><h2 style="font-weight:800;font-size:1.15rem">Dalibor Vujadinović</h2><p class="mut" style="font-size:.9rem">Dipl. inž. saobraćaja · instruktor vožnje · upis i informacije</p><a class="ph" href="tel:+38765803456">📞 065 803 456</a></div></div>
<div class="card tilt" id="vladana"><i class="gl"></i><div class="av y">VV</div><div><h2 style="font-weight:800;font-size:1.15rem">Vladana Vujadinović</h2><p class="mut" style="font-size:.9rem">Dipl. inž. saobraćaja · predavač teorijske nastave i instruktor B kategorije</p><a class="ph" href="tel:+38765858411">📞 065 858 411</a></div></div>
</div></div></section>''' + art(f'''
<h2>Dalibor <em>Vujadinović</em></h2>
<p class="lead">Diplomirani inženjer saobraćaja i instruktor vožnje u Autoškoli DrivePro. Vodi praktičnu obuku i termine časova vožnje. Njegov broj je glavni broj autoškole za upis i informacije.</p>
<p>Kod Dalibora počinje dio obuke koji kandidati najviše iščekuju, vožnja. Prvi časovi su posvećeni osnovama: podešavanju sjedišta i ogledala, polasku, mijenjanju brzina i kočenju. Zatim slijedi vožnja kroz grad, raskrsnice, kružni tokovi, parkiranje i vožnja van naselja, sve dok kandidat ne bude spreman za ispit i, još važnije, za samostalnu vožnju.</p>
<ul>
<li><strong>Strpljivo i bez pritiska.</strong> Greške se objašnjavaju, ne kažnjavaju.</li>
<li><strong>Ti biraš termine.</strong> Časove vožnje dogovaraš direktno s Daliborom.</li>
<li><strong>Vožnja kao u stvarnom životu.</strong> Priprema za stvarni saobraćaj, a ne samo za ispit.</li>
</ul>
<p>Za upis i termine časova vožnje zovi Dalibora: {TD}.</p>

<h2>Vladana <em>Vujadinović</em></h2>
<p class="lead">Vlasnica Autoškole DrivePro. Diplomirani inženjer saobraćaja, predavač teorijske nastave i instruktor B kategorije.</p>
<p>Kod Vladane prolaziš teoretsku nastavu, koja je u DrivePro besplatna. Na predavanjima se uče saobraćajni propisi, znakovi i raskrsnice, uz probne testove kakvi te čekaju na teorijskom ispitu. Kao instruktor B kategorije vodi i časove vožnje.</p>
<ul>
<li><strong>Diplomirani inženjer saobraćaja.</strong> Stručno znanje pretočeno u jasna predavanja.</li>
<li><strong>Teorija i vožnja.</strong> Predaje teorijsku nastavu i vodi obuku za B kategoriju.</li>
</ul>
<p>Kontakt: {TV}.</p>
<p><a class="btn btn-y" href="/kontakt/">Upiši se kod nas →</a></p>''', side('/instruktori/', 'Autoškola', [('/o-nama/', 'O nama'), ('/instruktori/', 'Instruktori'), ('/teorijska-nastava/', 'Teorijska nastava')]), alt=True)
    ld = [{"@type": "Person", "@id": DOMAIN + "/instruktori/#dalibor", "name": "Dalibor Vujadinović", "jobTitle": "Instruktor vožnje, dipl. inž. saobraćaja", "telephone": "+387 65 803 456", "worksFor": ORG, "url": DOMAIN + "/instruktori/#dalibor"},
          {"@type": "Person", "@id": DOMAIN + "/instruktori/#vladana", "name": "Vladana Vujadinović", "jobTitle": "Predavač teorijske nastave i instruktor B kategorije, dipl. inž. saobraćaja", "telephone": "+387 65 858 411", "worksFor": ORG, "knowsAbout": ["Bezbjednost saobraćaja", "Saobraćajni propisi", "Obuka vozača"], "url": DOMAIN + "/instruktori/#vladana"}]
    return dict(path='/instruktori/', title='Instruktori Autoškole DrivePro Brčko | Dalibor i Vladana Vujadinović',
                desc='Upoznaj instruktore Autoškole DrivePro u Brčkom: Dalibor i Vladana Vujadinović, diplomirani inženjeri saobraćaja. Vožnja, besplatna teorija i upis.',
                crumbs=[('/', 'Početna'), ('/instruktori/', 'Instruktori')], ld=ld,
                hero=dict(chip='🎓 Ljudi koji te uče', h1='Instruktori <span>Autoškole DrivePro</span>',
                          lead='Diplomirani inženjeri saobraćaja koji te uče, a ne samo ispituju. Strpljivo, individualno i bez pritiska.', big='DV',
                          cta='<a href="tel:+38765803456" class="btn btn-y">📞 Dalibor 065 803 456</a><a href="tel:+38765858411" class="btn btn-g">📞 Vladana 065 858 411</a>'),
                body=body)


# ---------------------------------------------------------------- TEORIJA
def teorija():
    prose = '''
<h2>Besplatna teorija koja se <em>razumije</em></h2>
<p class="lead">Teoretska nastava je temelj svake vozačke dozvole, a u Autoškoli DrivePro je besplatna. Predavanja drži Vladana Vujadinović, diplomirani inženjer saobraćaja, pa ne učiš samo šta piše u testu, nego i zašto pravilo postoji.</p>

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

<h2>Kako izgleda <em>teoretska nastava</em></h2>
<ol>
<li><strong>Početak nakon upisa.</strong> Termine i mjesto predavanja dobijaš prilikom upisa.</li>
<li><strong>Sedam radnih dana.</strong> Toliko traje teoretska nastava iz propisa za B kategoriju.</li>
<li><strong>Primjeri iz stvarnog saobraćaja.</strong> Raskrsnice i situacije koje svaki vozač u Brčkom poznaje.</li>
<li><strong>Probni testovi.</strong> Vježbaš pitanja kakva te čekaju na teorijskom ispitu.</li>
<li><strong>Teorijski ispit.</strong> Kada si spreman, prijavljujemo te na ispit.</li>
</ol>

<h2>Prva pomoć</h2>
<p>Svaki kandidat za vozača prolazi i obuku iz prve pomoći te polaže ispit iz prve pomoći. Obuka traje dva dana. Prema Zakonu o osnovama bezbjednosti saobraćaja na putevima u BiH, osposobljavanje kandidata iz prve pomoći obavlja Crveni krst. Pomoći ćemo ti da je uklopiš u raspored.</p>

<h2>Bez straha od testa i <em>od vožnje</em></h2>
<p>Ako imaš tremu od ispita ili od vožnje, nisi jedini. U Autoškoli DrivePro gradivo se dijeli na male cjeline i ponavlja kroz pitanja, a organizujemo i radionice za prevazilaženje straha od vožnje. Na njima se uči kako da usmjeriš pažnju, smiriš tremu i nastaviš sigurno i poslije greške.</p>'''
    return dict(path='/teorijska-nastava/', title='Besplatna teorijska nastava za vozački ispit u Brčkom | DrivePro',
                desc='Besplatna teoretska nastava za vozački ispit u Brčkom: propisi i znakovi kod diplomiranog inženjera saobraćaja, probni testovi i prva pomoć. Autoškola DrivePro.',
                crumbs=[('/', 'Početna'), ('/teorijska-nastava/', 'Teorijska nastava')],
                hero=dict(chip='🎓 Teoretska nastava besplatna', h1='Teorijska nastava <span>u Brčkom</span>',
                          lead='Saobraćajni propisi kod diplomiranog inženjera saobraćaja, bez naplate. Gradivo učiš s razumijevanjem, ne napamet.', big='0 KM',
                          cta='<a href="/upis/" class="btn btn-y">Kako se upisati →</a><a href="tel:+38765803456" class="btn btn-g">📞 065 803 456</a>'),
                body=art(prose, side('/teorijska-nastava/')),
                ld=[svc('Besplatna teorijska nastava za kandidate za vozače u Brčkom', '/teorijska-nastava/', 'Besplatna predavanja iz poznavanja propisa o bezbjednosti saobraćaja u Autoškoli DrivePro, Brčko.')])


# ---------------------------------------------------------------- UPIS
def upis():
    prose = f'''
<h2>Kako do vozačke dozvole u <em>Brčkom</em>, korak po korak</h2>
<p class="lead">Kratak i jasan vodič za kandidate koji žele upisati autoškolu u Brčkom i položiti vozački ispit iz prvog pokušaja. Ako ti bilo šta nije jasno, nazovi Dalibora na {TD} i sve objašnjavamo u jednom razgovoru.</p>

<h2>1. Šta je potrebno <em>za upis</em></h2>
<ul>
<li><strong>Važeća lična karta.</strong></li>
<li><strong>Prijava boravka.</strong></li>
<li><strong>Ljekarsko uvjerenje</strong> o zdravstvenoj sposobnosti za vozača. Prema zakonu se pribavlja prije početka obuke i važi 12 mjeseci od dana izdavanja.</li>
<li><strong>Odgovarajuće godine</strong> za kategoriju, na primjer 18 za B kategoriju. U proces obuke za B možeš ući tri mjeseca prije 18. rođendana. Pogledaj tabelu na stranici <a href="/kategorije/">Kategorije</a>.</li>
</ul>
<p>Tačan spisak dokumenata potvrdi pozivom prije upisa.</p>

<h2>2. Upis i <em>dogovor o plaćanju</em></h2>
<p>Dođi u ulicu {ADR} ili nas nazovi. Dogovaramo kategoriju, način plaćanja, odjednom ili u do 5 rata, i početak teoretske nastave.</p>

<h2>3. Teoretska nastava</h2>
<p>Saobraćajni propisi kod <a href="/teorijska-nastava/">diplomiranog inženjera saobraćaja</a>. Za B kategoriju nastava traje sedam radnih dana i besplatna je.</p>

<h2>4. Prva pomoć</h2>
<p>Dva dana obuke i ispit iz prve pomoći. Obuku iz prve pomoći, prema zakonu, sprovodi Crveni krst, a mi ti pomažemo da je uklopiš u raspored.</p>

<h2>5. Teorijski ispit</h2>
<p>Provjera znanja iz propisa i znakova. Kada položiš teoriju, prelaziš na vožnju.</p>

<h2>6. Časovi vožnje</h2>
<p>Za B kategoriju 35 časova vožnje sa strpljivim instruktorom, od osnovnih radnji vozilom do samostalne vožnje kroz grad i van naselja. Termine biraš sam i dogovaraš ih s instruktorom Daliborom na {TD}.</p>

<h2>7. Praktični ispit i <em>vozačka u rukama</em> 🏁</h2>
<p>Vožnja pred ispitnom komisijom koju imenuju nadležni organi Brčko distrikta. Komisija procjenjuje da li si osposobljen za sigurno upravljanje vozilom. Nakon položenog ispita podnosiš zahtjev za izdavanje vozačke dozvole nadležnom organu.</p>

<div class="note"><b>Teorija besplatna, obuka na rate</b>Teoretska nastava u Autoškoli DrivePro je besplatna, a ostatak obuke možeš platiti u do 5 rata. Pozovi za uslove i termin upisa u Brčkom.</div>

<h2>Nakon ispita: <em>prve dvije godine</em></h2>
<p>Vozači koji su dobili dozvolu za A1, A, B ili C1 kategoriju prve dvije godine ne smiju voziti brže od 70 km/h na putu, 90 km/h na brzom putu i 120 km/h na autoputu, ne smiju vući priključno vozilo i ne smiju organizovano prevoziti djecu. Tako propisuje {ZAKON}.</p>
{NOVA_PRAVILA}
<p><a class="btn btn-y" href="/kontakt/">Dogovori upis →</a></p>'''
    howto = {"@type": "HowTo", "name": "Kako do vozačke dozvole u Brčkom", "inLanguage": "bs",
             "step": [{"@type": "HowToStep", "position": i + 1, "name": n, "text": t} for i, (n, t) in enumerate([
                 ('Pripremi dokumente', 'Važeća lična karta, prijava boravka i ljekarsko uvjerenje o zdravstvenoj sposobnosti za vozača.'),
                 ('Upis u autoškolu', 'Dogovor o kategoriji, načinu plaćanja (odjednom ili u do 5 rata) i početku teoretske nastave.'),
                 ('Teoretska nastava', 'Besplatna predavanja iz saobraćajnih propisa, za B kategoriju sedam radnih dana.'),
                 ('Prva pomoć', 'Dva dana obuke i ispit iz prve pomoći.'),
                 ('Teorijski ispit', 'Provjera znanja iz propisa i znakova.'),
                 ('Časovi vožnje', 'Za B kategoriju 35 časova vožnje sa instruktorom, u terminima po izboru kandidata.'),
                 ('Praktični ispit', 'Vožnja pred ispitnom komisijom i izdavanje vozačke dozvole.')])]}
    return dict(path='/upis/', title='Kako do vozačke dozvole u Brčkom: upis i dokumenti | DrivePro',
                desc='Vodič za upis u autoškolu u Brčkom: dokumenti, ljekarsko uvjerenje, besplatna teorija, prva pomoć, 35 časova vožnje, ispiti i plaćanje do 5 rata. DrivePro.',
                crumbs=[('/', 'Početna'), ('/upis/', 'Upis')], ld=[howto],
                hero=dict(chip='📋 Vodič za kandidate', h1='Kako do vozačke dozvole <span>u Brčkom</span>',
                          lead='Dokumenti, redoslijed ispita i savjeti. Sve što trebaš znati prije upisa, na jednom mjestu.', big='1·7'),
                body=art(prose, side('/upis/')))


# ---------------------------------------------------------------- GALERIJA
def galerija():
    if GAL:
        body = f'''<section class="sec"><div class="wrap">
<p class="sub mut rvl" style="margin-top:0">Svaka fotografija je jedna položena vozačka. Hvala svim kandidatima koji su nam ukazali povjerenje! Klikni na fotografiju za uvećan prikaz.</p>
{gal_block()}
<p class="ctr" style="margin-top:36px">Više fotografija i čestitki objavljujemo na Instagramu <a class="more-link" style="margin-top:0" href="{IG}" target="_blank" rel="noopener">@driveproautoskola</a></p>
</div></section>'''
    else:
        body = f'''<section class="sec"><div class="wrap">
<p class="sub mut rvl" style="margin-top:0">Svaka fotografija je jedna položena vozačka. Hvala svim kandidatima koji su nam ukazali povjerenje!</p>
{gal_block()}
</div></section>'''
    ld = [{"@type": "ImageGallery", "name": "Galerija Autoškole DrivePro Brčko", "image": [
        {"@type": "ImageObject", "contentUrl": DOMAIN + f"/img/galerija/{f}.webp", "caption": a, "width": 560, "height": 700} for f, a, c in GAL]}] if GAL else []
    extra = {} if GAL else dict(robots='noindex,follow', sitemap=False)
    return dict(path='/galerija/', title='Galerija: položili su! Kandidati Autoškole DrivePro Brčko',
                desc='Fotografije kandidata Autoškole DrivePro iz Brčkog nakon položenog vozačkog ispita. Vozačka u ruke, osmijeh na licu.',
                crumbs=[('/', 'Početna'), ('/galerija/', 'Galerija')], ld=ld, prio='0.6', images=[f'/img/galerija/{f}.webp' for f, a, c in GAL],
                hero=dict(chip='📸 Naši kandidati', h1='Položili su! <span>Naši kandidati</span>',
                          lead='Vozačka u ruke, osmijeh na licu. Pogledaj kandidate koji su vozačku dozvolu stekli u Autoškoli DrivePro.', big='✓'),
                body=body, **extra)


# ---------------------------------------------------------------- PITANJA
PITANJA = [
    ('Upis', [
        HOME_FAQ[0], HOME_FAQ[4],
        ('Sa koliko godina mogu upisati autoškolu?', 'Zavisi od kategorije. Prema zakonu u BiH, B kategoriju možeš dobiti sa 18 godina, A sa 18, C1 sa 18, C i CE sa 21, a D sa 24 godine. U proces obuke za B kategoriju možeš ući tri mjeseca prije 18. rođendana. Pregled je na stranici <a href="/kategorije/">Kategorije</a>.'),
        ('Koliko važi ljekarsko uvjerenje?', 'Ljekarsko uvjerenje o zdravstvenoj sposobnosti za vozača pribavlja se prije početka obuke i važi 12 mjeseci od dana izdavanja.'),
        ('Primate li kandidate iz okoline Brčkog?', 'Primamo. Kandidati iz cijelog Brčko distrikta i okoline su dobrodošli.'),
    ]),
    ('Obuka', [
        HOME_FAQ[1], HOME_FAQ[5],
        ('Da li je teoretska nastava stvarno besplatna?', 'Jeste. Teoretska nastava u Autoškoli DrivePro je besplatna. Cijenu ostatka obuke i šta tačno obuhvata saznaješ pri upisu.'),
        ('Koliko časova vožnje ima obuka?', 'Za B kategoriju 35 časova. Za C kategoriju 20 časova ako već imaš B kategoriju, odnosno 8 časova ako imaš C1.'),
        ('Kako se dogovaraju časovi vožnje?', 'Termine časova vožnje i ispita biraš sam. Dogovaraš ih s instruktorom Daliborom na 065 803 456, tako da se uklope u školu ili posao.'),
        ('Imam strah od vožnje. Možete li mi pomoći?', 'Možemo. Radimo individualno i bez pritiska, a organizujemo i radionice za prevazilaženje straha od vožnje i treme pred ispit.'),
        ('Ko sprovodi obuku iz prve pomoći?', 'Prema Zakonu o osnovama bezbjednosti saobraćaja na putevima u BiH, osposobljavanje kandidata iz prve pomoći obavlja Crveni krst. Obuka traje dva dana, a mi ti pomažemo da je uklopiš u raspored.'),
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
    return dict(path='/pitanja/', title='Česta pitanja o autoškoli: upis, cijena, rate i ispit | DrivePro',
                desc='Odgovori na najčešća pitanja kandidata: upis, dokumenti, godine po kategorijama, besplatna teorija, rate, časovi vožnje, prva pomoć i ispit u Brčkom.',
                crumbs=[('/', 'Početna'), ('/pitanja/', 'Česta pitanja')], faq=flat,
                hero=dict(chip='❓ Pitanja i odgovori', h1='Česta pitanja o <span>autoškoli u Brčkom</span>',
                          lead='Sve što kandidati najčešće pitaju prije upisa, na jednom mjestu. Ako odgovor nije ovdje, nazovi nas.', big='?'),
                body=body)


# ---------------------------------------------------------------- KONTAKT
def kontakt():
    body = f'''<section class="sec"><div class="wrap">
<div class="ct rvl" style="margin-top:0">
  <div class="card tilt"><i class="gl"></i>
    <div class="row"><div class="ico">📍</div><div><small>Adresa</small><b>{ADR}, 76100 Brčko</b></div></div>
    <div class="row"><div class="ico">📞</div><div><small>Dalibor: upis, informacije i časovi vožnje</small><a href="tel:+38765803456"><b>065 803 456</b></a></div></div>
    <div class="row"><div class="ico">📞</div><div><small>Vladana: informacije i teorijska nastava</small><a href="tel:+38765858411"><b>065 858 411</b></a></div></div>
    <div class="row"><div class="ico">💬</div><div><small>SMS poruka</small><a href="sms:+38765803456"><b>Pošalji poruku Daliboru</b></a></div></div>
    <div class="row"><div class="ico">📸</div><div><small>Instagram</small><a href="{IG}" target="_blank" rel="noopener"><b>@driveproautoskola</b></a></div></div>
  </div>
  <div class="map">
    <iframe title="Mapa: Autoškola DrivePro, {ADR}, Brčko" loading="lazy" referrerpolicy="no-referrer-when-downgrade" src="{MAPS_EMBED}"></iframe>
    <a target="_blank" rel="noopener" href="{MAPS}">Otvori navigaciju →</a>
  </div>
</div></div></section>''' + art(f'''
<h2>Koga <em>zvati</em>?</h2>
<ul>
<li><strong>Upis, informacije, rate i časovi vožnje:</strong> Dalibor, {TD}.</li>
<li><strong>Informacije i teorijska nastava:</strong> Vladana, {TV}.</li>
</ul>
<h2>Kako do nas</h2>
<p>Autoškola DrivePro se nalazi u ulici <strong>{ADR}</strong> u Brčkom, poštanski broj 76100. Najlakše je da otvoriš <a href="{MAPS}" target="_blank" rel="noopener">navigaciju na Google mapama</a>.</p>
<p>Kandidati iz cijelog Brčko distrikta i okoline su dobrodošli.</p>
<h2>Prije nego što dođeš</h2>
<p>Ponesi ličnu kartu, a ako već imaš ljekarsko uvjerenje, i njega. Spisak potrebnih dokumenata je na stranici <a href="/upis/">Kako do vozačke dozvole</a>.</p>''', side('/kontakt/'), alt=True)
    return dict(path='/kontakt/', title='Kontakt | Autoškola DrivePro, Hasana Bećirevića 3, Brčko, 065 803 456',
                desc='Kontakt Autoškole DrivePro: Hasana Bećirevića 3, 76100 Brčko. Upis, informacije i časovi vožnje: Dalibor, 065 803 456. Vladana: 065 858 411.',
                crumbs=[('/', 'Početna'), ('/kontakt/', 'Kontakt')], page_type='ContactPage', prio='0.9',
                hero=dict(chip='📞 Javi nam se', h1='Autoškola Brčko: <span>kontakt i lokacija</span>',
                          lead=f'Pozovi, pošalji poruku ili svrati u ulicu {ADR}. Rado odgovaramo na sva pitanja o obuci, ratama i kategorijama.', big='065',
                          cta='<a href="tel:+38765803456" class="btn btn-y">📞 Dalibor 065 803 456</a><a href="tel:+38765858411" class="btn btn-g">📞 Vladana 065 858 411</a>'),
                body=body)


# ---------------------------------------------------------------- NOVOSTI
def novosti():
    body = '''<section class="sec"><div class="wrap">
<div class="banner" id="nw-banner" hidden><b>Primjeri objava.</b> Ovdje će se prikazivati objave Autoškole DrivePro.</div>
<div class="nw" id="nw-app">
  <div class="posts" id="nw-list"><div class="empty"><b>Učitavam objave…</b></div></div>
  <div id="nw-fb"></div>
</div>
<p class="ctr"><a class="more-link" id="nw-fblink" href="#" target="_blank" rel="noopener" hidden>Prati nas na Facebooku →</a></p>
</div></section>'''
    return dict(path='/novosti/', title='Novosti i obavještenja | Autoškola DrivePro Brčko',
                desc='Najnovije objave Autoškole DrivePro iz Brčkog: upis novih grupa, termini, obavještenja i čestitke kandidatima koji su položili vozački ispit.',
                crumbs=[('/', 'Početna'), ('/novosti/', 'Novosti')], freq='daily', prio='0.7', page_type='CollectionPage',
                hero=dict(chip='📣 Novosti i obavještenja', h1='Novosti iz <span>Autoškole DrivePro</span>',
                          lead='Obavještenja o upisu, terminima i ispitima te čestitke kandidatima, na jednom mjestu.', big='Novo',
                          cta=f'<a href="tel:+38765803456" class="btn btn-y">📞 065 803 456</a><a href="{IG}" target="_blank" rel="noopener" class="btn btn-g">📸 Instagram</a>'),
                body=body, scripts=['/assets/postavke.js', '/podaci/objave.js', '/assets/podaci.js'])


def p404():
    return dict(path='/404.html', title='Stranica nije pronađena | Autoškola DrivePro Brčko', desc='Tražena stranica ne postoji.',
                crumbs=[('/', 'Početna'), ('/404.html', 'Stranica nije pronađena')], robots='noindex,follow', sitemap=False,
                hero=dict(chip='🚧 Skretanje', h1='Ups, pogrešno <span>skretanje</span>',
                          lead='Ova stranica ne postoji ili je premještena. Vrati se na početnu ili odaberi neku od stranica ispod.', big='404',
                          cta='<a href="/" class="btn btn-y">← Početna</a><a href="/kontakt/" class="btn btn-g">Kontakt</a>'),
                body=related('Možda tražiš <em>ovo</em>', [('/b-kategorija/', 'B', 'B kategorija', 'Najtraženija obuka.'), ('/upis/', '📝', 'Upis', 'Kako do vozačke dozvole.'), ('/kontakt/', '📞', 'Kontakt', 'Pozovi i dogovori upis.')], alt=False))


def pages():
    return [home(), kategorije(), b_kat(), a_kat(), c_kat(), ce_kat(), d_kat(), o_nama(), instruktori(), teorija(),
            upis(), novosti(), galerija(), pitanja(), kontakt(), p404()]
