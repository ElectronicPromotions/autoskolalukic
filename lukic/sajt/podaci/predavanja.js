/* =========================================================
   RASPORED PREDAVANJA: Autoškola Lukić
   ---------------------------------------------------------
   • Svaka grupa je jedan blok { ... } u listi "grupe".
   • Javno se prikazuju: grupa, škola, kategorija, termini,
     teme, predavač i mjesto. Spiskovi kandidata se NE objavljuju.
   • Datum se piše kao "GGGG-MM-DD" (npr. "2026-11-18").
   • Vrijeme se piše kao "17:00 do 18:30".
   • OTKAZAN termin:    dodajte  status: "otkazano"
   • PROMIJENJEN termin: dodajte status: "promijenjeno", napomena: "šta je promijenjeno"
   • Obavještenje na vrhu rasporeda: upišite tekst u listu "obavjestenja".
   • Kad upišete stvarni raspored, promijenite  primjer: true  u  primjer: false
   ========================================================= */
window.PREDAVANJA = {
  primjer: true,
  azurirano: "2026-11-19",
  napomena: "Predavanja se održavaju u učionici Autoškole Lukić, Tina Ujevića 8, Brčko. Molimo da dođete 10 minuta ranije i ponesete svesku i olovku.",
  obavjestenja: [],

  grupe: [
    {
      naziv: "Grupa 1",
      skola: "Autoškola Lukić",
      kategorija: "B",
      predavac: "Doc. dr Violeta Lukić Vujadinović",
      mjesto: "Učionica, Tina Ujevića 8",
      napomena: "",
      termini: [
        { datum: "2026-11-11", vrijeme: "17:00 do 18:30", tema: "Uvod u saobraćajne propise" },
        { datum: "2026-11-13", vrijeme: "17:00 do 18:30", tema: "Znakovi opasnosti" },
        { datum: "2026-11-16", vrijeme: "17:00 do 18:30", tema: "Znakovi izričitih naredbi" },
        { datum: "2026-11-18", vrijeme: "17:00 do 18:30", tema: "Prednost prolaza na raskrsnicama" },
        { datum: "2026-11-20", vrijeme: "17:00 do 18:30", tema: "Brzina, rastojanje i preticanje" },
        { datum: "2026-11-23", vrijeme: "17:00 do 18:30", tema: "Probni test i ponavljanje" }
      ]
    },
    {
      naziv: "Grupa 2",
      skola: "Autoškola Lukić",
      kategorija: "B",
      predavac: "Doc. dr Violeta Lukić Vujadinović",
      mjesto: "Učionica, Tina Ujevića 8",
      napomena: "",
      termini: [
        { datum: "2026-11-24", vrijeme: "19:00 do 20:30", tema: "Uvod u saobraćajne propise" },
        { datum: "2026-11-26", vrijeme: "19:00 do 20:30", tema: "Znakovi opasnosti", status: "promijenjeno", napomena: "Primjer: termin pomjeren sa 18:00 na 19:00." },
        { datum: "2026-11-30", vrijeme: "19:00 do 20:30", tema: "Znakovi izričitih naredbi", status: "otkazano", napomena: "Primjer: termin otkazan, nadoknada će biti naknadno objavljena." },
        { datum: "2026-12-02", vrijeme: "19:00 do 20:30", tema: "Prednost prolaza na raskrsnicama" }
      ]
    },
    {
      naziv: "Grupa 3",
      skola: "Autoškola Lukić",
      kategorija: "C, CE",
      predavac: "Doc. dr Violeta Lukić Vujadinović",
      mjesto: "Učionica, Tina Ujevića 8",
      napomena: "",
      termini: [
        { datum: "2026-12-01", vrijeme: "16:00 do 17:30", tema: "Propisi za teretna vozila" },
        { datum: "2026-12-03", vrijeme: "16:00 do 17:30", tema: "Tahograf, odmori i opterećenje" }
      ]
    }
  ]
};
