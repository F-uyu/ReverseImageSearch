from PIL import Image
import imagehash, requests, lxml, re, urllib.request, json, os
from bs4 import BeautifulSoup
from io import BytesIO

headers = {
    "User-Agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/110.0.0.0 Safari/537.36"
}
params = {
    "q": "red uniqlo shirt",
    "tbm": "isch", 
    "hl": "en",
    "gl": "us",
    "ijn": "0"
}

html = requests.get("https://www.google.com/search", params=params, headers=headers, timeout = 30)
soup = BeautifulSoup(html.text, "lxml")

def get_original_image():
    google_images = []
    numOfImage = 0
    all_script_tags = soup.select("script")
    matched_images_data = "".join(re.findall(r"AF_initDataCallback\(([^<]+)\);", str(all_script_tags)))
    matched_images_dump = json.dumps(matched_images_data)
    matched_images_json = json.loads(matched_images_dump)
    matched_google_image_data = re.findall(r'\"b-GRID_STATE0\"(.*)sideChannel:\s?{}}', matched_images_json)
    matched_google_images_thumbnails = ", ".join(
        re.findall(r'\[\"(https\:\/\/encrypted-tbn0\.gstatic\.com\/images\?.*?)\",\d+,\d+\]',
                   str(matched_google_image_data))).split(", ")
    thumbnails = [
        bytes(bytes(thumbnail, "ascii").decode("unicode-escape"), "ascii").decode("unicode-escape") for thumbnail in matched_google_images_thumbnails
    ]
    removed_matched_google_images_thumbnails = re.sub(
        r'\[\"(https\:\/\/encrypted-tbn0\.gstatic\.com\/images\?.*?)\",\d+,\d+\]', "", str(matched_google_image_data))
    matched_google_full_resolution_images = re.findall(r"(?:'|,),\[\"(https:|http.*?)\",\d+,\d+\]", removed_matched_google_images_thumbnails)

    full_res_images = [
        bytes(bytes(img, "ascii").decode("unicode-escape"), "ascii").decode("unicode-escape") for img in matched_google_full_resolution_images
    ]
    for index, (metadata, thumbnail, original) in enumerate(zip(soup.select(".isv-r.PNCib.MSM1fd.BUooTd"), thumbnails, full_res_images), start=1):
        if numOfImage == 10:
            break
        numOfImage += 1
        google_images.append({
            "title": metadata.select_one(".VFACy.kGQAp.sMi44c.lNHeqe.WGvvNb")["title"],
            "link": metadata.select_one(".VFACy.kGQAp.sMi44c.lNHeqe.WGvvNb")["href"],
            "source": metadata.select_one(".fxgdke").text,
            "thumbnail": thumbnail,
            "original": original
        })

    return google_images


"""crew = 'TestImages/img_1.jpg'
crew_img = Image.open(crew)
crew_hash = imagehash.whash(crew_img)
print(crew_hash)
short = 'https://di2ponv0v5otw.cloudfront.net/posts/2019/06/11/5d000d3e26219ffabbfae37d/m_5d000d46689ebcbdb63a2952.jpg'
short_img = Image.open(short)
short_hash = imagehash.whash(short_img)
print(short_hash)
similarity = crew_hash-short_hash
print(similarity)"""
