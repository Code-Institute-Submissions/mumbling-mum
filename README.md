# The Mumbling Mum

A parenting blog site with a shop selling handmade items.

### Site Owners goal:
A site to sell my handmade items and to display and update my blog. 

### Site Users goal:
To view and purchase the items for sale and to read the blog, like and comment.

 
## UX
 
I wanted the site to feel creative and fun. The items for sale are sewing projects. I decided on a sewing theme for the background images. I wanted a mostly grey neutral tone with pops of colour. I have used bootstrap bg-light for the background as I feel this compliments the colours in the images and give a nice softness to the site making it feel welcoming.

User Stories:

-   As a new visitor to the site, I want to understand the purpose of the site from the homepage.
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

### User Authorization

I have used [django-allauth](https://django-allauth.readthedocs.io/en/latest/) to manage user sign up and log in. 

### Navigation

I wanted the navigation to be simple and intuitive. The navbar includes links to the blog, the store login/my account and the shopping bag.

### Homepage

If a user is not logged in there is a section displayed on the homepage introducing me and the purpose of the site. There are also large buttons for login and sign Up.
Below this are links to the blog and links to the store. 

### Creations

The Creations page contains all the items for sale. They can be filtered by category.
Each item can be selected by clicking on the image or the title. This takes the user to an item detail page where they can see the full details and select quantity and add to their shopping bag. 

### Shopping Bag

There are messages displayed when items are added to the bag. The message displays for a few seconds allowing the user to read the notification before it disappears automatically. This allows the user to continue to peruse the site uninterrupted. 
The Shopping bag contents are stored in session and are accessible across the site. The grand total of the items in the shopping bag is visible across the site (in the Nav bar).

### Checkout

The checkout page is accessible from the shopping bag page or the shopping bag messages.
If the user is a member they can choose to store their delivery details for future purchases. These can also be updated in the 'My Info' Page.
The Checkout page contains an order summary and Order Form.

### Mumblings

Mumblings is the blog page. Here blog posts are listed. Each post can be selected and the user will be taken to a page detailing that blog entry. A logged in user can like the entry, read and add comments. An anonymous user can only view how many likes and comments there are.

### Admin 

A 'staff' member can perform additional tasks. When logged in, in the 'My Account' drop down, on the nav bar, a staff member can access 'Mumbling Admin'. This brings them to a page where you can select 'Manage Creations' or 'Manage Mumblings'.

#### Manage Creations
The user is taken to a page showing all the items. Here Items can be edited, deleted or marked as out of stock. 
Marking an item as out of stock adds a banner to the item card and prevents the item from being added to the shopping bag. If an Item is out of stock the admin can select 'back in stock' and this removes the banner and allows the item to be added to the shopping bag again. Selecting Edit takes the user to a form page that is populated with the item data. Here the data can be modified and updated. There is also an option to flag an item as clearance, this adds a clearance banner to the top of the item card and show the original price alongside the reduced price in red. 

A new item can also be added here. Clicking 'Add a new item' takes the user to a form where they can add the item information. 

By clicking on 'Manage categories' the user is taken to a page listing all categories which can be edited or deleted or a new category added.

#### Manage Mumbles
The user is taken to a page listing the Blog Entries. Here entries can be edited or deleted.
If Edit is selected the user is taken to a form that is populated with all the blog info and it can be edited and updated.
There is also a button to 'Add a blog Entry' . When Selected the user is presented with the input form for a blog post. 
Blog categories can also be managed from the Manage the mumbles page. Selecting 'Manage categories' the user is taken to a page listing all categories which can be edited or deleted or a new category added.

### Use of Toasts across the site
I have used Bootstrap toasts to display messages using django message structure. For example, when an item is added to the shopping bag, when you have signed up or logged in, or if there is an issue with a password or login etc..

### Defensive Design
I feel I have approached the development in a way to protect the intended functionality. A user must be logged in as a staff user in order to access any admin features. I believe the design of the views and URLS protects the site so it is only used as intended.
 
### Features Left to Implement
I have been very tight for time on this project and therefore there are a few improvements that I would like to add going forward.

- Add link to latest products/clearance products to the homepage.
- Add link to latest blog post to the homepage.
- Filtering items in the store by clearance status. 
- Sorting items in the store by Price high to low, low to high.
- Improve the shopping bag and checkout layouts on the smallest devices.
- Add the ability to like a comment in the blog.
- Add the ability to add multiple images to the blog. 
- Add the functionality of storing a user's shopping bag if they log out before completing a purchase.  
- Invest further time in styling and font selection to improve look and feel.
- Improve Nav layout on mobile devices

## Technologies Used

- [VSCode](https://code.visualstudio.com/)  
    - I have used VSCode to develop this project as it is my preferred IDE. I have used .env to setup a virtual environment for development. 

- [HTML](https://en.wikipedia.org/wiki/HTML5) 

- [CSS](https://en.wikipedia.org/wiki/Cascading_Style_Sheets)

- [Bootstrap4](https://getbootstrap.com/)
    - I have used Bootstrap to style the site. I have produced this in a short time frame and have therefore made use of the bootstrap grid to ensure a responsive design and many of the bootstrap classes for styling. This has allowed me to focus my efforts on getting the site functionality right and looking well designed.

- [javascript](https://en.wikipedia.org/wiki/JavaScript)

- [Django](https://www.djangoproject.com/)
    - This is the first time I have used Django in anger and really got to grips with it. I feel I have learnt a lot but I am also aware that there are many more features to explore.

- [AWS S3](https://aws.amazon.com/s3/) 

- [Heroku](heroku.com)

- [GIMP](https://www.gimp.org/) 
    - I have used GIMP (GNU Image Manipulation program) to crop, resize and modify images. Some of the images I selected were a very high resolution and were causing the site to load very slowly so I resized them to resolve this.

- [Balsamiq](https://balsamiq.com/)
    - I used Balsamiq to create the wireframes for the mumbling mum.


- [Stripe](stripe.com)
    - I have integrated Stripe for the payments section of the site.

- [github](github.com)
    - I have used git hub for the version management of this site. I utilized separate git branches during development.   

## Testing

HTML Validation: I have run each HTML file through the validator.w3.org and corrected any issues.

Site Responsiveness: Throughout the development I have used Chrome developer tools to inspect each page on different device sizes. I have also encourage friends and family to take a look and provide feedback from use on different screen sizes. This has provided me with a degree of confidence in the design. 

Stripe Payments - I have tested the stripe elements following the documentation https://stripe.com/docs/testing. I created a webhook to ensure all payments are processed and this has been thoroughly tested during development.

Throughout development I tested each feature. Following the Deployment I distributed the URL to several friends and family members. The site has been used in anger and any niggles noted and rectified where possible. I am very confident that the site functions as explained here. Find the testing details below, including an Admin logon which will allow you to access the additional "staff" user features.
Click here for testing details: [Testing_Routine](./docs/MS4TestingRoutine.pdf)

Due to very limited time and experience I have been unable to complete automated testing for this project. However, I feel that the level of testing that has been completed provides enough confidence that the site functions as intended. I managed to include a small amount in my previous project and I intend to spend some time getting to grips with this going forward and add it to this project following the assessment.

## Deployment

### Deploying to Heroku:

During development in django the sqlite3 database is utilized. When the site was deployed a postgres database was utilized. This required several steps.

I have deployed the mumbling mum app using Heroku.

In order to do this, I first logged in to my Heroku account and created a new app. 
In the dashboard of the new app I selected 'Resources' and in the 'add-ons' section I searched for 'Heroku Postgres' I selected this and provisioned it for the application.
 
This in turn created a heroku config var: DATABASE_URL which I was then able to copy.
Back in VSCode I installed dj_database_url and modified the DATABASE section in settings.py to look for the DATABASE_URL in the environment variables, so, when deployed it will use the Heroku Postgres Database.

I then installed 'gunicorn' and updated my requirements.txt (pip freeze > requirements.txt). Next I created the Procfile.

I then logged in to Heroku (heroku login). At this point I did not want Heroku to collect my static files when it deployed (as I would be using AWS S3)and so I set DISABLE_COLLECTSTATIC to 1 in the config vars. (heroku config:set DISABLE_COLLECTSTATIC=1).

I then added all the environment variables in the config vars.

Heroku caonfig vars: [configvars](./docs/MS4HerokuConfigVars.pdf)

I then added and committed my code to GIT then pushed to git hub and Heroku. I also linked my repository to Heroku so that with every push to the master branch would also be deployed to Heroku.

The site is now operational but without the static files

### Setting up Static and Media files:
I navigated to AWS and logged in. I searched for S3. After opening S3 I created a new bucket and called it 'the-mumbling-mum' and allowed public access.
In the basic settings properties I turned on Static Website hosting.
In the permissions tab I set up the CORS config, which is required for access between Heroku and the S3 bucket.
I also created a bucket policy using the policy generator and included the bucket ARN code to allow access to all resources.
In the 'Access control' tab I set the list objects permission for 'everyone'.
I then navigated to IAM (AWS Identity and Access Management). I created a group by creating an access policy to access all files in the S3 bucket.

Back in VSCode I installed 2 new packages boto3 and django-storages and followed the direction in the course notes to link up the S3 bucket.

With DISABLE_COLLECTSTATIC=1 removed from the Heroku config vars and USE_AWS added everything was set up to collect static files each time git push issues an automatic heroku deployment.

### Running locally

The code is set up so that it can be both run locally and on the deployed site. 

The main difference between running locally is the database and static storage settings. Therefore local environment variables will be required which have been omitted from git hub.

I used django-dotenv for the environment variables. Dependant on your IDE you may have your preferred method for this. 

Local environment variables required are:
- DEVELOPMENT = True
- STRIPE_PUBLIC_KEY  
- STRIPE_SECRET_KEY 
- STRIPE_WH_SECRET
- SECRET_KEY

json files for the store categories and items can be found in the fixtures folder in the items app. These can easily be uploaded to your local sqlite3 and the site should be fully operational.


## Credits

### Media

All Background photo images were created by freepik https://www.freepik.com/photos/background"> 

All Item Images and descriptions were taken from:

https://www.etsy.com/uk/listing/841906697/handmade-flower-balloon-face-mask?ref=shop_home_active_42&frs=1
https://www.etsy.com/uk/listing/833780664/handmade-fox-face-mask-washable-reusable?ref=shop_home_active_26&frs=1&cns=1
https://www.etsy.com/uk/listing/847697607/handmade-lama-face-mask-washable?ref=shop_home_active_22&frs=1
https://www.etsy.com/uk/listing/834841843/handmade-fox-face-mask-washable-reusable?ref=related-2&frs=1
https://www.etsy.com/uk/listing/641196710/scandinavian-style-linear-stem-print?ref=related-1&frs=1
https://www.etsy.com/uk/listing/521282612/scandinavian-style-large-stem-print?ref=related-1&frs=1
https://www.etsy.com/uk/listing/538436749/scandinavian-style-lovebird-print-fabric?ref=related-2&frs=1
https://www.etsy.com/uk/listing/729842883/green-woodland-animal-drawstring-bag?ref=shop_home_active_27
https://www.etsy.com/uk/listing/716835710/navy-blue-chevron-cotton-drawstring-bag?ref=shop_home_active_9
https://www.etsy.com/uk/listing/729895367/mint-and-grey-cactus-drawstring-bag?ref=shop_home_active_11
https://www.etsy.com/uk/listing/753643313/navy-arrow-print-drawstring-bag-boys-pe?ref=shop_home_active_32
https://www.etsy.com/uk/listing/753643313/navy-arrow-print-drawstring-bag-boys-pe?ref=shop_home_active_32
https://www.etsy.com/uk/listing/601416094/mint-green-chevron-and-grey-cloud?ref=related-8
https://www.etsy.com/uk/listing/864620897/mustard-navy-and-grey-handmade-fabric?ref=shop_home_active_2
https://www.etsy.com/uk/listing/764534197/boys-nursery-safari-jungle-animal-beige?ref=related-6
https://www.etsy.com/uk/listing/706584491/navy-and-cloud-nursery-fabric-bunting?ga_order=most_relevant&ga_search_type=all&g

I followed the information in this article to use flexbox to get the footer to stay at the bottom of the page:
https://dev.to/domysee/keeping-the-footer-at-the-bottom-with-css-flexbox-5h5f

### Acknowledgements

- I received inspiration for this project from many of the different Mummy Bloggers that I like to follow online. UnmumsyMum, BrummyMummyof2, selfishmother and many others.

- I would like to thank My Mentor Ignatius Ukwuoma for all motivation, advice and help over the past 12 months.

### Disclaimer

- This site is my Final Milestone Project for the Code institute Full Stack Developer Course and is intended for educational purposes only. 

