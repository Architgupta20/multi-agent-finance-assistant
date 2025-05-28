from data_ingestion.api_agent import get_current_price
from data_ingestion.scraping_agent import scrape_earnings_news
from agents.retriever_agent import index_data, retrieve_top_k
from agents.analysis_agent import calculate_risk_exposure, detect_earning_surprises
from agents.language_agent import generate_market_brief
#from agents.voice_agent import speech_to_text, text_to_speech
from langchain.chat_models import ChatOpenAI


print("🔍 Testing API Agent...")
print(get_current_price("AAPL"))

print("\n🔍 Testing Scraper Agent...")
print(scrape_earnings_news("Samsung"))

print("\n🔍 Testing Retriever Agent...")
sample_texts = ["TSMC beat estimates by 4%", "Samsung missed earnings by 2%"]
index_data(sample_texts)
print(retrieve_top_k("earnings surprise"))

print("\n🔍 Testing Analysis Agent...")
print(calculate_risk_exposure())
print(detect_earning_surprises(["TSMC", "Samsung"]))

print("\n🔍 Testing Language Agent...")
risk = {'region': 'Asia', 'sector': 'Tech', 'today': 22, 'yesterday': 18}
earnings = {'TSMC': '+4%', 'Samsung': '-2%'}
print(generate_market_brief(risk, earnings))

print("\n🔍 Testing Voice Agent...")
#print(speech_to_text("input.wav"))  # Make sure input.wav exists
#text_to_speech("Test complete.")
