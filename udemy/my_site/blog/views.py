from datetime import date
from django.shortcuts import render

all_posts = [
    {
        "slug": "hike-in-the-mountains",
        "image": "mountains.jpg",
        "author": "Vijay",
        "date": date(2021, 7, 21),
        "title": "Mountain Hiking",
        "excerpt": "There is nothing like the views you get when hiking is the mountains! And I wasn't even prepared for what happened whilst I was enjoying the view!",
        "content": """
           Lorem ipsum dolor sit, amet consectetur adipisicing elit. Quae eaque labore facere nam consequuntur esse expedita itaque ex? Natus ipsa sequi error accusamus a tempore rerum nihil architecto quisquam minus!
           
           Lorem ipsum dolor sit, amet consectetur adipisicing elit. Quae eaque labore facere nam consequuntur esse expedita itaque ex? Natus ipsa sequi error accusamus a tempore rerum nihil architecto quisquam minus!
           
           Lorem ipsum dolor sit, amet consectetur adipisicing elit. Quae eaque labore facere nam consequuntur esse expedita itaque ex? Natus ipsa sequi error accusamus a tempore rerum nihil architecto quisquam minus! 
        """
    },
    
    {
        "slug": "programming-is-fun",
        "image": "coding.jpg",
        "author": "Vijay",
        "date": date(2022, 5, 11),
        "title": "Programming Is Great!",
        "excerpt": "Did you ever spend houors searching that one error in your code?",
        "content": """
           Lorem ipsum dolor sit, amet consectetur adipisicing elit. Quae eaque labore facere nam consequuntur esse expedita itaque ex? Natus ipsa sequi error accusamus a tempore rerum nihil architecto quisquam minus!
           
           Lorem ipsum dolor sit, amet consectetur adipisicing elit. Quae eaque labore facere nam consequuntur esse expedita itaque ex? Natus ipsa sequi error accusamus a tempore rerum nihil architecto quisquam minus!
           
           Lorem ipsum dolor sit, amet consectetur adipisicing elit. Quae eaque labore facere nam consequuntur esse expedita itaque ex? Natus ipsa sequi error accusamus a tempore rerum nihil architecto quisquam minus! 
        """
    },
    {
        "slug": "into-the-woods",
        "image": "woods.jpg",
        "author": "Vijay",
        "date": date(2020, 3, 17),
        "title": "Nature At Its Best!",
        "excerpt": "Nature is amazing! The amount of inspiration I get when I am walking through the woods or along the beach is unparalleled.",
        "content": """
           Lorem ipsum dolor sit, amet consectetur adipisicing elit. Quae eaque labore facere nam consequuntur esse expedita itaque ex? Natus ipsa sequi error accusamus a tempore rerum nihil architecto quisquam minus!
           
           Lorem ipsum dolor sit, amet consectetur adipisicing elit. Quae eaque labore facere nam consequuntur esse expedita itaque ex? Natus ipsa sequi error accusamus a tempore rerum nihil architecto quisquam minus!
           
           Lorem ipsum dolor sit, amet consectetur adipisicing elit. Quae eaque labore facere nam consequuntur esse expedita itaque ex? Natus ipsa sequi error accusamus a tempore rerum nihil architecto quisquam minus! 
        """
    }
]

def get_date(post):
    return post['date']
# Create your views here.

def starting_page(request):
    sorted_posts = sorted(all_posts, key=get_date)
    latest_posts = sorted_posts[-3:]
    return render(request, "blog/index.html", {
        "posts": latest_posts
    })

def posts(request):
    return render(request, "blog/all-posts.html", {
        "all_posts": all_posts
    })

def post_detail(request, slug):
    identified_post = next(post for post in all_posts if post['slug']==slug)
    return render(request, "blog/post-detail.html",{
        "post": identified_post
    })
