import streamlit as st

def style_background_home():
    st.markdown("""
               <style>
                    .stApp{
                        background : #F15888 !important;
                }
                </style>
                 
                """,
                unsafe_allow_html = True)
    

def style_background_dashboard():
    st.markdown("""
               <style>
                    .stApp{
                        background : #E0E3FF !important;
                }
                </style>
                 
                """,
                unsafe_allow_html = True)
    
def style_base__layout():
    st.markdown("""
               <style>
                @import url("https://fonts.googleapis.com/css2?family=Roboto:wght@400;700&display=swap");
                @import url('https://fonts.googleapis.com/css2?family=Outfit:wght@100..900&display=swap');
                /* Hide Top Bar of streamlit */
                    #MainMenu , footer, header{
                        visibilty: hidden;
                    }
                    .block-container{
                    padding-top:1.5rem !important;
                    }
                    h1{
                        font-family: 'Roboto', sans-serif !important;
                        font-size: 3.5rem !important;
                        line-height:1.1 !important;
                        margin-bottom: 0 rem !important;
                        color: #E0E3FF !important;
                    }
                    h2{
                        font-family: 'Roboto', sans-serif !important;
                        font-size: 3.5rem !important;
                        line-height:1.1 !important;
                        margin-bottom: 0 rem !important;
                        color: #E0E3FF !important;
                    }
                    h3, h4, p {
                        font-family: 'Outfit', sans-serif !important;
                        color: #E0E3FF !important;
                    }
                    button{
                        border-radius: 1.5 rem !important;
                        background: #EB459E !important;
                        color: white !important;
                        padding: 10px 20px !important;
                        border: none !important;
                        transition: transform 0.25s ease-in-out !important;
                    }
                    button[kind = "Secondary"] {
                        border-radius: 1.5 rem !important;
                        background: #EB459E !important;
                        color: white !important;
                        padding: 10px 20px !important;
                        border: none !important;
                        transition: transform 0.25s ease-in-out !important;

                    button[kind = "Tertiary"] {
                        border-radius: 1.5 rem !important;
                        background: #EB459E !important;
                        color: white !important;
                        padding: 10px 20px !important;
                        border: none !important;
                        transition: transform 0.25s ease-in-out !important;
                
                }    
                        font-family: 'Roboto', sans-serif !important;
                        background-color: #F15888 !important;
                        color: #E0E3FF !important;
                    }

                </style>
                 
                """,
                unsafe_allow_html = True)