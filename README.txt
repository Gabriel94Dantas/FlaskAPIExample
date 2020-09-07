Technologies:
	I used  Python 3, Flask, Sqlite3, and Pytest. The most significant framework I used was Flask because it could facilitate the build of an API.

Installation:
	I used Python3 on OSX operational system, so I decided to use the virtual environment provided by Python. I already had installed Python3 on my computer. To create the virtual environment I ran the following command:
python3 -m virtualenv venv
I ran this command inside my project directory.

After that, I had to activate my virtual environment:
source venv/bin/activate

The next step was to install all the necessaries packages:
pip install -r requirements.txt

To run this project I typed:
flask run

After all these steps I had an API running on port 5000 with five endpoints.

The index endpoint was "/" or "/index", this endpoint was to create the database on Sqlite3 and create the tables.

The add vessel endpoint was "/add/vessel", this endpoint receives a JSON and only HTTP POST can invoke this endpoint that was responsible to add a new vessel to the system.

The add equipment endpoint was "/add/equipment", this endpoint receives a JSON and only HTTP POST can invoke this endpoint that was responsible to add a new equipment to the system.

The update equipment endpoint was "/update/equipment", this endpoint receives a JSON and was invoked by HTTP POST and HTTP PUT that was responsible to deactivate an equipment.

The return activates equipment by vessel endpoint was "/get/equipment", this endpoint expected a parameter like "/get/equipment/?vesselCode=MV100" to run that was invoked by HTTP GET and return a list of activates equipment on a vessel.

Beyond that, I could run Pytest to test all the systems to do that you can activate the virtual environment and call Pytest inside the project root path.
