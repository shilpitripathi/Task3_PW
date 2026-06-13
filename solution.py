import pandas as pd
import zipfile
import os

# Create output folder
os.makedirs("output", exist_ok=True)

# Read Excel
df = pd.read_excel("metadata.xlsx")

# Open ZIP
with zipfile.ZipFile("images.zip", "r") as zip_file:

    files = zip_file.namelist()

    for _, row in df.iterrows():

        order = int(row["Display Order*"])

        question_file = row["Question Image"]

        solution_file = question_file.replace(
            "QUES_ENG_",
            "SOLU_ENG_"
        )

        # Extract Question
        if question_file in files:

            with zip_file.open(question_file) as src:

                with open(
                    f"output/Q{order}.png",
                    "wb"
                ) as dst:

                    dst.write(src.read())

        # Extract Solution
        if solution_file in files:

            with zip_file.open(solution_file) as src:

                with open(
                    f"output/S{order}.png",
                    "wb"
                ) as dst:

                    dst.write(src.read())

print("Done!")