# freesource-collective

## Project Description

Freesource Library Collective, collect free resources for life.

* Mission: 
To provide an easy to use tool that allows users to currate and organize the free resources available that best suits their needs.

* Vision: 
Freesource Library Collective is dedicated to providing access to the knowledge and tools needed to learn how to live, and allowing users the abilty to manage and categorize those resources in a way that works for them.

* Why is our mission and vision important?
This site is meant to help others by providing access to the accumulated knowledge and tools they need to learn how to live the life they want to live, and make it easy to save those resources that are most beneficial in a way that makes it faster to find that information the next time it needs referenced.

## Wireframes and User Stories

Users that are not logged in will be directed to the About page initially. The About, Home, Log In, and Register pages will be that only available pages until a valid user is logged in. The About page will give users information about the usage of the application as well as the idea behind the application. From this about page a valid logged in user can navigate to any other page in the navigation bar.

![About Page](https://user-images.githubusercontent.com/98247684/172153721-47193155-9bdf-4e06-b48b-cc70fa2ea809.png)

Upon navigating to the Home page users that are not logged in will have will have access to view and reference all resources available organized by their classifications in the database. A user may also click the resource and see more information about it on the Resource Detail page.


![Home Page](https://user-images.githubusercontent.com/98247684/172153660-3e678a8b-1c5c-4588-8c1f-517db325791d.png)

From the Resource Detail page users will see a short description of the resource and an external link for the resource. Users will also have access to add individual resources into a resource list of their own. 

![Resource Detail Page](https://user-images.githubusercontent.com/98247684/172153753-9714b6ae-81f3-4929-ba57-87a456329ee6.png)

On the Lists Page users will see all of their created resource lists complete with any assigned categorizations. Clicking on a List will then take users to a List Detail Page.

![List List Page](https://user-images.githubusercontent.com/98247684/172153897-1bbeb895-9efd-4235-9ff5-3d3dd0641fc9.png)

The List Detail page will display links to all resources that have been added to that list as well as an option that allows users to add the list into a book of resource lists. 

![List Detail Page](https://user-images.githubusercontent.com/98247684/172153779-cb6a7ecb-80dc-4252-b300-e796664dcbbd.png)

The Books Detail page will contain a listing of links to all Resource Books that a user has created as well as a short description of the book. 

![Book List Page](https://user-images.githubusercontent.com/98247684/172153919-3569230e-ed28-4f32-abc7-7835f0b24332.png)

The Book Detail Page will display the infomartion of all lists that have been added, including the title of each list and the name of each resource the list contains. 

![Book Detail Page](https://user-images.githubusercontent.com/98247684/172153987-86d7f5f1-aa5a-423c-890c-3c186a4a9361.png)

## MVP

* Create a fully functioning application that is deployed and free of errors.
* Application will be created and styled using Python, Django, Tailwind, PostgreSQL, and Heroku.
* CRUD functionality for users of books and lists focusing on only one resource type.

## Entity Relationships

![ERD](https://user-images.githubusercontent.com/98247684/172157786-388f4257-3bfb-4a1a-995c-cc2b0c14ec63.png)

### Stretch Features:

![Category Page](https://user-images.githubusercontent.com/98247684/172154008-28e05c32-e4ec-4178-b636-5fc2028c807c.png)

* Add additional resource types and implement a page for Listing Resources by Type and a detail page showing the resources by category within each reseource type. 
* Add search bars to any relevant page
* Implement private notes and public comments for users onto resources, lists, and books.
* Implement user profiles. 
