import pandas as pd

def generate_report(seo_data):
    print("📄 보고서 생성 중...")
    report_content = seo_data.to_string()
    with open("output/report.pdf", "w") as f:
        f.write(report_content)
    print("✅ 보고서 생성 완료!")
