import requests
from bs4 import BeautifulSoup


def get_remoteok_jobs(keyword=None):
    """
    Scrapes job listings from RemoteOK.
    :param keyword: Optional search keyword (string)
    :return: List of job dictionaries
    """

    url = "https://remoteok.com/"
    if keyword:
        keyword = keyword.lower().replace(" ", "-")
        url += f"remote-{keyword}-jobs"

    headers = {"User-Agent": "Mozilla/5.0"}
    response = requests.get(url, headers=headers)
    response.raise_for_status()

    soup = BeautifulSoup(response.text, "html.parser")
    jobs = []

    job_cards = soup.find_all("tr", class_="job")

    for job in job_cards:
        title_elem = job.find("h2", itemprop="title")
        company_elem = job.find("h3", itemprop="name")
        link_elem = job.find("a", class_="preventLink")
        date_elem = job.find("time")
        tags_elem = job.find_all("div", class_="tag")
        location_elem = job.find_all('div', class_='location')[0]
        salary_elem = (job.find_all('div', class_='tooltip')[0]
                       if job.find_all('div', class_='tooltip') else None)

        if not title_elem or not company_elem:
            continue

        jobs.append({
            "title": title_elem.get_text(strip=True),
            "company": company_elem.get_text(strip=True),
            "location": location_elem.get_text(strip=True),
            "salary": salary_elem.get_text(strip=True) if salary_elem else 'Unknown',
            "tags": [t.get_text(strip=True) for t in tags_elem],
            "date_posted": date_elem["datetime"] if date_elem else None,
            "link": (f"https://remoteok.com{link_elem['href']}" 
                    if link_elem else None)
        })

    return jobs
