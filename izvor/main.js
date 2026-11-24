(function () {
  var b = document.querySelector('.menu'), m = document.getElementById('mm');
  if (!b || !m) return;
  b.addEventListener('click', function () {
    var open = m.hasAttribute('hidden');
    if (open) m.removeAttribute('hidden'); else m.setAttribute('hidden', '');
    b.setAttribute('aria-expanded', open ? 'true' : 'false');
  });
  m.addEventListener('click', function (ev) {
    if (ev.target.tagName === 'A') { m.setAttribute('hidden', ''); b.setAttribute('aria-expanded', 'false'); }
  });
  document.addEventListener('keydown', function (ev) {
    if (ev.key === 'Escape' && !m.hasAttribute('hidden')) { m.setAttribute('hidden', ''); b.setAttribute('aria-expanded', 'false'); b.focus(); }
  });
})();

/* Facebook prozor: širina se šalje Facebooku prema stvarnoj širini okvira (telefon, tablet, računar) */
(function () {
  var fr = [].slice.call(document.querySelectorAll('iframe[data-fb]'));
  if (!fr.length) return;
  function set(f) {
    var w = Math.max(180, Math.min(500, Math.floor(f.parentNode.clientWidth)));
    var h = window.innerWidth <= 600 ? 560 : 640;
    if (f._w && Math.abs(f._w - w) < 30) return;
    f._w = w; f.height = h; f.style.height = h + 'px';
    f.src = 'https://www.facebook.com/plugins/page.php?href=' + f.getAttribute('data-fb') + '&tabs=timeline&width=' + w + '&height=' + h + '&small_header=true&adapt_container_width=true&hide_cover=false&show_facepile=false';
  }
  fr.forEach(set);
  var t; window.addEventListener('resize', function () { clearTimeout(t); t = setTimeout(function () { fr.forEach(set); }, 300); }, { passive: true });
})();
