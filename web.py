#using the requests library to see a website's HTML
# using websites to scrape

from bs4 import BeautifulSoup
import requests

#in that website we will access the text "posted few days ago" text 
html_text = requests.get('https://www.timesjobs.com/candidate/job-search.html?searchType=personalizedSearch&from=submit&searchTextSrc=ft&searchTextText=&txtKeywords=python&txtLocation=')
print(html_text)  #response [200]


#to get text in that website
html_text = requests.get('https://www.timesjobs.com/candidate/job-search.html?searchType=personalizedSearch&from=submit&searchTextSrc=ft&searchTextText=&txtKeywords=python&txtLocation=').text
#print(html_text)


#scraping a production Website
#scraping list which is li in website & h3 tag which is in li job name
# we can use their class name to access get into html code of it and copy the class name to pull
html_text = requests.get('https://www.timesjobs.com/candidate/job-search.html?searchType=personalizedSearch&from=submit&searchTextSrc=ft&searchTextText=&txtKeywords=python&txtLocation=').text
soup = BeautifulSoup(html_text, 'lxml')
job = soup.find('li', class_ = 'clearfix job-bx wht-shd-bx')
company_name = job.find('h3', class_ = 'joblist-comp-name').text.replace(' ','')
skills = job.find('span', class_ = 'srp-skills').text.replace(' ', '')

print(f''' 
Company Name: {company_name}

Required Skills: {skills}
''')

# all using loop #published status also we are scraping here we only printing "few days ago job posts"

html_text = requests.get('https://www.timesjobs.com/candidate/job-search.html?searchType=personalizedSearch&from=submit&searchTextSrc=ft&searchTextText=&txtKeywords=python&txtLocation=').text
soup = BeautifulSoup(html_text, 'lxml')
jobs = soup.find_all('li', class_ = 'clearfix job-bx wht-shd-bx')
for job in jobs:
    published_data = job.find('span', class_ = 'sim-posted').span.text
    if 'few' in published_data:
        company_name = job.find('h3', class_ = 'joblist-comp-name').text.replace(' ','')
        skills = job.find('span', class_ = 'srp-skills').text.replace(' ', '')
        
        print(f''' 
        Company Name: {company_name}
        Required Skills: {skills}
        ''')

        print('')
        
# adding some features and prettifying the jobs paragraph, removingall the spaces and prettifying it

html_text = requests.get('https://www.timesjobs.com/candidate/job-search.html?searchType=personalizedSearch&from=submit&searchTextSrc=ft&searchTextText=&txtKeywords=python&txtLocation=').text
soup = BeautifulSoup(html_text, 'lxml')
jobs = soup.find_all('li', class_ = 'clearfix job-bx wht-shd-bx')
for job in jobs:
    published_data = job.find('span', class_ = 'sim-posted').span.text
    if 'few' in published_data:
        company_name = job.find('h3', class_ = 'joblist-comp-name').text.replace(' ','')
        skills = job.find('span', class_ = 'srp-skills').text.replace(' ', '')
        print(f" Company Name: {company_name.strip()}")
        print(f" Required Skills : {skills.strip()}")

        print(" ")
        

# we can add links to them of a job portal
html_text = requests.get('https://www.timesjobs.com/candidate/job-search.html?searchType=personalizedSearch&from=submit&searchTextSrc=ft&searchTextText=&txtKeywords=python&txtLocation=').text
soup = BeautifulSoup(html_text, 'lxml')
jobs = soup.find_all('li', class_ = 'clearfix job-bx wht-shd-bx')
for job in jobs:
    published_data = job.find('span', class_ = 'sim-posted').span.text
    if 'few' in published_data:
        company_name = job.find('h3', class_ = 'joblist-comp-name').text.replace(' ','')
        skills = job.find('span', class_ = 'srp-skills').text.replace(' ', '')
        more_info = job.header.h2.a['href']
        print(f" Company Name: {company_name.strip()}")
        print(f" Required Skills : {skills.strip()}")
        print(f" More Info: {more_info}")

        print(" ")


#filter out some skill requirements that user can enter 

print("put some skill that you're no familiar with")
unfamiliar_skill = input('>')
print(f'filtering out {unfamiliar_skill}')
html_text = requests.get('https://www.timesjobs.com/candidate/job-search.html?searchType=personalizedSearch&from=submit&searchTextSrc=ft&searchTextText=&txtKeywords=python&txtLocation=').text
soup = BeautifulSoup(html_text, 'lxml')
jobs = soup.find_all('li', class_ = 'clearfix job-bx wht-shd-bx')
for job in jobs:
    published_data = job.find('span', class_ = 'sim-posted').span.text
    if 'few' in published_data:
        company_name = job.find('h3', class_ = 'joblist-comp-name').text.replace(' ','')
        skills = job.find('span', class_ = 'srp-skills').text.replace(' ', '')
        more_info = job.header.h2.a['href']
        if unfamiliar_skill not in skills:
            print(f" Company Name: {company_name.strip()}")
            print(f" Required Skills : {skills.strip()}")
            print(f" More Info: {more_info}")

            print(" ")


#storing the jobs paragraph in text files so created postsTextsaved folder .

print("put some skill that you're no familiar with")
unfamiliar_skill = input('>')
print(f'filtering out {unfamiliar_skill}')

def find_jobs():
        html_text = requests.get('https://www.timesjobs.com/candidate/job-search.html?searchType=personalizedSearch&from=submit&searchTextSrc=ft&searchTextText=&txtKeywords=python&txtLocation=').text
        soup = BeautifulSoup(html_text, 'lxml')
        jobs = soup.find_all('li', class_ = 'clearfix job-bx wht-shd-bx')
        for index, job in enumerate(jobs):
            published_data = job.find('span', class_ = 'sim-posted').span.text
            if 'few' in published_data:
                company_name = job.find('h3', class_ = 'joblist-comp-name').text.replace(' ','')
                skills = job.find('span', class_ = 'srp-skills').text.replace(' ', '')
                more_info = job.header.h2.a['href']
                if unfamiliar_skill not in skills:
                    with open(f'postsTextsaved/{index}.txt','w') as f:
                        f.write(f" Company Name: {company_name.strip()} \n")
                        f.write(f" Required Skills : {skills.strip()} \n")
                        f.write(f" More Info: {more_info}")
                    print(f'File save: {index}')


if __name__ == "__main__":
    while True:
        find_jobs()



def fun():
     print(f'this how we can scrap the web pages ')

