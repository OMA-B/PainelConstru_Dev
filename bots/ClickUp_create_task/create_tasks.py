import requests, os, time
from dotenv import load_dotenv
from datetime import datetime
from clickup import project1, client1, task

load_dotenv()

assignees_budgetist = {
  386: 44246993,
  489: 18901584,
  502: 81925823,
  98: 18901639,
}


def create_task_on_clickup(project_data: dict, client_data: dict, task_data: dict= None):
    
  # task data
  list_id = os.getenv('LIST_ID')
  if task_data is not None:
    list_id = task_data['Task_List']
    status = task_data['Task_Status']
  else: status = 'aberto'

  # Connect to the clickup API
  url = f"https://api.clickup.com/api/v2/list/{list_id}/task"

  query = {
    "custom_task_ids": True,
    "team_id": 386
  }

  # assigning projects
  if int(project_data['Proj_Budgetist']) in assignees_budgetist:
    assignee = assignees_budgetist[int(project_data['Proj_Budgetist'])]
  else:
    assignee = assignees_budgetist[386]

  # configuring project start and due date
  def convert_date_string_to_datetime(local_date_string):
    local_date = datetime.strptime(local_date_string, '%d/%m/%Y')
    timestamp = (local_date - datetime(year=1970, month=1, day=1)).total_seconds() * 1000
    return timestamp
  
  # start date
  if project_data['Proj_Date'] == None or '/' not in project_data['Proj_Date']:
    start_date = int(time.time() * 1000)
  else:
    start_date = convert_date_string_to_datetime(local_date_string=project_data['Proj_Date'])
  
  # due date
  if project_data['Proj_Duedate'] == None or '/' not in project_data['Proj_Duedate']:
    three_days_in_millisec = 259200000
    due_date = int(time.time() * 1000) + three_days_in_millisec
  else:
    due_date = convert_date_string_to_datetime(local_date_string=project_data['Proj_Duedate'])

  # setting 

  payload = {
    "name": f"{project_data['Proj_ID']} - {project_data['Proj_Name']}",
    "description": f"""
      Project Description:
          {project_data['Proj_Description']} 
          BOM List: {str(project_data['BOM_List'])}
      
      Project Location: 
          {project_data['Proj_Address']} 
          {project_data['Proj_City']} - {project_data['Proj_State']} - {project_data['Proj_Country']}
          CEP: {project_data['Proj_ZIP']}
      
      Client:
          {client_data['Client_ID']} - {client_data['Client_Name']} 
          WhatsApp: {client_data['Client_Whats']}
          Phone Number: {client_data['Client_Phone']} 
          Email Address: {client_data['Client_email']}
      
      Contact Origin:
          {client_data['Client_origin']}
    """,
    "assignees": [assignee],
    "status": status,
    "priority": 3,
    "due_date": due_date,
    "due_date_time": True,
    "start_date": start_date,
    "start_date_time": True,
    "time_estimate": 8640000,
    "notify_all": True,
  }

  headers = {
    "Content-Type": "application/json",
    "Authorization": os.getenv("IGOR_API_TOKEN")
  }

  # create a task 
  response = requests.post(url=url, json=payload, params=query, headers=headers)

  return {"task_ID": response.json()['id'], "task_link": response.json()['url']}




if __name__ == '__main__':

  create_task_on_clickup(project_data=project1, client_data=client1)