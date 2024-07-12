#scraping local files which is html (home.html)

from bs4 import BeautifulSoup

with open('home.html', 'r') as html_file:
    content = html_file.read()
    print(content) 


#using lxml and prettify() method

with open('home.html', 'r') as html_file:
    content = html_file.read()
    soup = BeautifulSoup(content, 'lxml')
    print(soup.prettify())


#using beautifulsoup find and find all methods
with open('home.html', 'r') as html_file:
    content = html_file.read()
    soup = BeautifulSoup(content, 'lxml')
    tags = soup.find('h5')
    print(tags)

with open('home.html', 'r') as html_file:
    content = html_file.read()
    soup = BeautifulSoup(content, 'lxml')
    tags = soup.find_all('h5')
    print(tags)

#to print only text removing all of the tags 
with open('home.html', 'r') as html_file:
    content = html_file.read()
    soup = BeautifulSoup(content, 'lxml')
    courses = soup.find_all('h5')
    for course in courses:
        print(course.text)


#to print course prices (course name and course price which is respectively h5 and a tags)

with open('home.html', 'r') as html_file:
    content = html_file.read()
    soup = BeautifulSoup(content, 'lxml')
    courses = soup.find_all('div', class_ = "card")
    for course in courses:
        course_name = course.h5.text
        course_price = course.a.text

        print(course_name)
        print(course_price)

#to print more of a sentence by keeping only price amount and combining it to course name 
with open('home.html', 'r') as html_file:
    content = html_file.read()
    soup = BeautifulSoup(content, 'lxml')
    courses = soup.find_all('div', class_ = "card")
    for course in courses:
        course_name = course.h5.text
        course_price = course.a.text.split()[-1] #it will only print last vriable which is price according to html file content

        print(f'{course_name} costs {course_price}')



