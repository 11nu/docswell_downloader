#!/usr/bin/env python3

# Copyright 2022 @11nu (https://github.com/11nu)
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#     https://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.

import os
from urllib.parse import urlparse

import img2pdf
import requests
from bs4 import BeautifulSoup
from tqdm import tqdm

BASE_DIR = os.path.dirname(os.path.abspath(__file__))
USER_AGENT = "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/105.0.0.0 Safari/537.36"  # noqa: E501

# Override here the URL of the docswell slide you want to download.
slide_url = "https://www.docswell.com/s/ku-suke/LK7J5V-hello-docswell"


def download_image(url, headers=None, timeout=5):
    response = requests.get(
        url, allow_redirects=False, timeout=timeout, headers=headers)

    if response.status_code != 200:
        err = Exception(f"HTTP status: {response.status_code}")
        raise err

    content_type = response.headers["content-type"]
    if "image" not in content_type:
        err = Exception(f"Content-Type: {content_type}")
        raise err

    return response.content


def main():
    slide_filename = urlparse(slide_url).path.split("/")[3]  # LK7J5V-hello-docswell
    slide_key = slide_filename[:6]  # LK7J5V
    embed_url = f"https://www.docswell.com/slide/{slide_key}/embed"

    request_headers = {
        "User-Agent": USER_AGENT,
    }

    html = requests.get(embed_url, headers=request_headers)
    soup = BeautifulSoup(html.content, "html.parser")
    thumbnail_image_elements = soup.find(
        "main", id="player").find_all("li", class_="splide__slide c-thumbnail")

    slide_image_urls = []
    for element in thumbnail_image_elements:
        thumbnail_image_url = urlparse(
            element.find("img")["data-splide-lazy"])._replace(query="").geturl()
        slide_image_url = thumbnail_image_url.replace("thumbnail", "page")

        slide_image_urls.append(slide_image_url)

    slide_images = []
    for slide_image_url in tqdm(slide_image_urls, desc="download"):
        slide_image = download_image(slide_image_url, headers=request_headers)

        slide_images.append(slide_image)

    output_dir = os.path.join(BASE_DIR, "output")
    abs_output_filepath = os.path.join(
        output_dir, os.path.basename(f"{slide_filename}.pdf"))
    with open(abs_output_filepath, "wb") as pdf_file:
        pdf_file.write(img2pdf.convert(slide_images))

    print(f"The file has been saveds: {abs_output_filepath}")


if __name__ == "__main__":
    main()
