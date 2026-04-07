<h3>CashNest Web Application</h3>

A full-stack finance tracking web application built with Django. <br>The system enables users to manage financial activities by recording expenses, credits, and setting financial goals through a responsive interface.
<hr>
<h4>Features</h4>
<ul>
  <li>User registration and authentication</li>
  <li>Create and manage financial goals</li>
  <li>Track expenses and credits</li>
  <li>Profit calculation based on transactions</li>
  <li>Responsive user interface</li>
</ul>
<hr>
<h4>Tech Stack</h4>
<ul>
  <li>Frontend: HTML, Tailwind CSS, JavaScript</li>
  <li>Backend: Python (Django)</li>
  <li>Database: SQLite</li>
</ul>
<hr>
<h4>Installation</h4>
<h5>Clone the repository</h5>
git clone https://github.com/veekshan-rai/Finance-Tracker.git <br>
cd Finance-Tracker
<hr>
<h4>Create a virtual environment</h4>
python -m venv venv
<hr>
<h4>Activate the virtual environment</h4>

<h5>Windows</h5>

venv\Scripts\activate

<h5>macOS/Linux</h5>

source venv/bin/activate
<hr>
<h4>Install dependencies</h4>
pip install -r requirements.txt
<hr>
<h4>Apply database migrations</h4>
python manage.py makemigrations
python manage.py migrate
<hr>
<h4>Run the application</h4>
python manage.py runserver



