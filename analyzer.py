import json
import os

from dotenv import load_dotenv
from openai import OpenAI


load_dotenv()

api_key = os.getenv("OPENAI_API_KEY")

if not api_key:
    raise ValueError(
        "OPENAI_API_KEY wurde nicht gefunden. "
        "Bitte trage den API-Key in die .env-Datei ein."
    )

client = OpenAI(api_key=api_key)


def analyze_job(job_text):
    prompt = f"""
Du analysierst deutsche Stellenanzeigen.

Extrahiere ausschließlich Informationen, die tatsächlich
in der Stellenanzeige enthalten sind.

Gib ausschließlich gültiges JSON zurück.
Keine zusätzlichen Erklärungen und keinen Markdown-Codeblock.

Verwende genau diese Struktur:

{{
    "company": null,
    "position": null,
    "location": null,
    "tasks": [],
    "must_have_skills": [],
    "nice_to_have_skills": [],
    "technical_skills": [],
    "soft_skills": [],
    "languages": [],
    "work_model": null,
    "hours": null,
    "missing_or_unclear": []
}}

Regeln:

- Erfinde keine Informationen.
- Verwende ausschließlich Informationen, die aus der Stellenanzeige hervorgehen.
- Fehlende einzelne Angaben werden als null ausgegeben.
- Fehlende Listen werden als leere Liste [] ausgegeben.

- Trenne Aufgaben klar von Anforderungen.
- Trenne Muss-Anforderungen von optionalen Anforderungen.
- Anforderungen mit Formulierungen wie "von Vorteil", "wünschenswert",
  "idealerweise" oder vergleichbaren Formulierungen gehören zu
  "nice_to_have_skills".

- Unter "technical_skills" nur konkret genannte Technologien, Tools,
  Plattformen oder technische Kenntnisse aufnehmen.
- Technische Skills nur aufnehmen, wenn sie ausdrücklich im Text vorkommen.
- Keine allgemeinen Tätigkeiten oder Prozessbeschreibungen wie
  Prozessdigitalisierung, Workflow-Automatisierung oder Prozessoptimierung
  als technische Skills ergänzen.

- Unter "soft_skills" nur Soft Skills aufnehmen, die ausdrücklich als
  Anforderung an die Bewerberin oder den Bewerber formuliert sind.
- Keine zusätzlichen Soft Skills aus Aufgaben, Rollenbeschreibungen,
  Benefits oder allgemeinen Aussagen über die Stelle ableiten.

- Sprachkenntnisse nur aufnehmen, wenn eine Sprache ausdrücklich genannt wird.
- Nicht allein aus der Sprache der Stellenanzeige auf geforderte
  Sprachkenntnisse schließen.

- Unter "work_model" nur ausdrücklich genannte Angaben wie Homeoffice,
  Remote, Hybrid, mobiles Arbeiten oder Vor-Ort-Arbeit aufnehmen.
- Unter "hours" nur ausdrücklich genannte Angaben zur Arbeitszeit oder
  Wochenstundenzahl aufnehmen.

- "missing_or_unclear" darf ausschließlich fehlende oder unklare Angaben
  zu folgenden Feldern enthalten:
  company, position, location, tasks, must_have_skills,
  nice_to_have_skills, technical_skills, soft_skills,
  languages, work_model und hours.

- Keine fehlenden Informationen zu zusätzlichen Kategorien wie Gehalt,
  Benefits, Vertragsart, Starttermin, Beschäftigungsdauer,
  Urlaub oder Bewerbungsprozess in "missing_or_unclear" aufnehmen.

- Keine zusätzlichen Kategorien oder JSON-Felder erzeugen.
- Verwende genau die vorgegebene JSON-Struktur.Stellenanzeige:

{job_text}
"""

    response = client.responses.create(
        model="gpt-5.6-luna",
        input=prompt
    )

    raw_text = response.output_text.strip()

    try:
        return json.loads(raw_text)
    except json.JSONDecodeError as error:
        raise ValueError(
            "Die KI hat kein gültiges JSON zurückgegeben."
        ) from error