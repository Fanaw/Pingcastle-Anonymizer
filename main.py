from bs4 import BeautifulSoup

def main():
    print('hello world!')
    with open('report/example.html', 'rb') as f:
        soup = BeautifulSoup(f, 'html.parser')
        print(soup.title)
        
    
if __name__ == '__main__':
    main()