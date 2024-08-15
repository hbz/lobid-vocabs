import re


def format_list_items(unformatted_list):
    formatted_list = [i + "\n\n" for i in unformatted_list]
    return formatted_list


with open("rpb-spatial.ttl", "r") as f:
    data = f.read()
    test_search = re.findall(r'^:n.*? \.$', data, flags=re.MULTILINE | re.DOTALL)
    prefix_matches = re.findall(r'^@prefix.+\.$\n', data, flags=re.MULTILINE)
    other_matches = re.findall(r'^(?!:n| |@|\n).*? \.$', data, flags=re.MULTILINE | re.DOTALL)
    list_sort = sorted(test_search, key=lambda x: (len(x.split(' ')[0]), x))
    prefix_matches.insert(len(prefix_matches), "\n")
    result = prefix_matches + format_list_items(other_matches) + format_list_items(list_sort)

    with open("rpb-spatial_sorted.ttl", "w") as outfile:
        outfile.write("".join(result))

