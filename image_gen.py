from openai import OpenAI
import user_config as uc
import webbrowser
from datetime import datetime

import requests
from PIL import Image

client = OpenAI(api_key=uc.openai_key)

def generate_img(promt):
    response = client.images.generate(
        model='dall-e-2',
        prompt=promt,
        n=1,
        size="1024x1024",
        quality='standard'
    )

    img_url = response.data[0].url
    ##get data from url:
    data = requests.get(img_url).content
    ## save data in file:
    date = datetime.datetime.now()
    f = open(f'img_{date.strftime('%H.%M.%S__%d.%m.%y')}.jpg', 'wb')
    f.write(data)
    f.close()
    ## Open image in webbrowser:
    # webbrowser.open(img_url)

