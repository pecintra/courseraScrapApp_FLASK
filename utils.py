from bs4 import BeautifulSoup
import requests
import pandas as pd

# This function will simply assign the choosen number to the course name as appeared on Coursera page request
def course_identifier(course_code):
    course_code = int(course_code)
    course_list = ["data-science","business","personal-development","computer-science","information-technology",
    "language-learning","math-and-logic","physical-science-and-engineering","health","social-sciences","arts-and-humanities"]
    return course_list[course_code]

# After selecting and identifying a course, gather informations from the desired field
def get_courses(course):
    response = requests.get('https://www.coursera.org/browse/'+course)
    soup = BeautifulSoup(response.content,'html.parser')
    html_courses = soup.findAll("a", "CardText-link")
    courses = {"course_link": [], "course_name": [], "course_provider": [], "course_description": [], "number_of_students_enrolled": [], "number_of_ratings": []}

    for i, name in enumerate(html_courses):
        course_link = 'https://www.coursera.org'+name['href']
        courses['course_link'].append(course_link)
        courses['course_name'].append(name.getText())
        course_provider, course_description, enrolled, ratings = get_other_info(course_link)
        courses['course_provider'].append(course_provider)
        courses['course_description'].append(course_description)
        courses['number_of_students_enrolled'].append(enrolled)
        courses['number_of_ratings'].append(ratings)

    return pd.DataFrame(courses).to_csv('coursera_info.csv', index=False)

# Enters every link from get_courses function to gather different informations
def get_other_info(course_link):
    response = requests.get(course_link)
    soup = BeautifulSoup(response.content,'html.parser')
    
    course_provider = soup.findAll('a',{"data-click-key": "xdp_v1.xdp.click.partner_name"})
    if course_provider:
        course_provider = [t.getText() for t in course_provider]
        course_provider = " and ".join(course_provider)
    
    course_description = soup.findAll('div','description')
    if course_description:
        course_description = course_description[0].getText()
    else:
        course_description = soup.findAll("div", "css-6ohxmr")
        if course_description:
            course_description = course_description[0].getText()
        else:
            course_description = ''

    enrolled = soup.findAll("div", "learners-count")
    if enrolled:
        enrolled = enrolled[0].getText()
        enrolled = int("".join(filter(str.isdigit, enrolled)))
    else:
        enrolled = 0

    ratings = soup.findAll("span", {"data-test": "ratings-count-without-asterisks"})
    if ratings:
        ratings = ratings[0].getText()
        ratings = int("".join(filter(str.isdigit, ratings)))
    else:
        ratings = 0

    return course_provider, course_description, enrolled, ratings