from modules.scrapper import check_price

URLs = [
    'https://www.tokopedia.com/istorebdg/macbook-air-m2-chip-2022-13-inch-8gb-256gb-garansi-resmi-ibox-inter-silver-7c6c',
    'https://www.tokopedia.com/istorebdg/macbook-air-m2-chip-2022-13-inch-8gb-512gb-garansi-resmi-ibox-inter-starlight-8c87',
    'https://www.tokopedia.com/istorebdg/apple-macbook-pro-2021-14-inch-m1-pro-chip-mkgp3-mkgr3-16gb-512gb-inter-silver-398b',
    'https://www.tokopedia.com/istorebdg/apple-macbook-pro-2021-14-inch-m1-pro-chip-mkgq3-mkgt3-16gb-1tb-inter-space-grey'
]

for source in URLs:
    check_price(source)