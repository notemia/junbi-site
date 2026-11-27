#!/usr/bin/env python3
"""Builds the Junbi site (landing, privacy policy, support) in 12 languages. Run from the repo root: python3 _src/build.py
Copy lives in _src/langs.py. English also serves en-GB, Spanish also serves es-MX (same URLs in App Store Connect)."""
import html, os, shutil, sys
HERE = os.path.dirname(os.path.abspath(__file__)); SITE = os.path.expanduser(os.environ.get('JUNBI_OUT', os.path.dirname(HERE))); sys.path.insert(0, HERE)
from langs import L
from extra import X
for c, x in X.items():      # 2026-11-27: the full-game purchase and Game Center; the old short version said "no in-app purchases"
    t = L[c]; t['updated'] = t['updated'].replace('25', '27'); secs = list(t['sections'])
    secs[0] = (secs[0][0], [x['short']]); secs[2:2] = [(x['buy'][0], [x['buy'][1]]), (x['gc'][0], [x['gc'][1]])]; t['sections'] = secs
    faq = list(t['faq']); faq.insert(3, x['restore']); t['faq'] = faq
# Since 2026-11-27 the site lives at https://notemia.app/junbi/ (folder junbi/ of the notemia/app repo, the site of all Notemia apps):
#   JUNBI_OUT=~/path/to/app/junbi python3 _src/build.py      builds there
#   python3 _src/build.py redirect                           turns this repo (notemia.github.io/junbi-site) into redirects to it
BASE = os.environ.get('JUNBI_BASE', 'https://notemia.app/junbi/')
MAIL = 'helpyoutofeel@gmail.com'; UNITY = 'https://unity.com/legal/privacy-policy'
STORE = ''   # App Store address of the app, once it is live
ORDER = [('en', '', 'English'), ('ru', 'ru/', 'Русский'), ('fr', 'fr/', 'Français'), ('de', 'de/', 'Deutsch'), ('es', 'es/', 'Español'),
         ('pt-br', 'pt-br/', 'Português (Brasil)'), ('pl', 'pl/', 'Polski'), ('tr', 'tr/', 'Türkçe'), ('ar', 'ar/', 'العربية'),
         ('ko', 'ko/', '한국어'), ('zh-hans', 'zh-hans/', '简体中文'), ('zh-hant', 'zh-hant/', '繁體中文')]
HREFLANG = {'en': 'en', 'ru': 'ru', 'fr': 'fr', 'de': 'de', 'es': 'es', 'pt-br': 'pt-BR', 'pl': 'pl', 'tr': 'tr', 'ar': 'ar', 'ko': 'ko', 'zh-hans': 'zh-Hans', 'zh-hant': 'zh-Hant'}
e = lambda s: html.escape(s, quote=False)
import hashlib; IV = hashlib.md5(open(os.path.join(os.path.dirname(HERE), 'icon.png'), 'rb').read()).hexdigest()[:8]      # ?v= on the icon: a new icon is not hidden by caches
CSS = """:root{--bg:#fff;--fg:#14161c;--mut:#5b6170;--card:#f4f5f8;--line:#e3e5ea;--acc:#c8102e;--acc2:#003087}
@media(prefers-color-scheme:dark){:root{--bg:#0e1016;--fg:#eef0f5;--mut:#9aa1b2;--card:#171a23;--line:#262a36;--acc:#ff4d63;--acc2:#6aa0ff}}
*{box-sizing:border-box}body{margin:0;background:var(--bg);color:var(--fg);font:17px/1.6 -apple-system,BlinkMacSystemFont,"Segoe UI",Roboto,Helvetica,Arial,sans-serif}
.wrap{max-width:760px;margin:0 auto;padding:0 20px}header{border-bottom:1px solid var(--line)}
.bar{display:flex;align-items:center;gap:14px;padding:14px 0;flex-wrap:wrap}.brand{display:flex;align-items:center;gap:10px;font-weight:700;color:var(--fg);text-decoration:none}
.brand img{width:36px;height:36px;border-radius:9px}nav{display:flex;gap:18px;margin-inline-start:auto;flex-wrap:wrap}nav a{color:var(--mut);text-decoration:none}nav a.on,nav a:hover{color:var(--fg)}
h1{font-size:2rem;line-height:1.2;margin:2rem 0 .5rem}h2{font-size:1.2rem;margin:2rem 0 .4rem}p{margin:.5rem 0}.mut{color:var(--mut)}
.hero{display:flex;gap:22px;align-items:center;padding:36px 0 8px;flex-wrap:wrap}.hero img{width:132px;height:132px;border-radius:30px;box-shadow:0 10px 30px rgba(0,0,0,.25)}
ul.f{list-style:none;padding:0;margin:20px 0;display:grid;gap:10px}ul.f li{background:var(--card);border:1px solid var(--line);border-radius:12px;padding:12px 16px}
.btn{display:inline-block;margin:6px 8px 6px 0;padding:10px 18px;border-radius:10px;background:var(--acc);color:#fff;text-decoration:none;font-weight:600}.btn.o{background:none;color:var(--fg);border:1px solid var(--line)}
a{color:var(--acc2)}details{background:var(--card);border:1px solid var(--line);border-radius:12px;padding:12px 16px;margin:10px 0}summary{cursor:pointer;font-weight:600}
footer{border-top:1px solid var(--line);margin-top:48px;padding:22px 0 40px;color:var(--mut);font-size:.9rem}footer .langs{display:flex;flex-wrap:wrap;gap:6px 14px;margin-bottom:12px}footer a{color:var(--mut)}"""

def page(code, folder, kind):
    t = L[code]; d = t.get('dir', 'ltr'); depth = folder.count('/'); up = '../' * depth
    nav = [('', t['home']), ('privacy.html', t['privacy']), ('support.html', t['support'])]
    title = {'': f"{t['name']}: {t['tag']}", 'privacy.html': f"{t['priv_title']} — {t['name']}", 'support.html': f"{t['sup_title']} — {t['name']}"}[kind]
    desc = t['lead'] if kind == '' else (t['priv_intro'] if kind == 'privacy.html' else t['sup_intro'])
    h = [f'<!doctype html><html lang="{HREFLANG[code]}" dir="{d}"><head><meta charset="utf-8"><meta name="viewport" content="width=device-width,initial-scale=1">',
         f'<title>{e(title)}</title><meta name="description" content="{html.escape(desc)}"><meta name="color-scheme" content="light dark">',
         f'<link rel="icon" href="{up}icon.png?v={IV}"><link rel="apple-touch-icon" href="{up}icon.png?v={IV}"><link rel="stylesheet" href="{up}style.css">',
         f'<link rel="canonical" href="{BASE}{folder}{kind}">']
    for c, f, _ in ORDER: h.append(f'<link rel="alternate" hreflang="{HREFLANG[c]}" href="{BASE}{f}{kind}">')
    h.append(f'<link rel="alternate" hreflang="x-default" href="{BASE}{kind}"></head><body>')
    h.append(f'<header><div class="wrap bar"><a class="brand" href="{up}{folder}"><img src="{up}icon.png?v={IV}" alt=""><span>{e(t["name"])}</span></a><nav>')
    for k, lbl in nav: h.append(f'<a href="{up}{folder}{k}"{" class=on" if k == kind else ""}>{e(lbl)}</a>')
    h.append('</nav></div></header><main class="wrap">')
    if kind == '':
        h.append(f'<div class="hero"><img src="{up}icon.png?v={IV}" alt="{e(t["name"])}"><div><h1 style="margin:0">{e(t["name"])}</h1><p class="mut" style="font-size:1.2rem;margin:.2rem 0">{e(t["tag"])}</p></div></div>')
        h.append(f'<p>{e(t["lead"])}</p><ul class="f">' + ''.join(f'<li>{e(x)}</li>' for x in t['features']) + '</ul>')
        if STORE: h.append(f'<a class="btn" href="{STORE}">App Store</a>')
        h.append(f'<a class="btn o" href="privacy.html">{e(t["privacy"])}</a><a class="btn o" href="support.html">{e(t["support"])}</a>')
    elif kind == 'privacy.html':
        h.append(f'<h1>{e(t["priv_title"])}</h1><p class="mut">{e(t["updated"])}</p><p>{e(t["priv_intro"])}</p>')
        for hd, ps in t['sections']:
            h.append(f'<h2>{e(hd)}</h2>')
            for p in ps:
                p = e(p).replace('{unity}', f'<a href="{UNITY}" rel="noopener">{e(t["unity_label"])}</a>').replace('{mail}', f'<a href="mailto:{MAIL}">{MAIL}</a>')
                h.append(f'<p>{p}</p>')
    else:
        h.append(f'<h1>{e(t["sup_title"])}</h1><p>{e(t["sup_intro"])}</p><p><a class="btn" href="mailto:{MAIL}?subject=Junbi">{e(t["sup_mail"])}: {MAIL}</a></p><h2>{e(t["sup_faq"])}</h2>')
        for q, a in t['faq']: h.append(f'<details><summary>{e(q)}</summary><p>{e(a)}</p></details>')
        h.append(f'<p><a href="privacy.html">{e(t["more_priv"])}</a></p>')
    h.append('</main><footer><div class="wrap"><div class="langs">')
    for c, f, nm in ORDER: h.append(f'<a href="{up}{f}{kind}" hreflang="{HREFLANG[c]}">{e(nm)}</a>')
    h.append(f'</div>© 2026 Notemia · <a href="mailto:{MAIL}">{MAIL}</a></div></footer></body></html>')
    return ''.join(h)

if sys.argv[1:] == ['redirect']:
    for c, f, _ in ORDER:
        for kind in ('', 'privacy.html', 'support.html'):
            u = BASE + f + kind
            open(os.path.join(SITE, f, kind or 'index.html'), 'w', encoding='utf-8').write(f'<!doctype html><html lang="{HREFLANG[c]}"><head><meta charset="utf-8"><title>Junbi</title><link rel="canonical" href="{u}"><meta http-equiv="refresh" content="0; url={u}"><meta name="robots" content="noindex"></head><body><a href="{u}">{u}</a><script>location.replace({u!r}+location.hash)</script></body></html>')
    for x in ('sitemap.xml', 'robots.txt'):
        if os.path.exists(os.path.join(SITE, x)): os.remove(os.path.join(SITE, x))
    print('redirects to', BASE); sys.exit()
for c, f, _ in ORDER:
    os.makedirs(os.path.join(SITE, f), exist_ok=True)
    for kind in ('', 'privacy.html', 'support.html'):
        open(os.path.join(SITE, f, kind or 'index.html'), 'w', encoding='utf-8').write(page(c, f, kind))
open(os.path.join(SITE, 'style.css'), 'w').write(CSS)
shutil.copy(os.path.join(os.path.dirname(HERE), 'icon.png'), os.path.join(SITE, 'icon.png')) if os.path.abspath(SITE) != os.path.dirname(HERE) else None
open(os.path.join(SITE, '.nojekyll'), 'w').write('')
open(os.path.join(SITE, 'robots.txt'), 'w').write(f'User-agent: *\nAllow: /\nSitemap: {BASE}sitemap.xml\n')
urls = ''.join(f'<url><loc>{BASE}{f}{k}</loc></url>' for _, f, _ in ORDER for k in ('', 'privacy.html', 'support.html'))
open(os.path.join(SITE, 'sitemap.xml'), 'w').write(f'<?xml version="1.0" encoding="UTF-8"?><urlset xmlns="http://www.sitemaps.org/schemas/sitemap/0.9">{urls}</urlset>')
print('built', len(ORDER) * 3, 'pages')
