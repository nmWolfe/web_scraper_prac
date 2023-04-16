import requests
import bs4

# Set the base, so it can be formatted with pages
base_url = "http://books.toscrape.com/catalogue/page-{}.html"

# result = base url + formatted page no. 
res = requests.get(base_url.format(1))

# Create soup of page text
soup = bs4.BeautifulSoup(res.text, 'lxml')
products = soup.select(".product_pod")
example = products[0]

# Do a boolean check for results
"star-rating Three" in str(example)

# Return a boolean 
[] == example.select('.star-rating.Two')

# Return the title 
example.select('a')[1]['title']

# We can check if something is 2 stars (str call in, example.select(rating))
# example.select('a')[1]['title'] to grab book title

two_star_titles = []

# Pull all the two star titles from the website
for n in range(1,51):
    
    scrape_url = base_url.format(n)
    res = requests.get(scrape_url)
    
    soup = bs4.BeautifulSoup(res.text, 'lxml')
    books = soup.select(".product_pod")
    
    for book in books:
        # if 'star-rating Two' in str(book)
        
        if len(book.select('.star-rating.Two')) != 0:
            book_title = book.select('a')[1]['title']
            two_star_titles.append(book_title)

# Print the books in a easily readable format
for book in two_star_titles:
    print(book)