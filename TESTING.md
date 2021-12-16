# Testing

## Manual Testing

### User Stories Testing

* As a shopper I want to view a list of products so that i can see what i can buy

![User Stories](static/docs/product-list.png "Product List")

* As a shopper i want to view an individual products details so that i can see the price, size, alcohol content, product description

![User Stories](static/docs/individual-product.png "Individual Product")

* As a shopper i want to view different beer styles so that i can view different products of a style i like

![User Stories](static/docs/style-categories.png "Styles")

* As a shopper i want to view different breweries so that i can see what what beers from my favourite breweries are on sale

![User Stories](static/docs/brewery-categories.png "Breweries")

* As a shopper i want to view beers from different countries so that i can find my favourite beers easily

![User Stories](static/docs/country-categories.png "Countries")

* As a shopper i want to easily view the total of my purchases so that i can avoid spending too much and see how much more i need to spend for free delivery

![User Stories](static/docs/view-total.png "Total Price")

* As a shopper i want to view latest blog posts on site so that i can Keep up with the latest goings on in the world of beer

![User Stories](static/docs/beer-blog.png "Beer Blog")

* As a shopper i want to view info about company so that i can see contact info and social media accounts

![User Stories](static/docs/footer-info.png "Footer Info")

* As a shopper i want to sort the list of beers so that i can identify best priced beers and from a-z

![User Stories](static/docs/soting-dropdown.png "Sorting Dropdown")

* As a shopper i want to search for a beer by name or description so that i can find a specific beer or type of beer i want to buy

* As a shopper i want to see what ive searched for and the number of results so that i can see if what i want is available

![User Stories](static/docs/search-function.png "Search Function")

* As a shopper i want to select the quantity of a beer that i want so that i can get the exact amount i want

![User Stories](static/docs/quantity-select.png "Quantity Select")


* As a shopper i want to adjust quantity of items in my bag so that i can reduce or increase amount i need due to my needs or budget

![User Stories](static/docs/update-quantity.png "Adjust Quantity")

* As a shopper i want to Remove items from bag so that i can incase i go over budget or get rid of an unwanted product

![User Stories](static/docs/remove-from-bag.png  "Remove Item")

* As a shopper i want to Make a purchase with my card which is familiar and secure so that i can Feel that my details are being handled securely

![User Stories](static/docs/payment-form.png "Payment Form")

* As a shopper i want to view confirmation of order after checkout so that i can verify that i havent made any mistakes

![User Stories](static/docs/purchase-confirmation.png "Purchase Confirmation")

* As a shopper i want to recieve email confirmation of my purchase

![User Stories](static/docs/email-confirm-order.png "Email Order Confirmation")

* As a user i want to easily register for an account so that i can have a personal account

* As a user i want to Recieve a confirmation email so that i can Verify my account creation

![User Stories](static/docs/reg-test.png "Registration")

![User Stories](static/docs/reg-confirm-email.png "Registration")

![User Stories](static/docs/reg-confirm-page.png "Registration")

* As a user i want to login and out so that i can access my account info

* As a user i want to personalise my user profile so that i can so that my details are saved

![User Stories](static/docs/update-info-section.png "User Info Page")

* As a user i want to add items to a wishlist so that i can compile a list of beers that i might buy before purchasing

![User Stories](static/docs/quantity-select.png "wishlist toggle heart")

![User Stories](static/docs/wishlist.png "Wishlist")

* As the store owner i want to add a product so that i can add new items to the store

![User Stories](static/docs/wishlist.png "Add Product")

* As the store owner i want to edit/update product so that i can change product prices, descriptions, images etc.

* As the store owner i want to delete product so that i can Delete a product that is no longer available

![User Stories](static/docs/store-owner-edit-delete.png "Edit Delete Product")

![User Stories](static/docs/product-edit-page.png "Edit Page")

All tests carried out on Email confirmation, Updating Product, etc. Successful

### Responsivenes Testing

---

## Automated Testing

### Code Validation
---
I used W3 Schools code validators for the HTML and CSS.

* I found a couple of bugs in the code which i have rectified, there was a duplicate ID tag and a href attribut in a span tag which have been removed.

![Crafties html report](static/docs/html-validation-bugs.png "Crafties html report")

![Crafties html report](static/docs/html-validation-report.png "Crafties html report")

* There were no errors in the CSS.

![Crafites CSS Report](static/docs/CSS-validator.png "Crafites CSS Report")

## Other Testing
---
* I ran the [JSHint](https://jshint.com/) command in the terminal to review the javascript code and corrected where possible.

* I ran the [Flake8](https://flake8.pycqa.org/en/latest/) command in the terminal to review the python code and corrected where possible to clean the code and make it Pep8 compliant.

---

## Lighthouse Accessibility Report

![Lighthouse Report](static/docs/lightouse-report.png "Lighthouse Report")

- Added meta description tag in base template to improve seo rating of 89 to 100

`<meta name="description" content="crafties an irish online craft beer shop, selling ale, lager, stout, saison.">`