# calls all agents in order

#from agents.voice_agent import speech_to_text, text_to_speech
from data_ingestion.api_agent import get_stock_data
from data_ingestion.scraping_agent import scrape_earnings_news
from agents.analysis_agent import calculate_risk_exposure, detect_earning_surprises
from agents.language_agent import generate_market_brief

def process_query(audio_file):
    return "Test response: Earnings report summary would appear here."
    news = scrape_earnings_news("Asia tech stocks")
    risk = calculate_risk_exposure()
    earnings = detect_earning_surprises(news)
    summary = generate_market_brief(risk, earnings)
    text_to_speech(summary)
    return summary
