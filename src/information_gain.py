from scipy.stats import entropy
import pandas as pd


def calculate_information_gain(members, split):
    """Measures the reduction in entropy after the split
    :param v: Pandas Series of the members
    :param split: Pandas Series of the split
    :return: information gain
    :examples:
    >>> members = pd.Series(["yellow", "yellow", "green", "green", "blue", "blue"])
    >>> split = pd.Series([0, 0, 1, 1, 0, 1])
    >>> print(calculate_information_gain(members, split))
    0.4620981203732968
    """
    entropy_before = entropy(members.value_counts(normalize=True))
    split.name = "split"
    members.name = "members"
    grouped_distrib = (
        members.groupby(split)
        .value_counts(normalize=True)
        .reset_index(name="count")
        .pivot_table(index="split", columns="members", values="count")
        .fillna(0)
    )
    entropy_after = entropy(grouped_distrib, axis=1)
    entropy_after *= split.value_counts(sort=False, normalize=True)
    return entropy_before - entropy_after.sum()


def calculate_information_gain_ratio(members, split):
    """Measures the reduction in entropy after the split, normalized by split
    distribution entropy.
    :param v: Pandas Series of the members
    :param split: Pandas Series of the split
    :return: information gain ratio
    :examples:
    >>> members = pd.Series(["yellow", "yellow", "green", "green", "blue", "blue"])
    >>> split = pd.Series([0, 0, 1, 1, 0, 1])
    >>> print(calculate_information_gain_ratio(members, split))
    0.6666666666666665
    """
    information_gain = calculate_information_gain(members, split)
    entropy_split = entropy(split.value_counts(normalize=True))

    return information_gain / entropy_split
