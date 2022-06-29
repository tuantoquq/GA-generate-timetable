import json


def load_data(json_file):
    inp_file = open(json_file)
    data = json.load(inp_file)
    subject = data['Subjects']
    classes = data['Classes']
    weekdays = data['Weekdays']
    teachers = data['Teachers']


if __name__ == '__main__':
    load_data('input/inp01.json')
