import base64
from datetime import datetime
from html import escape
from pathlib import Path
import streamlit as st

PROFILE = {
    "name": "Biswajeet Behera",
    "role": "Aspiring Data Scientist",
    "study": "M.Tech, CSE (Data Science), in progress",
    "stack": "Python, SQL, Power BI, Excel",
    "focus": "Analytics, ML, data pipelines, Rag System",
    "lead": "Detail-oriented CSE postgraduate specializing in Data Science with expertise in: "
            " machine learning, statistical analysis, and Python/SQL development. "
            "Proven ability to bridge the gap between analytical theory and practical business research. "
            "Looking to leverage technical skills and predictive modeling capabilities in an entry-level Data position.",
    "open_to": "open to internships and data roles",
    "email": "work.biswajeetbehera@gmail.com",
    "linkedin": "https://www.linkedin.com/in/biswajeet-in",
    "github": "https://github.com/biswajeet-gitcom",
}

GH = "https://github.com/biswajeet-gitcom/"

# The featured project; its flow drives the animated pipeline strip inside its card.
FEATURED = {
    "name": "swiggy-food-project",
    "title": "Swiggy end-to-end data platform",
    "text": "Raw food-delivery data modelled in a warehouse, analysed in Python, then served through an app and a chatbot, with revenue forecasting.",
    "url": GH + "swiggy-food-project",
    "flow": ["Snowflake", "dbt", "Python EDA", "Streamlit", "LLM / RAG chatbot"],
    "tags": ["Snowflake", "dbt", "Python", "Streamlit"],
}

# Shown under the signal bars. Edit freely; the layout follows.
RESEARCH = {
    "title": "Fact and claim verification in RAG systems",
    "gap": "RAG answers are built from retrieved text, yet few systems check whether each "
           "claim in the answer is actually supported by that evidence.",
    "flow": ["query", "retrieve", "verify claims", "generate"],
    "highlight": 2,
    "tags": ["RAG", "Fact checking", "Claim verification", "LLM evaluation"],
}

PROJECTS = [
    {
        "name": "supply_chain_logistic",
        "title": "Supply chain and logistics study",
        "text": "Data cleaning, EDA, business KPIs, profitability, operational bottlenecks, time trends and late-delivery prediction.",
        "tags": ["Python", "Machine learning", "Jupyter"],
        "url": GH + "supply_chain_logistic",
    },
    {
        "name": "Superstore_sales_analysis_Power-BI",
        "title": "Superstore sales and profit dashboard",
        "text": "Full Power BI report and dashboard covering sales, profit, customers and logistics.",
        "tags": ["Power BI", "DAX", "Excel"],
        "url": GH + "Superstore_sales_analysis_Power-BI",
    },
    {
        "name": "lung_cancer_analysis",
        "title": "Lung cancer analysis and prediction",
        "text": "Cancer analysis and prediction using machine learning and data science.",
        "tags": ["Python", "Machine learning", "Jupyter"],
        "url": GH + "lung_cancer_analysis",
    },
    {
        "name": "Restaurant-data-analysis",
        "title": "Restaurant sales analysis",
        "text": "Restaurant sales analysis with interactive dashboards.",
        "tags": ["Power BI", "Excel"],
        "url": GH + "Restaurant-data-analysis",
    },
    {
        "name": "HR-Analysis-Report",
        "title": "HR attrition report",
        "text": "Employee attrition trends and the factors behind them.",
        "tags": ["Power BI", "HR analytics"],
        "url": GH + "HR-Analysis-Report",
    },
    {
        "name": "Cognifyz_intern",
        "title": "Cognifyz data analysis internship",
        "text": "First data analysis internship tasks at Cognifyz Tech.",
        "tags": ["Python", "EDA", "Jupyter"],
        "url": GH + "Cognifyz_intern",
    },
]

SKILLS = {
    "languages_and_analysis": ["Python", "SQL", "MySQL", "PostgreSQL"],
    "data_and_ml": ["Pandas", "NumPy", "scikit-learn", "Jupyter"],
    "bi_and_tools": ["Power BI", "DAX", "Excel", "Snowflake", "dbt", "Git", "GitHub"],
    "focus": ["Analytics", "ML prediction", "Data pipelines", "Streamlit", "LLM and RAG"],
    "research": ["Literature review", "Research methodology", "Experiment design", "Model evaluation", "Fact checking", "Scientific writing"],
}

RESUME_PATH = Path(__file__).parent / "assets" / "resume.pdf"

# --------------------------------------------------------------------------
# Page setup and CSS
# --------------------------------------------------------------------------
st.set_page_config(
    page_title=f"{PROFILE['name']} | {PROFILE['role']}",
    page_icon="🔞",
    layout="wide",
    initial_sidebar_state="collapsed",
)

CSS = """
<style>
@import url('https://fonts.googleapis.com/css2?family=JetBrains+Mono:wght@400;700&family=Space+Grotesk:wght@500;700&display=swap');
:root{--bg:#04080a;--panel:#071014;--line:#12301f;--tx:#b6ffd8;--dim:#6fa88a;--g:#39ff88;--m:#ff4fd8;--c:#5ce1ff}
[data-testid="stSidebar"],[data-testid="stSidebarCollapsedControl"],[data-testid="stHeader"],[data-testid="stToolbar"],[data-testid="stDecoration"],#MainMenu,footer{display:none!important}
[data-testid="stApp"]{background:
 radial-gradient(900px 420px at 50% -80px,rgba(57,255,136,.14),transparent 70%),
 radial-gradient(rgba(57,255,136,.10) 1px,transparent 1px) 0 0/26px 26px,var(--bg);color:var(--tx)}
[data-testid="stMain"]{scroll-behavior:smooth}
[data-testid="stMainBlockContainer"],.block-container{max-width:1080px;padding:84px 24px 90px!important}
[data-testid="stVerticalBlock"]{gap:0!important}
[data-testid="stElementContainer"]{margin:0!important}
.pf,.pf *{box-sizing:border-box}
.pf{font:14px/1.65 'JetBrains Mono',monospace;color:var(--tx)}
.pf a{color:inherit;text-decoration:none}
.pf h1,.pf h2,.pf h3{font-family:'Space Grotesk',sans-serif;color:#fff;margin:0;letter-spacing:-.02em}
.k{color:var(--dim)}.g{color:var(--g)}.m{color:var(--m)}
.scan{position:fixed;inset:0;pointer-events:none;z-index:60;background:repeating-linear-gradient(0deg,rgba(255,255,255,.03) 0 1px,transparent 1px 3px)}

.nav{position:fixed;top:0;left:0;right:0;z-index:50;display:flex;justify-content:space-between;align-items:center;padding:12px max(24px,calc(50% - 540px));background:rgba(4,8,10,.82);backdrop-filter:blur(10px);border-bottom:1px solid var(--line);font-size:13px}
.nav b{font-weight:700;color:#fff}.nav nav{display:flex;gap:22px;align-items:center}
.nav nav a{color:var(--dim);transition:color .2s}.nav nav a:hover{color:var(--g)}
.on{display:inline-flex;align-items:center;gap:7px;color:var(--g);font-size:12px}
.on i{width:7px;height:7px;border-radius:50%;background:var(--g);box-shadow:0 0 10px var(--g);animation:bl 1.6s ease-in-out infinite}
@keyframes bl{50%{opacity:.25}}

.gut{position:fixed;left:max(10px,calc(50% - 650px));top:84px;z-index:1;color:var(--g);opacity:.16;font-size:12px;line-height:1.65;text-align:right;pointer-events:none;display:none}
@media(min-width:1280px){.gut{display:block}}

.hero{display:grid;grid-template-columns:minmax(0,1.2fr) minmax(0,1fr);gap:28px;padding:34px 0 26px;scroll-margin-top:70px}
.term{display:flex;flex-direction:column;border:1px solid var(--line);border-radius:10px;background:rgba(7,16,20,.8);overflow:hidden}
.tb{display:flex;gap:7px;align-items:center;padding:10px 14px;border-bottom:1px solid var(--line);color:var(--dim);font-size:12px}
.tb i{width:10px;height:10px;border-radius:50%;background:var(--line)}.tb i:first-child{background:var(--g)}
.tbody{flex:1;display:flex;flex-direction:column;padding:22px 22px 24px}.tbody .cta{margin-bottom:22px}.tbody .pr{margin-top:auto;color:var(--dim)}.cur{display:inline-block;width:8px;height:15px;background:var(--g);vertical-align:-2px;animation:bl 1.1s steps(1) infinite}
.hero h1{font-size:clamp(34px,6vw,58px);line-height:1.02;margin:8px 0 14px;font-weight:700}
.ty{display:inline-block;overflow:hidden;white-space:nowrap;vertical-align:bottom;width:0;max-width:100%;border-right:2px solid var(--g);animation:ty 3.2s steps(var(--n)) infinite alternate}
@keyframes ty{to{width:calc(var(--n)*1ch)}}
.nf{display:grid;grid-template-columns:auto 1fr;gap:2px 16px;margin:0 0 20px;font-size:13px}.nf dt{color:var(--g)}.nf dd{margin:0;color:var(--tx)}
.lead{color:var(--dim);margin:16px 0 20px;max-width:46ch}
.cta{display:flex;flex-wrap:wrap;gap:10px}
.btn{display:inline-block;padding:8px 14px;border:1px solid var(--g);border-radius:6px;color:var(--g);font-size:13px;transition:all .2s}
.btn:hover{background:var(--g);color:#04080a;box-shadow:0 0 22px rgba(57,255,136,.45)}
.btn.alt{border-color:var(--line);color:var(--tx)}.btn.alt:hover{border-color:var(--m);background:transparent;color:var(--m);box-shadow:none}

.side{display:flex;flex-direction:column;gap:12px}
.hm,.bars{position:relative;border:1px solid var(--line);background:var(--panel);border-radius:8px;padding:12px}
.hm{padding:26px 14px 14px}
.heat{display:grid;grid-auto-flow:column;grid-template-rows:repeat(7,1fr);grid-template-columns:repeat(24,1fr);gap:3px}
.heat i{aspect-ratio:1;border-radius:3px;background:#0a1a14}
.heat .a{background:#0c2a1c}.heat .b{background:#0e4a2a}
.heat .t{background:var(--g);box-shadow:0 0 9px rgba(57,255,136,.55);animation:lit .7s ease-out both;animation-delay:var(--d)}
@keyframes lit{from{background:#0a1a14;box-shadow:none;transform:scale(.55)}}
.bars{display:flex;align-items:flex-end;gap:7px;height:118px;padding:14px}
.bars i{flex:1;height:var(--h);background:linear-gradient(var(--g),#0b7a46);transform-origin:bottom;animation:gr 2.2s ease-in-out infinite alternate;animation-delay:var(--d)}
@keyframes gr{from{transform:scaleY(.45)}}
.cap{position:absolute;top:6px;right:10px;font-size:10px;color:var(--dim)}

.rs{border:1px solid var(--line);border-left:2px solid var(--m);background:var(--panel);border-radius:8px;padding:14px 16px}
.rs .fn{display:flex;justify-content:space-between;align-items:center;font-size:12px;color:var(--m)}
.rs h3{font-size:18px;line-height:1.25;margin:8px 0 8px}
.rs p{margin:0 0 12px;color:var(--dim);font-size:12.5px}
.rf{display:flex;flex-wrap:wrap;align-items:center;gap:6px;margin:0 0 12px;font-size:11px}
.rf span{padding:3px 9px;border:1px solid var(--line);border-radius:99px;background:var(--bg)}
.rf em{font-style:normal;color:var(--dim)}
.rf .hl{border-color:var(--m);color:var(--m);animation:pk 2.4s ease-in-out infinite}
@keyframes pk{50%{box-shadow:0 0 14px rgba(255,79,216,.45)}}
.feat{position:relative;display:block;margin:12px 0 14px;padding:20px 20px 18px;border:1px solid var(--line);border-radius:10px;background:var(--panel);overflow:hidden;transition:border-color .2s,box-shadow .2s}
.feat:hover{border-color:var(--g);box-shadow:0 0 30px rgba(57,255,136,.14)}
.feat .fn{display:flex;justify-content:space-between;color:var(--g);font-size:12px}
.feat h3{font-size:clamp(22px,3.4vw,30px);margin:8px 0 6px}.feat p{margin:0 0 16px;color:var(--dim);max-width:60ch}
.flow{display:flex;align-items:center;justify-content:space-between;gap:8px;margin:0 0 14px;padding:12px 14px;border:1px dashed var(--line);border-radius:8px;position:relative;overflow:hidden}
.flow span{position:relative;z-index:2;padding:4px 12px;border:1px solid var(--line);border-radius:99px;background:var(--bg);font-size:12px;color:var(--tx);white-space:nowrap}
.flow::before{content:"";position:absolute;left:4%;right:4%;top:50%;height:1px;background:var(--line)}
.flow::after{content:"";position:absolute;top:calc(50% - 3px);left:4%;width:7px;height:7px;border-radius:50%;background:var(--g);box-shadow:0 0 12px var(--g);animation:mv 4.5s linear infinite}
@keyframes mv{to{left:96%}}

.sec{scroll-margin-top:76px;margin:0 0 56px}
.sh{display:flex;align-items:baseline;gap:12px;margin:0 0 18px;padding-bottom:10px;border-bottom:1px solid var(--line)}
.sh h2{font-size:26px;font-weight:700}.sh span{color:var(--dim);font-size:13px;margin-left:auto}

.pg{display:grid;grid-template-columns:repeat(auto-fill,minmax(300px,1fr));gap:14px}
.pc{position:relative;display:block;padding:16px 16px 14px;border:1px solid var(--line);border-radius:8px;background:var(--panel);transition:transform .2s,border-color .2s,box-shadow .2s}
.pc::before,.pc::after{content:"";position:absolute;width:12px;height:12px;border:2px solid var(--g);opacity:0;transition:opacity .2s}
.pc::before{top:-1px;left:-1px;border-right:0;border-bottom:0}.pc::after{right:-1px;bottom:-1px;border-left:0;border-top:0}
.pc:hover{transform:translateY(-3px);border-color:var(--g);box-shadow:0 0 26px rgba(57,255,136,.14)}.pc:hover::before,.pc:hover::after{opacity:1}
.pc .fn{display:flex;justify-content:space-between;gap:10px;color:var(--g);font-size:12px}
.pc h3{font-size:19px;margin:8px 0 6px}.pc p{margin:0 0 12px;color:var(--dim);font-size:13px;min-height:62px}
.tg{display:flex;flex-wrap:wrap;gap:6px}.tg span{font-size:11px;padding:2px 9px;border:1px solid var(--line);border-radius:99px;color:var(--c)}

.sg{display:grid;grid-template-columns:repeat(auto-fit,minmax(210px,1fr));gap:14px}
.sk{border:1px solid var(--line);background:var(--panel);border-radius:8px;padding:14px}
.sk .gk{color:var(--m);font-size:12px;margin-bottom:10px}
.sk .tg span{color:var(--tx)}

.ct{display:grid;grid-template-columns:minmax(0,1.3fr) minmax(0,1fr);gap:14px}
.ct .big{font:700 clamp(22px,3.6vw,34px)/1.15 'Space Grotesk',sans-serif;color:#fff;margin:6px 0 16px}
.ln{display:flex;flex-direction:column;gap:8px;padding:16px;border:1px solid var(--line);border-radius:8px;background:var(--panel)}
.ln a{display:flex;justify-content:space-between;color:var(--tx);padding:3px 0;border-bottom:1px dashed var(--line)}.ln a:hover{color:var(--g)}

.status{position:fixed;left:0;right:0;bottom:0;z-index:55;display:flex;gap:18px;align-items:center;padding:5px max(24px,calc(50% - 540px));background:#071014;border-top:1px solid var(--line);color:var(--dim);font-size:11px}
.status .r{margin-left:auto}

@media(max-width:820px){
 .hero,.ct{grid-template-columns:1fr}.nav nav{gap:14px}.nav .on{display:none}.flow{flex-wrap:wrap;justify-content:flex-start}.flow::before,.flow::after{display:none}
 .status span:nth-child(3){display:none}}
@media(prefers-reduced-motion:reduce){.pf *{animation:none!important}.ty{width:calc(var(--n)*1ch)}}
</style>
"""


def resume_button() -> str:
    """Inline download link, shown only if assets/resume.pdf exists."""
    if not RESUME_PATH.exists():
        return ""
    data = base64.b64encode(RESUME_PATH.read_bytes()).decode()
    return (
        f'<a class="btn" download="Biswajeet_Behera_Resume.pdf" '
        f'href="data:application/pdf;base64,{data}">resume.pdf</a>'
    )


def tags(items):
    return "".join(f"<span>{escape(t)}</span>" for t in items)


LETTER_B = ["####.", "#...#", "#...#", "####.", "#...#", "#...#", "####."]


def heatmap(cols: int = 24) -> str:
    """Activity-style grid with 'BB' picked out in bright cells (decorative, not real commit data)."""
    start = (cols - 11) // 2
    seed, cells = 7, []
    for c in range(cols):
        lc = c - start
        for r in range(7):
            seed = (seed * 9301 + 49297) % 233280
            v = seed / 233280
            letter = 0 <= lc < 11 and lc != 5 and LETTER_B[r][lc if lc < 5 else lc - 6] == "#"
            if letter:
                cells.append(f"<i class='t' style='--d:{lc * 70}ms'></i>")
            else:
                cells.append("<i class='a'></i>" if v > .78 else "<i class='b'></i>" if v > .9 else "<i></i>")
    return "".join(cells)


def build_page() -> str:
    p = PROFILE
    f = FEATURED
    gutter = "<br>".join(str(i) for i in range(1, 61))

    heat = heatmap()
    rs = RESEARCH
    steps = []
    for i, step in enumerate(rs["flow"]):
        steps.append(f"<span{' class=hl' if i == rs['highlight'] else ''}>{escape(step)}</span>")
    rflow = "<em>&rarr;</em>".join(steps)
    bars = "".join(
        f"<i style='--h:{h}%;--d:{d / 5:.1f}s'></i>"
        for d, h in enumerate([50, 80, 60, 95, 70, 85, 55, 100, 75, 90])
    )
    flow = "".join(f"<span>{escape(s)}</span>" for s in f["flow"])

    projects = "".join(
        f"""<a class="pc" href="{escape(x['url'])}" target="_blank" rel="noopener">
        <div class="fn"><span>{escape(x['name'])}/</span><span>open &#8599;</span></div>
        <h3>{escape(x['title'])}</h3><p>{escape(x['text'])}</p><div class="tg">{tags(x['tags'])}</div></a>"""
        for x in PROJECTS
    )

    skills = "".join(
        f"<div class='sk'><div class='gk'>{escape(k)}:</div><div class='tg'>{tags(v)}</div></div>"
        for k, v in SKILLS.items()
    )

    if p["email"]:
        mail = f"mailto:{p['email']}?subject=Hello%20Biswajeet"
        main_btn = f'<a class="btn" href="{escape(mail)}" style="display:inline-block">{escape(p["email"])}</a>'
        email_row = f'<a href="{escape(mail)}"><span>email</span><span class="g">&#8599;</span></a>'
    else:
        main_btn = (f'<a class="btn" href="{escape(p["linkedin"])}" target="_blank" rel="noopener" '
                    f'style="display:inline-block">message me on linkedin</a>')
        email_row = ""

    return f"""
<div class="pf">
<div class="scan"></div>
<div class="gut">{gutter}</div>

<div class="nav"><b>biswajeet<span class="g">_</span></b>
<nav><a href="#home">home</a><a href="#projects">projects</a><a href="#skills">skills</a><a href="#contact">contact</a>
<span class="on"><i></i>open to internships</span></nav></div>

<section class="hero" id="home">
 <div class="term">
  <div class="tb"><i></i><i></i><i></i><span style="margin-left:8px">biswajeet@portfolio:~</span></div>
  <div class="tbody">
   <div><span class="k">&#36;</span> whoami</div>
   <h1>{escape(p['name'])}</h1>
   <div><span class="g">role</span> <span class="ty" style="--n:{len(p['role'])}">{escape(p['role'])}</span></div>
   <p class="lead">{escape(p['lead'])}</p>
   <dl class="nf"><dt>study</dt><dd>{escape(p['study'])}</dd><dt>stack</dt><dd>{escape(p['stack'])}</dd><dt>focus</dt><dd>{escape(p['focus'])}</dd></dl>
   <div class="cta">{resume_button()}<a class="btn alt" href="{escape(p['github'])}" target="_blank" rel="noopener">github</a><a class="btn alt" href="{escape(p['linkedin'])}" target="_blank" rel="noopener">linkedin</a></div>
   <div class="pr"><span class="g">&#36;</span> <span class="cur"></span></div>
  </div>
 </div>
 <div class="side">
  <div class="hm"><span class="cap">// BB.map</span><div class="heat">{heat}</div></div>
  <div class="bars"><span class="cap">// signal</span>{bars}</div>
  <div class="rs">
   <div class="fn"><span>research/</span><span class="on"><i></i>in progress</span></div>
   <h3>{escape(rs['title'])}</h3>
   <p><span class="m">gap:</span> {escape(rs['gap'])}</p>
   <div class="rf">{rflow}</div>
   <div class="tg">{tags(rs['tags'])}</div>
  </div>
 </div>
</section>

<section class="sec" id="projects">
 <div class="sh"><h2>Projects</h2><span><span class="k">&#36;</span> ls ~/projects</span></div>
 <a class="feat" href="{escape(f['url'])}" target="_blank" rel="noopener">
  <div class="fn"><span>{escape(f['name'])}/</span><span>featured &#8599;</span></div>
  <h3>{escape(f['title'])}</h3><p>{escape(f['text'])}</p>
  <div class="flow">{flow}</div><div class="tg">{tags(f['tags'])}</div>
 </a>
 <div class="pg">{projects}</div>
</section>

<section class="sec" id="skills">
 <div class="sh"><h2>Skills</h2><span><span class="k">&#36;</span> ./skills --list</span></div>
 <div class="sg">{skills}</div>
</section>

<section class="sec" id="contact">
 <div class="sh"><h2>Contact</h2><span><span class="k">&#36;</span> ./say_hello.sh</span></div>
 <div class="ct">
  <div class="ln" style="justify-content:center">
   <div class="k">{escape(p['open_to'])}.</div>
   <div class="big">Open to internships and data roles. Let’s talk.</div>
   <div>{main_btn}</div>
  </div>
  <div class="ln">
   <a href="{escape(p['linkedin'])}" target="_blank" rel="noopener"><span>linkedin</span><span class="g">&#8599;</span></a>
   <a href="{escape(p['github'])}" target="_blank" rel="noopener"><span>github</span><span class="g">&#8599;</span></a>
   {email_row}
  </div>
 </div>
</section>

<div class="status"><span class="g">&#9679; online</span><span class="r">&copy; {datetime.now().year} {escape(p['name'])}</span></div>
</div>
"""


st.html(CSS)
st.html(build_page())