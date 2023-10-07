import requests, os, pprint, time, random
from dotenv import load_dotenv
from faker import Faker


load_dotenv()

# create fake data for testing
fake_data = Faker()


def create_task_on_clickup(id_proj, proj_name, proj_detail: str, assignee: int):
    
  # Connect to the clickup API
  list_id = os.getenv('LIST_ID')
  url = f"https://api.clickup.com/api/v2/list/{list_id}/task"
  mock_url = f'https://a00fb6e0-339c-4201-972f-503b9932d17a.remockly.com/list/{list_id}/task'

  query = {
    "custom_task_ids": True,
    "team_id": 386
  }

  # configuring project start date and due date
  three_days_in_millisec = 259200000
  start_date = int(time.time() * 1000)



  payload = {
    "name": f"{id_proj} - {proj_name}",
    "description": proj_detail,
    "assignees": [386, 489, 502, 98],
    # "tags": [tag],
    # "status": "open",
    "priority": 3,
    "due_date": start_date + three_days_in_millisec, # 1508369194377    1696640018
    "due_date_time": False,
    # "time_estimate": 8640000,
    "start_date": 1696643789945,
    "start_date_time": False,
    "notify_all": True,
  }

  headers = {
    "Content-Type": "application/json",
    "Authorization": os.getenv("API_TOKEN_2")
  }

  # create a task 
  response = requests.post(url=url, json=payload, params=query, headers=headers)

  pprint.pprint(response.json())

  pprint.pprint({'actual_start_date': start_date, 'actual_due_date': start_date + three_days_in_millisec})


if __name__ == '__main__':

  create_task_on_clickup(id_proj=random.randint(100, 200), proj_name=fake_data.name(), proj_detail=fake_data.text(), assignee=random.choice([386, 489, 502, 98]))