# Trail Direct

<img src="media/logo-readme.jpg">

## A e-commerce site designed to provide mountain bike cyclists with the best upgrades and accorriess to maximize their mountain bike experiences.

### By Luke Courtney

## [Live Site](https://trail-direct-77691eb3f453.herokuapp.com/)  |  [Repository](https://github.com/lukecdev/Trail-Direct)


## Table of contents
<a name="contents">Back to Top</a>
 1. [ Business Model ](#business)
 2. [ UX ](#ux)
 3. [Agile Development](#agile)
 4. [ Features ](#features)  
 5. [ Features Left to Implement ](#left)  
 6. [ Technology used ](#tech) 
 7. [ Testing ](#testing)  
 8. [ Bugs ](#bugs)  
 9. [ Deployment](#deployment)
 10. [ Credits](#credits)
 11. [ Content](#content)  
 12. [ Acknowledgements](#acknowledgements) 

<a name="business"></a>

## Business Overview

The business is a B2C e-commerce platform to provide phyical products to customers through an online store.

The types of products for sale high-end products for cyclists, specializing in bike parts for mountain bikes. 

### Search Engine Optimization and Social Media Marketing
In order to improve the business's visibility to search engines, I used an approach of meta tags, keywords, a sitemap.xml file, and a robots.txt file.
I set up a newsletter that users could sign up to recieve more details on products.
A Facebook page was set up also to promote the business online and allow customers to contact the company through Facebook. [Facebook-Page](https://www.facebook.com/profile.php?id=61555703349226)


<summary>FaceBook Page</summary>	
<img src="media/trail-direc-facebook.jpg">



### Keywords
Appropriate and relevent keywords where used for the site in making it better suited for SEO. This will improve the websites visibility and help new users search the site. 
I have included a screenshot of the head element from my base.html page that shows the keywords within the relevant meta tag.


<summary>Keywords</summary>
<img src="media/meta-tags-td.jpg">


### Sitemaps
I generated a sitemap.xml file for the site using XML-Sitemaps and included it in the root level of the project repository. This will help search engines crawl the site more effectively.

### Robots
I created a robots.txt at the root level of the project file. This tells search engine crawlers which URLs the crawler can access on the site. This is used mainly to avoid overloading the site with requests.

### Newsletter Marketing
An embedded custom model newsletter form is included in the bottom of the home page. Users can subscribe to the newsletter to hear any updates or offers upcoming. This will help the business market to interested returning customers.

## UX
<a name="ux"></a>

### Color Pallette
- Color Pallette for the website.
<img src="media/readme/color-website-sc.jpg">

### Wireframes

Wireframes were created for the website layout including mobile wireframes for pages that have a slightly different layout to the desktop version.

Some slight layout differences exist between the finished website and the wireframes.

- WireFrames 
    <img src="media/readme/Wireframe-TD.png">

<details>
	<summary> Index page </summary>
	<br>
    <img src="media/readme/Trail-direct-Home.jpg">
</details>

<details>
	<summary> Mobile page </summary>
	<br>
    <img src="media/readme/td-mobile-home.jpg">
</details>

<details>
	<summary> Login Wireframe </summary>
	<br>
    <img src="media/readme/trail-direct-login.jpg">
</details>

<details>
	<summary> Register Wireframe </summary>
	<br>
    <img src="media/readme/trail-direct-register.jpg">
</details>

<details>
	<summary> Product Page Wireframe </summary>
	<br>
    <img src="media/readme/trail-direct-product.jpg">
</details>

#### Database Schema

Pre-project planning involved generating an entity relationship diagram. This was done in order to create a clear plan as to how all of the database models interact with each other. This was also done to determine what data fields were needed for each model. The review & question model was not implented due to time contraint. The relationship between each model and another is noted in the diagram with "FK" denoting Foreign Key. 

<details>
	<summary>Entity Relationship Diagram</summary>
<img src="media/readme/TD-ERG.jpg">
</details>


<summary> Database Structure</summary>
<br>

<summary>Profiles App</summary>

#### UserProfile Model
| id | Field |
|--|--|
|user|OneToOneField|
|default_phone_number|CharField|
|default_street_address1|CharField|
|default_street_address2|CharField|
|default_town_or_city|CharField|
|default_county|CharField|
|default_postcode|CharField|
|default_country|CharField|
|first_name|CharField|
|last_name|CharField|
|country|CharField|

<summary>Blog App</summary>

#### Post Model

| id | Field |
|--|--|
|title|CharField|
|slug|SlugField|
|author|ForeignKey|
|image_url|URLField|
|image|ImageField|
|excerpt|TextField|
|updated_on|DateTimeField|
|content|TextField|
|created_on|DateTimeField|
|status|IntegerField|

<summary>Checkout App</summary>

#### Order Model

| id | Field |
|--|--|
|order_number|CharField|
|user|ForeignKey|
|full_name|CharField|
|email|EmailField|
|phone_number|CharField|
|country|CountryField|
|street_address1|CharField|
|street_address2|CharField|
|town_or_city|CharField|
|postcode|CharField|
|county|CharField|
|date|DateTimeField|
|deliver_cost|DecimalField|
|order_total|DecimalField|
|grand_total|DecimalField|
|original_cart|TextField|
|stripe_pid|CharField|

#### OrderLineItem Model

| id | Field |
|--|--|
|order|ForeignKey|
|product|ForeignKey|
|product_size|CharField|
|quantity|IntegerField|
|lineitem_total|DecimalField|

<summary>Contact App</summary>

#### Contact Model

|id|Field|
|--|--|
|email|EmailField|
|subject|CharField|
|message|TextField|
|reason|CharField|

<summary>Home App</summary>

#### Newsletter Model

|id|Field|
|--|--|
|name|CharField|
|email|EmailField|
|created|DateTimeField|
|subscribed|BooleanField|

#### SubscribedUsers Model

|id|Field|
|--|--|
|name|CharField|
|email|EmailField|
|created_date|DateTimeField|

<summary>Products App</summary>

#### Category Model

|id|Field|
|--|--|
|name|CharField|
|display_name|CharField|

#### Product Model

|id|Field|
|--|--|
|name|CharField|
|category|CharField|
|sku|CharField|
|description|TextField|
|price|DecimalField|
|stock|IntegerField|
|in_stock|BooleanField|
|image_url|URLField|
|image|ImageField|
|rating|DecimalField|
|created|DateTimeField|



<a name="agile"></a>

## Agile Development

### Agile Overview
Once I had settled on a website idea I was going to build, I started preplanning by creating a github prjects page to track the epics, user stories and tasks that were required for the project.

This allowed me to better manage my workload effectively.

As I worked through the project, I moved the tasks on the board from not started through to being completed. 

One of the sections in my project boards is called NINTH. This stands for "Not importants, nice to have". This is usually for expanding the project beyond MVP and adding additional features to enhance user experience.

### GitHub Project Board
I used the github projects as a agile tool to manage the planning and implamentation of functions to the site. 
[Project Board](https://github.com/users/lukecdev/projects/2)

#### Epics

	1. [Epic: User Registration & Accounts](https://github.com/lukecdev/Trail-Direct/issues/1)
	2. [Epic: Shopping Bag](https://github.com/lukecdev/Trail-Direct/issues/2)
	3. [Epic: Product Admin](https://github.com/lukecdev/Trail-Direct/issues/3)
	4. [Epic: Blog](https://github.com/lukecdev/Trail-Direct/issues/4)
	5. [Epic: Newsletter](https://github.com/lukecdev/Trail-Direct/issues/5)
	6. [Epic: Profiles](https://github.com/lukecdev/Trail-Direct/issues/6)
	7. [Epic: Site Navigation](https://github.com/lukecdev/Trail-Direct/issues/7)
	8. [Epic: Contact & FAQ](https://github.com/lukecdev/Trail-Direct/issues/8)
	9. [Epic: SEO & Marketing](https://github.com/lukecdev/Trail-Direct/issues/9)
	10. [Epic: ReadMe.md](https://github.com/lukecdev/Trail-Direct/issues/10)
	11. [Epic: Deploy Project](https://github.com/lukecdev/Trail-Direct/issues/11)


Each Epic may have more than one user stories associated with each tasks.

The full breakdown of these user stories can be found in the project board. 

Due to time contsraints some items where moved to NINTH after I were deemed not mandatory for the final project.

[Back to Top of page](#contents)


<a name="features"></a>

## Features

The main features of the website are documented in this section.

- Navigation
    - The navigation bar is available throughout the website. It is attached to the base. It contains all the relevant links for users to use the site. Extra admin links are displayed for an admin logged in so that changes to the site can be made. The center logo is a link to the home page. The bag item in the right corner displays the current bag total and links to the checkout.
<details>
	<summary> Navigation </summary>
    <img src="media/readme/features/desk-nav-feature.jpg">
</details>
<details>
	<summary> Navigation Admin </summary>
    <img src="media/readme/features/navbar-admin-sc-features.jpg">
</details>
    - On mobile the navigation bar collapses.
<details>
	<summary> Navigation Mobile </summary>
    <img src="media/readme/features/mobile-nav-sc.jpg">
</details>
    - In the footer on every page, there are links to other internal pages plus external links to socials.
<details>
	<summary> Navigation Footer </summary>
    <img src="media/readme/features/footer-sc-features.jpg">
</details>
- Authentication
    - The authentication for the site is handled by Django Allauth and links to the main login, logout & register pages are found in the account section of the navbar. Messages are displayed to the user if there is an error with their imputs.
<details>
<summary> Register Page </summary>
    <img src="media/readme/features/register-sc.jpg">
</details>
- Confirmation Email
	- New user gets sent a email to confirm their details and finish registration.
<details>
<summary> Email Confirmation </summary>
    <img src="media/readme/features/signup-email-sc.jpg">
</details>
- Products
	The products are displayed under various heading, based on slected catagories or sorted by price.
<details>
<summary> Products Page </summary>
    <img src="media/readme/features/products-sc-feature.jpg">
</details>
<details>
<summary> Products Page </summary>
    <img src="media/readme/features/products-sc-feature.jpg">
</details>
<details>
<summary> Products Details </summary>
    <img src="media/readme/features/product-deta-sc-features.jpg">
</details>
<details>
<summary> Products Details </summary>
    <img src="media/readme/features/product-description-sc-features.jpg">
</details>
	- Catagories of products could be slected on the home page through the cars below the hero image.
<details>
<summary> Product Catagory Home Page </summary>
    <img src="media/readme/features/catagory-sc-features.jpg">
</details>
- Product Admin
	- When the admin is signed-in, they get access to addional buttons to edit the products and add products in the navbar.
<details>
<summary> Admin Products </summary>
    <img src="media/readme/features/edit-delete-product-sc.jpg">
</details>
<details>
<summary> Admin Edit Products </summary>
    <img src="media/readme/features/edit-product-1-sc.jpg">
	<img src="media/readme/features/edit-product-2-sc.jpg">
	<img src="media/readme/features/product-edit-success-sc.jpg">
</details>
<details>
<summary> Admin Add Products </summary>
    <img src="media/readme/features/add-product-sc.jpg">
</details>
-Shopping Bag
	The bag contains the list of products that the user has added to possibly purchase. The quantities of the products can be adjusted in the bag as well as product deletion. The overall price and extra charges are calculated in the bag before checkout.
<details>
<summary> Bag Details </summary>
    <img src="media/readme/features/blog-details.jpg">
</details>
<details>
<summary> Bag Remove Item </summary>
    <img src="media/readme/features/bag-remove-sc.jpg">
</details>
- Checkout
	- The checkout page contains more details on the users order, the final charges and the delivery address of the products is be entered.
<details>
<summary> Checkout Details </summary>
    <img src="media/readme/features/checkout-details-sc.jpg">
</details>
<details>
<summary> Delivery Details </summary>
    <img src="media/readme/features/delivery-form-sc.jpg">
</details>
<details>
<summary> Stripe Details </summary>
    <img src="media/readme/features/stripe-sc.jpg">
</details>
	- Once payment goes through, the user will be shown a confirmation page which confirms all the details of the transiation.
<details>
<summary> Order Confirmation </summary>
    <img src="media/readme/features/order-confirmation-screen.jpg">
</details>
- Blog
	- The blog page shows articles posed by the admin.
<details>
<summary> Blog Page </summary>
    <img src="media/readme/features/blog-user-sc.jpg">
</details>
<details>
<summary> Blog Detail </summary>
    <img src="media/readme/features/blog-details.jpg">
</details>
	- Blog admin can edit, delete or add blog posts when signed in as admins.
<details>
<summary> Admin Blog </summary>
    <img src="media/readme/features/blog-sc.jpg">
</details>
- Contact
	- A contact page is accessable for all users, where a FAQ is also to provide users answers to any issues they had. There is a support email that is accessable to logged-in users to help with order issues.
<details>
<summary> Contact </summary>
    <img src="media/readme/features/contact-sc.jpg">
</details>
<details>
<summary> Contact Form </summary>
    <img src="media/readme/features/contact-form-sc.jpg">
</details>
<details>
<summary> FAQ </summary>
    <img src="media/readme/features/faq-sc.jpg">
</details>
- Newsletter
	- The newsletter is for users to sign up with their email to recieve updates from the site.
<details>
<summary> Newsletter </summary>
    <img src="media/readme/features/newsletter-sc-features.jpg">
</details>
	- Admin page for sending newsletter to subcribed users.
<details>
<summary> Newsletter Admin </summary>
    <img src="media/readme/features/send-newsletter.jpg">
</details>
- Privacy Policy
<details>
<summary> Privacy Policy </summary>
    <img src="media/readme/features/privacy-policy-sc.jpg">
</details>
- 404 Error Page
<details>
<summary> 404 Error </summary>
    <img src="media/readme/features/404-sc.jpg">
</details>
- Restrictions
	- Users are redirected from pages they do not have authorization to view. They are brought back to the home page or sent to sign in page.

<a name="left"></a>

### Future Features
	- A review section under each product. This would show reviews from users who have bought the product before to leave a review. This was not put in due to time constraints.
	- Adding FAQ sections to the contact form from the front end.
	- Product questions. This is a submitted questions on products details that are answered by site experts. 

[Back to top](#contents)

<a name="tech"></a>
##  Technology Used
### Html
 - Used to structure the website

### CSS
 - Custom CSS was written to make the site as close to the wireframes.

### JavaScript
 -  Used to add timeout function for messages as well as to enable the menu on index.html

### Python
 -  Used for the logic in this project.

### Django
 -  Framework used to build this project.

### Font Awesome
 -  Icon library used in the navigstion bar and footer.

### Bootstrap 5
 - Used as the base front end framework to work alongside Django

### GitHub
 - Used to store the code for this project & for the projects Kanban board used to complete it.

### Heroku
 - Used to host and deploy this project

### ElephantSQL
 - Storage for the database

### Git
- Used for version control throughout the project and to ensure a good clean record of work done was maintained.

### AWS S3 and IAM
- Used to host static and media files for this project and IAM for the permissions based roles for accessing the S3 buckets.

### Stripe
- Stripe is used to handle website payments.

### Django-Crispy-Forms
- Used to style the forms in this project.

[Back to Top of page](#contents)


<a name="Testing"></a>

## Testing 

Testing documentation can be found [here.](TESTING.md)

## Bugs

<a name="bugs"></a>

Known:
	- When a product gets added to the basket, a toast is displayed but it does not disapear after the set time. It does also not close when the cornor 'x' is clicked. The user has to click on something else to remove the toast. I belive this is an issue with how my JS function is interacting with the toast html.
	- In the shopping bag, the sub-total is still in $ instead of €. When an item is added to the baf, the icon changes but still has the $ instead of euro symbol. 
	- The mobile site is not fully respionsive as some product images do not scale down correctly, this is an issue with the scaling and break points in the css.
	- The search bar doesn't bring all the items forward. This is because the q value is not added correctly to new products added.
	- Order confirmation email were not being sent after the order has been processed. This was perviously working and other emails such as password verification are sending. 

<a name="deployment"></a>

## Deployment and Local Development
The live deployed version of the website can be found on [Heroku](https://trail-direct-77691eb3f453.herokuapp.com/). The steps and technologies involved in deploying it are outlined below. The steps on how to fork or clone the repository for the website are also outlined.

### ElephantSQL Database

The PostgreSQL Database for this project was obtained using [ElephantSQL](https://www.elephantsql.com), a service which you can sign-up to with your GitHub account. Once signed up follow these steps:

- Click **Create New Instance** to start a new database.
- Name used: `Trail Direct`.
- Select the **Tiny Turtle (Free)** plan.
- **Tags** can be left blank.
- Normally you select the **Region** and **Data Center** closest to you in this case EU-West-1.
- For my project, I had to select a differnt region (West-US) as this provided a newer Postgres version that was needed for my project requirements.
- Once created, click on the new database name, where you can view the database URL which will be needed for the Heroku Config Vars.

### Amazon AWS

This project uses [Amazon Web Services (AWS)](https://aws.amazon.com) to store its media and static files.

Once you've created an AWS account and logged-in, navigate to the **AWS Management Console** page & follow these series of steps to get your project connected.

#### S3 Bucket

- Search for **S3**.
- Create a new bucket, give it a name (matching your Heroku app name), and choose the region closest to you.
- Uncheck **Block all public access**, and acknowledge that the bucket will be public (required for it to work on Heroku).
- From **Object Ownership**, make sure to have **ACLs enabled**, and **Bucket owner preferred** selected.
- From the **Properties** tab, turn on static website hosting, and type `index.html` and `error.html` in their respective fields, then click **Save**.
- From the **Permissions** tab, paste in the following CORS configuration:

	```shell
	[
		{
			"AllowedHeaders": [
				"Authorization"
			],
			"AllowedMethods": [
				"GET"
			],
			"AllowedOrigins": [
				"*"
			],
			"ExposeHeaders": []
		}
	]
	```

- Copy your **ARN** string.
- From the **Bucket Policy** tab, select the **Policy Generator** link, and use the following steps:
	- Policy Type: **S3 Bucket Policy**
	- Effect: **Allow**
	- Principal: `*`
	- Actions: **GetObject**
	- Amazon Resource Name (ARN): **paste-your-ARN-here**
	- Click **Add Statement**
	- Click **Generate Policy**
	- Copy the entire Policy, and paste it into the **Bucket Policy Editor**

		```shell
		{
			"Id": "Policy1234567890",
			"Version": "2012-10-17",
			"Statement": [
				{
					"Sid": "Stmt1234567890",
					"Action": [
						"s3:GetObject"
					],
					"Effect": "Allow",
					"Resource": "arn:aws:s3:::your-bucket-name/*"
					"Principal": "*",
				}
			]
		}
		```

	- Before you click "Save", add `/*` to the end of the Resource key in the Bucket Policy Editor (like above).
	- Click **Save**.
- From the **Access Control List (ACL)** section, click "Edit" and enable **List** for **Everyone (public access)**, and accept the warning box.
	- If the edit button is disabled, you need to change the **Object Ownership** section above to **ACLs enabled** (mentioned above).

#### IAM

Back on the AWS Services Menu, search for and open **IAM** (Identity and Access Management).
Once on the IAM page, follow these steps:

- From **User Groups**, click **Create New Group**.
	- Name: `manage-trail-direct`
- Tags are optional, but you must click it to get to the **review policy** page.
- From **User Groups**, select your newly created group, and go to the **Permissions** tab.
- Open the **Add Permissions** dropdown, and click **Attach Policies**.
- Select the policy, then click **Add Permissions** at the bottom when finished.
- From the **JSON** tab, select the **Import Managed Policy** link.
	- Search for **S3**, select the `AmazonS3FullAccess` policy, and then **Import**.
	- You'll need your ARN from the S3 Bucket copied again, which is pasted into the "Resource" key on the Policy.

		```shell
		{
			"Version": "2012-10-17",
			"Statement": [
				{
					"Effect": "Allow",
					"Action": "s3:*",
					"Resource": [
						"arn:aws:s3:::your-bucket-name",
						"arn:aws:s3:::your-bucket-name/*"
					]
				}
			]
		}
		```
	
	- Click **Review Policy**.
	- Name: `trail-direct-policy`
	- Provide a description:
		- "Access to S3 Bucket for Trail Direct static files."
	- Click **Create Policy**.
- From **User Groups**, click `manage-trail-direct`.
- Click **Attach Policy**.
- Search for the policy you've just created (`trail-direct-policy`) and select it, then click **Attach Policy**.
- From **User Groups**, click **Add User**.
	- Name: `trail-direct-staticfiles-user`
- For "Select AWS Access Type", select **Programmatic Access**.
- Select the group to add your new user to: `manage-trail-direct`
- Tags are optional, but you must click it to get to the **review user** page.
- Click **Create User** once done.
- You should see a button to **Download .csv**, so click it to save a copy on your system.
- If you don't see an option to downlod the CSV file go to IAM and select **Users**
- Select the user for whom you wish to create a CSV file.
- Select the **Security Credentials** tab.
- Scroll to **Access Keys** and click **Create access key**
- Select **Application running outside AWS**, and click next.
- On the next screen, you can leave the **Description tag** value blank. Click **Create Access Key**.
- Click the **Download .csv file** button.
    - **IMPORTANT**: once you pass this page, you cannot come back to download it again, so do it immediately!
	- This contains the user's **Access key ID** and **Secret access key**.
	- `AWS_ACCESS_KEY_ID` = **Access key ID**
	- `AWS_SECRET_ACCESS_KEY` = **Secret access key**
- These will be needed for the Heroku Config Vars.

#### Final AWS Setup

- Follow the steps described later for [Heroku Deployment](#heroku-deployment) and then return here to follow these final AWS steps below.
- If Heroku Config Vars has `DISABLE_COLLECTSTATIC` still, this can be removed now, so that AWS will handle the static files.
- Back within **S3**, create a new folder called: `media`.
- Inside the media file select **Upload** and **Add Files**.
- Select the images from your hard-drive that you wish to upload.
- Under **Manage Public Permissions**, select **Grant public read access to this object(s)**.
- No further settings are required, so click next through to the end and **Upload**.

### Stripe API

This project uses [Stripe](https://stripe.com) to handle the ecommerce payments.

Once you've created a Stripe account and logged-in, follow these series of steps to get your project connected.

- From your Stripe dashboard, click **API keys for developers**.
- You'll have two keys here:
	- `STRIPE_PUBLIC_KEY` = Publishable Key (starts with **pk**)
	- `STRIPE_SECRET_KEY` = Secret Key - click **Reveal test key** (starts with **sk**)

As a backup, in case users prematurely close the checkout page during payment, we can include Stripe Webhooks.

- From your Stripe dashboard, click **Developers**, and select **Webhooks**.
- From there, click **Add Endpoint**.
	- `https://trail-direct-77691eb3f453.herokuapp.com/checkout/wh/`
- Click **receive all events**.
- Click **Add Endpoint** to complete the process.
- You'll have a new key here under "Signing secret":
	- `STRIPE_WH_SECRET` = Under signing Secret - click `Reveal` (starts with **wh**)

### Gmail API

This project uses [Gmail](https://mail.google.com) to handle sending emails to users for account verification and purchase order confirmations.

Once you've created a Gmail (Google) account and logged-in, follow these series of steps to get your project connected.

- Click on the **Account Settings** (cog icon) in the top-right corner of Gmail.
- Click on the **See all settings** link.
- Click on the **Accounts and Import** tab.
- Within the section called "Change account settings", click on the link for **Other Google Account settings**.
- This opens a page in a new tab, select **Security** on the left.
- Select **2-Step Verification** to turn it on (verify your password and account).
- Once verified, select **Turn On** for 2FA.
- Navigate back to the **Security** page, and you'll see a new option called **App passwords**.
- This might prompt you once again to confirm your password and account.
- Select **Mail** for the app type.
- Select **Other (Custom name)** for the device type.
	- Any custom name, such as "Django" or the project name.
- You'll be provided with a 16-character password (API key).
	- Save this somewhere locally, as you cannot access this key again later!
	- `EMAIL_HOST_PASS` = user's 16-character API key
	- `EMAIL_HOST_USER` = user's own personal Gmail email address

### Heroku Deployment

This project uses [Heroku](https://www.heroku.com) for deployment to the web. The deployment steps are as follows, after account setup:

- Select **New** in the top-right corner of your Heroku Dashboard, and select **Create new app** from the dropdown menu.
- Your app name must be unique, and then choose a region closest to you (EU or USA), and finally, select **Create App**.
- From the new app **Settings**, click **Reveal Config Vars**, and set your environment variables.

| Key | Value |
| --- | --- |
| `AWS_ACCESS_KEY_ID` | user's own value |
| `AWS_SECRET_ACCESS_KEY` | user's own value |
| `DATABASE_URL` | user's own postgres value |
| `DISABLE_COLLECTSTATIC` | 1 (*this is temporary, and can be removed for the final deployment*) |
| `EMAIL_HOST_PASS` | user's own value |
| `EMAIL_HOST_USER` | user's gmail |
| `SECRET_KEY` | user's own value |
| `STRIPE_PUBLIC_KEY` | user's own value |
| `STRIPE_SECRET_KEY` | user's own value |
| `STRIPE_WH_SECRET` | user's own value |
| `USE_AWS` | True |

Heroku needs two additional files in order to deploy properly.

- requirements.txt
- Procfile

You can install this project's **requirements** (where applicable) using:

- `pip3 install -r requirements.txt`

If you have your own packages that have been installed, then the requirements file need to be updated using:

- `pip3 freeze --local > requirements.txt`

Create a **Procfile** at the root level of the project:

- Open the Procfile and enter the following line of code: `web: gunicorn app_name.wsgi:application` and save.
- *replace **app_name** with the name of your primary Django app name; the folder where settings.py is located*.

For Heroku deployment, follow these steps to connect your own GitHub repository to the newly created app:

Either:

- Select **Automatic Deployment** from the Heroku app.

Or:

- Ensure Heroku is installed for these following commands to work.
- If it is not run `curl https://cli-assets.heroku.com/install.sh | sh` in the terminal/CLI.
- Then connect to Heroku using this command: `heroku login -i`
- Set the remote for Heroku: `heroku git:remote -a app_name` (replace *app_name* with your app name)
- After performing the standard Git `add`, `commit`, and `push` to GitHub, you can now type:
	- `git push heroku main`

The project should now be connected and deployed to Heroku!

### Local Development
The steps below describe how to fork or clone the repository if desired.
#### How to Fork
1. Log in to Github.
2. Navigate to the [repository](https://github.com/lukecdev/Trail-Direct) for this website.
3. Click the Fork button in the top right corner.
4. You will be brought to a new page with a short form to be completed.
5. Upon completing, click on the "Create fork" button and this will create a fork of the repository in your personal account.

#### How to Clone
1. Log in to GitHub.
2. Navigate to the [repository](https://github.com/lukecdev/Trail-Direct) for this website.
3. Click on the **Code** button and a modal will appear.
4. Within this modal select the local tab.
5. Within this tab there are HTTPS, SSH, or GitHub CLI tabs.
6. Click on the HTTPS tab and copy the link shown.
7. In your development environment open the terminal.
8. Change the current working directory to the location where you want the cloned directory to be.
9. Type `git clone` into the terminal, then paste the URL you copied in step 6.
10. Press **Enter** to create your local clone.
11. In the terminal install the requirements by using the following: `pip3 install -r requirements.txt`.
12. If you have your own packages that have been installed, then the requirements file needs to be updated using: `pip3 freeze --local > requirements.txt`.
13. Next create the env.py file which tells our project which variables to use.
14. Add env.py the file to a .gitignore file to prevent it from being pushed to github.
15. Start the Django app: `python3 manage.py runserver`.
16. Make migrations by running : `python3 manage.py makemigrations`
17. Then migrate those changes with `python3 manage.py migrate`
18. To view the website type `python3 manage.py runserver` into the terminal and open port 8000.
19. The project is now ready to work on locally and any changes made can viewed using port 8000.

[Back to top](#contents)

## Credits

### Media
| Source | Location | Type |
| --- | --- | --- |
|[Tyres Blog Photo](https://d1nymbkeomeoqg.cloudfront.net/photos/26/6/382146_3623_XL.jpg) | Blog Article | image |
|[Product Image TRP ](https://www.bike-discount.de/media/image/fb/g0/7a/TRP-SLATE-EVO-Scheibenbremsen-Set-20126827_a_800x800.jpg) | Product detail | image |
|[Product Image pedals ](https://www.bike-discount.de/media/image/32/c7/1b/DMR-Vault-Plattformpedale-DMR-VAULT-O2_800x800.jpg) | Product detail pedals | image |
|[Pedal Product Photo](https://www.bike-discount.de/media/image/4a/db/8d/DMR-V12-blau-DMR-VV12-B9_800x800.jpg) | Products | image |
|[Tool Product Photo](https://www.bike-discount.de/media/image/75/38/39/15410087_1_800x800.jpg) | Products | image |
|[Tyre Product Photo](https://www.bike-discount.de/media/image/0e/4b/af/Michelin-475741-Wild-Enduro-Front-MAGI-X-DH-Racing-Line-29-Faltreifen-1_800x800.jpg) | Products | image |


### Resources
	- The Code Institute "Building an E-Commerce Platform" Boutique Ado project was very much relied upon to build this project.
	- Kim Bergstroem's Easy Keyboard project from [GitHub](https://github.com/KimBergstroem/PP5/tree/main) was used as inpiration in the website design, especially for the contact page and layout of the site.

### Acknowledgements

	- My Mentor Chris Quinn, for the contunied helpful feedback through out my project.
	- Jason and Oisin from Tutor support at Code Institute for their amazing support.
	- Alan Bushell at Code Institute for the contunied support through out the course.

[Back to top](#contents)