Wayfarer Travel Community
==============================================================

### A group project for GA's Django Unit
#### Group Members: Rommel Aquino, Henry McGehee, Nathan J Harris


Home Page:
==============================================================
![Home Page](/images/wayfarer-homepage.png)


What is the Wayfarer Travel Community?  
--------------------------------------
A web application where users can interact with city travel destinations by adding posts and viewing other users' posts sharing travel tips per city along the way.  Each user can also navigate their own profile page showing recent posts as well as make comments on posts.  

Technologies Used
-----------------
- Server Language: Python
- Web Framework: Django
- Database: Postgresql
- Templates: HTML and Django Templating Language
- CSS Library: Bulma
- Javascript


Code Snippet
-------------
The following is the view function for the city page

```{.python}
# ________________   City Index Route  ____________________

def city_index(request, city_id):
    cities = City.objects.all()
    city = City.objects.get(id=city_id)
    current_user = request.user
    id = current_user.id
    profile = Profile.objects.get(user=id)
    # POST METHOD
    if request.method == 'POST':
        form = PostForm(request.POST)
        if form.is_valid():
            new_post = form.save(commit = False)
            new_post.city_id = city_id
            new_post.profile_id = profile.id
            new_post.save()
        return redirect('city_index', city_id)
    # GET METHOD
    else:
        form = PostForm()
        context = {
            'city': city,
            'form': form,
            'cities': cities,
            'profile': profile,
        }
        return render(request, 'city/city.html', context)
```

City Page:
==============================================================
![City Page](/images/city-page.png)


Link: 
======
herokuapp link

A Very Special Thanks...
========================
To our associate instructor Yulia Tsernant who served as our client for this project as well as helping us whenever we got stuck on a Django error message!  Also many thanks to instructors Kenny Bushman and Michael Petty for teaching us Python, Django, and SQL as well as helping us with seeding the database for development.  

Upcoming Features
=================
- Image upload for users to upload to their profile, city pages, posts, and comments
- Add new city button
- Welcome email for new users

All images on this site were courtesy of Unsplash.com