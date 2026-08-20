
import streamlit as st

# ---------------- PAGE CONFIG ----------------

st.set_page_config(
    page_title="Avengers | Iconic Quotes",
    page_icon="⚡",
    layout="wide"
)

# ---------------- CUSTOM CSS ----------------

st.markdown("""
<style>

@import url('https://fonts.googleapis.com/css2?family=Bebas+Neue&family=Cinzel:wght@500;700&family=Montserrat:wght@400;600&display=swap');

.stApp {
    background:
        radial-gradient(circle at top, #252525 0%, #0b0b0b 45%, #000000 100%);
    color: white;
}

/* Main Title */

.main-title {
    text-align: center;
    font-family: 'Bebas Neue', sans-serif;
    font-size: 85px;
    letter-spacing: 10px;
    color: white;
    margin-top: 20px;
    margin-bottom: 0;
    text-shadow:
        0px 0px 15px rgba(255,255,255,0.3),
        0px 0px 35px rgba(255,0,0,0.4);
}

.subtitle {
    text-align: center;
    font-family: 'Cinzel', serif;
    font-size: 18px;
    color: #aaa;
    letter-spacing: 5px;
    margin-bottom: 50px;
}

/* Cards */

.card {
    background: linear-gradient(
        145deg,
        rgba(40,40,40,0.95),
        rgba(8,8,8,0.98)
    );

    border-radius: 20px;
    overflow: hidden;

    border: 1px solid rgba(255,255,255,0.15);

    box-shadow:
        0px 15px 40px rgba(0,0,0,0.7);

    transition: 0.4s ease;

    margin-bottom: 35px;
}

.card:hover {
    transform: translateY(-10px) scale(1.02);

    border: 1px solid rgba(255,255,255,0.4);

    box-shadow:
        0px 25px 60px rgba(0,0,0,0.9);
}

/* Character Name */

.character-name {
    font-family: 'Bebas Neue', sans-serif;
    font-size: 42px;
    letter-spacing: 4px;
    text-align: center;
    margin-top: 15px;
    color: white;
}

/* Quote */

.quote {
    font-family: 'Cinzel', serif;
    font-size: 21px;
    line-height: 1.7;
    text-align: center;
    padding: 10px 30px 30px;
    color: #eeeeee;
}

.quote-mark {
    font-size: 55px;
    color: #777;
    font-family: Georgia, serif;
}

/* Footer */

.footer {
    text-align: center;
    color: #666;
    font-family: 'Montserrat', sans-serif;
    margin-top: 30px;
    padding: 30px;
    letter-spacing: 3px;
}

</style>
""", unsafe_allow_html=True)


# ---------------- TITLE ----------------

st.markdown(
    '<div class="main-title">MARVEL LEGENDS</div>',
    unsafe_allow_html=True
)

st.markdown(
    '<div class="subtitle">ICONIC HEROES • ICONIC WORDS</div>',
    unsafe_allow_html=True
)
st.markdown(
    '<div class="subtitle">Created by Shahid Mansuri</div>',
    unsafe_allow_html=True
)


# ---------------- AVENGERS DATA ----------------

avengers = [

    {
        "name": "IRON MAN",
        "image": "C:\\Users\\shahi\\OneDrive\\Desktop\\Iron_Man_Mark_III_armor_from_Iron_Man_(2008_film).jpg",
        "quote": "Truth is...I am Iron Man."
    },

    {
        "name": "CAPTAIN AMERICA",
        "image": "C:\\Users\\shahi\\OneDrive\\Desktop\\captain america.jpg",
        "quote": "I can do this all day."
    },

    {
        "name": "THANOS",
        "image": "C:\\Users\\shahi\\OneDrive\\Desktop\\Behold_The_Mad_Titan_Thanos.webp",
        "quote": "The hardest choices require the strongest wills."
    },

    {
        "name": "DOCTOR STRANGE",
        "image": "C:\\Users\\shahi\\OneDrive\\Desktop\\dr strange.jpg",
        "quote": "I love you. I love you in every universe. It's not that I don't want to care or want someone to care for me... it's just I get scared."
    }

]


# ---------------- DISPLAY CARDS ----------------

for i in range(0, len(avengers), 2):

    col1, col2 = st.columns(2, gap="large")

    # LEFT CARD

    with col1:

        hero = avengers[i]

        st.markdown(
            '<div class="card">',
            unsafe_allow_html=True
        )

        st.image(
            hero["image"],
            use_container_width=True
        )

        st.markdown(
            f'<div class="character-name">{hero["name"]}</div>',
            unsafe_allow_html=True
        )

        st.markdown(
            f"""
            <div class="quote">
                <span class="quote-mark">“</span>
                <br>
                {hero["quote"]}
                <br>
                <span class="quote-mark">”</span>
            </div>
            """,
            unsafe_allow_html=True
        )

        st.markdown(
            '</div>',
            unsafe_allow_html=True
        )


    # RIGHT CARD

    with col2:

        hero = avengers[i + 1]

        st.markdown(
            '<div class="card">',
            unsafe_allow_html=True
        )

        st.image(
            hero["image"],
            use_container_width=True
        )

        st.markdown(
            f'<div class="character-name">{hero["name"]}</div>',
            unsafe_allow_html=True
        )

        st.markdown(
            f"""
            <div class="quote">
                <span class="quote-mark">“</span>
                <br>
                {hero["quote"]}
                <br>
                <span class="quote-mark">”</span>
            </div>
            """,
            unsafe_allow_html=True
        )

        st.markdown(
            '</div>',
            unsafe_allow_html=True
        )


# ---------------- FOOTER ----------------

st.markdown(
    """
    <div class="footer">
        ⚡ MARVEL LEGENDS ⚡
        <br><br>
        HEROES • VILLAINS • LEGENDS
    </div>
    """,
    unsafe_allow_html=True
)



