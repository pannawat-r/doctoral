import osmnx as ox

class Package:
    def __init__(self, mode, place):
        self.osm_graph = None
        self.gtfs_graph = None
        self.mode = mode
        self.place = place
    
    def create_osm_graph(self):
        self.osm_graph = ox.graph_from_place(self.place, network_type=self.mode)
        return self.graph

    def create_gtfs_graph(self):
        self.gtfs_graph = None
        return None
    
    def map_matching(self, start, end):
        return None
    
    def combine_graph(self, osm_graph, gtfs_graph):
        return None
    
    def calculate_accessibility(self, start, end):
        return None
