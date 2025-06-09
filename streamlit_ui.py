import streamlit as st
from Config.config import configure
from Agents.travel_planner import generate_itinerary
from Agents.pdf_summarizer import summarize_pdf
from Agents.map_linker import MapLinker
from Agents.budget_estimator import estimate_budget
from Agents.flight_checker import check_flight_cost
from Agents.agent_manager import AgentManager



configure()
manager = AgentManager()


st.set_page_config(page_title="Travel Planner AI", page_icon="🌍")
st.title("🧳 Travel Planner Agent")
st.write("Plan your trip with the help of Gemini AI!")

place_main = st.text_input("Where do you want to go?")
days = st.number_input("How many days?", min_value=1, max_value=30, step=1)

if st.button("Generate Plan"):
    with st.spinner("Planning your trip..."):
        itinerary = generate_itinerary(place_main, days)
        st.success("Here's your travel plan:")
        st.write(itinerary)

        pdf_file = manager.export_itinerary_pdf(itinerary)
        with open(pdf_file, "rb") as f:
            st.download_button("⬇️ Download Travel Planner PDF", f, file_name=pdf_file, mime="application/pdf")
        
        
        with st.spinner("Fetching some amazing images..."):
            images = manager.get_images(place_main)
            st.subheader(f"📷 Images of {place_main}")
            for url in images:
                st.image(url, use_column_width=True)


st.header("📄 Upload Travel PDF for Summary")
pdf_file = st.file_uploader("Upload your travel document", type=["pdf"])
if pdf_file and st.button("Summarize PDF"):
    summary = summarize_pdf(pdf_file)
    st.write(summary)
    
st.header("📍 Google Map Tools")
place = st.text_input("Enter location:")
if st.button("🔍 Search on Map"):
    st.markdown(f"[Open Map]({MapLinker.generate_search_url(place)})")

from_loc = st.text_input("From:")
to_loc = st.text_input("To:")
if st.button("🧭 Get Directions"):
    url = MapLinker.generate_directions_url(from_loc, to_loc)
    st.markdown(f"[Get Directions]({url})")


if place_main and st.button("Estimate Budget"):
    budget = estimate_budget(place_main, days)
    st.subheader("💸 Estimated Budget:")
    st.write(budget)
    
st.header("✈️ Flight Price Checker")
src = st.text_input("From:", key="map_from")
dest = st.text_input("To:", key="map_to")
date = st.date_input("Date of Travel")

if src and dest and st.button("Check Flights"):
    result = check_flight_cost(src, dest, str(date))
    st.write(result)
    
    
    
    
    
    
    