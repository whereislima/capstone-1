import requests

url = "https://sephora.p.rapidapi.com/auto-complete"

search_term = "serums"

querystring = {"q": search_term}

headers = {
    'x-rapidapi-host': "sephora.p.rapidapi.com",
    'x-rapidapi-key': "4aff8a97ccmsh04b89d869aa3d1ap1fbf25jsn746679575818"
    }

response = requests.request("GET", url, headers=headers, params=querystring)

print(response.text)



{'responseSource': 'NLP', 
    'typeAheadTerms': 
    [
        {'term': 'cleanser'}, 
        {'term': 'youth to the people superfood antioxidant cleanser'}, 
        {'term': 'superfood antioxidant cleanser'}, 
        {'brandName': 'fresh', 'defaultSku': {
            'skuId': '2421816', 'skuImages': {
                'image50': 'https://www.sephora.com/productimages/sku/s2421816-main-thumb-50.jpg'}}, 
                'productId': 'P7880', 
                'productName': 'Soy Makeup Removing Face Wash'}, 
        {'brandName': 'Youth To The People', 'defaultSku': {
            'skuId': '1863588', 'skuImages': {
                'image50': 'https://www.sephora.com/productimages/sku/s1863588-main-thumb-50.jpg'}}, 
                'productId': 'P411387', 
                'productName': 'Superfood Antioxidant Cleanser'}, 
        {'brandName': 'Tatcha', 'defaultSku': {
            'skuId': '2382232', 'skuImages': {
                'image50': 'https://www.sephora.com/productimages/sku/s2382232-main-thumb-50.jpg'}}, 
                'productId': 'P461537', 
                'productName': 'The Rice Wash Skin-Softening Cleanser'}, 
        {'brandName': 'The INKEY List', 'defaultSku': {
            'skuId': '2335636', 'skuImages': {
                'image50': 'https://www.sephora.com/productimages/sku/s2335636-main-thumb-50.jpg'}}, 
                'productId': 'P455364', 
                'productName': 'Oat Cleansing Balm'}, 
        {'brandName': 'The INKEY List', 'defaultSku': {
                'skuId': '2425163', 'skuImages': {
                'image50': 'https://www.sephora.com/productimages/sku/s2425163-main-thumb-50.jpg'}}, 
                'productId': 'P469088', 
                'productName': 'Fulvic Acid Brightening Cleanser'}, 
        {'brandName': 'The INKEY List', 
        'defaultSku': 
            {
            'skuId': '2211605', 
                'skuImages': 
                {
                    'image50': 'https://www.sephora.com/productimages/sku/s2211605-main-thumb-50.jpg'
                }
            }, 
                    'productId': 'P443833', 
                    'productName': 'Salicylic Acid Acne + Pore Cleanser'
        }
    ]
}
