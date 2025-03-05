# google-search-top-10-restaurants

## start

invoke the venv: source venv/Scripts/activate   
run the main file: python main.py

## Approach

1. using https://serpapi.com/search.json to search query in google
2. stored api and api_key in .env 
3. using path param

        params = {  
            "engine": "google_local",   
            "q": "top+10+restaurants+for+best+food",    
            "location": "Delhi",    
            "gl": "in", 
            "hl": "en",     
            "api_key": API_KEY      
        }

2. create a search method which takes the user given city name
and fetch the data.
3. formatted the data as retaurant name as key and (reviews and rating) as value
4. dump the formatted data in a json file

## Example

enter the name of the city
<img width="466" alt="image" src="https://github.com/user-attachments/assets/39a5e1f1-1bbb-4925-a3ee-0b6e41ca2c82" />

hit enter
<img width="367" alt="image" src="https://github.com/user-attachments/assets/adf1f64a-753d-4483-b91c-068fbd70eb41" />

extracted restaurant data is saved in extract.json file
<img width="904" alt="image" src="https://github.com/user-attachments/assets/ec3f9bfa-4874-4ef0-9a26-6edad35f803b" />




