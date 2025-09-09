"""
Block for loading data from Jira issues.
"""
# ignore: pylint: disable=possibly-used-before-assignment
# ignore: pylint: disable=unused-argument

import os
from ttt.jira import JiraClient

if 'data_loader' not in globals():
    from mage_ai.data_preparation.decorators import data_loader
if 'test' not in globals():
    from mage_ai.data_preparation.decorators import test

URL = os.environ.get("JIRA_SERVER")
USER_NAME = os.environ.get("JIRA_USERNAME")
PASSWORD = os.environ.get("JIRA_PASSWORD")

@data_loader
def load_data(*args, **kwargs):
    """
    Template code for loading data from any source.

    Returns:
        Anything (e.g. data frame, dictionary, array, int, str, etc.)
    """
    # Specify your data loading logic here
    jira_client = JiraClient(URL, USER_NAME, PASSWORD)
    return jira_client.


@test
def test_output(output, *args) -> None:
    """
    Template code for testing the output of the block.
    """
    assert output is not None, 'The output is undefined'
