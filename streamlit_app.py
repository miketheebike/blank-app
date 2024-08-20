import streamlit as st
import plotly.graph_objs as go
import pandas as pd

# # Initialize a session state to store the probability distribution
# if 'prob_dist' not in st.session_state:
#     st.session_state.prob_dist = [0.2, 0.2, 0.2, 0.2, 0.2]  # Example with 5 bars

# # Function to update probability distribution based on clicks
# def update_prob_dist(click_data):
#     bar_idx = click_data['points'][0]['x']
#     new_height = click_data['points'][0]['y']
#     st.session_state.prob_dist[bar_idx] = new_height / sum(st.session_state.prob_dist)

# # Plotting the probability distribution
# def plot_prob_dist():
#     fig = go.Figure(
#         data=[
#             go.Bar(x=list(range(len(st.session_state.prob_dist))),
#                    y=st.session_state.prob_dist, marker_color='blue')
#         ]
#     )
#     fig.update_layout(
#         title="Click on the bars to adjust probability distribution",
#         xaxis_title="Option",
#         yaxis_title="Probability",
#         yaxis=dict(range=[0, 1]),
#     )
#     return fig

# st.title("Interactive Probability Distribution Survey")

# # Display the bar chart
# fig = plot_prob_dist()
# click_data = st.plotly_chart(fig, use_container_width=True)

# # Update the probability distribution based on user interaction
# if click_data is not None:
#     update_prob_dist(click_data['clickData'])

# # Display the updated probability distribution in a table
# st.write("Current Probability Distribution")
# prob_df = pd.DataFrame({
#     "Option": [f"Option {i+1}" for i in range(len(st.session_state.prob_dist))],
#     "Probability": st.session_state.prob_dist
# })
st.table(prob_df)
