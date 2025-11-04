from pytrends.request import TrendReq
import plotly.express as px
def show_trends(keyword):
    try:
        pytrends = TrendReq(hl='en-US', tz=360)
        pytrends.build_payload([keyword], timeframe='today 12-m')
        data = pytrends.interest_by_region()
        data = data.reset_index()
        fig = px.choropleth(data, locations="geoName", locationmode="country names",
                            color=keyword, title="Global Dream Trends", color_continuous_scale="Purples")
        return fig
    except Exception:
        return px.scatter(title="Trend data unavailable.")
