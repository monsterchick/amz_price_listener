if res.status_code == 200:
    soup = BeautifulSoup(res.text,'html.parser')
    selected_elements = soup.select('#corePrice_feature_div span.a-price.aok-align-center span.a-offscreen')
    print(selected_elements)
    for element in selected_elements:
        # print(e.text)
        pattern = re.compile(r'<span class="a-color-price a-text-bold">.*?</span>')
        print(type(pattern))
        print(pattern)
        # price = re.findall(pattern, str(element))[0]
        # print(price)