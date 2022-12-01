For this task, you will be creating a Python script that scrapes course info from coursera.org

The script should have an interface where you can enter a category name corresponding to a Coursera category such as Data Science: https://www.coursera.org/browse/data-science

Then the script will collect all courses from this category and place them into a CSV file. Here is the info that is required from each course:

Course name
Course provider
Course description
Number of Students enrolled
Number of Ratings

Here is an example CSV file for this course page. The script should collect data from ALL courses within the category that is inputted. Once finished, the script should place the CSV file on the server and provide a link to access it.

Once you are done, upload your script to the web that shows the interface which allows the user to select a coursera category. Submit the live URL to your script, along with a txt file containing the source code, in this form here: https://forms.gle/rCGGTsdgVXQ1594p7

## Setting up your development environment

### Installing the libraries
At the same directory as this file, run:
  - `pip install pipenv`
  - `pipenv install`

### Running the API for development
Initialize your app using `pipenv`:

- `pipenv shell`

Then run the following commands:

- flask run

And your app will be running on http://127.0.0.1:5000/

# made by Pedro Cintra