import streamlit as st
from PIL import Image

def registration_form():
    st.title("ANIRVEDA'S IPL Auction 2023")
    st.write("💫 Greetings PDEU!! 💫")
    st.write("Gear up for the most thrilling event of the academic calendar! 🎉")
    st.write("The ✨ IPL auction ✨ is just a few days away, and it promises to be an unforgettable experience.")
    st.write("This is your chance to step into the shoes of team owners and strategize like the pros🫱🏻‍🫲🏻")
    st.write("Remember, it's not just about picking the best players; it's about managing your budget wisely and building a balanced squad. 💰🏏")
    st.write("Will you go all-in for a star player or opt for emerging talent with potential? The choice is yours! 🌟🌟")
    st.write("Assemble your team of cricket enthusiasts, polish your auctioneer skills, and prepare for a rollercoaster ride of bidding wars, unexpected twists, and strategic maneuvers. 🔄✨💼")
    st.write("For more details, join the WhatsApp group:")
    st.write("https://chat.whatsapp.com/BCovv8RfVUBGs0PMHhfnzA")
    st.write("")
    st.write("")
    st.write("Please fill in the following details to register:")

    # Input fields
    name = st.text_input("Name:", key="name")
    roll_number = st.text_input("Roll Number:", key="roll_number")

    # Dropdown for Year of Study
    year_of_study_options = ['1st year', '2nd year', '3rd year', '4th year']
    year_of_study = st.selectbox("Year of Study:", year_of_study_options, key="year_of_study")

    # Dropdown for School
    school_options = ['SOT', 'SLS', 'SPT', 'SOET']
    school = st.selectbox("School:", school_options, key="school")

    

    st.header("Team Details")
    team_name = st.text_input("Team Name:", key="team_name")

    st.header("Player Details")

    # Player 1 (Team Leader)
    st.subheader("Player 1 (Team Leader)")
    player1_name = st.text_input("Name:", key="player1_name")
    player1_roll_number = st.text_input("Roll Number:", key="player1_roll_number")
    player1_contact = st.text_input("Contact Number (WhatsApp):", key="player1_contact")
    player1_email = st.text_input("Email:", key="player1_email")

    # Player 2
    st.subheader("Player 2")
    player2_name = st.text_input("Name:", key="player2_name")
    player2_roll_number = st.text_input("Roll Number:", key="player2_roll_number")
    player2_contact = st.text_input("Contact Number (WhatsApp):", key="player2_contact")
    player2_email = st.text_input("Email:", key="player2_email")

    # Player 3
    st.subheader("Player 3")
    player3_name = st.text_input("Name:", key="player3_name")
    player3_roll_number = st.text_input("Roll Number:", key="player3_roll_number")
    player3_contact = st.text_input("Contact Number (WhatsApp):", key="player3_contact")
    player3_email = st.text_input("Email:", key="player3_email")

    # Player 4
    st.subheader("Player 4")
    player4_name = st.text_input("Name:", key="player4_name")
    player4_roll_number = st.text_input("Roll Number:", key="player4_roll_number")
    player4_contact = st.text_input("Contact Number (WhatsApp):", key="player4_contact")
    player4_email = st.text_input("Email:", key="player4_email")

    
    # Registration Fees
    st.header("Registration Fees")
    st.write("If you have mode of payment as online pay using the following qr code or via the upi id: ritikaadhiya21@oksbi")
    st.write("If you have mode of payment as cash, please contact the following numbers: ")
    st.write("Rajat Agrawal: 9664981455")
    st.write("Sumer Pandey: 9979878903")
    st.write("Registration Fees: RS50 per team")
    registration_fees = 50
    st.write(f"Total Registration Fees: ${registration_fees}")

    # Payment Instructions Image
    payment_instructions_image = Image.open("payment.jpg")
    st.image(payment_instructions_image, caption="Payment Instructions:", use_column_width=True)

    # Screenshot Upload
    st.write("Please upload a screenshot as proof of payment:")
    screenshot = st.file_uploader("Upload Screenshot (JPG or PNG)", type=["jpg", "png"], key="screenshot", accept_multiple_files=False)

    # Queries
    queries = st.text_area("Do you have any queries or special requests? (Optional):", key="queries")

    # Submit button
    if st.button("Submit"):
        try:
            # Validate required fields
            if not all([
                name, roll_number, year_of_study, school, team_name,
                player1_name, player1_roll_number, player1_contact, player1_email
            ]):
                st.error("Please fill in all the required fields.")
            elif not screenshot:
                st.error("Please upload a screenshot as proof of payment.")
            else:
                # Save the screenshot as proof
                screenshot.save("payment_proof.png")

                st.success("Registration Successful!")
                # You can add code to submit the registration details and the payment proof to a database or another service here.

        except Exception as e:
            st.error("An error occurred during registration. Please try again later.")
            st.error(str(e))

if __name__ == "__main__":
    registration_form()