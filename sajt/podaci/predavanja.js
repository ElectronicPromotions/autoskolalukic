/* =========================================================
   RASPORED PREDAVANJA  do  Autoškola Lukić
   ---------------------------------------------------------
   • Svaka grupa je jedan blok { ... } u listi "grupe".
   • Datum se piše kao "GGGG-MM-DD" (npr. "2026-11-18").
   • Vrijeme se piše kao "17:00 do 18:30".
   • Kandidate upisujte kao "Ime P." (ime + početno slovo prezimena)
      do  stranica je javna, pa je tako bolje za privatnost kandidata.
   • Kad upišete stvarni raspored, promijenite  primjer: true  u  primjer: false
   ========================================================= */
window.PREDAVANJA = {
  primjer: true,
  azurirano: "2026-11-17",
  napomena: "Predavanja se održavaju u učionici Autoškole Lukić, Tina Ujevića 8, Brčko. Molimo da dođete 10 minuta ranije i ponesete svesku i olovku.",

  grupe: [
    {
      naziv: "Grupa 1",
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
      ],
      kandidati: ["Kandidat 1", "Kandidat 2", "Kandidat 3", "Kandidat 4", "Kandidat 5", "Kandidat 6", "Kandidat 7", "Kandidat 8"]
    },
    {
      naziv: "Grupa 2",
      kategorija: "B",
      predavac: "Doc. dr Violeta Lukić Vujadinović",
      mjesto: "Učionica, Tina Ujevića 8",
      napomena: "Večernji termin  do  pogodno za zaposlene.",
      termini: [
        { datum: "2026-11-24", vrijeme: "19:00 do 20:30", tema: "Uvod u saobraćajne propise" },
        { datum: "2026-11-26", vrijeme: "19:00 do 20:30", tema: "Znakovi opasnosti" },
        { datum: "2026-11-30", vrijeme: "19:00 do 20:30", tema: "Znakovi izričitih naredbi" },
        { datum: "2026-12-02", vrijeme: "19:00 do 20:30", tema: "Prednost prolaza na raskrsnicama" }
      ],
      kandidati: ["Kandidat 9", "Kandidat 10", "Kandidat 11", "Kandidat 12", "Kandidat 13"]
    },
    {
      naziv: "Grupa 3",
      kategorija: "C, CE",
      predavac: "Doc. dr Violeta Lukić Vujadinović",
      mjesto: "Učionica, Tina Ujevića 8",
      napomena: "",
      termini: [
        { datum: "2026-12-01", vrijeme: "16:00 do 17:30", tema: "Propisi za teretna vozila" },
        { datum: "2026-12-03", vrijeme: "16:00 do 17:30", tema: "Tahograf, odmori i opterećenje" }
      ],
      kandidati: ["Kandidat 14", "Kandidat 15", "Kandidat 16"]
    }
  ]
};
