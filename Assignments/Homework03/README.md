# 🎬 IMDb Movie Analysis 🍿

## 📖 Description
This project analyzes an IMDb movies dataset using Python.
It calculates the movie with the highest net profit, determines the most common genre, and identifies the top director by rating.
The project is containerized using Docker for easy execution.

## 📂 Contents
1. **analyze_data.py** - Reads and processes the IMDb dataset (`data.json`), extracting insights
2. **test_analyze_data.py** - Unit tests to verify the accuracy of `analyze_data.py`
3. **Dockerfile** - Configuration file for containerizing the project
4. **data.json** - IMDb dataset
---
## 📦 Building the Docker Image
To build the Docker image, run:
```sh
docker build -t imdb-analysis .
```
---
## 🏃🏻‍♂️ Running the Program in Docker
To execute `analyze_data.py` within the Docker container:
```sh
docker run --rm imdb-analysis
```
---
## 🏃🏻‍♂️ Running the Program Locally
To execute `analyze_data.py` within terminal:
```sh
pip install -r requirements.txt
```
```sh
python analyze_data.py data.json
```
---
