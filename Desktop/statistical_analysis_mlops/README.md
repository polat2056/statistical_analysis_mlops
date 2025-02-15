# Statistical Analysis MLOps

This project aims to create a sustainable and automated MLOps pipeline for statistical data analysis.

## Project Structure

## Getting Started

### Prerequisites
- Docker
- Git

### Installation
1. Clone the repository
    ```bash
    git clone https://github.com/kullanici_adi/statistical_analysis_mlops.git
    ```
2. Build the Docker image
    ```bash
    docker build -t statistical_analysis_mlops .
    ```

3. Run the Docker container
    ```bash
    docker run -it --rm statistical_analysis_mlops
    ```

## Usage
- Add your raw data to the `data/raw` folder.
- Implement your preprocessing and feature engineering in the `src/data` and `src/features` folders.
- Train your model using `src/models/train_model.py`.

## Contributing
Pull requests are welcome. For major changes, please open an issue first to discuss what you would like to change.

## License
[MIT](https://choosealicense.com/licenses/mit/)
