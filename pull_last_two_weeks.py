# %%
import datetime
import matplotlib.pyplot as plt
import numpy as np
import pandas as pd


# %%
today = datetime.datetime.now()
this_monday = today - datetime.timedelta(days=datetime.datetime.weekday(today))
last_monday = this_monday - datetime.timedelta(days=7)
this_monday_str = this_monday.strftime('%Y-%m-%d')
last_monday_str = last_monday.strftime('%Y-%m-%d')

last_week = pd.date_range(start=last_monday_str, periods=7, freq='D')
this_week = pd.date_range(start=this_monday_str, periods=7, freq='D')


# %%
tweek_values = np.random.randn(len(this_week)).cumsum()
lweek_values = np.random.randn(len(last_week)).cumsum()
df = pd.DataFrame(
    {
        'x': np.concatenate((lweek_values, tweek_values))
    }, index=last_week.append(this_week)
    
)


# %%
my_fig, axes = plt.subplots(2, 1)
axes[0].plot(lweek_values)
axes[1].plot(tweek_values)


qticks_lweek = axes[0].set_xticks(np.arange(7))
md_ticks_lweek = [i.strftime('%a %m/%d') for i in last_week]
labels_lweek = axes[0].set_xticklabels(
    md_ticks_lweek,
    rotation=0, fontsize='small'
)


qticks_tweek = axes[1].set_xticks(np.arange(7))
md_ticks_tweek = [i.strftime('%a %m/%d') for i in this_week]
labels_lweek = axes[1].set_xticklabels(
    md_ticks_tweek,
    rotation=0, fontsize='small'
)


# %%


# %%
# time series and annotations
time_fig = plt.figure()
ax = time_fig.add_subplot(1, 1, 1)

raw_source = 'https://raw.githubusercontent.com/wesm/pydata-book/2nd-edition/examples/spx.csv'
raw_df = pd.read_csv(raw_source, index_col=0, parse_dates=True)
spx = raw_df['SPX']

#ax.plot(data=spx, style='k-')
spx.plot(ax=ax, style='k-')

crisis_data = [
    (datetime.datetime(2007, 10, 11), 'Peak of bull market'),
    (datetime.datetime(2008, 3,  12), 'Bear Stearns fails'),
    (datetime.datetime(2008, 9,  15), 'Lehman bankruptcy'),
]

for date, label in crisis_data:
    ax.annotate(label, xy=(date, spx.asof(date) + 80),
        xytext=(date, spx.asof(date) + 225),
        arrowprops=dict(facecolor='black', headwidth=4, width=2,
            headlength=4),
        horizontalalignment='left', verticalalignment='top')

ax.set_xlim(['1/1/2007', '1/1/2011'])
ax.set_ylim([600, 1800])

ax.set_title('A few dates in the financial crisis')


# %%



# %%



# %%