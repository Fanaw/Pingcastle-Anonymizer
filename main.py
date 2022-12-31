from bs4 import BeautifulSoup
REPORT = 'report/example.html'

def read_report(report_file_path: str):
    with open(report_file_path, 'rb') as f:
        return BeautifulSoup(f, 'html.parser')

def find_category_score(soup: BeautifulSoup):
    score = []
    for tag in soup.find_all('div', class_='col-md-6 col-xs-8 col-sm-9'):
        score.append(tag.find('strong').string)
    return score

def main():
    soup = read_report(REPORT)
    domain = soup.h1.string.split(' ')[0]
    category_score = find_category_score(soup)
    print(category_score)
        
    
if __name__ == '__main__':
    main()