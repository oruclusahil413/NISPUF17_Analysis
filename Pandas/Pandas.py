def proportion_of_education():
    import pandas as pd
    df = pd.read_csv("assets/NISPUF17.csv")
    education_of_moms = df["EDUC1"]

    av = len(education_of_moms)

    last = {
        "less than high school": (education_of_moms == 1).sum() / av,
        "high school": (education_of_moms == 2).sum() / av,
        "more than high school but not college": (education_of_moms == 3).sum() / av,
        "college": (education_of_moms == 4).sum() / av
    }
    return last

    assert type(proportion_of_education()) == type({}), "You must return a dictionary."


assert len(proportion_of_education()) == 4, "You have not returned a dictionary with four items in it."
assert "less than high school" in proportion_of_education().keys(), "You have not returned a dictionary with the correct keys."
assert "high school" in proportion_of_education().keys(), "You have not returned a dictionary with the correct keys."
assert "more than high school but not college" in proportion_of_education().keys(), "You have not returned a dictionary with the correct keys."
assert "college" in proportion_of_education().keys(), "You have not returned a dictionary with the correct keys."
