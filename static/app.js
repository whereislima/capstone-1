"use strict";

const BASE_API = "https://api.sandbox.ebay.com/buy/browse/v1/item_summary/methods/search?q=";
const token = "v^1.1#i^1#I^3#f^0#p^1#r^0#t^H4sIAAAAAAAAAOVYf2wTVRxf9wsmG4giIkFSDwQH9u7dXdu1J610sLmZ/Sh0zDF/kPvxrjt2vav33rlVRCYuiKCRxCghREMQQwjqHyYaMTGCEEET0OhikJgoiUSUQCKCLCai79ptdJOMQatZYpPm8t77/vy874/3HugpLVuwoW7DpQrXhMIdPaCn0OViJ4Gy0pKFk4sKZ5YUgCwC146euT3F64tOL0JiQk8KyyFKmgaC7u6EbiAhPRmibMsQTBFpSDDEBEQCloVYpLFB4GggJC0Tm7KpU+76pSHKL3lVr+gPBgEPfCrrI7PGoMwWM0Spfgg5vgoEoALEgLOMkA3rDYRFA4coDnCsBwQ8HNsCOMEbEHwczQJfO+VuhRbSTIOQ0IAKp60V0rxWlqmjWyoiBC1MhFDh+khtrDlSv7SmqWURkyUrPABDDIvYRsNHS0wFultF3Yajq0FpaiFmyzJEiGLCGQ3DhQqRQWNuwPwM0lVeVfFVyTwXhDIns3mBsta0EiIe3Q5nRlM8appUgAbWcOpaiBI0pNVQxgOjJiKifqnb+SyzRV1TNWiFqJrqyMpINEqFG7RG0RM3TQV1aoYnVt3mCQS8fl5mWeBhg5LPL6n8gJKMpAGIR2hZYhqK5gCG3E0mrobEYjgSFz4LF0LUbDRbERU71mTTeYfwY9udDc3soI07DGdPYYKA4E4Pr43+EDfGlibZGA5JGLmQhidEicmkplAjF9NxOBA63ShEdWCcFBimq6uL7uJp04ozHAAs09bYEJM7YEKkBmmdXEfatRk8WtoVGRJOpAk4lSS2dJM4JQYYcSrM+wN+1juA+3CzwiNn/zGR5TMzPBvylR1VVdAnBRSvrPoA9PKBfGRHeCBAGccOKIkpT0K0OiFO6qIMPTKJMzsBLU0ReJ/K8QEVehR/UPV4g6rqkXyK38OqEAIIJUkOBv4vSTLWMI9B2YI4f3GejxiPoyBuaOhqa2ZjDyi18baOWujn2YYV8frqaHVdNNrYFjebYzxrtcdDY82Eqzq/RNcIMi1Ef14BcHI9ZxDqTIShkpN7MdlMwqipa3JqfG0wbylR0cKpajtFxjGo6+STk6uRZLI+j9U6H05eR6G4MZ/z3KH+++50Va+QE7TjyyuHHxEBYlKjnf5Dy2aCMUVy8GBEJ9eT2qq01e7RCAeJGMlO0XEbIkwsUcjZb8xMGinkNGllythZMo2SODF2FnKvUGwZ35CidEemCZpavAOj69LZnQsokq135hR0GrkwjKuQI+5m/NaUzEmfTjtPoydk2oLItC1yyaGbncNvi9kJDXKcwJap69BqZXMupImEjUVJh+OtouahumhiDmed4vWuff+GX6yfC/pYL8tzOfkmp08zq8ZbT8hnH7yO+wwz/GElXJD+setdHwGyjYUuF6gi+heCytKiFcVF5RQilYRGoqFIZjetiSpNipghYtuCdCdMJUXNKix1aSf65P6sJ50dj4IZQ486ZUXspKwXHjDrykoJO+X2Co4FAfLnvAEf1w7mXFktZqcXT3txf+n5QveM3vePXjxL7enecpaRtoGKISKXq6SAxF/BTZs6p535OtZ6D5jS17E7FFx388FDTfbDaxbXvHxu5tEv1h8C9tnZ3zynPcuYDTtXbizf/N1+eOHSZ8dObI/3bWDu3yvMDn9Qsr3l8QcLSyte3/nr6t6Ot/rvrpxwevLbB8r3aVM/WSmUbYp8dWvNgstbJ83q+/Mh/ZXoD8Id358s+Yl6cvGMO+fNPL9u4rd1nR8i1PTbkeN/7d3Vd2/lp7VPzZ+zZf66Ccv77rrv0IHfhWrp8sTS8hXs4breAnljz7JbGn9+7flYqv+l1mds7tThc73v+i6+8MjGP7bOq9win/i4veZVfGHr2i/f+fy9M3ue3jVxzu5T29gpmx47tmbqbQcXr+3/8Y031c3TfzlunjwyN7ONfwMLoqm+bBMAAA=="

// async function searchProduct() {
//   console.log('reached searchProduct function')
//   const response = await axios({
//     url: `${BASE_API}facewash`,
//     method: "GET",
//     headers: { 'Authorization' : `Bearer ${token}` }
//   })
  
//   console.log(response)
// }

// const productForm = document.querySelector('#product-search');
// const input = document.querySelector('input[name="product"]');


// productForm.addEventListener('submit', async function(evt){
//   evt.preventDefault();

//   console.log('product form button clicked')

//   await searchProduct();
// })

