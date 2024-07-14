import streamlit as st
from dotenv import load_dotenv
from ai_utils import get_gemini_response, generate_embedding
from tips import get_daily_car_tip
from ui_utils import set_page_config, display_chat_history
from vector_store import create_index_if_not_exists, upsert_vectors, query_vectors

# Load environment variables
load_dotenv()

# Initialize Pinecone index
create_index_if_not_exists()


def main():
    set_page_config()

    st.markdown('<p class="big-font">Garagemate AI</p>', unsafe_allow_html=True)
    st.write("Your comprehensive car maintenance companion powered by advanced AI")

    # Daily car tip
    st.info(f"🚗 Daily Car Tip: {get_daily_car_tip()}")

    # Sidebar for different functionalities
    st.sidebar.title("Features")
    feature = st.sidebar.radio("Choose a feature:", ["Chat", "Maintenance Guide", "Cost Estimator", "Part Finder", "Service Scheduler"])

    if feature == "Chat":
        display_chat_history()

    elif feature == "Maintenance Guide":
        st.subheader("Car Maintenance Guide")
        car_type = st.selectbox("Choose your car type:", ["Sedan", "SUV", "Truck", "Electric Vehicle"])
        mileage = st.number_input("Enter your car's mileage:", min_value=0, max_value=500000, value=50000)
        if st.button("Generate Maintenance Guide"):
            guide_prompt = f"Provide a maintenance guide for a {car_type} with {mileage} miles. Include recommended services, their frequency, and importance."
            response = get_gemini_response(guide_prompt)
            st.write(response)

    elif feature == "Cost Estimator":
        st.subheader("Service Cost Estimator")
        service = st.selectbox("Choose a service:", ["Oil Change", "Tire Rotation", "Brake Service", "Engine Tune-up", "A/C Service"])
        car_make = st.text_input("Enter your car make (e.g., Toyota, Ford):")
        car_model = st.text_input("Enter your car model:")
        car_year = st.number_input("Enter your car year:", min_value=1900, max_value=2024, value=2020)
        if st.button("Estimate Cost"):
            cost_prompt = f"Estimate the cost range for {service} for a {car_year} {car_make} {car_model}. Provide a low and high estimate and factors that might affect the cost."
            response = get_gemini_response(cost_prompt)
            st.write(response)

    elif feature == "Part Finder":
        st.subheader("Car Part Finder")
        part_name = st.text_input("Enter the name of the part you're looking for:")
        car_make = st.text_input("Enter your car make:")
        car_model = st.text_input("Enter your car model:")
        car_year = st.number_input("Enter your car year:", min_value=1900, max_value=2024, value=2020)
        if st.button("Find Part"):
            part_prompt = f"Provide information about {part_name} for a {car_year} {car_make} {car_model}. Include possible part numbers, estimated price range, and where to find it."
            response = get_gemini_response(part_prompt)
            st.write(response)

    elif feature == "Service Scheduler":
        st.subheader("Service Scheduler Assistant")
        service_type = st.selectbox("Choose a service type:", ["Oil Change", "Tire Rotation", "Brake Service", "Engine Tune-up", "A/C Service"])
        last_service_date = st.date_input("When was your last service?")
        mileage = st.number_input("Current mileage:", min_value=0, step=1000)
        if st.button("Get Next Service Recommendation"):
            schedule_prompt = f"Based on a {service_type} performed on {last_service_date} for a vehicle with {mileage} miles, when should the next service be scheduled? Provide a recommendation and explain the factors considered."
            response = get_gemini_response(schedule_prompt)
            st.write(response)

    # Footer
    st.markdown("---")
    st.markdown("**Disclaimer:** Garagemate AI is for informational purposes only. Always consult with a qualified mechanic for professional advice.")
    
    # Feedback
    st.sidebar.markdown("---")
    if st.sidebar.button("Give Feedback"):
        st.sidebar.text_area("We'd love to hear your thoughts!", key="feedback")
        if st.sidebar.button("Submit Feedback"):
            st.sidebar.success("Thank you for your feedback!")

if __name__ == "__main__":
    main()