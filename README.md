🔆 Shiksha Ki Kiran – Empowering Rural Education with Technology
Shiksha Ki Kiran is an EdTech initiative built using Django to bridge the digital education divide in rural areas. It aims to provide remote learning tools, quizzes, video content, and community engagement features to enhance the quality of education in underserved regions.

🚀 Features
🎥 Curated YouTube video lessons across subjects

📝 Interactive quizzes and questions

👨‍🏫 Role-based login for students, teachers, and admins

🧠 Performance tracking and submissions

🌍 Focused on rural outreach and tech-enabled learning

🛠️ Tech Stack
Backend: Django, Django REST Framework

Frontend: HTML, CSS, Bootstrap

Database: SQLite (can be migrated to PostgreSQL/MySQL)

APIs: YouTube Embed, Django REST API for quizzes

👨‍💻 Developed By
Rehan Alam – Full Stack Developer | Final Year B.Tech CSE @ LPU
Passionate about using technology to solve real-world problems in education.

firstly clone 
goto that file 

than follow from step 3
python -m venv env

env\Scripts\activate

pip install -r requirements.txt  # or pip install django if no file

python manage.py makemigrations
python manage.py migrate
python manage.py createsuperuser
python manage.py runserver
