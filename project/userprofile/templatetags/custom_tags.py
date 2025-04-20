from django import template

register = template.Library()

@register.filter
def is_liked(obj,user):
    return obj.likes.all().filter(username=user.username).exists()

@register.filter
def is_saved(obj,user):
    return user.SavedPostModel_user.posts.all().filter(id=obj.id).exists()

@register.filter
def is_follow(obj,user):
    return user.UserRelationModel_user.following.all().filter(id=obj.id).exists()
