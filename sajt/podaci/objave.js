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
  primjer: true,
  autor: "Doc. dr Violeta Lukić Vujadinović",
  objave: [
    {
      datum: "2026-11-17",
      naslov: "Primjer objave: upis nove grupe za B kategoriju",
      tekst: "Ovako će izgledati Violetina objava na sajtu.\nOvdje ide tekst objave sa Facebooka, na primjer obavještenje o upisu nove grupe, terminima predavanja ili čestitka kandidatima koji su položili.\n\nUpis i informacije: 065 537 043.",
      slika: "/img/galerija/teoretska-nastava-ucionica.webp",
      link: ""
    },
    {
      datum: "2026-11-10",
      naslov: "Primjer objave: čestitamo novim vozačima!",
      tekst: "Primjer objave sa fotografijom kandidata koji su položili vozački ispit. Zamijenite ovaj tekst stvarnom objavom.",
      slika: "/img/galerija/kandidati-ispred-skolskog-automobila.webp",
      link: ""
    }
  ]
};
