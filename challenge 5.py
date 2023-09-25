def linear_search_product(products, target_product_name):
  indices = []
  for i, product in enumerate(products):
    if product["name"] == target_product_name:
      indices.append(i)

  return indices 
products = [
  {"name": "apple"},
  {"name": "banana"},
  {"name": "orange"},
]

target_product_name = "orange"

indices = linear_search_product(products, target_product_name)

print(indices) 