from pathlib import Path
from network_pluralism.setup.paths import (
    COMPUTATION_PATH,
    PREPROCESSED_DATA_DECISIONS,
    PREPROCESSED_DATA_STATUTES,
)
import pandas as pd


def load_look_up_tables():
    global all_elements_DF, all_elements_df_UUID_INDEX, all_elements_df_item_INDEX
    if Path.exists(COMPUTATION_PATH / "ids.pkl"):
        # Load all elements
        all_elements_DF = pd.read_pickle(COMPUTATION_PATH / "ids.pkl")
        all_elements_df_UUID_INDEX = all_elements_DF.set_index("UUID")
        all_elements_df_item_INDEX = all_elements_DF.set_index("item")

    global well_written_sections, law_names_df
    well_written_sections_path = PREPROCESSED_DATA_STATUTES / "written_sections.pkl"
    if well_written_sections_path.exists():
        well_written_sections = pd.read_pickle(well_written_sections_path)
        well_written_sections.set_index("sem_id", inplace=True)
        law_names_df = pd.read_csv(PREPROCESSED_DATA_STATUTES / "law_names_written.csv")
        law_names_df["short_sem_id"] = law_names_df["sem_id"].apply(
            lambda x: x.split("_")[0]
        )
        law_names_df.set_index("short_sem_id", inplace=True)

load_look_up_tables()

def get_well_written_section(item, language: str = "de"):
    row = well_written_sections.loc[item]

    return f"{row[f'written_{language}']} {row['law_name']}".strip()

def get_statute_name_for_sem_id(item, language: str = "de"):
    row = well_written_sections.loc[item]

    return f"{row['law_name']}".strip()


def get_well_written_sections(items, language: str = "de"):
    if items[0] in law_names_df.index:
        print(
            "Inside get_well_written_sections, but detected statute name. Calling get_statutes_names()"
        )
        return get_statutes_names(items)
    rows = well_written_sections.loc[items]
    written_sections = {
        index: f"{row[f'written_{language}']} {row['law_name']}".strip()
        for index, row in rows.iterrows()
    }
    for k, v in written_sections.items():
        if not (v.startswith("§") or v.startswith("Section")):
            written_sections[k] = f"Art. {v}" if language == "de" else f"Article {v}"
    return written_sections


def get_statute_name(sem_id):
    try:
        rows = law_names_df.loc[sem_id, "written"]
    except KeyError:
        print('key error')
        return get_statute_name(sem_id.split("_")[0])
    if not isinstance(rows, str):
        return rows.loc[~rows.index.duplicated(keep="first")].iloc[0]
    return rows


def get_statutes_names(sem_ids):
    # TODO: Fix the line below
    sem_ids = [s.split("_")[0] for s in sem_ids]
    rows = law_names_df.loc[sem_ids]
    rows = rows.loc[~rows.index.duplicated(keep="first")]
    written_statutes = {index: row["written"].strip() for index, row in rows.iterrows()}
    return written_statutes
