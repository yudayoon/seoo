import pandas as pd

def analyze_keywords(trend_data):
    print("📊 SEO 키워드 분석 중...")
    seo_results = [{"키워드": kw, "검색량": 1000, "CPC": 0.5, "경쟁도": "낮음"} for kw in trend_data["네이버"]]
    df = pd.DataFrame(seo_results)
    df.to_csv("output/seo_analysis.csv", index=False, encoding="utf-8-sig")
    print("✅ SEO 키워드 분석 완료!")
    return df
