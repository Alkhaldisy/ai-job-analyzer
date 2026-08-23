\# AI Job Application Analyzer



Eine kleine Python-Anwendung, die unstrukturierte Stellenanzeigen mithilfe von KI analysiert, wichtige Informationen strukturiert aufbereitet und die Ergebnisse für eine spätere Weiterverarbeitung und Bewerbungsverwaltung nutzbar macht.







\## Demo



\### KI-Analyse und Kurzüberblick



!\[AI Job Application Analyzer](assets/app-demo.png)



\### Excel-Historie und Bewerbungs-Tracking



!\[Excel-Historie und Bewerbungs-Tracking](assets/app-demo2.png)



\### Excel-Historie – Übersicht



!\[Excel-Historie Übersicht](assets/excel-demo.png)



\### Excel-Historie – Job-Details



!\[Excel-Historie Job-Details](assets/excel-demo2.png)







\## Problem



Stellenanzeigen enthalten viele relevante Informationen in unstrukturierter Form:



\* Aufgaben

\* Muss- und Kann-Anforderungen

\* technische Skills

\* Soft Skills

\* Arbeitsmodell

\* Arbeitszeit

\* Sprachkenntnisse



Bei mehreren Stellenanzeigen wird die manuelle Analyse schnell unübersichtlich. Zusätzlich gehen bereits analysierte Stellen häufig wieder verloren oder müssen separat dokumentiert werden.



\## Lösung



Der AI Job Application Analyzer kombiniert KI-basierte Informationsextraktion mit einer einfachen Bewerbungs-Historie.



Der Workflow:



```text

Stellenanzeige

&#x20;     ↓

KI-Analyse

&#x20;     ↓

strukturierte Daten

&#x20;     ↓

Kurzüberblick

&#x20;     ↓

Detaillierte Analyse

&#x20;     ↓

Excel-Historie + Bewerbungs-Tracking

```



Die KI analysiert den Text der Stellenanzeige und gibt die Informationen in einer festen JSON-Struktur zurück.



Die Ergebnisse werden anschließend:



1\. kompakt in der Weboberfläche dargestellt,

2\. bei Bedarf vollständig angezeigt,

3\. als JSON exportiert,

4\. zusammen mit Bewerbungsinformationen in einer Excel-Historie gespeichert.



\## Funktionen



\### KI-basierte Stellenanalyse



Die Anwendung extrahiert unter anderem:



\* Unternehmen

\* Position

\* Standort

\* Aufgaben

\* Muss-Anforderungen

\* Nice-to-have-Anforderungen

\* technische Skills

\* Soft Skills

\* Sprachen

\* Arbeitsmodell

\* Arbeitszeit

\* fehlende oder unklare Informationen



\### Kurzüberblick



Damit die KI-Ausgabe nicht genauso umfangreich wie die ursprüngliche Stellenanzeige wird, zeigt die Anwendung zuerst nur die wichtigsten Informationen:



\* Unternehmen

\* Position

\* Standort

\* wichtigste Muss-Anforderungen

\* wichtigste Technologien

\* Arbeitsmodell

\* Arbeitszeit



Die vollständige Analyse kann anschließend über einen aufklappbaren Bereich angezeigt werden.



\### Strukturierte JSON-Ausgabe



Die Analyse wird intern als strukturierte Python-Datenstruktur verarbeitet und kann als JSON-Datei exportiert werden.



Dadurch können die Ergebnisse später auch von anderen Anwendungen oder Automatisierungs-Workflows weiterverarbeitet werden.



\### Excel-Historie



Analysen können in einer lokalen Excel-Datei gespeichert werden:



```text

job\_analysis\_history.xlsx

```



Die Datei enthält zwei Bereiche:



\#### Übersicht



Jede analysierte Stelle wird als eine Zeile gespeichert.



Enthalten sind unter anderem:



\* Analyse-ID

\* Analyse-Datum

\* Unternehmen

\* Position

\* Standort

\* wichtigste Anforderungen

\* Technologien

\* Arbeitsmodell

\* Arbeitszeit

\* Bewerbungsstatus

\* Bewerbungsdatum

\* Stellenlink

\* Notizen



\#### Job-Details



Für jede Stelle werden zusätzlich die vollständigen Analyseergebnisse gespeichert.



Über den Link:



```text

Details öffnen

```



kann direkt von der Übersicht zur vollständigen Analyse einer Stelle gewechselt werden.



Ein Rücklink führt wieder zur entsprechenden Stelle in der Übersicht.



\### Bewerbungs-Tracking



Zusätzlich zur KI-Analyse können manuell Informationen zum Bewerbungsprozess ergänzt werden.



Unterstützte Status:



```text

Nur analysiert

Interessant

Bewerbung geplant

Beworben

Interview

Absage

Zusage

```



Zusätzlich können gespeichert werden:



\* Bewerbungsdatum

\* Stellenlink

\* persönliche Notizen



Damit dient die Excel-Datei nicht nur als Export, sondern als einfache Bewerbungs-Historie.



\## Technischer Ablauf



```text

Stellenanzeige

&#x20;     ↓

Streamlit UI

&#x20;     ↓

analyze\_job()

&#x20;     ↓

OpenAI API

&#x20;     ↓

JSON

&#x20;     ↓

Python Dictionary

&#x20;     ↓

┌─────────────────────────────┐

│ Kurzüberblick               │

│ Detaillierte Analyse        │

│ JSON Export                 │

│ Excel-Historie              │

└─────────────────────────────┘

```



\## Projektstruktur



```text

ai-job-analyzer/

│

├── app.py

├── analyzer.py

├── excel\_manager.py

├── requirements.txt

├── .env.example

├── .gitignore

├── README.md

│

└── examples/

&#x20;   └── sample\_job.txt

```



\### `app.py`



Enthält die Streamlit-Benutzeroberfläche und verbindet die einzelnen Komponenten.



\### `analyzer.py`



Enthält die KI-Logik:



\* Prompt

\* OpenAI-API-Aufruf

\* JSON-Verarbeitung

\* Fehlerbehandlung



\### `excel\_manager.py`



Verantwortlich für:



\* Erstellen der Excel-Historie

\* automatische Analyse-IDs

\* Analyse-Datum

\* Übersicht

\* Job-Details

\* Status-Dropdown

\* interne Excel-Hyperlinks

\* Stellenlinks



\## Tech Stack



\* Python

\* Streamlit

\* OpenAI API

\* JSON

\* openpyxl

\* python-dotenv

\* Git / GitHub



\## Installation



Repository klonen:



```bash

git clone <REPOSITORY-URL>

cd ai-job-analyzer

```



Virtuelle Python-Umgebung erstellen:



```bash

python -m venv .venv

```



Unter Windows aktivieren:



```powershell

.\\.venv\\Scripts\\Activate.ps1

```



Dependencies installieren:



```bash

pip install -r requirements.txt

```



\## API-Key konfigurieren



Die Datei:



```text

.env.example

```



zeigt die benötigte Umgebungsvariable:



```text

OPENAI\_API\_KEY=your\_api\_key\_here

```



Eine lokale Datei `.env` erstellen und dort den eigenen API-Key eintragen:



```text

OPENAI\_API\_KEY=...

```



Die `.env`-Datei wird über `.gitignore` nicht in Git gespeichert.



\## Anwendung starten



```bash

streamlit run app.py

```



Anschließend öffnet sich die Anwendung lokal im Browser.



\## Verwendung



1\. Stellenanzeige in das Textfeld einfügen.

2\. `Stellenanzeige analysieren` auswählen.

3\. Kurzüberblick prüfen.

4\. Bei Bedarf die detaillierte Analyse öffnen.

5\. Optional das Ergebnis als JSON herunterladen.

6\. Bewerbungsstatus, Link und Notizen ergänzen.

7\. `Analyse in Excel speichern` auswählen.

8\. Die Historie kann anschließend direkt aus der lokalen Anwendung geöffnet werden.



\## Datenschutz und lokale Dateien



Folgende Dateien werden bewusst nicht in Git gespeichert:



```text

.env

.venv/

\_\_pycache\_\_/

job\_analysis\_history.xlsx

```



Dadurch bleiben insbesondere der API-Key und die persönliche Bewerbungs-Historie lokal.



\## Grenzen des aktuellen MVP



Die Anwendung ist bewusst als kleines MVP umgesetzt.



Aktuelle Einschränkungen:



\* KI-Ergebnisse sollten bei wichtigen Entscheidungen manuell geprüft werden.

\* Stellenanzeigen werden aktuell als Text eingefügt und nicht automatisch über eine URL geladen.

\* Die Excel-Historie ist für lokale Einzelbenutzung ausgelegt.

\* Das direkte Öffnen der Excel-Datei ist aktuell für die lokale Windows-Version vorgesehen.

\* Eine automatische Duplikaterkennung für bereits gespeicherte Stellen ist noch nicht implementiert.



\## Mögliche Weiterentwicklung



Die strukturierte Ausgabe wurde bewusst so aufgebaut, dass weitere Automatisierung möglich ist.



Mögliche nächste Schritte:



\* Übergabe der JSON-Daten an einen n8n-Workflow

\* Speicherung der Ergebnisse in Airtable

\* automatische Verarbeitung von Stellenlinks

\* Vergleich einer Stellenanzeige mit einem Bewerberprofil oder Lebenslauf

\* Skill-Gap-Analyse

\* Vergleich mehrerer analysierter Stellen

\* zentrale Datenbank anstelle einer lokalen Excel-Datei



Ein möglicher späterer Workflow könnte beispielsweise so aussehen:



```text

Stellenanzeige

&#x20;     ↓

KI-Analyse

&#x20;     ↓

strukturierte JSON-Daten

&#x20;     ↓

n8n

&#x20;     ↓

Airtable / Reporting / weitere Prozesse

```



\## Motivation



Das Projekt entstand aus einem wiederkehrenden manuellen Prozess: Stellenanzeigen lesen, relevante Anforderungen identifizieren, Informationen strukturieren und interessante Stellen separat dokumentieren.



Ziel war deshalb nicht nur, ein Sprachmodell aufzurufen, sondern den gesamten Prozess in kleinere Schritte zu zerlegen und die KI-Ausgabe anschließend für weitere Prozesse nutzbar zu machen.



Der Schwerpunkt liegt damit auf:



```text

Prozess verstehen

&#x20;     ↓

strukturieren

&#x20;     ↓

KI einsetzen

&#x20;     ↓

Ergebnisse weiterverwenden

```



