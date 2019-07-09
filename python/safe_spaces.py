"""Solve the spy game!"""
class SafetyFinder:
    """A class that contains everything we need to find the
    safest places in the city for Alex to hide out
    """

    def convert_coordinates(self, agents):
        pos_0index = []
        for i in agents:
            if int(i[1:]) < 11:#so coordinates like 'A12' are not further processed(10x10 matrix)
                #looking for position in unicode is faster than dictionary
                pos_0index.append([ord(i[0]) - 65, int(i[1:]) - 1])
        return pos_0index

    def find_safe_spaces(self, agents):
        #checks every coordinate's distance to every agent, since a subtraction is faster than a comparison to clarify whether to subtract or not
        #dictionary hash table not that useful, since only the greatest distance is of interest??
        safe_spots = []
        greatest_distance = 0
        x = 0
        if len(agents) != 0:
            while(x != 10):
                y = 0
                while(y - 10 != 0):
                    distance = min(abs(i[0] - x) + abs(i[1] - y) for i in agents)
                    if distance == greatest_distance:#happen more often than finding a greater distance
                        safe_spots.append([x, y])
                    elif distance > greatest_distance:
                        greatest_distance = distance
                        safe_spots.clear()
                        safe_spots.append([x, y])
                    y += 1
                x += 1
        return safe_spots

    def advice_for_alex(self, agents):
        advice = []
        for i in self.find_safe_spaces(self.convert_coordinates(agents)):
            advice.append(chr(i[0] + 65) + str(i[1] + 1))
        if advice == []:
            return 'The whole city is safe for Alex! :-)'
        elif len(advice) == 100:
            return 'There are no safe locations for Alex! :-('
        else:
            return advice
