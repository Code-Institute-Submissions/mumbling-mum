# The Mumbling Mum

A parenting blog site with a shop selling handmade items.

### Site Owners goal:
A site to sell my handmade items and to display and update my blog. 

### Site Users goal:
To view and purchase the items for sale and to read the blog, like and comment

 
## UX
 
I wanted the site to feel creative and fun. As the items for sale are sewing projects. I decided on a sewing theme for the background images. I wanted a mostly grey neutral tone with pops of colour.

User Stories:

-   As a new visitor to the site, i want to understand the purpose of the site from the homepage.
-   As a new visitor to the site, I want to be able to view and purchase items for sale.
-   As a new visitor, I want to be able to view the Blog posts.
-   As a new visitor, I want to be able to sign up to become a member.
-   As a member, I want to be able to easily Login.
-   As a member, I want to be able to store my details to speed up future purchases.
-   As a member, I want to be able to view my previous orders.
-   As a member, I want to be able to read comments on blog posts.
-   As a member, I want to be able to like blog posts.
-   As a member, I want to be able to add comments to blog posts.
-   As a member, I want to be able to delete my comments on blog posts.
-   As a user, I want to be able to filter items for sale by category.
-   As a user, I want to be able to filter blog posts by category.
-   As a staff member, I want to be able to add new items for sale.
-   As a staff member, I want to be able to create, update and delete item categories.
-   As a staff member, I want to be able to remove items that are for sale.
-   As a staff member, I want to be able to mark items as out of stock
-   As a staff member, I want to be able to mark items as back in stock
-   As a staff member, I want to be able to alter item details
-   As a staff member, i want to be able to flag an item as clearance stock.
-   As a staff member, I want to be able to un-flag an item as clearance stock.
-   As a staff member, I want to be able to add a new blog post.
-   As a staff member, I want to be able to edit a blog post.
-   As a staff member, I want to be able to delete a blog post.
-   As a staff member, I want to be able to create, update and delete blog categories. 

Click here for [WireFrames](./docs/MS4Wireframes.pdf)

Click here for [DatabaseSchema](./docs/MS4DatabaseSchema.pdf)


## Features

### Navigation

I wanted the navigation to be straight forward. The navbar includes links to the blog and the store login/my account and the shopping bag.

### Homepage

If a user is not logged in there is a section displayed on the homepage introducing me and the purpose of the site. There are also large buttons for login and sign Up.
Below this are links to the blog and links to the store. 

### Creations

The Creations page contains all the items for sale. They can be filtered by category.
Each item can be selected by clicking on the image or the title. This takes the user to an item detail page where they can see the full details and select quantity and add to their shopping bag. 

I have

SKU - Stock Keeping Unit
Even though the store is small, I thought it prudent for each Item to have a SKU. I decided to keep the SKU simple. I have used the category pk multiplied by 10 and the Item PK multiplied by 10. e.g. category.pk=1 and item.pk=20 SKU =10200. This ensures the SKU is always unique and never starts with 0. It also allows items to be easily identified and ordered by the SKU. 

When logged in a staff Member can Add, Edit and Delete items. If an items category is changed then the SKU will be updated to reflect this.  

### Shopping Bag

### Checkout

### Use of Toasts across the site
In this section, you should go over the different parts of your project, and describe each in a sentence or so.
 
### Existing Features
- Feature 1 - allows users X to achieve Y, by having them fill out Z
- ...

For some/all of your features, you may choose to reference the specific project files that implement them, although this is entirely optional.

In addition, you may also use this section to discuss plans for additional features to be implemented in the future:

### Features Left to Implement
I have been very tight for time on this project and therefore there are a few improvements that I would like to add going forward.

- Add link to latest products/clearance products to the homepage.
- Add link to latest blog post to the homepage.
- Filtering items in the store by clearance status. 
- Sorting items in the store by Price high to low, low to high.
- Improve the shopping bag and checkout layouts on the smallest devices.
- Add the ability to like a comment in the blog.
- Add the ability to add multiple images to the blog.   

## Technologies Used

- [VSCode](https://code.visualstudio.com/)  
    - I have used VSCode to develop this project as it is my preferred IDE. I have used .env to setup a virtual environment for development. 
    
- [HTML](https://en.wikipedia.org/wiki/HTML5) 

- [CSS](https://en.wikipedia.org/wiki/Cascading_Style_Sheets)

- [Bootstrap4](https://getbootstrap.com/)
    - I have used Bootstrap to style the site. I have produced this in a short time frame and have therefore made use of the bootstrap grid to ensure a responsive design and many of the bootstrap classes for styling. This has allowed me to focus my efforts on getting the site functionality right.

- [javascript](https://en.wikipedia.org/wiki/JavaScript)

- [Django](https://www.djangoproject.com/)

- [AWS S3](https://aws.amazon.com/s3/) 

- [Heroku](heroku.com)

In this section, you should mention all of the languages, frameworks, libraries, and any other tools that you have used to construct this project. For each, provide its name, a link to its official site and a short sentence of why it was used.



## Testing

In this section, you need to convince the assessor that you have conducted enough testing to legitimately believe that the site works well. Essentially, in this part you will want to go over all of your user stories from the UX section and ensure that they all work as intended, with the project providing an easy and straightforward way for the users to achieve their goals.

Whenever it is feasible, prefer to automate your tests, and if you've done so, provide a brief explanation of your approach, link to the test file(s) and explain how to run them.

For any scenarios that have not been automated, test the user stories manually and provide as much detail as is relevant. A particularly useful form for describing your testing process is via scenarios, such as:

1. Contact form:
    1. Go to the "Contact Us" page
    2. Try to submit the empty form and verify that an error message about the required fields appears
    3. Try to submit the form with an invalid email address and verify that a relevant error message appears
    4. Try to submit the form with all inputs valid and verify that a success message appears.

In addition, you should mention in this section how your project looks and works on different browsers and screen sizes.

You should also mention in this section any interesting bugs or problems you discovered during your testing, even if you haven't addressed them yet.

If this section grows too long, you may want to split it off into a separate file and link to it from here.

## Deployment

I have deployed the mumbling mum app using Heroku. 
In order to do this, I first logged in to my Heroku account and created a new app. 
In the dashboard of the new app I selected 'Resources' and in the 'add-ons' section I searched for 'Heroku Postgres' I selected this and provisioned it for the application. This in turn created a heroku config var: DATABASE_URL which I was then able to copy.
Back in VSCode I installed dj_database_url and modified the DATABASE section in settings.py to look for the DATABASE_URL in the environment variables, so, when deployed it will use the Heroku Postgres Database.   
I then installed 'gunicorn' and updated my requirements.txt (pip freeze > requirements.txt). Next I created the Procfile.
I then logged in to Heroku (heroku login). At this point I did not want Heroku to collect my static files when it deployed (as I would be using AWS S3)and so I set DISABLE_COLLECTSTATIC to 1. (heroku config:set DISABLE_COLLECTSTATIC=1). 
I then added all the environment variables in the config vars.
I then added and committed my code to GIT then pushed to git hub and Heroku. I also linked my repository to Heroku so that with every push to the master branch would also be deployed to Heroku.


This section should describe the process you went through to deploy the project to a hosting platform (e.g. GitHub Pages or Heroku).

In particular, you should provide all details of the differences between the deployed version and the development version, if any, including:
- Different values for environment variables (Heroku Config Vars)?
- Different configuration files?
- Separate git branch?

In addition, if it is not obvious, you should also describe how to run your code locally.


## Credits

### Content
- The text for section Y was copied from the [Wikipedia article Z](https://en.wikipedia.org/wiki/Z)

### Media
- The photos used in this site were obtained from ...

### Acknowledgements

- I received inspiration for this project from X

https://www.etsy.com/uk/listing/823858959/garden-bird-bunting?gpla=1&gao=1&&utm_source=google&utm_medium=cpc&utm_campaign=shopping_uk_en_gb_ds-b-Paper_Goods-paper_and_party_supplies-party_supplies-party_decor-garlands_flags_and_bunting&utm_custom1=67a3938d-5bea-4087-8192-8e8433a6a654&utm_content=go_6479445330_78125087672_380846581081_pla-315318922049_c__823858959engb&utm_custom2=6479445330&gclid=EAIaIQobChMIwZvxpKG-6wIViK3tCh2u5AlQEAQYAiABEgLf1_D_BwE

I followed the information in this article to use flexbox to get the footer to stay at the bottom of the page:
https://dev.to/domysee/keeping-the-footer-at-the-bottom-with-css-flexbox-5h5f