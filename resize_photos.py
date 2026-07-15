# -*- coding: utf-8 -*-
"""새 폴더(3) 실사진 → 웹용 리사이즈(EXIF 회전보정) → 어부림 images"""
import os
from PIL import Image, ImageOps

SRC = os.path.expanduser(r"~/OneDrive/바탕 화면/새 폴더 (3)")
DST = os.path.dirname(os.path.abspath(__file__)) + "/images"
os.makedirs(DST, exist_ok=True)

MAP = {
    "KakaoTalk_20260715_210853373.jpg": "gochu_field.jpg",     # 고추밭
    "KakaoTalk_20260715_210917427.jpg": "gochu_drying.jpg",    # 붉은고추 건조
    "KakaoTalk_20260715_210943796.jpg": "jangdok.jpg",         # 발효탱크
    "KakaoTalk_20260715_211144534.jpg": "dogil_night.jpg",     # 독일마을 야경
    "KakaoTalk_20260715_211157109.jpg": "dogil_gate.jpg",      # 독일마을 게이트
    "KakaoTalk_20260715_211209725.jpg": "dogil_street.jpg",    # 독일마을 거리
    "KakaoTalk_20260715_211504553.jpg": "eobulim_exterior.jpg",# 어부림 외관+간판
    "KakaoTalk_20260715_212316273.jpg": "beer_sausage.jpg",    # 독일 맥주+소시지
}
MAXW = 1400

for src, dst in MAP.items():
    p = os.path.join(SRC, src)
    if not os.path.exists(p):
        print("MISSING", src); continue
    im = Image.open(p)
    im = ImageOps.exif_transpose(im).convert("RGB")
    if im.width > MAXW:
        h = round(im.height * MAXW / im.width)
        im = im.resize((MAXW, h), Image.LANCZOS)
    out = os.path.join(DST, dst)
    im.save(out, "JPEG", quality=82, optimize=True)
    print(f"{dst:22s} {im.size}  {os.path.getsize(out)//1024}KB")
print("done")
