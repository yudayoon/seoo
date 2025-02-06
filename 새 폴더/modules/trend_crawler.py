import requests
from bs4 import BeautifulSoup
import pandas as pd

HEADERS = {"User-Agent": "Mozilla/5.0"}

def get_naver_trends():
    url = "https://datalab.naver.com/keyword/realtimeList.naver"
    response = requests.get(url, headers=HEADERS)
    soup = BeautifulSoup(response.text, "html.parser")
    return [item.text for item in soup.select(".rank_inner .list span.item_title")][:10]

def get_trend_data():
    print("🔍 트렌드 키워드 크롤링 중...")
    trends = {"네이버": get_naver_trends()}
    df = pd.DataFrame(dict([(k, pd.Series(v)) for k, v in trends.items()]))
    df.to_csv("output/trend_keywords.csv", index=False, encoding="utf-8-sig")
    print("✅ 트렌드 키워드 크롤링 완료!")
    return trends
