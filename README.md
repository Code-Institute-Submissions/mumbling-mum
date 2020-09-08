# The Mumbling Mum

A parenting blog site with a shop selling handmade items.

### Site Owners goal:
A site to sell my handmade items and to display and update my blog. 

### Site Users goal:
To view and purchase the items for sale and to read the blog, like and comment

 
## UX
 
Use this section to provide insight into your UX process, focusing on who this website is for, what it is that they want to achieve and how your project is the best way to help them achieve these things.

In particular, as part of this section we recommend that you provide a list of User Stories, with the following general structure:
- As a user type, I want to perform an action, so that I can achieve a goal.

This section is also where you would share links to any wireframes, mockups, diagrams etc. that you created as part of the design process. These files should themselves either be included as a pdf file in the project itself (in an separate directory), or just hosted elsewhere online and can be in any format that is viewable inside the browser.

## Features

### Creations

The Creations page contains all the items for sale. They can be filtered by Category.

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
- Another feature idea

## Technologies Used

- [VSCode](https://code.visualstudio.com/)  
    - I have used VSCode to develop this project as it is my preferred IDE. i have used .env to setup a virtual environment for development. 
- [HTML](https://en.wikipedia.org/wiki/HTML5) 

- [CSS](https://en.wikipedia.org/wiki/Cascading_Style_Sheets)

- [Bootstrap4](https://getbootstrap.com/)
    - I have used Bootstrap to style the site. ADD MORE HERE...

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