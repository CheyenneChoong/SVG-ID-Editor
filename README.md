# SVG ID Editor ✏️
## Overview
![HTML5](https://img.shields.io/badge/html5-%23E34F26.svg?style=for-the-badge&logo=html5&logoColor=white) ![Python](https://img.shields.io/badge/python-3670A0?style=for-the-badge&logo=python&logoColor=ffdd54) ![Flask](https://img.shields.io/badge/flask-%23000.svg?style=for-the-badge&logo=flask&logoColor=white)

This project aims to create a tool that could help in placing IDs within a SVG file. The program identifies the components within the SVG and ID the components based on the ID list uploaded and based on the colour code of the components. The project utilizes HTML5 for the frontend and Python for the backend with Flask as the framework.

## Tech Stack
|||
| --- | --- |
| Frontend | HTML5 |
| Backend | Python 3.13 |
| Framework | Flask |

## How It Works
#### What would you need to prepare?
- SVG file (.svg) with the fill of each component to be ID colour coded. No two component can have the exact same hexadecimal colour code.
- Text file (.txt) with the list of ID placed in the format of
    ```
    The colour of the component, The ID for the component, The colour of the component after the ID (the intended colour)
    #000000, ID, #000000
    ```
  The first colour is for identifying the component in the image. This is why no two component can have the same hexadecimal code otherwise more than one component would have the same ID. The second colour is the actual colour you want the component to be.

#### Steps to ID
1. Upload SVG file.
2. Upload ID text file.
3. Click 'ID SVG'.

#### Test SVG
After placing the ID in the SVG, you can already test if the ID works by entering the ID and clicking the 'Highlight' button. The component with the ID will be highlighted in the colour you chose. Click 'Export' if you want to download the newly edited SVG.
