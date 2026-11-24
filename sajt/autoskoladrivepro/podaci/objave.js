/* =========================================================
   OBJAVE · Autoškola DrivePro (stranica /novosti/)
   ---------------------------------------------------------
   Dva načina da se objava pojavi na sajtu:
   A) Prepišite tekst objave (najbolje za Google pretragu):
      { datum: "2026-11-20", naslov: "...", tekst: "...", slika: "/autoskoladrivepro/img/objave/ime.jpg", link: "https://www.instagram.com/p/..." }
   B) Samo zalijepite link javne Facebook objave, bez teksta:
      { datum: "2026-11-20", link: "https://www.facebook.com/.../posts/..." }
      Sajt tada prikazuje originalnu objavu sa Facebooka.
   Najnovije objave stavljajte NA VRH liste.
   Dok je lista prazna, na sajtu se automatski prikazuju objave sa Facebook stranice (postavke.js).
   Dok je  primjer: true  objave se ne prikazuju na početnoj stranici,
   a na /novosti/ stoji oznaka da su to primjeri.
   Kad unesete prave objave, promijenite  primjer: true  u  primjer: false
   ========================================================= */
window.OBJAVE = {
  primjer: false,
  autor: "Autoškola DrivePro",
  objave: []
};
