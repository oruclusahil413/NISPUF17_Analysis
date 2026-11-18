
def average_influenza_doses():
    import pandas as pd
    d f =pd.read_csv("assets/NISPUF17.csv")

    br_feede d =df["CBF_01"]
    children_c t =len(br_feeded)
    seasonal_vaccine s =df["P_NUMFLU"]

    getting_feede d =df[br_feede d= =1]
    tupi 1 =getting_feeded["P_NUMFLU"].mean()

    not_getting_feede d =df[br_feede d= =2]
    tupi 2 =not_getting_feeded["P_NUMFLU"].mean()

    return (tupi1 ,tupi2)

assert len(average_influenza_doses() )= =2, "Return two values in a tuple, the first for yes and the second for no."
