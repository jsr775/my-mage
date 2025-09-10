"""
Block for loading data from Jira.
"""

# pylint: disable=possibly-used-before-assignment
# pylint: disable=unused-argument
import re
from ttt.jira import JiraClient

if "data_loader" not in globals():
    from mage_ai.data_preparation.decorators import data_loader
if "test" not in globals():
    from mage_ai.data_preparation.decorators import test


@data_loader
def load_data(*args, **kwargs):
    """
    Template code for loading data from any source.

    Returns:
        Anything (e.g. data frame, dictionary, array, int, str, etc.)
    """

    def get_sprint(sprint_str: str) -> str | None:
        """
        Extract the sprint name from the sprint string.

        Args:
            sprint_str (str): The sprint string to extract the name from.
        """
        match = re.search(r"name=([^,]+)", sprint_str)
        return match.group(1) if match else None

    jira_client = JiraClient()

    df = jira_client.get_issues(
        jql="project = TTTD and Sprint in openSprints()",
        fields=[
            "summary",
            "status",
            "Developer",
            "Story Points",
            "priority",
            "Sprint",
            "description",
        ],
        limit=300,
    )

    # Extract 'name' field from dictionary columns
    columns_to_extract = ["Developer", "Status", "Priority"]
    for column in columns_to_extract:
        df[column] = df[column].apply(
            lambda x: x["name"] if isinstance(x, dict) else None
        )

    df["Sprint"] = df["Sprint"].apply(
        lambda x: (get_sprint(x[len(x) - 1]) if isinstance(x, list) and x else None)
    )

    developer_mapping = {
        "RDhinge": "Raj",
        "nikhil.deore": "Nikhil",
        "jose.solorio": "Jose",
        "cris.serrano": "Cris",
        "lashaun.johnson": "Lashaun",
        "darrel.belen": "Darrel",
    }

    df["Developer"] = df["Developer"].map(developer_mapping).fillna(df["Developer"])

    return df


@test
def test_output(output, *args) -> None:
    """
    Template code for testing the output of the block.
    """
    assert output is not None, "The output is undefined"
