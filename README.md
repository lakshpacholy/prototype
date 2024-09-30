# Matsya Navigation - Ship Routing Application

Matsya Navigation is a real-time ship routing application that allows users to interactively track a ship’s current location, speed, course, and weather conditions. It calculates the best routes between Indian ports using data from the SeaRoutes API and visualizes these routes on a map with Folium. The application is built using the Dash framework, leveraging Bootstrap components for styling.

---

## Table of Contents

1. [Application Structure](#application-structure)
2. [Dependencies](#dependencies)
3. [Modules](#modules)
    - [`app.py`](#app-py)
    - [`route_calculator.py`](#route_calculator-py)
    - [`folium_map.py`](#folium_map-py)
4. [API Integration](#api-integration)
5. [Callback Functions](#callback-functions)
6. [How to Run](#how-to-run)
7. [Future Enhancements](#future-enhancements)

---

## 1. Application Structure

```bash
adaptive-ship-routing/
├── app.py                      # Main Dash application code
├── src/
│   ├── algorithms/
│   │   └── route_calculator.py  # Route calculations using SeaRoutes API and Geopy
│   ├── visualization/
│   │   └── folium_map.py        # Folium map rendering and route visualization
└── assets/                      # Static files (CSS, images, etc.)
```

## 2. Dependencies
The application requires the following Python libraries:

```bash
dash
dash-bootstrap-components
dash-iconify
geopy
folium
requests

```