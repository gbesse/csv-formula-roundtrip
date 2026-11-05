# csv-formula-roundtrip

## Français

Tester un export CSV sans confondre texte et formule.

Données fictives ; aucun accès réseau ni secret requis.

```sh
python -m csv_formula_roundtrip examples/demo.json --lang fr
python -m unittest discover -s tests -v
```

### Méthode et différence

Écrit puis relit un vrai CSV ; distingue échappement CSV et neutralisation de préfixes interprétables comme formules, en signalant chaque cellule transformée.

### Limites

Tous les champs sont du texte ; apostrophe choisie peut être visible selon le tableur. Aucun Excel/LibreOffice exécuté, aucune garantie universelle contre injection.

### Validation

Tests de domaine, cas limites et interface FR/EN/ES. La CI teste Python 3.11/3.13 et exécute la wheel installée hors du checkout. JSON conserve les identifiants techniques et les données fournis. Erreur d’entrée : code de sortie 2.

## English

Test CSV export without confusing text and formulas.

Synthetic data; no network access or secret required.

```sh
python -m csv_formula_roundtrip examples/demo.json --lang en
python -m unittest discover -s tests -v
```

### Method and difference

Writes and rereads actual CSV; distinguishes CSV escaping from neutralizing formula-like prefixes and reports each transformed cell.

### Limits

All fields are text; chosen apostrophe may remain visible depending on spreadsheet. No Excel/LibreOffice execution or universal injection guarantee.

### Validation

Domain tests, boundary cases and FR/EN/ES interface. CI tests Python 3.11/3.13 and runs the installed wheel outside the checkout. JSON preserves technical identifiers and supplied data. Invalid input exits with code 2.

## Español

Probar exportación CSV sin confundir texto y fórmulas.

Datos sintéticos; no requiere red ni secretos.

```sh
python -m csv_formula_roundtrip examples/demo.json --lang es
python -m unittest discover -s tests -v
```

### Método y diferencia

Escribe y relee CSV real; distingue escape CSV de neutralización de prefijos de fórmulas e informa cada celda transformada.

### Límites

Todos los campos son texto; apóstrofo puede quedar visible según hoja de cálculo. Sin ejecutar Excel/LibreOffice ni garantía universal contra inyección.

### Validación

Pruebas de dominio, casos límite e interfaz FR/EN/ES. CI prueba Python 3.11/3.13 y ejecuta la wheel instalada fuera del repositorio. JSON conserva identificadores técnicos y datos proporcionados. Entrada inválida termina con código 2.

## Sources / Fuentes

- https://owasp.org/www-community/attacks/CSV_Injection
