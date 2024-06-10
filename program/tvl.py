from program.soup import get_soup


def get_total_value_locked(url):
    soup = get_soup(url)
    total_value_locked = soup.find('div', class_ = 'sc-289dd4cb-0 sc-e4643b47-5 fKBsp eDcbYQ').find('details').find('summary').find_all('span')[-1].text
    return total_value_locked

