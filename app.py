import streamlit as st

import time_series_visualizer

# Title and Introduction
st.title('Time Series Visualizer')
st.write('Select a visualization to display:')

# Visualization selection
option = st.selectbox(
    'Choose a visualization:',
    ('Line Plot', 'Bar Plot', 'Box Plot')
)

# Display the selected visualization
if option == 'Line Plot':
    st.pyplot(time_series_visualizer.draw_line_plot())
elif option == 'Bar Plot':
    st.pyplot(time_series_visualizer.draw_bar_plot())
elif option == 'Box Plot':
    st.pyplot(time_series_visualizer.draw_box_plot())
