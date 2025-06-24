import streamlit as st
import osmnx as ox
import networkx as nx
import folium
from streamlit_folium import st_folium
from geopy.geocoders import Nominatim

# Page config
st.set_page_config(page_title="Best Route Finder", layout="wide")

st.title("🧭 Best Route Finder App")

# Get locations
start = st.text_input("Enter start location", "India Gate, New Delhi")
end = st.text_input("Enter destination location", "Red Fort, New Delhi")

if st.button("Find Route"):
    try:
        # Geocoding
        geolocator = Nominatim(user_agent="route_finder")
        location_start = geolocator.geocode(start)
        location_end = geolocator.geocode(end)

        orig_point = (location_start.latitude, location_start.longitude)
        dest_point = (location_end.latitude, location_end.longitude)

        # Create graph around midpoint
        midpoint = ((orig_point[0] + dest_point[0]) / 2, (orig_point[1] + dest_point[1]) / 2)
        G = ox.graph_from_point(midpoint, dist=10000, network_type='walk')

        orig_node = ox.nearest_nodes(G, orig_point[1], orig_point[0])
        dest_node = ox.nearest_nodes(G, dest_point[1], dest_point[0])

        # Shortest path
        shortest_path = nx.shortest_path(G, orig_node, dest_node, weight='length')

        # Map plot
        route_map = ox.plot_route_folium(G, shortest_path, route_color='blue', opacity=0.7)

        # Mark start and end
        folium.Marker(location=orig_point, popup="Start", icon=folium.Icon(color='green')).add_to(route_map)
        folium.Marker(location=dest_point, popup="End", icon=folium.Icon(color='red')).add_to(route_map)

        # Display
        st_folium(route_map, width=800, height=600)

    except Exception as e:
        st.error(f"Could not find route: {e}")
