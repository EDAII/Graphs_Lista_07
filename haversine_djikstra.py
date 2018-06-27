import heapq
from math import sin, cos, sqrt, atan2, radians
from graph import Graph


def shortest(vertex, path):

    if vertex.previous:
        path.append(vertex.previous.get_name())
        shortest(vertex.previous, path)

    return


def dijkstra(graph, origin, destination):

    origin.set_distance(0)
    unvisited_queue = [(v.get_distance(), v) for v in graph]
    heapq.heapify(unvisited_queue)

    while len(unvisited_queue):

        # get min dist vertex from heap
        min_dist_vertex = heapq.heappop(unvisited_queue)
        current = min_dist_vertex[1]
        current.set_visited()

        for next in current.adjacent:
            if next.visited:
                continue
            new_dist = current.get_distance() + current.get_weight(next)

            if new_dist < next.get_distance():
                next.set_distance(new_dist)
                next.set_previous(current)

        # Rebuild heap
        while len(unvisited_queue):
            heapq.heappop(unvisited_queue)

        # Rebuild queue
        unvisited_queue = [(v.get_distance(), v) for v in graph if not v.visited]
        heapq.heapify(unvisited_queue)


def haversine_dist(long1, lat1, long2, lat2):

    # Aproximate earth radius for  optimized for locations around
    # 39 degrees from the equator
    earth_radius = 6373.0

    dist_longitude = long2 - long1
    dist_latitude = lat2 - lat1

    # Formula de Haversine
    a = sin(dist_latitude / 2)**2 + cos(lat1) * cos(lat2) \
        * sin(dist_longitude / 2)**2

    c = 2 * atan2(sqrt(a), sqrt(1 - a))
    circle_distance = earth_radius * c

    return circle_distance

if __name__ == '__main__':

    # Coordinates
    ny_long, ny_lat = radians(40.730610), radians(-73.935242)
    wds_long, wds_lat = radians(38.889931), radians(-77.009003)
    wv_long, wv_lat = radians(37.302120), radians(-81.690674)
    b_long, b_lat = radians(42.361145), radians(-71.057083)

    g = Graph()

    g.add_vertex('New York')
    g.add_vertex('Washington')
    g.add_vertex('West Virgina')
    g.add_vertex('Boston')

    g.add_edge('New York', 'Washington', haversine_dist(ny_long, ny_lat,
                                                        wds_long, wds_lat))
    g.add_edge('New York', 'West Virgina', haversine_dist(ny_long, ny_lat,
                                                          wv_long, wv_lat))
    g.add_edge('West Virgina', 'Boston', haversine_dist(wv_long, wv_lat,
                                                        b_long, b_lat))
    g.add_edge('Washington', 'Boston', haversine_dist(wv_long, wv_lat,
                                                      b_long, b_lat))

    origin = g.get_vertex('New York')
    target = g.get_vertex('Boston')
    dijkstra(g, origin, target)

    path = [target.get_name()]
    shortest(target, path)

    print('Shortest path from ' + origin.get_name() + ' to ' + target.get_name())
    print('is: %s' % (path[::-1]))
