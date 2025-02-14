from django.http import JsonResponse
import requests
import csv
import os

def get_facebook_data(request):
    access_token = ''  # Replace with your actual access token
    page_id = ''  # Replace with your actual page ID
    url = f'https://graph.facebook.com/v14.0/{page_id}/posts?access_token={access_token}'
    
    all_posts = []
    
    # Loop to get all posts (pagination handling)
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
    
    # Define the file path where the CSV will be saved
    file_path = 'scraper/files/facebook_posts.csv'
    
    # Ensure the directory exists
    os.makedirs(os.path.dirname(file_path), exist_ok=True)
    
    # Create and write the data to a CSV file
    try:
        with open(file_path, mode='w', newline='', encoding='utf-8') as file:
            writer = csv.DictWriter(file, fieldnames=['id', 'message', 'created_time'])
            writer.writeheader()  # Write the header row
            
            # Write each post as a row in the CSV file
            for post in all_posts:
                writer.writerow(post)

        # Return success message with file path
        return JsonResponse({
            'message': 'CSV file created successfully!',
            'file_path': file_path
        })

    except Exception as e:
        # If there's an error creating the file, return an error message
        return JsonResponse({'error': str(e)}, status=500)
