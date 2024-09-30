<p align="center">
  <img src="src/web_interface/assets/ship.jpg" width="20%" alt="PROTOTYPE-logo">
</p>
<p align="center">
    <h1 align="center">PROTOTYPE</h1>
</p>
<p align="center">
    <em><code>❯ REPLACE-ME</code></em>
</p>
<p align="center">
	<img src="https://img.shields.io/github/license/lakshpacholy/prototype?style=flat&logo=opensourceinitiative&logoColor=white&color=0080ff" alt="license">
	<img src="https://img.shields.io/github/last-commit/lakshpacholy/prototype?style=flat&logo=git&logoColor=white&color=0080ff" alt="last-commit">
	<img src="https://img.shields.io/github/languages/top/lakshpacholy/prototype?style=flat&color=0080ff" alt="repo-top-language">
	<img src="https://img.shields.io/github/languages/count/lakshpacholy/prototype?style=flat&color=0080ff" alt="repo-language-count">
</p>
<p align="center">
		<em>Built with the tools and technologies:</em>
</p>
<p align="center">
	<img src="https://img.shields.io/badge/Folium-77B829.svg?style=flat&logo=Folium&logoColor=white" alt="Folium">
	<img src="https://img.shields.io/badge/Plotly-3F4F75.svg?style=flat&logo=Plotly&logoColor=white" alt="Plotly">
	<img src="https://img.shields.io/badge/Python-3776AB.svg?style=flat&logo=Python&logoColor=white" alt="Python">
	<img src="https://img.shields.io/badge/Dash-008DE4.svg?style=flat&logo=Dash&logoColor=white" alt="Dash">
</p>

<br>

#####  Table of Contents

- [ Overview](#-overview)
- [ Features](#-features)
- [ Repository Structure](#-repository-structure)
- [ Modules](#-modules)
- [ Getting Started](#-getting-started)
    - [ Prerequisites](#-prerequisites)
    - [ Installation](#-installation)
    - [ Usage](#-usage)
    - [ Tests](#-tests)
- [ Project Roadmap](#-project-roadmap)
- [ Contributing](#-contributing)
- [ License](#-license)
- [ Acknowledgments](#-acknowledgments)

---

##  Overview

<code>❯ Matsya Navigation is a real-time ship routing application that allows users to interactively track a ship’s current location, speed, course, and weather conditions. It calculates the best routes between Indian ports using data from the SeaRoutes API and visualizes these routes on a map with Folium. The application is built using the Dash framework, leveraging Bootstrap components for styling.</code>

---

##  Features

<code>❯ Key features of the application include real-time tracking of maritime routes, integration of weather data, a user-friendly interface for port selection, and a dynamic route calculation that takes into account various maritime conditions for optimal navigation.</code>

---

##  Repository Structure

```sh
└── prototype/
    ├── README.md
    ├── app.py
    ├── requirements.txt
    └── src
        ├── algorithms
        ├── visualization
        └── web_interface
```

---

##  Modules

<details closed><summary>.</summary>

| File | Summary |
| --- | --- |
| [requirements.txt](https://github.com/lakshpacholy/prototype/blob/main/requirements.txt) | <code>❯ Contains all necessary Python libraries required to run the application.</code> |
| [app.py](https://github.com/lakshpacholy/prototype/blob/main/app.py) | <code>❯ Main entry point for the application that handles user interactions and renders the layout.</code> |

</details>

<details closed><summary>src.algorithms</summary>

| File | Summary |
| --- | --- |
| [route_calculator.py](https://github.com/lakshpacholy/prototype/blob/main/src/algorithms/route_calculator.py) | <code>❯ Manages the logic for calculating maritime routes using the SeaRoutes API and Geopy for distance calculations.</code> |

</details>

<details closed><summary>src.visualization</summary>

| File | Summary |
| --- | --- |
| [folium_map.py](https://github.com/lakshpacholy/prototype/blob/main/src/visualization/folium_map.py) | <code>❯ Handles the rendering of routes and waypoints on a Folium map.</code> |
| [plotly_charts.py](https://github.com/lakshpacholy/prototype/blob/main/src/visualization/plotly_charts.py) | <code>❯ (Future implementation) Will handle the rendering of additional data visualizations using Plotly.</code> |

</details>

---

##  Getting Started

###  Prerequisites

**Python**: `version 3.8` or higher is required to run this project.

###  Installation

Build the project from source:

1. Clone the prototype repository:
    ```sh
    ❯ git clone https://github.com/lakshpacholy/prototype
    ```

2. Navigate to the project directory:
    ```sh
    ❯ cd prototype
    ```

3. Install the required dependencies:
    ```sh
    ❯ pip install -r requirements.txt
    ```

###  Usage

To run the project, execute the following command:

```sh
❯ python app.py
```

###  Tests

Execute the test suite using the following command:

```sh
❯ pytest
```

---

##  Project Roadmap

The project roadmap outlines the key tasks and features planned for the prototype. Each task indicates its current status, helping contributors understand what is completed and what remains to be done.

- [X] **`Task 1`**: <strike>Implement feature one.</strike> This task has been completed and is fully functional.
- [ ] **`Task 2`**: Implement feature two. This task is currently in progress and requires further development.
- [ ] **`Task 3`**: Implement feature three. This task is yet to be started, pending the completion of prior tasks.

Future tasks will be added as the project evolves, and contributors are encouraged to suggest additional features or improvements.


##  Contributing

Contributions are welcome! Here are several ways you can contribute:

- **[Report Issues](https://github.com/lakshpacholy/prototype/issues)**: Submit bugs found or log feature requests for the `prototype` project.
- **[Submit Pull Requests](https://github.com/lakshpacholy/prototype/blob/main/CONTRIBUTING.md)**: Review open PRs, and submit your own PRs.
- **[Join the Discussions](https://github.com/lakshpacholy/prototype/discussions)**: Share your insights, provide feedback, or ask questions.

<details closed>
<summary>Contributing Guidelines</summary>

1. **Fork the Repository**: Start by forking the project repository to your github account.
2. **Clone Locally**: Clone the forked repository to your local machine using a git client.
   ```sh
   git clone https://github.com/lakshpacholy/prototype
   ```
3. **Create a New Branch**: Always work on a new branch, giving it a descriptive name.
   ```sh
   git checkout -b new-feature-x
   ```
4. **Make Your Changes**: Develop and test your changes locally.
5. **Commit Your Changes**: Commit with a clear message describing your updates.
   ```sh
   git commit -m 'Implemented new feature x.'
   ```
6. **Push to github**: Push the changes to your forked repository.
   ```sh
   git push origin new-feature-x
   ```
7. **Submit a Pull Request**: Create a PR against the original project repository. Clearly describe the changes and their motivations.
8. **Review**: Once your PR is reviewed and approved, it will be merged into the main branch. Congratulations on your contribution!
</details>

<details closed>
<summary>Contributor Graph</summary>
<br>
<p align="left">
   <a href="https://github.com{/lakshpacholy/prototype/}graphs/contributors">
      <img src="https://contrib.rocks/image?repo=lakshpacholy/prototype">
   </a>
</p>
</details>

---

##  License

This project is licensed under the [MIT License](https://choosealicense.com/licenses/mit/). You can find the full text of the license in the [LICENSE](https://github.com/lakshpacholy/prototype/blob/main/LICENSE) file.

---

##  Acknowledgments

- Acknowledgment to **Folium** for their powerful mapping capabilities that enabled dynamic visualizations of geographic data.
- Thanks to **Plotly** for their interactive graphing library, which facilitated the creation of engaging visual representations of data insights.
- Appreciation for the **Python community**, whose numerous tutorials, documentation, and open-source contributions have significantly aided in the development process.
- Thanks to all contributors and community members who provided valuable feedback, support, and suggestions for improving the project.
- Acknowledgment to the **maintainers of libraries** used in this project for their continuous efforts in maintaining and updating these resources, ensuring compatibility and performance.
- Special mention to my peers and mentors who provided insights and motivation throughout the project lifecycle.
w

---