import altair as alt
import numpy as np
import pandas as pd
import streamlit as st
import matplotlib.pyplot as plt
import numpy as np



# Title of the questionnaire
st.title("Comprehensive Questionnaire")

# Open question for name
name = st.text_input("What is your name?")

# Open question for work relation
work_relation = st.text_input("What is your work relation?")

# Define the 60 questions
questions = [
    "I communicate in a supportive way when people in my unit share their problems with me.",
    "I encourage others in my unit to generate new ideas and methods.",
    "I motivate and energize others to do a better job.",
    "I keep close track of how my unit is performing.",
    "I regularly coach subordinates to improve their management skills so they can achieve higher levels of performance.",
    "I insist on intense hard work and high productivity from my subordinates.",
    "I establish ambitious goals that challenge subordinates to achieve performance levels above the standard.",
    "I generate, or help others obtain, the resources necessary to implement their innovative ideas.",
    "When someone comes up with a new idea, I help sponsor them to follow through on it.",
    "I make certain that all employees are clear about our policies, values, and objectives.",
    "I make certain that others have a clear picture of how their job fits with others in the organization.",
    "I build cohesive, committed teams of people.",
    "I give my subordinates regular feedback about how I think they're doing.",
    "I articulate a clear vision of what can be accomplished in the future.",
    "I foster a sense of competitiveness that helps members of my work group perform at higher levels than members of other units.",
    "I assure that regular reports and assessments occur in my unit.",
    "I interpret and simplify complex information so that it makes sense to others and can be shared throughout the organization.",
    "I facilitate effective information sharing and problem solving in my group.",
    "I foster rational, systematic decision analysis in my unit (e.g., logically analyzing component parts of problems) to reduce the complexity of important issues.",
    "I make sure that others in my unit are provided with opportunities for personal growth and development.",
    "I create an environment where involvement and participation in decisions are encouraged and rewarded.",
    "In groups I lead, I make sure that sufficient attention is given to both task accomplishment and to interpersonal relationships.",
    "When giving negative feedback to others, I foster their self- improvement rather than defensiveness or anger.",
    "I give others assignments and responsibilities that provide opportunities for their personal growth and development.",
    "I actively help prepare others to move up in the organization.",
    "I regularly come up with new, creative ideas regarding processes, products or procedures for my organization.",
    "I constantly restate and reinforce my vision of the future to members of my unit.",
    "I help others visualize a new kind of future that includes possibilities as well as probabilities.",
    "I am always working to improve the processes we use to achieve our desired output.",
    "I push my unit to achieve world-class competitive performance in service and/or products.",
    "By empowering others in my unit, I foster a motivational climate that energizes everyone involved.",
    "I have consistent and frequent personal contact with my internal and my external customers.",
    "I make sure that we assess how well we are meeting our customers’ expectations.",
    "I provide experiences for employees that help them become socialized and integrated into the culture of our organization.",
    "I increase the competitiveness of my unit by encouraging others to provide services and/or products that surprise and delight customers by exceeding their expectations.",
    "I have established a control system that assures consistency in quality, service, cost and productivity in my unit.",
    "I coordinate regularly with managers in other units in my organization.",
    "I routinely share information across functional boundaries in my organization to facilitate coordination.",
    "I use a measurement system that consistently monitors both work processes and outcomes.",
    "I clarify for members of my unit exactly what is expected of them.",
    "I assure that everything we do is focused on better serving our customers.",
    "I facilitate a climate of aggressiveness and intensity in my unit.",
    "I constantly monitor the strengths and weaknesses of our best competition and provide my unit with information on how we measure up.",
    "I facilitate a climate of continuous improvement in my unit.",
    "I have developed a clear strategy for helping my unit successfully accomplish my vision of the future.",
    "I capture the imagination and emotional commitment of others when I talk about my vision of the future.",
    "I facilitate a work environment where peers as well as subordinates learn from and help develop one another.",
    "I listen openly and attentively to others who give me their ideas, even when I disagree.",
    "When leading a group, I ensure collaboration and positive conflict resolution among group members.",
    "I foster trust and openness by showing understanding for the point of view of individuals who come to me with problems or concerns.",
    "I create an environment where experimentation and creativity are rewarded and recognized.",
    "I encourage everyone in my unit to constantly improve and update everything they do.",
    "I encourage all employees to make small improvements continuously in the way they do their jobs.",
    "I make sure that my unit continually gathers information on our customers' needs and preferences.",
    "I involve customers in my unit's planning and evaluations.",
    "I establish ceremonies and rewards in my unit that reinforce the values and culture of our organization.",
    "I maintain a formal system for gathering and responding to information that originates in other units outside my own.",
    "I initiate cross-functional teams or task forces that focus on important organizational issues.",
    "I help my employees strive for improvement in all aspects of their lives, not just in job related activities.",
    "I create a climate where individuals in my unit want to achieve higher levels of performance than the competition.",
]

# Define categories and corresponding questions
categories = {
    "Managing Acculturation": [10, 11, 34, 40, 56],
    "Managing the Control System": [4, 16, 19, 36, 39],
    "Managing Coordination": [17, 37, 38, 57, 58],
    "Managing Competitiveness": [15, 30, 35, 43, 60],
    "Energizing Employees": [3, 6, 7, 31, 42],
    "Managing Customer Service": [32, 33, 41, 54, 55],
    "Managing Teams": [12, 18, 21, 22, 49],
    "Managing Interpersonal Relationships": [1, 13, 23, 48, 50],
    "Managing the Development of Others": [5, 20, 24, 25, 47],
    "Managing Innovation": [2, 8, 9, 26, 51],
    "Managing the Future": [14, 27, 28, 45, 46],
    "Managing Continuous Improvement": [29, 44, 52, 53, 59]
}

# Collect responses for the 60 questions using sliders
responses = {}
for i, question in enumerate(questions):
    response = st.slider(question, 1, 4, key=i)
    responses[i + 1] = response

# Calculate average scores for each category
category_scores = {}
for category, question_indices in categories.items():
    total_score = sum(responses[q] for q in question_indices)
    average_score = total_score / len(question_indices)
    category_scores[category] = average_score

# Submit button
if st.button("Submit"):
    st.write("Here are your responses:")
    st.write(f"Name: {name}")
    st.write(f"Work Relation: {work_relation}")

    # Spider graph plot
    categories_list = list(categories.keys())
    values = list(category_scores.values())
    
    # Number of variables we're plotting
    num_vars = len(categories_list)

    # Compute angle of each axis
    angles = np.linspace(0, 2 * np.pi, num_vars, endpoint=False).tolist()

    # The plot is a circle, so we need to "complete the loop"
    values += values[:1]
    angles += angles[:1]

    fig, ax = plt.subplots(figsize=(6, 6), subplot_kw=dict(polar=True))
    ax.set_yticks([1, 2, 3, 4])  # Adjust the ticks to reflect the response range
    ax.set_yticklabels([1, 2, 3, 4])  # Adjust the tick labels accordingly
    ax.set_xticks(angles[:-1])
    ax.set_xticklabels(categories_list)

    # Fill the area inside the radar
    ax.fill(angles, values, color='red', alpha=0.25)

    # Draw the outline
    ax.plot(angles, values, color='red', linewidth=2)

    # Show the plot
    st.pyplot(fig)

  
