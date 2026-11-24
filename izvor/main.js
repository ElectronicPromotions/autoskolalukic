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
