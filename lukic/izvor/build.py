#!/usr/bin/env python3
"""Generator statičkog sajta Autoškole Lukić.
Pokretanje:  python3 build.py   (stranice se upisuju u ../sajt/)
Sadržaj stranica je u sadrzaj.py, a izgled (header, footer, head) ovdje."""
import json, os, html, sys
ROOT = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, ROOT)
import sadrzaj as S

OUT = os.path.join(ROOT, '..', 'sajt')
DOMAIN = 'https://autoskolalukic.vercel.app'
DATUM = '2026-11-17'
VER = '4'

# ---------- CSS ----------
base = open(os.path.join(ROOT, 'base.css'), encoding='utf-8').read()
base = base.replace('@media(min-width:1024px){nav.d{display:flex}#mb{display:none}#mm{display:none!important}}',
                    '@media(min-width:1180px){nav.d{display:flex}#mb{display:none}#mm{display:none!important}}')
base = base.replace('nav.d{display:none;gap:26px', 'nav.d{display:none;gap:22px')
base = base.replace('@media(min-width:800px){footer .fgrid{grid-template-columns:1.5fr 1fr 1.2fr;gap:48px}}',
                    '@media(min-width:700px){footer .fgrid{grid-template-columns:1fr 1fr}}@media(min-width:1000px){footer .fgrid{grid-template-columns:1.4fr .9fr 1fr 1.2fr;gap:44px}}')
extra = open(os.path.join(ROOT, 'extra.css'), encoding='utf-8').read()
os.makedirs(os.path.join(OUT, 'assets'), exist_ok=True)
open(os.path.join(OUT, 'assets', 'style.css'), 'w', encoding='utf-8').write(base + '\n' + extra)

e = html.escape

# ---------- navigacija ----------
KAT = [('/b-kategorija/', 'B kategorija', 'automobil'), ('/a-kategorija/', 'A kategorija', 'motocikl'),
       ('/c-kategorija/', 'C1 i C kategorija', 'kamion'), ('/ce-kategorija/', 'CE kategorija', 'kamion s prikolicom'),
       ('/d-kategorija/', 'D kategorija', 'autobus')]
ONAMA = [('/o-nama/', 'O nama'), ('/instruktori/', 'Instruktori'), ('/teorijska-nastava/', 'Teorijska nastava'),
         ('/galerija/', 'Galerija'), ('/pitanja/', 'Česta pitanja')]
MAIN = [('/upis/', 'Upis'), ('/novosti/', 'Novosti'), ('/kontakt/', 'Kontakt')]


def cur(p, path):
    return ' aria-current="page"' if p == path else ''


def header(path):
    dd1 = ''.join(f'<a href="{p}"{cur(p,path)}>{n}</a>' for p, n in ONAMA)
    dd2 = ''.join(f'<a href="{p}"{cur(p,path)}>{n} <small>{s}</small></a>' for p, n, s in KAT) + f'<a href="/kategorije/"{cur("/kategorije/",path)}>Sve kategorije <small>pregled</small></a>'
    main = ''.join(f'<a href="{p}"{cur(p,path)}>{n}</a>' for p, n in MAIN)
    mob = ('<a class="up" href="/__brcko__/">← Autoškole Brčko</a><a href="/">Početna</a>' + '<span class="mg">Obuka</span>' +
           ''.join(f'<a class="sub2" href="{p}"{cur(p,path)}>{n}</a>' for p, n, s in KAT) +
           f'<a class="sub2" href="/kategorije/">Sve kategorije</a><span class="mg">Autoškola</span>' +
           ''.join(f'<a href="{p}"{cur(p,path)}>{n}</a>' for p, n in MAIN + ONAMA))
    return f'''<!--H--><header id="hd">
  <div class="wrap hd">
    <a class="bkb" href="/__brcko__/" aria-label="Nazad na Autoškole Brčko" title="Nazad na Autoškole Brčko"><span class="bki"><svg width="16" height="16" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2.6" stroke-linecap="round" stroke-linejoin="round" aria-hidden="true"><path d="M19 12H5M11 18l-6-6 6-6"/></svg></span><span class="bkt"><small>Nazad na</small><b>Autoškole Brčko</b></span></a><span class="bkd" aria-hidden="true"></span><a href="/" class="logo" aria-label="Autoškola Lukić, početna stranica"><span class="lg"><i class="fr f">L</i><i class="bk">🚗</i></span><span class="lt">Autoškola Lukić</span></a>
    <nav class="d" aria-label="Glavni meni">
      <div class="dd"><button type="button" aria-haspopup="true" aria-expanded="false">O nama</button><div class="ddm">{dd1}</div></div>
      <div class="dd"><button type="button" aria-haspopup="true" aria-expanded="false">Kategorije</button><div class="ddm">{dd2}</div></div>
      {main}
      <a href="/kontakt/" class="btn btn-y">Upiši se</a>
    </nav>
    <button type="button" id="mb" aria-label="Meni" aria-expanded="false" aria-controls="mm">☰</button>
  </div>
  <nav id="mm" aria-label="Mobilni meni">{mob}</nav>
</header><a class="bkf" href="/__brcko__/" aria-label="Nazad na Autoškole Brčko"><span class="bki"><svg width="15" height="15" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2.6" stroke-linecap="round" stroke-linejoin="round" aria-hidden="true"><path d="M19 12H5M11 18l-6-6 6-6"/></svg></span><span class="bkt"><small>Nazad na</small><b>Autoškole Brčko</b></span></a><!--/H-->'''


def footer():
    k = ''.join(f'<a href="{p}">{n}</a>' for p, n, s in KAT)
    s = ''.join(f'<a href="{p}">{n}</a>' for p, n in [('/', 'Početna')] + ONAMA[:3] + MAIN[:4] + ONAMA[3:] + [('/__brcko__/', 'Autoškole Brčko')])
    return f'''<!--F--><div class="road"></div>
<footer>
  <div class="wrap fgrid">
    <div class="fb">
      <a href="/" class="logo flogo"><span class="lg"><i class="fr f">L</i><i class="bk">🚗</i></span><span class="lt">Autoškola Lukić</span></a>
      <p>25 godina iskustva u obuci vozača u Brčkom. Kategorije A, B, C1, C, CE i D, teorija kod doktora nauka iz saobraćaja i plaćanje na rate.</p>
      <a class="ig" href="https://www.instagram.com/autoskolalukic" target="_blank" rel="noopener">📸 @autoskolalukic</a>
    </div>
    <div><h2 class="fh">Obuka</h2>{k}<a href="/kategorije/">Sve kategorije</a></div>
    <div><h2 class="fh">Stranica</h2>{s}</div>
    <div>
      <h2 class="fh">Kontakt</h2>
      <span>📍 Tina Ujevića 8, 76100 Brčko</span>
      <a href="tel:+38765537043">📞 Violeta: 065 537 043</a>
      <a href="tel:+38765803456">📞 Dalibor: 065 803 456</a>
      <a href="https://www.google.com/maps/search/?api=1&amp;query=Tina+Ujevi%C4%87a+8+Br%C4%8Dko+76100" target="_blank" rel="noopener">🧭 Navigacija</a>
      <a href="/kontakt/">✉️ Sve kontakt informacije</a>
    </div>
  </div>
  <div class="fbar"><div class="wrap">
    <span>© 2026 Autoškola Lukić Brčko. Članica <a href="/__brcko__/">Autoškola Brčko</a>.</span>
    <span class="cr">Izrada stranice: <a href="https://www.rbcweb.top/" target="_blank" rel="noopener">RbcWeb</a></span>
  </div></div>
</footer>
<button type="button" id="st" aria-label="Nazad na vrh"><svg viewBox="0 0 60 60" aria-hidden="true"><circle class="bg" cx="30" cy="30" r="27"/><circle class="pg" cx="30" cy="30" r="27"/></svg><span class="c3"><i class="a">L</i><i class="b">↑</i></span></button><!--/F-->'''


FIN = '''<!--C--><section class="fin">
  <div class="wrap fg">
    <div>
      <h2>Spreman za prvi čas?</h2>
      <p>Nazovi i dogovori termin upisa. Rado odgovaramo na sva pitanja o obuci, ratama i kategorijama.</p>
      <div class="cta">
        <a href="tel:+38765537043" class="btn btn-y">Pozovi Violetu</a>
        <a href="tel:+38765803456" class="btn btn-g">Pozovi Dalibora</a>
      </div>
    </div>
    <div class="scene" id="scene">
      <svg id="wheel" viewBox="0 0 200 200" aria-hidden="true"><circle cx="100" cy="100" r="86" fill="none" stroke="#3A3A3A" stroke-width="16"/><circle cx="100" cy="100" r="86" fill="none" stroke="#FFCC00" stroke-width="2" stroke-dasharray="6 6"/><path d="M16 100H72M184 100H128M100 128V186" stroke="#0E0E0E" stroke-width="14" stroke-linecap="round"/><circle cx="100" cy="100" r="30" fill="#FFCC00"/><text x="100" y="112" text-anchor="middle" font-size="34" font-weight="900" fill="#1C1C1C" font-family="Montserrat,Arial,sans-serif">L</text><path d="M100 12v12" stroke="#C2410C" stroke-width="5"/></svg>
      <div class="sg s1" aria-hidden="true">50</div><div class="sg s2" aria-hidden="true">P</div><div class="sg s3" aria-hidden="true">!</div>
    </div>
  </div>
</section><!--/C-->'''

ORG_ID = DOMAIN + '/#autoskola'
ORG_MINI = {"@type": "DrivingSchool", "@id": ORG_ID, "name": "Autoškola Lukić", "url": DOMAIN + "/", "telephone": "+387 65 537 043",
            "image": DOMAIN + "/og-image.jpg", "sameAs": ["https://www.instagram.com/autoskolalukic"],
            "address": {"@type": "PostalAddress", "streetAddress": "Tina Ujevića 8", "addressLocality": "Brčko", "postalCode": "76100", "addressRegion": "Brčko distrikt", "addressCountry": "BA"}}


def breadcrumbs_ld(url, crumbs):
    return {"@type": "BreadcrumbList", "@id": url + '#putanja', "itemListElement": [
        {"@type": "ListItem", "position": i + 1, "name": n, "item": DOMAIN + p} for i, (p, n) in enumerate(crumbs)]}


def crumbs_html(crumbs):
    parts = []
    for i, (p, n) in enumerate(crumbs):
        if i == len(crumbs) - 1:
            parts.append(f'<span aria-current="page">{e(n)}</span>')
        else:
            parts.append(f'<a href="{p}">{e(n)}</a><span aria-hidden="true">›</span>')
    return '<nav class="bc" aria-label="Putanja">' + ''.join(parts) + '</nav>'


def faq_ld(url, qa):
    return {"@type": "FAQPage", "@id": url + '#pitanja', "inLanguage": "bs", "mainEntity": [
        {"@type": "Question", "name": q, "acceptedAnswer": {"@type": "Answer", "text": S.strip_tags(a)}} for q, a in qa]}


SITEMAP = []


def render(pg):
    path = pg['path']
    url = DOMAIN + path
    title = pg['title']
    desc = pg['desc']
    ogt = pg.get('og_title', title)
    if pg.get('home'):
        ld = S.home_ld(DOMAIN, ORG_ID)
    else:
        ld = [ORG_MINI,
              {"@type": pg.get('page_type', 'WebPage'), "@id": url + '#stranica', "url": url, "name": title, "description": desc,
               "inLanguage": "bs", "isPartOf": {"@type": "WebSite", "@id": DOMAIN + '/#website', "url": DOMAIN + "/", "name": "Autoškola Lukić Brčko"},
               "about": {"@id": ORG_ID}, "dateModified": DATUM, "breadcrumb": {"@id": url + '#putanja'},
               "primaryImageOfPage": pg.get('image', DOMAIN + '/og-image.jpg')},
              breadcrumbs_ld(url, pg['crumbs'])]
        ld += pg.get('ld', [])
        if pg.get('faq'):
            ld.append(faq_ld(url, pg['faq']))
    ld_txt = json.dumps({"@context": "https://schema.org", "@graph": ld}, ensure_ascii=False, separators=(',', ':'))
    robots = pg.get('robots', 'index,follow,max-image-preview:large,max-snippet:-1,max-video-preview:-1')
    scripts = ''.join(f'<script src="{s}?v={VER}" defer></script>' for s in pg.get('scripts', []))
    hero = pg.get('hero_html')
    if hero is None:
        h = pg['hero']
        btns = h.get('cta', '<a href="/kontakt/" class="btn btn-y">Dogovori upis →</a><a href="tel:+38765537043" class="btn btn-g">📞 065 537 043</a>')
        hero = f'''<section class="phero">
  <div class="orb o1"></div>
  {('<div class="big" aria-hidden="true">'+h['big']+'</div>') if h.get('big') else ''}
  <div class="wrap">
    {crumbs_html(pg['crumbs'])}
    <span class="chip">{h['chip']}</span>
    <h1>{h['h1']}</h1>
    <p class="l">{h['lead']}</p>
    <div class="cta">{btns}</div>
  </div>
</section>
<div class="road sm"></div><div class="curb"></div>'''
    preload = ''.join(f'<link rel="preload" as="image" href="{x}">\n' for x in pg.get('preload', []))
    doc = f'''<!DOCTYPE html>
<html lang="bs">
<head>
<meta charset="UTF-8">
<meta name="viewport" content="width=device-width, initial-scale=1, viewport-fit=cover">
<script>(function(){{var n=navigator,m=n.deviceMemory,c=n.hardwareConcurrency,s=n.connection&&n.connection.saveData;if((m&&m<=2)||(c&&c<=4)||s)document.documentElement.classList.add('lite')}})()</script>
<title>{e(title)}</title>
<meta name="description" content="{e(desc)}">
<meta name="robots" content="{robots}">
<meta name="author" content="RbcWeb">
<meta name="theme-color" content="#FFCC00">
<meta name="format-detection" content="telephone=yes">
<meta name="geo.region" content="BA-BRC">
<meta name="geo.placename" content="Brčko">
<link rel="canonical" href="{url}">
<meta property="og:type" content="website">
<meta property="og:locale" content="bs_BA">
<meta property="og:site_name" content="Autoškola Lukić Brčko">
<meta property="og:title" content="{e(ogt)}">
<meta property="og:description" content="{e(desc)}">
<meta property="og:url" content="{url}">
<meta property="og:image" content="{DOMAIN}/og-image.jpg">
<meta property="og:image:width" content="1200">
<meta property="og:image:height" content="630">
<meta property="og:image:alt" content="Autoškola Lukić Brčko, 25 godina iskustva">
<meta name="twitter:card" content="summary_large_image">
<meta name="twitter:title" content="{e(ogt)}">
<meta name="twitter:description" content="{e(desc)}">
<meta name="twitter:image" content="{DOMAIN}/og-image.jpg">
<link rel="icon" href="/favicon.ico" sizes="any">
<link rel="icon" type="image/png" sizes="32x32" href="/favicon-32x32.png">
<link rel="icon" type="image/png" sizes="16x16" href="/favicon-16x16.png">
<link rel="apple-touch-icon" sizes="180x180" href="/apple-touch-icon.png">
<link rel="manifest" href="/site.webmanifest">
<link rel="preconnect" href="https://fonts.googleapis.com">
<link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
<link href="https://fonts.googleapis.com/css2?family=Montserrat:wght@500;700;800;900&family=Inter:wght@400;500;600&display=swap" rel="stylesheet">
<link rel="stylesheet" href="/assets/style.css?v={VER}">
{preload}<script type="application/ld+json">{ld_txt}</script>
</head>
<body>
<div id="ts" aria-hidden="true"></div>
<a class="skip" href="#sadrzaj">Preskoči na sadržaj</a>
<!--S-->{S.CARSYM if pg.get('home') else ''}<!--/S-->
{header(path)}
<main id="sadrzaj"><!--M-->
{hero}
{pg['body']}
<!--/M-->{'' if pg.get('no_fin') else FIN}
</main>
{footer()}
<script src="/assets/main.js?v={VER}" defer></script>
{scripts}
</body>
</html>
'''
    rel = path.strip('/')
    if not rel:
        fn = os.path.join(OUT, 'index.html')
    elif rel.endswith('.html'):
        fn = os.path.join(OUT, rel)
    else:
        fn = os.path.join(OUT, rel, 'index.html')
    os.makedirs(os.path.dirname(fn), exist_ok=True)
    open(fn, 'w', encoding='utf-8').write(doc)
    if pg.get('sitemap', True):
        SITEMAP.append((url, pg.get('prio', '0.8'), pg.get('freq', 'monthly'), pg.get('images', [])))


for pg in S.pages():
    render(pg)

sm = ['<?xml version="1.0" encoding="UTF-8"?>', '<urlset xmlns="http://www.sitemaps.org/schemas/sitemap/0.9" xmlns:image="http://www.google.com/schemas/sitemap-image/1.1">']
for u, pr, fr, imgs in SITEMAP:
    im = ''.join(f'<image:image><image:loc>{DOMAIN}{x}</image:loc></image:image>' for x in imgs)
    sm.append(f'  <url><loc>{u}</loc><lastmod>{DATUM}</lastmod><changefreq>{fr}</changefreq><priority>{pr}</priority>{im}</url>')
sm.append('</urlset>\n')
open(os.path.join(OUT, 'sitemap.xml'), 'w', encoding='utf-8').write('\n'.join(sm))
open(os.path.join(OUT, 'robots.txt'), 'w').write('User-agent: *\nAllow: /\n\nSitemap: https://autoskolalukic.vercel.app/sitemap.xml\n')
print('Generisano stranica:', len(SITEMAP), '+ 404')
