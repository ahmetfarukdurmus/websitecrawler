import requests
from bs4 import BeautifulSoup
from urllib.parse import urljoin, urlparse

target_url = "https://www.realmadrid.com/en-US/"

response = requests.get(target_url)
soup = BeautifulSoup(response.text, 'html.parser')

# Benzersiz linkleri saklamak için set kullanıyoruz
unique_links = set()

for link in soup.find_all('a'):
    href = link.get('href')
    
    if href:
        # Göreceli linkleri mutlak linklere çeviriyoruz
        absolute_url = urljoin(target_url, href)
        
        # Sadece aynı domain'den gelen linkleri alıyoruz (isteğe bağlı)
        parsed_url = urlparse(absolute_url)
        if parsed_url.netloc == urlparse(target_url).netloc:
            unique_links.add(absolute_url)

# Benzersiz linkleri yazdırıyoruz
print(f"Toplam {len(unique_links)} benzersiz link bulundu:")
print("-" * 50)

for i, link in enumerate(sorted(unique_links), 1):
    print(f"{i}. {link}")