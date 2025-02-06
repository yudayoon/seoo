from modules.trend_crawler import get_trend_data
from modules.seo_analysis import analyze_keywords
from modules.report_generator import generate_report
from modules.notifications import send_notifications

def main():
    print("🚀 트렌드 키워드 크롤링 시작...")
    trend_data = get_trend_data()

    print("📊 SEO 분석 실행 중...")
    seo_data = analyze_keywords(trend_data)

    print("📝 보고서 생성 중...")
    generate_report(seo_data)

    print("🔔 알림 전송 중...")
    send_notifications()

    print("✅ 모든 작업이 완료되었습니다!")

if __name__ == "__main__":
    main()
