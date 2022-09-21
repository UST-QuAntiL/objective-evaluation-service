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
    sorted_costs_dict = [{'bitstring': tup[0], 'num_occurrences': tup[1], 'cost': tup[2]} for tup in sorted_costs]
    return sorted_costs_dict
