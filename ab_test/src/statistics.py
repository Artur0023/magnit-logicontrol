from scipy import stats

def ttest_delay(df):
    """
    t-test средней задержки между A и B
    """
    a = df[df["ab_group"] == "A"]["delay_days"]
    b = df[df["ab_group"] == "B"]["delay_days"]

    stat, pvalue = stats.ttest_ind(a, b, equal_var=False)
    return {
        "t_stat": round(stat, 3),
        "p_value": round(pvalue, 5)
    }
