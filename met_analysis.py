"""
Analysis of Mentor Evaluation Tool Data for Psychology Summer Institute
"""

import matplotlib.pyplot as plt
import pandas as pd
from radar import radar_factory


TOOL = [ 
    "My mentor is accessible.",
    "My mentor is an active listener.",
    "My mentor demonstrates professional expertise.",
    "My mentor encourages me to establish an independent career.",
    "My mentor provides useful critiques of my work.",
    "My mentor motivates me to improve my work.",
    "My mentor is helpful in providing direction and guidance on professional issues.",
    "My mentor acknowledges my contributions appropriately.",
    "My mentor takes a sincere interest in my career.",
    "My mentor helps me to formulate clear goals.",
    "My mentor facilitates building my professional network.",
    "My mentor provides thoughtful advice on my scholarly work.",
    "My mentor is supportive of work-life balance.",
    "Overall, I'm satisfied with my mentor.",
]
MEETING_COMMUNICATION = [
    "My mentor is accessible.",
    "My mentor is an active listener.",
    "Overall, I'm satisfied with my mentor.",
]
EXPECTATIONS_FEEDBACK = [
    "My mentor is an active listener.",
    "My mentor provides useful critiques of my work.",
    "My mentor acknowledges my contributions appropriately.",
    "My mentor provides thoughtful advice on my scholarly work.",
    "Overall, I'm satisfied with my mentor.",
]
RESEARCH_SUPPORT = [
    "My mentor demonstrates professional expertise.",
    "My mentor provides useful critiques of my work.",
    "My mentor motivates me to improve my work.",
    "My mentor provides thoughtful advice on my scholarly work.",
    "Overall, I'm satisfied with my mentor.",
]
CAREER_DEVELOPMENT = [
    "My mentor encourages me to establish an independent career.",
    "My mentor is helpful in providing direction and guidance on professional issues.",
    "My mentor acknowledges my contributions appropriately.",
    "My mentor helps me to formulate clear goals.",
    "My mentor facilitates building my professional network.",
    "Overall, I'm satisfied with my mentor.",
]
PSYCHOSOCIAL_SUPPORT = [
    "My mentor takes a sincere interest in my career.",
    "My mentor is supportive of work-life balance.",
    "Overall, I'm satisfied with my mentor.",
]

DOMAINS = [
    "Meetings and communication",
    "Expectations and feedback",
    "Career development",
    "Research support",
    "Psychosocial support",
]
DOMAIN_VARS = [
    MEETING_COMMUNICATION,
    EXPECTATIONS_FEEDBACK,
    RESEARCH_SUPPORT,
    CAREER_DEVELOPMENT,
    PSYCHOSOCIAL_SUPPORT,
]

folder = "C:\\Users\\Sexg\\Documents\\PSI\\2024\\Survey Analysis\\Pre-Post Analysis\\"
excel_file = "MET Pilot Results.xlsx"
filepath = f"{folder}{excel_file}"
output = "output.xlsx"
output_path = f"{folder}{output}"

def score_analyzer(filename: str, analyzed_file: str):
    df = pd.read_excel(filename, sheet_name="MET Pilot Results", header=0)
    
    score_df = df[TOOL] + 4
    all_scores = score_df.mean()

    web_df = score_df
    for d, v in zip(DOMAINS, DOMAIN_VARS):
        web_df[d] = web_df[v].mean(axis=1)
    summary = web_df[DOMAINS].mean()

    with pd.ExcelWriter(f"{analyzed_file}") as writer:
        summary.to_excel(writer, sheet_name="summary")
        all_scores.to_excel(writer, sheet_name="all scores")

def score_data(filename: str):
    df = pd.read_excel(filename, sheet_name="MET Pilot Results", header=0)

    score_df = df[TOOL] + 4
    web_df = pd.DataFrame()
    for d, v in zip(DOMAINS, DOMAIN_VARS):
        web_df[d] = score_df[v].mean(axis=1)
    web_df = web_df.mean()
    
    return web_df

if __name__ == "__main__":
    #score_analyzer(filepath, output_path)

    df = score_data(filepath) + 4
    N = len(df)
    theta = radar_factory(N, frame="polygon")
    spoke_lables = DOMAINS

    fig, ax = plt.subplots(
        #figsize=(9, 9),
        nrows=1,
        ncols=1,
        subplot_kw=dict(projection="radar")
    )
    ax.set_title(
        "Mentor Evaluation at PSI",
        weight="bold",
        size="medium",
        horizontalalignment="center",
        verticalalignment="center",
    )
    ax.plot(theta, df)
    ax.set_varlabels(spoke_lables)
    plt.savefig(f"{folder}MentorEvaluationPSI.png")