from {{cookiecutter.project_slug}}.calculate import sum


def test_sum_of_1_and_2_equals_3() -> None:
    assert sum(1, 2) == 3
