import os
import json

import streamlit as st

from analyzer import analyze_job
from excel_manager import (
    EXCEL_FILE,
    STATUS_VALUES,
    save_analysis_to_excel,
)

st.set_page_config(
    page_title="AI Job Application Analyzer",
    page_icon="🔎",
    layout="wide"
)

st.title("AI Job Application Analyzer")
st.caption("KI-gestützte Analyse von Stellenanzeigen")

left_column, right_column = st.columns(2)


with left_column:
    st.subheader("Stellenanzeige")

    job_text = st.text_area(
        "Stellenanzeige einfügen:",
        height=500,
        placeholder="Füge hier den Text der Stellenanzeige ein ..."
    )

    if st.button(
        "Stellenanzeige analysieren",
        type="primary",
        use_container_width=True
    ):
        if job_text.strip():
            try:
                with st.spinner(
                    "Stellenanzeige wird analysiert ..."
                ):
                    result = analyze_job(job_text)

                st.session_state["analysis_result"] = result

                # Eingabefelder für eine neue Analyse zurücksetzen
                st.session_state["excel_status"] = "Nur analysiert"
                st.session_state["excel_link"] = ""
                st.session_state["excel_notes"] = ""

                if "excel_application_date" in st.session_state:
                    del st.session_state[
                        "excel_application_date"
                    ]

                st.success("Analyse erfolgreich.")

            except Exception as error:
                st.error(
                    f"Fehler bei der Analyse: {error}"
                )

        else:
            st.warning(
                "Bitte zuerst eine Stellenanzeige eingeben."
            )


with right_column:
    st.subheader("Analyseergebnis")

    result = st.session_state.get(
        "analysis_result"
    )

    if result:
        # ---------------------------------
        # Kurzüberblick
        # ---------------------------------

        st.markdown("### Kurzüberblick")

        st.markdown(
            f"**Unternehmen:** "
            f"{result.get('company') or 'Nicht angegeben'}"
        )

        st.markdown(
            f"**Position:** "
            f"{result.get('position') or 'Nicht angegeben'}"
        )

        st.markdown(
            f"**Standort:** "
            f"{result.get('location') or 'Nicht angegeben'}"
        )

        st.markdown("#### Muss-Anforderungen")

        must_have = result.get(
            "must_have_skills",
            []
        )

        if must_have:
            for item in must_have[:5]:
                st.write(f"- {item}")
        else:
            st.write("Nicht angegeben")

        st.markdown("#### Technologien")

        technical_skills = result.get(
            "technical_skills",
            []
        )

        if technical_skills:
            st.write(
                ", ".join(
                    technical_skills[:8]
                )
            )
        else:
            st.write("Nicht angegeben")

        st.markdown("#### Rahmenbedingungen")

        st.write(
            f"**Arbeitsmodell:** "
            f"{result.get('work_model') or 'Nicht angegeben'}"
        )

        st.write(
            f"**Arbeitszeit:** "
            f"{result.get('hours') or 'Nicht angegeben'}"
        )

        # ---------------------------------
        # Detaillierte Analyse
        # ---------------------------------

        with st.expander(
            "Detaillierte Analyse anzeigen"
        ):
            st.markdown("### Aufgaben")

            for item in result.get(
                "tasks",
                []
            ):
                st.write(f"- {item}")

            st.markdown(
                "### Muss-Anforderungen"
            )

            for item in result.get(
                "must_have_skills",
                []
            ):
                st.write(f"- {item}")

            st.markdown("### Nice-to-have")

            nice_to_have = result.get(
                "nice_to_have_skills",
                []
            )

            if nice_to_have:
                for item in nice_to_have:
                    st.write(f"- {item}")
            else:
                st.write("Keine angegeben")

            st.markdown(
                "### Technische Skills"
            )

            technical_skills = result.get(
                "technical_skills",
                []
            )

            st.write(
                ", ".join(technical_skills)
                if technical_skills
                else "Nicht angegeben"
            )

            st.markdown("### Soft Skills")

            soft_skills = result.get(
                "soft_skills",
                []
            )

            st.write(
                ", ".join(soft_skills)
                if soft_skills
                else "Nicht angegeben"
            )

            st.markdown(
                "### Weitere Angaben"
            )

            languages = result.get(
                "languages",
                []
            )

            st.write(
                "**Sprachen:** "
                + (
                    ", ".join(languages)
                    if languages
                    else "Nicht angegeben"
                )
            )

            st.write(
                f"**Arbeitsmodell:** "
                f"{result.get('work_model') or 'Nicht angegeben'}"
            )

            st.write(
                f"**Arbeitszeit:** "
                f"{result.get('hours') or 'Nicht angegeben'}"
            )

        # ---------------------------------
        # JSON Export
        # ---------------------------------

        json_data = json.dumps(
            result,
            ensure_ascii=False,
            indent=2
        )

        st.download_button(
            label="JSON herunterladen",
            data=json_data,
            file_name="job_analysis.json",
            mime="application/json",
            use_container_width=True
        )

        # ---------------------------------
        # Excel-Historie
        # ---------------------------------

        st.divider()

        st.markdown(
            "### Excel-Historie"
        )

        st.caption(
            "Analyse zusammen mit "
            "Bewerbungsinformationen speichern."
        )

        bewerbungsstatus = st.selectbox(
            "Bewerbungsstatus:",
            options=STATUS_VALUES,
            key="excel_status"
        )

        # Bewerbungsdatum nur anzeigen,
        # wenn bereits eine Bewerbung existiert
        status_with_application_date = [
            "Beworben",
            "Interview",
            "Absage",
            "Zusage",
        ]

        bewerbungsdatum = None

        if (
            bewerbungsstatus
            in status_with_application_date
        ):
            bewerbungsdatum = st.date_input(
                "Bewerbungsdatum:",
                key="excel_application_date"
            )

        stellenlink = st.text_input(
            "Stellenlink:",
            placeholder=(
                "https://unternehmen.de/stellenanzeige"
            ),
            key="excel_link"
        )

        notizen = st.text_area(
            "Notizen:",
            placeholder=(
                "z. B. gute Passung, "
                "fehlender Skill, Interview vorbereiten ..."
            ),
            height=100,
            key="excel_notes"
        )

        if st.button(
            "Analyse in Excel speichern",
            use_container_width=True
        ):
            try:
                analysis_id = save_analysis_to_excel(
                    result=result,
                    bewerbungsstatus=bewerbungsstatus,
                    bewerbungsdatum=bewerbungsdatum,
                    stellenlink=stellenlink.strip(),
                    notizen=notizen.strip()
                )

                st.success(
                    "Analyse wurde erfolgreich "
                    "in Excel gespeichert. "
                    f"Analyse-ID: {analysis_id}"
                )

            except PermissionError:
                st.error(
                    "Die Excel-Datei ist vermutlich "
                    "noch in Microsoft Excel geöffnet. "
                    "Bitte die Datei schließen und "
                    "erneut speichern."
                )

            except Exception as error:
                st.error(
                    "Fehler beim Speichern in Excel: "
                    f"{error}"
                )

                  
        if st.button(
            "Excel-Datei öffnen",
            use_container_width=True
        ):
            try:
                if EXCEL_FILE.exists():
                    os.startfile(str(EXCEL_FILE.resolve()))
                    

                    st.info(
                        "Excel-Datei wurde geöffnet."
                    )

                else:
                    st.warning(
                        "Die Excel-Datei existiert noch nicht."
                    )

            except Exception as error:
                st.error(
                    "Excel-Datei konnte nicht geöffnet werden: "
                    f"{error}"
                )
    else:
        st.info(
            "Nach der Analyse wird das "
            "strukturierte Ergebnis hier angezeigt."
        )