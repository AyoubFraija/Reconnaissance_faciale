# Plateforme de notification des présences par Reconnaissance Faciale 

## Table of Contents
* [General Info](#general-information)
* [Technologies Used](#technologies-used)
* [Screenshots](#screenshots)
<!-- * [License](#license) -->


## General Information
The facial recognition system captures real-time video feed from a webcam, detecting and recognizing faces using the LBPH (Local Binary Patterns Histograms) algorithm. The system systematically processes each frame to extract facial features, which are then compared against a pre-trained model to identify individuals. Upon successful recognition, the system logs the presence of the identified individuals into a MySQL database. Django orchestrates the entire process, managing user authentication, data storage, and real-time updates. As a final step, the recognized faces and their corresponding presence data are displayed on an interactive web dashboard, providing a comprehensive overview of attendance.
<!-- You don't have to answer all the questions - just the ones relevant to your project. -->


## Technologies Used
- Python
- Django
- OpenCV
- MySQL
- Pandas



## Screenshots
![Example screenshot](Screenshots/home1.PNG)
![Example screenshot](screenshots/home2.PNG)
![Example screenshot](screenshots/home3.PNG)
<!-- If you have screenshots you'd like to share, include them here. -->



<!-- Optional -->
<!-- ## License -->
<!-- This project is open source and available under the [... License](). -->

<!-- You don't have to include all sections - just the one's relevant to your project -->
