# %% 
# function to page through SODA (Socrata Open Data API)
# takes an endpoint and returns a list of endpoints to use

def page_soda(
    endpoint='https://data.lacity.org/resource/e7h6-4a3e.csv?',
    limit=10000, off=0, order_by=''
    ):

        output = []
        if limit <= 10000:
            output.append(f'{endpoint}&$limit={limit}')
        else:
            pages = limit // 10000
            for i in range(pages + 1):
                pages_urls = f'{endpoint}&$limit=10000&$offset={i * 10000}&$order={order_by}'
                output.append(pages_urls)

        return output


if __name__ == "__main__":
    pages = page_soda(limit=40000, order_by='spaceid')
    print(pages)
# %%
