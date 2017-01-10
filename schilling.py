import math
import random
import copy

width = 1000
height = 1000
num_x_cells = 20
num_y_cells = 20
cell_width = width/num_x_cells
cell_height = height/num_y_cells
w_offset = cell_width*0.5
h_offset = cell_height*0.5
neighbourhood_radius = 110
tolerance = 0.35

print "width", width, "height", height
print "num_x_cells", num_x_cells, "num_y_cells", num_y_cells
print "cell_width", cell_width, "cell_height", cell_height
print "w_offset", w_offset, "h_offset", h_offset
print "neighbourhood_radius", neighbourhood_radius

cell_state = []
new_cells_state = []
races = [{"name": "Oompaloompa", "id": 0, "colour": color(255, 165,   0)},
         {"name": "Axolotl",     "id": 1, "colour": color(  0, 255,   0)},
         {"name": "empty",       "id": 2, "colour": color(255, 255, 255)},
         {"name": "empty",       "id": 2, "colour": color(255, 255, 255)}]


def distance(thisCell, otherCell):
    dist = math.hypot(thisCell["geography"]["x"] - otherCell["geography"]["x"],
                      thisCell["geography"]["y"] - otherCell["geography"]["y"])
    return dist


def draw_neighbourhoods(thisCell, allCells):
    """Draws a line from this cell to neighbourhood cells"""
    stroke(id)
    strokeWeight(4)
    line(thisCell["x"], thisCell["y"], allCells[id]["x"], allCells[id]["y"])


def draw_neighbourhood_radius(thisCell):
    """Draws a line from this cell to neighbourhood cells"""
    stroke(50)
    strokeWeight(1)
    noFill()
    ellipse(thisCell["geography"]["x"], thisCell["geography"]["y"],
            neighbourhood_radius,   neighbourhood_radius)


def how_happy(cell):
    """Calculates the motivation to move"""
    # TODO:Needs much more attention to this calculation.
    # I think the small number is calusing some kind of near infinity crash?
    ratio = cell["occupant"]["upsides"]/(cell["occupant"]["downsides"]+0.01)
    if ratio > 1:
        ratio = 1
    return ratio


def move_house(thisCell):
    thisOccupant = dict(thisCell["occupant"])
    # move out of this house
    new_cells_state[thisCell["id"]]["occupant"] = {"race": races[2],  # empty
                                              "upsides": 0,
                                              "downsides": 0,
                                              "contentedness": 0}
    stillLooking = True
    while stillLooking:
        thisHouse = random.choice(new_cells_state)
        if thisHouse["occupant"]["race"]["name"] == "empty":
            stillLooking = False
            thisHouse["occupant"] = thisOccupant


def setup():
    """Gets the data structure ready to draw. This is the only place where a
    full n^2 search is done because the neighbourhoods are locked down here.
    This _should_ make things a lot faster in draw() because we're not looking
    at hundreds of neighbours, just a few.
    """
    size(width, height)
    colorMode(RGB, 255)
    counter = 0
    for i in range(num_x_cells):
        for j in range(num_y_cells):
            cell_state.append({"id": counter,
                               "geography": {"x": i*cell_width + w_offset,
                                             "y": j*cell_height + h_offset,
                                             "neighbourhood": []},
                               "occupant": {"race": random.choice(races),
                                            "upsides": 0,
                                            "downsides": 0,
                                            "contentedness": 0}
                               })
            counter += 1

    for cell in cell_state:
        for other_cell in cell_state:
            if other_cell["id"] != cell["id"]:
                dist = distance(cell, other_cell)
                if dist < neighbourhood_radius:
                    cell["geography"]["neighbourhood"].append(other_cell["id"])


def draw():
    global cell_state, new_cells_state
    # draw this round's states
    for cell in cell_state:
        noStroke()
        fill(cell["occupant"]["race"]["colour"])
        ellipse(cell["geography"]["x"],
                cell["geography"]["y"],
                cell_width,   # * cell["occupant"]["contentedness"],
                cell_height)  # * cell["occupant"]["contentedness"])
        # draw_neighbourhoods(cell, cell_state)
        # draw_neighbourhood_radius(cell)

        cell["occupant"]["downsides"] = 0
        cell["occupant"]["upsides"] = 0
        cell["occupant"]["contentedness"] = 0

        for id in cell["geography"]["neighbourhood"]:
            # draw_neighbourhoods()
            race = cell["occupant"]["race"]["name"]
            if race == cell_state[id]["occupant"]["race"]["name"]:
                cell["occupant"]["upsides"] += 1
            elif race == "empty":
                pass
            else:
                cell["occupant"]["downsides"] += 1
        cell["occupant"]["contentedness"] = how_happy(cell)

    contentedness = [c["occupant"]["contentedness"] for c in cell_state]
    # calculate next round's states
    new_cells_state = copy.deepcopy(cell_state)
    print "ave contentedness:", (sum(contentedness) / len(contentedness))

    for cell in new_cells_state:
        if cell["occupant"]["contentedness"] > tolerance:
            move_house(cell)
    cell_state = copy.deepcopy(new_cells_state)
