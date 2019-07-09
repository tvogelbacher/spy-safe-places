"""Solve the spy game!"""
class SafetyFinder:
    """A class that contains everything we need to find the
    safest places in the city for Alex to hide out
    """

    def convert_coordinates(self, agents):
        """This method should take a list of alphanumeric coordinates (e.g. 'A6')
        and return an array of the coordinates converted to arrays with zero-indexing.
        For instance, 'A6' should become [0, 5]
        Arguments:
        agents -- a list-like object containing alphanumeric coordinates.
        Returns a list of coordinates in zero-indexed vector form.
        """
        zero_indexed = []
        for i in agents:
            matrix_limit = int(i[1:])
            if matrix_limit < 11:#so coordinates like 'A12' are not further processed(10x10 matrix)
                #looking for position in unicode is faster than dictionary
                zero_indexed.append([ord(i[0]) - 65, matrix_limit - 1])
        return zero_indexed

    def find_safe_spaces(self, agents):
        """This method will take an array with agent locations and find
        the safest places in the city for Alex to hang out.
        Arguments:
        agents -- a list-like object containing the map coordinates of agents.
            Each entry should be formatted in indexed vector form,
            e.g. [0, 5], [3, 7], etc.
        Returns a list of safe spaces in indexed vector form.
        """
        #checks every coordinate's distance to every agent, since a subtraction is faster than a comparison to clarify whether to subtract or not
        #dictionary hash table not that useful, since only the greatest distance is of interest??
        safe_spots = []
        greatest_distance = 0
        x = 0
        if agents:
            while(x != 10):
                y = 0
                while(y - 10 != 0):
                    distance = min(abs(i[0] - x) + abs(i[1] - y) for i in agents)
                    if distance == greatest_distance:#happens more often than finding a greater distance
                        safe_spots.append([x, y])
                    elif distance > greatest_distance:
                        greatest_distance = distance
                        safe_spots.clear()
                        safe_spots.append([x, y])
                    y += 1
                x += 1
        return safe_spots

    def advice_for_alex(self, agents):
        """This method will take an array with agent locations and offer advice
        to Alex for where she should hide out in the city, with special advice for
        edge cases.
        Arguments:
        agents -- a list-like object containing the map coordinates of the agents.
            Each entry should be formatted in alphanumeric form, e.g. A10, E6, etc.
        Returns either a list of alphanumeric map coordinates for Alex to hide in,
        or a specialized message informing her of edge cases
        """
        advice = []
        for i in self.find_safe_spaces(self.convert_coordinates(agents)):
            advice.append(chr(i[0] + 65) + str(i[1] + 1))
        if not advice:
            return 'The whole city is safe for Alex! :-)'
        elif len(advice) == 100:
            return 'There are no safe locations for Alex! :-('
        else:
            return advice
