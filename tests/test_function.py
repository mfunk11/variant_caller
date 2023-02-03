from mf_pkg import main


def test_compute_dist_gen():
    num1 = 2
    num2 = 7
    expected_sum = 9
    n_sum = main.sum(num1, num2)
    assert n_sum == expected_sum, "The sum of 2 and 7 is 9 not" + str(sum)


def test_lines_function():
    file = "six-lines.txt"
    expected_lines = 6
    n_lines = main.read_data(file)
    assert n_lines == expected_lines, "The expected number of lines is 6."
