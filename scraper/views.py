from django.http import JsonResponse
import requests

def get_facebook_data(request):
    access_token = ''
    page_id = ''
    url = f'https://graph.facebook.com/v14.0/{page_id}/posts?access_token={access_token}'
    
    all_posts = []
    
    while True:
        response = requests.get(url)
        data = response.json()
        
        if 'data' in data:
            for post in data['data']:
                all_posts.append({
                    'id': post['id'],
                    'message': post.get('message', 'No message'),
                    'created_time': post['created_time']
                })
        
        # Check if there's a next page of posts
        if 'paging' in data and 'next' in data['paging']:
            url = data['paging']['next']  # Get the URL for the next page
        else:
            break
    
    return JsonResponse(all_posts, safe=False)