# Spicks

![Spicks Visualization](static/images/spicks_logo.png)


Spicks, an abbreviation for Station Picks is an action plan project for Global Seismology Observation Course (Seminar Course Participant) developed by Akhadi-san and Jambari-san.

Spicks is a Django application designed for seismic data processing and visualization. It integrates PyGMT and ObsPy to analyze seismic events, station data, and phase picks, and generates visualizations such as station maps, residual plots, and histograms.

## Prerequisites
Before you begin, ensure you have the following installed:

- **Miniconda or Anaconda**: [Download and install from here](https://docs.conda.io/en/latest/miniconda.html).
- **Git**: [Download and install from here](https://git-scm.com/downloads).

## Step 1: Clone the Repository
Clone the repository to your local machine:

```bash
git clone https://github.com/jambari/Spicks.git
cd Spicks
```

## Step 2: Set Up the Conda Environment

Create the Conda Environment:
Use the provided `environment.yml` file to create the `django_pygmt` environment:

```bash
conda env create -f environment.yml
```

If you don’t have an `environment.yml` file, create one with the following content:

```yaml
name: django_pygmt
channels:
  - conda-forge
  - defaults
dependencies:
  - python=3.9
  - django
  - pygmt
  - obspy
  - pip
```

Activate the Environment:
After the environment is created, activate it:

```bash
conda activate django_pygmt
```

## Step 3: Install Additional Dependencies

If there are additional Python dependencies not included in the `environment.yml` file, install them using `pip`:

```bash
pip install -r requirements.txt
```

## Step 4: Set Up the Django Project

Migrate the Database:
Run the following commands to apply database migrations:

```bash
python manage.py migrate
```

Create a Superuser (Optional):
If you need access to the Django admin panel, create a superuser:

```bash
python manage.py createsuperuser
```

Load Initial Data:
Run fixtures for the initial data to load, use the following command:
We will import stations data from IA Network **BMKG**

```bash
python manage.py loaddata slmon.all.laststatus.json
```

## Step 5: Run the Development Server

Start the Django development server:

```bash
python manage.py runserver
```

Visit [http://127.0.0.1:8000/](http://127.0.0.1:8000/) in your browser to view the application.

## Step 6: Using PyGMT and ObsPy

The project is already set up to use PyGMT and ObsPy. You can import these libraries in your Django views, models, or scripts:


## Step 7: Directory Structure

Here’s an overview of the project structure:

```
focal_mechanism/
├── manage.py
├── seismic/                  # Django app
│   ├── migrations/
│   ├── static/
│   ├── templates/
│   ├── admin.py
│   ├── models.py
│   ├── views.py
│   └── urls.py
├── focal_mechanism/              # Django project settings
│   ├── settings.py
│   ├── urls.py
│   └── wsgi.py
├── static/                      # Static files
│   └── images/                  # Generated images
│       ├── station_locs/        # Station location maps
│       ├── distancebins/        # Distance bins plots
│       ├── distresid/           # Distance residuals plots
│       ├── logathist/           # Log amplitude histograms
│       ├── monthlypics/         # Monthly event pictures
│       ├── P.timehist/          # P-wave time histograms
│       ├── S.timehist/          # S-wave time histograms
│       ├── residmap/            # Residual maps
│       └── residualazimuth/     # Residual azimuth plots
├── requirements.txt             # Python dependencies
├── environment.yml              # Conda environment setup
└── README.md                    # Project documentation
```

## Step 8: Deploying the Project

For deployment, follow the official Django deployment guide: [Django Deployment Checklist](https://docs.djangoproject.com/en/stable/howto/deployment/checklist/).

## Troubleshooting

### Conda Environment Issues:
- If the environment fails to create, ensure you have the correct channels (`conda-forge` and `defaults`) in your `environment.yml`.
- Update Conda and try again:

```bash
conda update conda
```

### PyGMT Installation Issues:
- PyGMT requires GMT to be installed. Ensure it is installed correctly by running:

```bash
pygmt.show_versions()
```

- If GMT is missing, install it using:

```bash
conda install -c conda-forge gmt
```

### Django Server Not Starting:
- Ensure all migrations are applied and there are no database conflicts.
- Check the logs for errors and resolve them.

## Contributing

If you’d like to contribute to this project, please follow these steps:

1. Fork the repository.
2. Create a new branch for your feature or bugfix.
3. Commit your changes and push to the branch.
4. Submit a pull request.

## License

This project is licensed under the MIT License. See the `LICENSE` file for details.

## Contact

For any questions or issues, please contact **Muhammad Akhadi** at **muhammad.akhadi@bmkg.go.id**, **jambari** at **jambari@bmkg.go.id**
