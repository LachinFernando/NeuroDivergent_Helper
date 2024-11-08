import streamlit as st

from Utils import image_generation, question_generator, question_processor
from Utils import SAVE_IMAGE_NAME
from prompts import HOME_IMAGE_GENERATION_PROMPT, HOME_QUESTION_GENERATION_PROMPT


# constants
IMAGE_ADDRESS = "https://1997bb66.rocketcdn.me/wp-content/uploads/2023/04/4-9-RMH-What-Neurodivergent-and-Neurotypical-Mean.jpg"


# callback functions
def test_one_callback():
    st.session_state.test_one = True
    st.session_state.test_two = False


def test_two_callback():
    st.session_state.test_one = False
    st.session_state.test_two = True
    st.session_state.test_one_cont = ""
    st.session_state.test_two_cont = ""


def set_test_one_content_callback():
    st.session_state.test_one_cont = ""


def set_test_two_content_callback():
    st.session_state.test_two_cont = ""


# states
# Initialize session state variables
if 'test_one' not in st.session_state:
    st.session_state.test_one = False

if 'test_one_cont' not in st.session_state:
    st.session_state.test_one_cont = ""

if 'test_two' not in st.session_state:
    st.session_state.test_two = False

if 'test_two_cont' not in st.session_state:
    st.session_state.test_two_cont = ""


# title of the app
st.title("Neurodivergent Tester")
# image of the app
st.image(IMAGE_ADDRESS, caption = "Neurodiverse Disorder")

# create columns
column_one, column_two = st.columns(2)

with column_one:
    st.button("Test One", on_click = test_one_callback, use_container_width = True)

with column_two:
    st.button("Test Two", on_click = test_two_callback, use_container_width = True)


if st.session_state.test_one:
    if not st.session_state.test_one_cont:
        with st.spinner("Generating......."):
            generate_image = image_generation()
            if not generate_image:
                st.error("Ouch..Error has occured! Please contact the developer.", icon = "🛑")
                st.stop()
            q_a = question_generator()
            st.session_state.test_one_cont = q_a
        
    question, answer_set, correct_ans = question_processor(st.session_state.test_one_cont)
    # display the image
    st.image(SAVE_IMAGE_NAME)
    st.write(question)
    # radio button select the answer
    user_answer = st.radio(
        "Please select the correct answer",
        answer_set,
        index = None
    )

    if user_answer:
        if user_answer.lower() == correct_ans.lower():
            st.markdown("**Your Answer is Correct**")
            # button to try another
            st.button("Try Another!", on_click = set_test_one_content_callback)
        else:
            st.markdown("**Your Answer is Incorrect**")
            # button to try another
            st.button("Try Another!", on_click = set_test_one_content_callback)


if st.session_state.test_two:
    if not st.session_state.test_two_cont:
        with st.spinner("Generating......."):
            generate_image_two = image_generation(required_prompt = HOME_IMAGE_GENERATION_PROMPT)
            if not generate_image_two:
                st.error("Ouch..Error has occured! Please contact the developer.", icon = "🛑")
                st.stop()
            q_a_two = question_generator(required_prompt = HOME_QUESTION_GENERATION_PROMPT)
            st.session_state.test_two_cont = q_a_two
        
    question_two, answer_set_two, correct_ans_two = question_processor(st.session_state.test_two_cont)
    # display the image
    st.image(SAVE_IMAGE_NAME)
    st.write(question_two)
    # radio button select the answer
    user_answer_two = st.radio(
        "Please select the correct answer",
        answer_set_two,
        index = None
    )

    if user_answer_two:
        if user_answer_two.lower() == correct_ans_two.lower():
            st.markdown("**Your Answer is Correct**")
            # button to try another
            st.button("Try Another!", on_click = set_test_two_content_callback)
        else:
            st.markdown("**Your Answer is Incorrect**")
            # button to try another
            st.button("Try Another!", on_click = set_test_two_content_callback)

