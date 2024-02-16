# import stuff

def create_task(project_data=None, client_data=None, task_data=None):
    
    # YOUR MAGIC GOES HERE
    task_id='9988'
    
    return(task_id)


# if __name__ == '__main__':
"""This will be used to test the create_task"""

project1={
    'Proj_Name':'Test task 5',
    'Proj_ID': 400,
    'Proj_Description':'Project created to test the clickup CRM API connection',
    'Proj_Address':'Av. Iguaçu, 123',
    'Proj_City':'Porto Alegre',
    'Proj_State':'RS',
    'Proj_Country':'Brasil',
    'Proj_ZIP':90610285,
    'Proj_Date': None, #'15/08/2023', #change it to a datetime format
    'Proj_Duedate': '15/08/2024', #change it to a datetime format
    'Proj_Budgetist':386,
    'Proj_Status':None,
    'BOM_List':None
}

client1={
    'Client_Name':'Test Client',
    'Client_ID':3214,
    'Client_Whats':5551993777410,
    'Client_Phone':5551993777410,
    'Client_email':'igor@painelconstru.com.br',
    'Client_origin':'whatsapp'
}

# If this is an existing task at clickup, we might send the task information along to be updated.
task={
    'Task_ID': 9988,
    'Task_Status':'iniciado',
    'Task_List': 901300730376
}


    # print(create_task(project_data=project1,client_data=client1))