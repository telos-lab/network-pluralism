from network_pluralism.setup.paths import PREPROCESSED_DATA_DECISIONS

import json


def get_panels_of_court(court):
    with open(
        PREPROCESSED_DATA_DECISIONS / f"court_structure.json",
        "r",
    ) as f:
        s = json.load(f)
    return list(s[court].keys())


def get_decision_ids(institution: str):
    """Returning a set of decisions for a specific institution"""
    with open(
        PREPROCESSED_DATA_DECISIONS / f"court_structure.json",
        "r",
    ) as f:
        s = json.load(f)

    decisions = []
    if institution in s.keys():  # Institution is a court
        for p in get_panels_of_court(institution):
            decisions.extend(list(s[institution][p].keys()))
    else:
        for court, panel_data in s.items():
            for panel, d in panel_data.items():
                if panel == institution:
                    decisions.extend(d.keys())
    return decisions


def get_decision_ids_for_institutions(instutions: list[str]):
    decisions = []
    for panel in instutions:
        print(panel)
        decisions.extend(get_decision_ids(panel))
    return decisions


def get_paragraph_ids(institution: str):
    """Returning a set of decisions for a specific institution"""
    with open(
        PREPROCESSED_DATA_DECISIONS / f"court_structure.json",
        "r",
    ) as f:
        s = json.load(f)

    paragraphs = []
    if institution in s.keys():  # Institution is a court
        for p in get_panels_of_court(institution):
            for d, paras in s[institution][p].items():
                paragraphs.extend(list(paras.keys()))
    else:
        for court, panel_data in s.items():
            for panel, d in panel_data.items():
                if panel == institution:
                    for d, paras in s[court][panel].items():
                        paragraphs.extend(list(paras.keys()))
    return paragraphs


def get_paragraph_ids_for_institutions(instutions: list[str]):
    paragraphs = []
    for panel in instutions:
        print(panel)
        paragraphs.extend(get_paragraph_ids(panel))
    return paragraphs
