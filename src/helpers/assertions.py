def assert_status_code(response, expected_status):
    """
    Assert that the response contains the expected HTTP status code.
    """

    assert response.status_code == expected_status, (
        f"Expected status code {expected_status}, "
        f"but got {response.status_code}.\n"
        f"Response body:\n{response.text}"
    )