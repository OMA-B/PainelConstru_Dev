import requests, os, pprint, random
from create_tasks import assignees_budgetist
from faker import Faker


task_data = {'task_ID': '86a1bdvgu', 'task_link': 'https://app.clickup.com/t/86a1bdvgu'}
fake = Faker()

def add_comments_to_tasks(task_id: str, assignee: int, comment: str):

  url = f"https://api.clickup.com/api/v2/task/{task_id}/comment"

  query = {
    "custom_task_ids": True,
    "team_id": 386
  }

  payload = {
    "comment_text": comment,
    "assignee": assignees_budgetist[int(assignee)],
    "notify_all": True
  }

  headers = {
    "Content-Type": "application/json",
    "Authorization": os.getenv('IGOR_API_TOKEN')
  }

  response = requests.post(url, json=payload, headers=headers, params=query)

  return response.status_code


if __name__ == '__main__':
  add_comments_to_tasks(task_id=task_data["task_ID"], assignee=random.choice([386, 489, 502, 98]), comment="your comment goes here") #assignees should be the person the comment is for, and should be anyone in the random list