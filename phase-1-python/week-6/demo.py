import plotly.express as px
import seaborn as sns

tips = sns.load_dataset("tips")

fig = px.line(tips, y="tip", title="Tip Line Graph")
fig.show()
