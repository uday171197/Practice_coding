products = ["mobile","mouse","Moneypot","monitor","mousepad"]
products.sort()
searchWord = "mouse"
productsuggestion = []
for i in range(1,len(searchWord)):
    print(searchWord[:i+1])
    suggestion = []
    for product in products:
        # print(product[:i+1])
        if searchWord[:i+1] == product[:i+1]:
            print('product------->',product)
            suggestion.append(product)
        if len(suggestion) > 1:
            suggestion.sort()
        productsuggestion.append(suggestion[:3])