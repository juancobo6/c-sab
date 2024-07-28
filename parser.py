import json
from main import *


def parse(json_path):
    data = json.loads(open(json_path).read())
    venue_name = data['name']
    x_max = data['x_max']
    y_max = data['y_max']

    origins_list = list(data['origins'].values())
    distribution = origins_list.pop()
    origins = []
    for i in range(0, len(origins_list), 5):
        origins.append(Origin(origins_list[i], origins_list[i+1], origins_list[i+2], origins_list[i+3], origins_list[i+4]))
            
    checkpoints_list = list(data['checkpoints'].values())
    checkpoints = []
    for i in range(0, len(checkpoints_list), 4):
        checkpoints.append(Checkpoint(checkpoints_list[i], checkpoints_list[i+1], checkpoints_list[i+2], checkpoints_list[i+3]))

    return Venue(venue_name, x_max, y_max, origins, checkpoints)

