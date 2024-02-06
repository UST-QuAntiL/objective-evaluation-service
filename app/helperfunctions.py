from fractions import Fraction


def take_first(elem):
    return elem[0]


def take_second(elem):
    return elem[1]


def take_third(elem):
    return elem[2]


def get_solution_string(counts):
    return take_first(max(counts, key=take_second))


def parse_solution(sol):
    return [int(i) for i in sol]


def figure_to_base64(fig):
    import matplotlib.pyplot as plt
    import io
    import base64

    my_stringIObytes = io.BytesIO()
    plt.savefig(my_stringIObytes, format="png", bbox_inches="tight")
    my_stringIObytes.seek(0)
    my_base64_jpgData = base64.b64encode(my_stringIObytes.read()).decode("utf-8")
    plt.savefig("temp_visualized.png", format="png", bbox_inches="tight")
    plt.close(fig)
    return my_base64_jpgData


def convert_cost_object_to_dict(cost_object):
    sorted_costs = sorted(cost_object, key=take_second, reverse=True)
    sorted_costs_dict = [
        {"bitstring": tup[0], "num_occurrences": tup[1], "cost": tup[2]}
        for tup in sorted_costs
    ]
    return sorted_costs_dict


def find_period(result_list: [(int, int, int)], n: int, p: int, g: int) -> int:
    """The order of the generator is not given, it has to be determined.
    The list of results for the whole circuit will be used, since the
    measurement of stage1 allows for phase estimation of the operator
    (similar to Shor's algorithm for prime factorization)."""
    smallest_fitting_denominator = (
        p + 1
    )  # init to p+1 (sth larger than the real result)
    for (y1, _, _) in result_list:
        meas_div = y1 / (2**n)
        frac_meas = Fraction(meas_div).limit_denominator(p - 1)

        # check if denominator fits
        r_candidate = frac_meas.denominator
        if g**r_candidate % p == 1:
            # fits
            if r_candidate < smallest_fitting_denominator:
                smallest_fitting_denominator = r_candidate

    print("Found r=", smallest_fitting_denominator)
    return smallest_fitting_denominator
