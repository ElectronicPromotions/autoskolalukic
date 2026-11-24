/* =========================================================
   OBJAVE SA FACEBOOKA · Autoškola Lukić (stranica /novosti/)
   ---------------------------------------------------------
   Dva načina da se objava pojavi na sajtu:
   A) Prepišite tekst objave (najbolje za Google pretragu):
      { datum: "2026-11-17", naslov: "...", tekst: "...", slika: "/img/objave/ime.jpg", link: "https://www.facebook.com/..." }
   B) Samo zalijepite link javne Facebook objave, bez teksta:
      { datum: "2026-11-17", link: "https://www.facebook.com/.../posts/..." }
      Sajt tada prikazuje originalnu objavu sa Facebooka.
   Najnovije objave stavljajte NA VRH liste.
   Kad unesete prave objave, promijenite  primjer: true  u  primjer: false
   ========================================================= */
window.OBJAVE = {
  primjer: false,
  autor: "Doc. dr Violeta Lukić Vujadinović",
  // Objave sa Facebook stranice se prikazuju automatski (postavke.js → facebookStranica).
  // Ovdje dodajte samo objave koje želite i kao karticu na sajtu (vidi uputstvo iznad).
  objave: []
};
