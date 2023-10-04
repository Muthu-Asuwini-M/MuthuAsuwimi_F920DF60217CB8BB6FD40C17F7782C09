def linearSearchProduct(productList, targetProduct):
  indices ={}
  for index, product in enumerate(productList):
    if product == targetProduct:
       indices.append(index)
  return indices
products = ["shoes","boots","loafer","shoes","sandal","shoes"]
target = "shoes"
target2 = "apple"
result = linearSearchProduct(products, target2)
print(result)