# Autoškole Brčko (autoskolebrcko.vercel.app, kasnije pravi domen)

Jedan sajt, jedan domen:
- `/`: zajednička početna Autoškole Brčko
- `/autoskolalukic/`: cijeli sajt Autoškole Lukić
- `/autoskoladrivepro/`: cijeli sajt Autoškole DrivePro

Folderi:
- `sajt/`: gotov sajt za objavu (Vercel čita `vercel.json`, izlaz je `sajt/`).
- `izvor/`: generator zajedničkog dijela. Podaci o školama su u `izvor/build.py` (SKOLE, TIM, KATEGORIJE).
- `lukic/`: izvor i gotov sajt Autoškole Lukić.
- `drivepro/`: izvor i gotov sajt Autoškole DrivePro (uputstvo u `drivepro/UPUTSTVO.md`).

Izmjene:
1. Lukić: `cd lukic/izvor && python3 build.py`; DrivePro: `cd drivepro/izvor && python3 build.py`
2. Sve zajedno: `cd izvor && python3 build.py`. Ovo pravi zajedničku početnu, pa kopira sajtove škola u `sajt/autoskolalukic/` i `sajt/autoskoladrivepro/` i sve njihove linkove prebacuje pod te putanje.

Podaci škola za zajedničku početnu (adresa, telefoni, kategorije, Facebook) su u `izvor/build.py`, rječnik `SKOLE`.

Domen: glavna adresa je u `izvor/build.py` (DOMAIN). Sada je https://autoskolebrcko.vercel.app; kad se kupi pravi domen, promijeniti DOMAIN i ponovo pokrenuti build.
