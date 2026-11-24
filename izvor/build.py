# -*- coding: utf-8 -*-
"""Generator sajta Autoškole Brčko.  Pokretanje:  cd izvor && python3 build.py
Sve podatke o školama mijenjaš u rječniku SKOLE ispod. Prazno ('' ili []) = prikazuje se "uskoro"."""
import os, json, html, urllib.parse

DOMAIN = 'https://autoskolebrcko.vercel.app'   # privremeno, dok se ne kupi pravi domen
LUKIC = '/autoskolalukic'                              # Lukić sajt je dio ovog sajta
DRIVEPRO = '/autoskoladrivepro'
LUKIC_IZVOR = os.path.join(os.path.dirname(os.path.abspath(__file__)), '..', 'lukic', 'sajt')
DRIVEPRO_IZVOR = os.path.join(os.path.dirname(os.path.abspath(__file__)), '..', 'drivepro', 'sajt')
OUT = os.path.join(os.path.dirname(os.path.abspath(__file__)), '..', 'sajt')

SKOLE = {
    'lukic': {
        'naziv': 'Autoškola Lukić',
        'url': LUKIC + '/',
        'adresa': 'Tina Ujevića 8, Brčko',
        'telefoni': [('Violeta', '065 537 043'), ('Dalibor', '065 803 456')],
        'email': '',
        'radno': '',
        'facebook': 'https://www.facebook.com/autoskola.lukic',
        'kategorije': ['A', 'B', 'C1', 'C', 'CE', 'D'],
        'opis': '25 godina iskustva. Teorijsku nastavu drži doktor nauka iz oblasti saobraćaja. Moguće plaćanje na rate.',
        'boja': '#C2410C',
    },
    'drivepro': {
        'naziv': 'Autoškola DrivePro',
        'url': DRIVEPRO + '/',
        'adresa': 'Hasana Bećirevića 3, Brčko',
        'telefoni': [('Dalibor', '065 803 456'), ('Vladana', '065 858 411')],
        'email': '',
        'radno': '',
        'facebook': 'https://www.facebook.com/profile.php?id=61558353308315',
        'kategorije': ['A', 'B', 'C1', 'C', 'CE', 'D'],
        'opis': 'Instruktori su diplomirani inženjeri saobraćaja. Teorijska nastava je besplatna. Moguće plaćanje na rate.',
        'boja': '#1F2329',
    },
}

KATEGORIJE = [  # oznaka, vozilo, uvjet, stranica kod Lukića
    ('A', 'Motocikli', 'od 18 godina', '/a-kategorija/'),
    ('B', 'Putnički automobili', 'od 18 godina', '/b-kategorija/'),
    ('C1', 'Lakša teretna vozila', 'od 18 godina', '/c-kategorija/'),
    ('C', 'Teretna vozila', 'od 21 godine', '/c-kategorija/'),
    ('CE', 'Teretna vozila s prikolicom', 'za vozače koji već imaju C', '/ce-kategorija/'),
    ('D', 'Autobusi', 'od 24 godine, uz prethodnu B, C ili D1', '/d-kategorija/'),
]

TIM = [  # ime, titula (značka), opis, škola, link
    ('Violeta Lukić Vujadinović', 'Doc. dr', 'Doktor nauka iz oblasti saobraćaja, predavač teorijske nastave', 'lukic', LUKIC + '/instruktori/#violeta'),
    ('Dalibor Vujadinović', 'Dipl. inž.', 'Dipl. inž. saobraćaja, instruktor vožnje', 'lukic drivepro', DRIVEPRO + '/instruktori/#dalibor'),
    ('Vladana Vujadinović', 'Dipl. inž.', 'Vlasnica Autoškole DrivePro, predavač teorijske nastave i instruktor B kategorije', 'drivepro', DRIVEPRO + '/instruktori/#vladana'),
]

KORACI = [
    ('Ljekarsko uvjerenje', 'Pribavlja se prije početka obuke i važi 12 mjeseci od dana izdavanja.'),
    ('Upis i dogovor o plaćanju', 'Javi se školi koju biraš. Dogovarate kategoriju, način plaćanja i grupu za teoriju.'),
    ('Prva pomoć', 'Obuku i ispit iz prve pomoći, prema zakonu, sprovodi Crveni krst.'),
    ('Teorijska nastava i ispit', 'Saobraćajni propisi i znakovi. Grupu i termine dobijaš prilikom upisa.'),
    ('Časovi vožnje', 'Od osnovnih radnji vozilom do samostalne vožnje kroz grad i van naselja.'),
    ('Praktični ispit', 'Vožnja pred ispitnom komisijom. Nakon položenog ispita podnosiš zahtjev za vozačku dozvolu.'),
]

e = html.escape
def tel(n): return 'tel:+387' + n.replace(' ', '')[1:]
def mapa(a): return 'https://www.google.com/maps/search/?api=1&query=' + urllib.parse.quote(a)
def ext(url): return url.startswith('http')

ARROW = '<svg width="18" height="18" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2.2" stroke-linecap="round" stroke-linejoin="round" aria-hidden="true"><path d="M5 12h14M13 6l6 6-6 6"/></svg>'
PHONE = '<svg width="18" height="18" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round" aria-hidden="true"><path d="M22 16.9v3a2 2 0 0 1-2.2 2 19.8 19.8 0 0 1-8.6-3.1 19.5 19.5 0 0 1-6-6A19.8 19.8 0 0 1 2.1 4.2 2 2 0 0 1 4.1 2h3a2 2 0 0 1 2 1.7c.1.9.4 1.8.7 2.7a2 2 0 0 1-.5 2.1L8 9.8a16 16 0 0 0 6 6l1.3-1.3a2 2 0 0 1 2.1-.4c.9.3 1.8.6 2.7.7a2 2 0 0 1 1.7 2z"/></svg>'
PIN = '<svg width="18" height="18" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round" aria-hidden="true"><path d="M20 10c0 6-8 12-8 12S4 16 4 10a8 8 0 0 1 16 0z"/><circle cx="12" cy="10" r="3"/></svg>'
IMG = '<svg width="30" height="30" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.6" stroke-linecap="round" stroke-linejoin="round" aria-hidden="true"><rect x="3" y="5" width="18" height="14" rx="2"/><circle cx="8.5" cy="10" r="1.5"/><path d="M21 16l-5-5-8 8"/></svg>'
PERSON = '<svg width="30" height="30" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.5" stroke-linecap="round" aria-hidden="true"><circle cx="12" cy="8" r="4"/><path d="M4 21c0-4.4 3.6-8 8-8s8 3.6 8 8"/></svg>'
LOGO = '<svg width="28" height="39" viewBox="19 2 83 116" aria-hidden="true"><g transform="translate(2 0)"><path d="M30 59V15H60A22 22 0 0 1 60 59Z" fill="none" stroke="#1F2329" stroke-width="18"/><path d="M30 59H64A23 23 0 0 1 64 105H30Z" fill="none" stroke="#C2410C" stroke-width="18"/><path d="M30 59V15H60A22 22 0 0 1 60 59" fill="none" stroke="#fff" stroke-width="2.4" stroke-dasharray="5 5"/><path d="M30 59H64A23 23 0 0 1 64 105H30Z" fill="none" stroke="#fff" stroke-width="2.4" stroke-dasharray="5 5"/></g></svg>'

def slot(title, sub, cls=''):
    return f'<div class="slot {cls}" role="img" aria-label="{e(title)}: {e(sub)}">{IMG}<b>{e(title)}</b><span>{e(sub)}</span></div>'

def uskoro(txt='Podaci uskoro'):
    return f'<span class="soon">{e(txt)}</span>'

def head(title, desc, path):
    return f'''<!doctype html>
<html lang="bs">
<head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width, initial-scale=1">
<title>{e(title)}</title>
<meta name="description" content="{e(desc)}">
<link rel="canonical" href="{DOMAIN}{path}">
<meta property="og:type" content="website"><meta property="og:title" content="{e(title)}"><meta property="og:description" content="{e(desc)}"><meta property="og:url" content="{DOMAIN}{path}"><meta property="og:image" content="{DOMAIN}/og-image.png"><meta property="og:locale" content="bs_BA">
<meta name="theme-color" content="#1F2329">
<link rel="icon" href="/favicon.svg" type="image/svg+xml"><link rel="icon" href="/favicon-32.png" sizes="32x32"><link rel="apple-touch-icon" href="/apple-touch-icon.png">
<link rel="stylesheet" href="/assets/style.css">
</head>
<body>
<a class="skip" href="#sadrzaj">Preskoči na sadržaj</a>
'''

def header(home):
    p = '' if home else '/'
    links = [(SKOLE['lukic']['url'], 'Autoškola Lukić'), (DRIVEPRO + '/', 'Autoškola DrivePro'),
             (p + '#kategorije', 'Kategorije'), (p + '#instruktori', 'Instruktori'), (p + '#upis', 'Upis'),
             (p + '#novosti', 'Novosti'), (p + '#kontakt', 'Kontakt')]
    nav = ''.join(f'<a href="{u}">{t}</a>' for u, t in links)
    return f'''<header>
<div class="wrap hdr">
<a class="brand" href="/" aria-label="Autoškole Brčko, početna">{LOGO}<span><span class="wm d">Autoškole Brčko</span><span class="bars" aria-hidden="true"><i style="width:40px;background:#C2410C"></i><i style="width:58px;background:#1F2329"></i></span></span></a>
<nav class="main" aria-label="Glavni meni">{nav}</nav>
<button class="menu" type="button" aria-label="Otvori meni" aria-expanded="false" aria-controls="mm"><svg width="22" height="22" viewBox="0 0 24 24" fill="none" stroke="#1F2329" stroke-width="2" stroke-linecap="round" aria-hidden="true"><path d="M4 7h16M4 12h16M4 17h16"/></svg></button>
</div>
<nav id="mm" class="mm" aria-label="Meni za telefon" hidden><div class="wrap">{nav}</div></nav>
</header>
'''

def school_contacts(s, big=False):
    out = []
    out.append(f'<p class="ci">{PIN}<span>{e(s["adresa"]) if s["adresa"] else uskoro("Adresa uskoro")}</span></p>')
    if s['telefoni']:
        for ime, n in s['telefoni']:
            out.append(f'<p class="ci">{PHONE}<a href="{tel(n)}"><b>{e(n)}</b></a><span class="m">{e(ime)}</span></p>')
    else:
        out.append(f'<p class="ci">{PHONE}{uskoro("Telefon uskoro")}</p>')
    if big:
        if s['email']:
            out.append(f'<p class="ci">✉<a href="mailto:{e(s["email"])}">{e(s["email"])}</a></p>')
        if s['radno']:
            out.append(f'<p class="ci m2">Radno vrijeme: {e(s["radno"])}</p>')
    return ''.join(out)

def footer():
    L, D = SKOLE['lukic'], SKOLE['drivepro']
    def col(s):
        tels = ''.join(f'<a class="ph" href="{tel(n)}">{e(n)} <span>{e(i)}</span></a>' for i, n in s['telefoni']) or '<p>Kontakt uskoro</p>'
        return f'<div><h4><a href="{s["url"]}">{e(s["naziv"])}</a></h4><p>{e(s["adresa"]) or "Adresa uskoro"}</p>{tels}</div>'
    soc = ''.join(f'<a href="{s["facebook"]}" rel="noopener">Facebook {e(s["naziv"].split()[-1])}</a>' for s in (L, D) if s['facebook'])
    return f'''<footer>
<div class="wrap">
<div class="ft">
<div><span class="wm d" style="display:block;color:#fff">Autoškole Brčko</span><span class="bars" aria-hidden="true"><i style="width:40px;background:#FB923C"></i><i style="width:58px;background:#fff"></i></span><p style="margin-top:14px">Zajednička stranica autoškola Lukić i DrivePro iz Brčkog.</p></div>
{col(L)}
{col(D)}
</div>
<div class="fb"><span>© 2026 Autoškole Brčko</span><span>Izrada stranice: <a href="https://www.rbcweb.top/" target="_blank" rel="noopener" style="color:#fff;font-weight:600;text-decoration:underline;text-underline-offset:3px">RbcWeb</a></span><nav aria-label="Društvene mreže">{soc}</nav></div>
</div>
</footer>
<script src="/assets/main.js" defer></script>
</body>
</html>
'''

def home():
    L, D = SKOLE['lukic'], SKOLE['drivepro']
    # škole
    def card(key):
        s = SKOLE[key]
        cats = ''.join(f'<span class="box">{k}</span>' for k in s['kategorije']) or uskoro('Kategorije uskoro')
        opis = f'<p class="sd">{e(s["opis"])}</p>' if s['opis'] else ''
        return f'''<article class="school">
<h3 class="d"><i style="background:{s["boja"]}"></i>{e(s["naziv"])}</h3>
{slot('Fotografija', 'Vozilo ili tim, ' + s['naziv'], 'sc-slot')}
{opis}
<div class="cts">{school_contacts(s)}</div>
<div class="cats"><small>Kategorije</small>{cats}</div>
<a class="sbtn-full {'lk' if key=='lukic' else 'dp'}" href="{s["url"]}">Otvori stranicu {e(s["naziv"].replace("Autoškola", "Autoškole"))} {ARROW}</a>
</article>'''
    # kategorije
    kc = []
    for k, v, u, lp in KATEGORIJE:
        chips = []
        if k in L['kategorije']:
            chips.append(f'<a class="chip lk" href="{LUKIC}{lp}">Lukić {ARROW}</a>')
        if k in D['kategorije']:
            chips.append(f'<a class="chip dp" href="{DRIVEPRO}{lp}">DrivePro {ARROW}</a>')
        kc.append(f'''<article class="kc">
<div class="kc-ph" role="img" aria-label="Fotografija vozila, {k} kategorija">{IMG}<span>Fotografija vozila</span></div>
<div class="kc-b"><div class="kc-t"><span class="L d">{k}</span><div><h3>{e(v)}</h3><p>{e(u)}</p></div></div>
<div class="chips"><small>Obuku izvodi</small>{''.join(chips)}</div></div>
</article>''')
    # tim
    tim = []
    for ime, tit, opis, sk, link in TIM:
        tim.append(f'''<li><a href="{link}"><div class="foto">{PERSON}<span>Fotografija</span><span class="tit">{e(tit)}</span></div>
<div class="t"><b>{e(ime)}</b><span class="r">{e(opis)}</span><em class="{sk}">{' · '.join(SKOLE[x]["naziv"].split()[-1] for x in sk.split())}</em></div></a></li>''')
    koraci = ''.join(f'<li><span class="n d">{i}</span><div><h3>{e(t)}</h3><p>{e(d)}</p></div></li>' for i, (t, d) in enumerate(KORACI, 1))
    def fbframe(s):
        if not s['facebook']:
            return ''
        return f'''<div class="fbw"><iframe title="Objave {e(s['naziv'].replace('Autoškola', 'Autoškole'))} na Facebooku" src="https://www.facebook.com/plugins/page.php?href={urllib.parse.quote(s['facebook'], safe='')}&tabs=timeline&width=500&height=600&small_header=true&adapt_container_width=true&hide_cover=false&show_facepile=false" width="500" height="600" style="border:none;overflow:hidden;width:100%;max-width:500px" scrolling="no" frameborder="0" allowfullscreen="true" allow="clipboard-write; encrypted-media; picture-in-picture; web-share" loading="lazy"></iframe></div>'''
    fb = fbframe(L)
    dfb = (fbframe(D) or '<p class="soon-b">Objave Autoškole DrivePro pojavit će se ovdje čim povežemo njihovu Facebook stranicu.</p>') + f'<a class="link" href="{DRIVEPRO}/novosti/">Sve novosti na stranici DrivePro</a>'

    ld = {"@context": "https://schema.org", "@type": "Organization", "name": "Autoškole Brčko", "url": DOMAIN + "/",
          "member": [{"@type": "DrivingSchool", "name": L['naziv'], "url": L['url'], "telephone": "+38765537043",
                      "address": {"@type": "PostalAddress", "streetAddress": "Tina Ujevića 8", "addressLocality": "Brčko", "addressCountry": "BA"}},
                     {"@type": "DrivingSchool", "name": D['naziv'], "url": DOMAIN + DRIVEPRO + "/", "telephone": "+38765803456",
                      "address": {"@type": "PostalAddress", "streetAddress": "Hasana Bećirevića 3", "addressLocality": "Brčko", "addressCountry": "BA"}}]}

    return head('Autoškole Brčko: Autoškola Lukić i Autoškola DrivePro',
                'Dvije autoškole iz Brčkog na jednom mjestu. Obuka za A, B, C1, C, CE i D kategoriju. Izaberi školu, kategoriju i instruktora.', '/') + header(True) + f'''
<main id="sadrzaj">
<section class="wrap hero">
<div>
<p class="kicker">Autoškola Lukić i Autoškola DrivePro</p>
<h1 class="d">Obuka za vožnju uz <em>stručnu podršku.</em></h1>
<p class="lead">Dvije autoškole iz Brčkog na jednom mjestu. Teoriju i vožnju vode stručnjaci iz oblasti saobraćaja.</p>
<div class="pick">
<a class="sbtn lk" href="{L['url']}"><span><small>Stranica škole</small>Autoškola Lukić</span>{ARROW}</a>
<a class="sbtn dp" href="{DRIVEPRO}/"><span><small>Stranica škole</small>Autoškola DrivePro</span>{ARROW}</a>
</div>
<a class="link" href="#kategorije" style="display:inline-block;margin-top:22px">Pogledaj kategorije</a>
</div>
{slot('Fotografija', 'Tim ili vozila obje škole', 'hero-slot')}
</section>

<div class="strip">
<div class="wrap">
<div class="c"><b>Autoškola Lukić</b><span>{e(L['adresa'])}</span><a href="{tel(L['telefoni'][0][1])}">{e(L['telefoni'][0][1])}</a></div>
<div class="c"><b>Autoškola DrivePro</b><span>{e(D['adresa']) or 'Adresa uskoro'}</span>{f'<a href="{tel(D["telefoni"][0][1])}">{e(D["telefoni"][0][1])}</a>' if D['telefoni'] else '<a href="{DRIVEPRO}/">Stranica škole</a>'}</div>
</div>
</div>

<section class="wrap sec" id="skole">
<div class="sec-h"><h2 class="d">Naše škole</h2><p>Javi se direktno školi koja ti odgovara.</p></div>
<div class="schools">{card('lukic')}{card('drivepro')}</div>
</section>

<section class="wrap sec" id="kategorije">
<div class="sec-h"><h2 class="d">Kategorije</h2><p>Za svaku kategoriju vidiš koja škola izvodi obuku. Klik vodi na detalje obuke.</p></div>
<div class="kgrid">{''.join(kc)}</div>
</section>

<section class="ws" id="instruktori">
<div class="wrap">
<div class="ins-wrap">
<div class="ins-h">
<p class="kicker">Instruktori i predavači</p>
<h2 class="d">Ljudi koji te uče da voziš</h2>
<p>Predavači i instruktori obje škole.</p>
</div>
<ul class="ins">{''.join(tim)}</ul>
</div>
</div>
</section>

<section class="wrap sec" id="upis">
<div class="sec-h"><h2 class="d">Kako do vozačke</h2><p>Redoslijed je isti u obje škole. Tačan spisak dokumenata potvrdi pozivom prije upisa.</p></div>
<ol class="steps">{koraci}</ol>
<div class="pay">
<div><h3 class="d">Plaćanje i uslovi</h3><p>Cijene ne objavljujemo jer se ponuda dogovara prema kategoriji i kandidatu. U obje škole moguće je plaćanje na rate. Uslove dogovaraš sa školom pri upisu.</p></div>
<a class="btn" href="{tel(L['telefoni'][0][1])}">{PHONE} Lukić {e(L['telefoni'][0][1])}</a>
</div>
</section>

<section class="wrap sec" id="novosti">
<div class="sec-h"><h2 class="d">Novosti</h2><p>Objave škola sa Facebooka, automatski.</p></div>
<div class="news">
<div><h3 class="nh"><i style="background:#C2410C"></i>Autoškola Lukić</h3>{fb}<a class="link" href="{LUKIC}/novosti/">Sve novosti na stranici Lukić</a></div>
<div><h3 class="nh"><i style="background:#1F2329"></i>Autoškola DrivePro</h3>{dfb}</div>
</div>
</section>

<section class="wrap sec" id="kontakt">
<div class="sec-h"><h2 class="d">Kontakt</h2><p>Pozovi školu direktno. Na telefonu dodirni broj za poziv.</p></div>
<div class="kontakt">
<div class="kk"><h3 class="d"><i style="background:#C2410C"></i>Autoškola Lukić</h3>{school_contacts(L, True)}<a class="link" href="{mapa('Tina Ujevića 8, Brčko')}" rel="noopener">Otvori u mapama</a></div>
<div class="kk"><h3 class="d"><i style="background:#1F2329"></i>Autoškola DrivePro</h3>{school_contacts(D, True)}{f'<a class="link" href="{mapa(D["adresa"])}" rel="noopener">Otvori u mapama</a>' if D['adresa'] else ''}</div>
</div>
</section>
</main>
<script type="application/ld+json">{json.dumps(ld, ensure_ascii=False)}</script>
''' + footer()

def drivepro():
    D = SKOLE['drivepro']
    cats = ''.join(f'<span class="box">{k}</span>' for k in D['kategorije']) or uskoro('Kategorije se objavljuju nakon potvrde ponude')
    vl = TIM[2]
    return head('Autoškola DrivePro | Autoškole Brčko',
                'Autoškola DrivePro iz Brčkog: kategorije, instruktori, predavači i kontakt.', DRIVEPRO + '/') + header(False) + f'''
<main id="sadrzaj">
<section class="wrap phero">
<p class="crumb"><a href="/">Autoškole Brčko</a> › DrivePro</p>
<div class="ph-grid">
<div>
<p class="kicker">Članica Autoškola Brčko</p>
<h1 class="d">Autoškola <em>DrivePro</em></h1>
{f'<p class="lead">{e(D["opis"])}</p>' if D['opis'] else ''}
<div class="cts big">{school_contacts(D, True)}</div>
</div>
{slot('Logo i fotografija', 'Vozilo, učionica ili tim DrivePro', 'dp-slot')}
</div>
</section>

<section class="wrap sec" id="kategorije">
<div class="sec-h"><h2 class="d">Kategorije</h2><p>Kategorije za koje DrivePro izvodi obuku.</p></div>
<div class="cats">{cats}</div>
</section>

<section class="wrap sec" id="tim">
<div class="sec-h"><h2 class="d">Tim</h2><p>Instruktori i predavači Autoškole DrivePro.</p></div>
<article class="person" id="vladana">
<div class="pfoto">{PERSON}<span>Fotografija</span></div>
<div>
<h3 class="d">{e(vl[0])}</h3>
<ul class="facts"><li><small>Zvanje</small>Diplomirani inženjer saobraćaja</li><li><small>Uloga</small>Predavač teorijske nastave, instruktor vožnje</li><li><small>Kategorije</small><span class="box">B</span></li></ul>
<p>Vladana je diplomirani inženjer saobraćaja. U Autoškoli DrivePro radi kao predavač teorijske nastave i instruktor vožnje B kategorije. Učestvuje u teorijskom osposobljavanju kandidata i izvodi praktičnu obuku za B kategoriju.</p>
</div>
</article>
</section>

<section class="wrap sec">
<div class="sec-h"><h2 class="d">Učionica i vozila</h2><p>Prostor i vozila za obuku.</p></div>
<div class="g3">{slot('Fotografija', 'Učionica')}{slot('Fotografija', 'Vozilo za obuku')}{slot('Fotografija', 'Praktična obuka')}</div>
</section>

<section class="wrap sec">
<div class="back"><p>Tražiš drugu školu?</p><a class="sbtn-full lk" href="{SKOLE['lukic']['url']}">Otvori stranicu Autoškole Lukić {ARROW}</a></div>
</section>
</main>
''' + footer()

def p404():
    return head('Stranica nije pronađena | Autoškole Brčko', 'Stranica nije pronađena.', '/404.html') + header(False) + f'''
<main id="sadrzaj" class="wrap sec" style="min-height:50vh">
<h1 class="d" style="font-size:44px">Ova stranica ne postoji.</h1>
<p style="margin-top:16px">Vrati se na <a class="link" href="/">početnu</a> ili otvori <a class="link" href="{LUKIC}/">Autoškolu Lukić</a>.</p>
</main>
''' + footer()

def write(path, txt):
    p = os.path.join(OUT, path)
    os.makedirs(os.path.dirname(p), exist_ok=True)
    open(p, 'w', encoding='utf-8').write(txt)

def spoji(BASE, IZVOR, stari):
    """Kopira gotov sajt škole u sajt/<BASE>/ i sve njegove linkove prebacuje pod tu putanju."""
    import re, shutil
    LUKIC = BASE
    dst = os.path.join(OUT, BASE.strip('/'))
    shutil.rmtree(dst, ignore_errors=True)
    shutil.copytree(IZVOR, dst, ignore=shutil.ignore_patterns('404.html', 'CNAME', '.gitkeep', '.nojekyll'))
    for root, _, files in os.walk(dst):
        for f in files:
            if not f.endswith(('.html', '.js', '.xml', '.webmanifest', '.txt', '.css')):
                continue
            p = os.path.join(root, f)
            t = open(p, encoding='utf-8').read()
            t = t.replace(stari, DOMAIN + LUKIC)
            if f.endswith('.html'):
                t = re.sub(r'((?:href|src|action)=")/(?!/)', r'\1' + LUKIC + '/', t)
            elif f.endswith('.webmanifest'):
                t = re.sub(r'("(?:src|start_url)":\s*")/', r'\1' + LUKIC + '/', t)
            elif f.endswith('.js'):
                t = t.replace('"/predavanja/', '"' + LUKIC + '/predavanja/').replace('"/img/', '"' + LUKIC + '/img/')
            t = t.replace(LUKIC + '/__brcko__/', '/')
            open(p, 'w', encoding='utf-8').write(t)
    os.remove(os.path.join(dst, 'robots.txt')) if os.path.exists(os.path.join(dst, 'robots.txt')) else None

def optimizuj():
    """Brzina: smanjen CSS, verzija po sadržaju za CSS/JS (dugo keširanje), bez duplih poziva za fontove."""
    import re, hashlib
    def mini_css(c):
        c = re.sub(r'/\*.*?\*/', '', c, flags=re.S)
        c = re.sub(r'\s+', ' ', c)
        c = re.sub(r'\s*([{};,>])\s*', r'\1', c)
        c = c.replace(';}', '}')
        return c.strip()
    ver = {}
    for root, _, files in os.walk(OUT):
        for f in files:
            p = os.path.join(root, f)
            rel = '/' + os.path.relpath(p, OUT).replace(os.sep, '/')
            if f.endswith('.css'):
                t = open(p, encoding='utf-8').read(); m = mini_css(t)
                open(p, 'w', encoding='utf-8').write(m)
            if '/assets/' in rel and f.endswith(('.css', '.js')):
                ver[rel] = hashlib.md5(open(p, 'rb').read()).hexdigest()[:10]
    pre = '<link rel="preconnect" href="https://fonts.googleapis.com">\n<link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>\n'
    for root, _, files in os.walk(OUT):
        for f in files:
            if not f.endswith('.html'):
                continue
            p = os.path.join(root, f); t = open(p, encoding='utf-8').read()
            for rel, h in ver.items():
                t = re.sub(r'(["\'])' + re.escape(rel) + r'(\?v=[^"\']*)?(["\'])', r'\1' + rel + '?v=' + h + r'\3', t)
            if t.count(pre) > 1:
                i = t.find(pre) + len(pre); t = t[:i] + t[i:].replace(pre, '')
            fl = re.findall(r'<link href="https://fonts\.googleapis\.com/css2[^>]*>\n?', t)
            if len(fl) > 1:
                i = t.find(fl[0]) + len(fl[0]); t = t[:i] + t[i:].replace(fl[0], '', len(fl) - 1)
            open(p, 'w', encoding='utf-8').write(t)
    return ver

if __name__ == '__main__':
    css = open(os.path.join(os.path.dirname(__file__), 'style.css'), encoding='utf-8').read()
    write('assets/style.css', css)
    write('assets/main.js', open(os.path.join(os.path.dirname(__file__), 'main.js'), encoding='utf-8').read())
    write('index.html', home())
    write('404.html', p404())
    write('robots.txt', f'User-agent: *\nAllow: /\nSitemap: {DOMAIN}/sitemap.xml\nSitemap: {DOMAIN}{LUKIC}/sitemap.xml\nSitemap: {DOMAIN}{DRIVEPRO}/sitemap.xml\n')
    write('sitemap.xml', '<?xml version="1.0" encoding="UTF-8"?>\n<urlset xmlns="http://www.sitemaps.org/schemas/sitemap/0.9">\n' +
          ''.join(f'<url><loc>{DOMAIN}{u}</loc></url>\n' for u in ('/',)) + '</urlset>\n')
    spoji(LUKIC, LUKIC_IZVOR, 'https://autoskolalukic.vercel.app')
    spoji(DRIVEPRO, DRIVEPRO_IZVOR, 'https://autoskoladrivepro.vercel.app')
    optimizuj()
    print('Gotovo:', os.path.abspath(OUT))
