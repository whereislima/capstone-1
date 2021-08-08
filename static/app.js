// API request for product search using eBay API

const API = "";


async function searchProduct() {
  const response = await axios.get('')
  const ul = document.querySelector("#products")
  console.log(response.data)
  for(let product of response.data) {
    console.log(product.name);
    const newProduct = document.createElement('LI');
    newProduct.innerText = product.name;
    ul.append(newProduct);
  }
}

// searchItem() in console

const productForm = document.getElementById('product-search');

productForm.addEventListener('submit', function(){
  console.log('product form button clicked')
})

