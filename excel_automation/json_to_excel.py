import openpyxl, json


# load in json
with open(file='projects2.json', mode='r') as file:
    projects_data = json.load(fp=file)['projects']

# read from the templates file the parameters
template_workbook = openpyxl.load_workbook(filename='template_project_parameters_all_fields.xlsx')

template_sheet = template_workbook.active
# create a new worksheet
new_workbook = openpyxl.Workbook()

new_sheet = new_workbook.active
# rename new_sheet
new_sheet.title = template_sheet.title

# take note of last cell position, for use later
sector_position = None
# use contents in template sheet to create contents in new sheet
for row in template_sheet.iter_rows():
    for cell in row:
        # insert normal parameters that are needed, such as heading
        if cell.value != None:
            new_sheet[cell.coordinate] = cell.value
        # insert values of parameters that are present in json
        if cell.value in projects_data:
            try: new_sheet[cell.coordinate] = projects_data[cell.value]
            except ValueError: pass
        # when finally at sectors, start restructuring data sector by sector, based on how many sectors are available
        if cell.value == 'sectors': sector_position = cell.coordinate
        
if sector_position is not None:
    for sector in projects_data[0]['sectors']:
        print(sector_position, sector)
        new_sheet[sector_position] = sector
        
        sector_items = projects_data[0]['sectors'][sector]
        for item in sector_items:
            # increment cell position to write items under sector
            sector_position = f'{sector_position[0]}{int(sector_position[1:])+1}'
            new_sheet[sector_position] = f'{item["ID"]} {item["name"]}'
            # loop through template again to get positions of quantity, unit and total
            for row in template_sheet.iter_rows():
                for cell in row:
                    if cell.value == 'Qtd.': new_sheet[f'{cell.coordinate[0]}{sector_position[1:]}'] = item['bom_quant']
                    if cell.value == 'Un': new_sheet[f'{cell.coordinate[0]}{sector_position[1:]}'] = item['unit']
                    if cell.value == 'Total': new_sheet[f'{cell.coordinate[0]}{sector_position[1:]}'] = item['bom_avgprice']
        # leave a row, then write Total de sectors in next row
        sector_position = f'{sector_position[0]}{int(sector_position[1:])+2}'
        new_sheet[sector_position] = f'Total de {sector}'
        # leave a row again before the next loop
        sector_position = f'{sector_position[0]}{int(sector_position[1:])+2}'


# take note of last cell position, for use later
sectors_parameters_position = None
project_parameters_position = None

def retrieve_parameters_cell_position_to_list(parameter_value) -> list:
    global sectors_parameters_position, project_parameters_position
    for row in template_sheet.iter_rows():
        for cell in row:
            if cell.value == parameter_value and 'sectors' in parameter_value: sectors_parameters_position = cell.coordinate
            elif cell.value == parameter_value and 'project' in parameter_value: project_parameters_position = cell.coordinate

    cell_position = sectors_parameters_position if 'sectors' in parameter_value else project_parameters_position
    cells_list = []
    for _ in range(100):
        cell_position = f'{cell_position[0]}{int(cell_position[1:])+1}'
        if template_sheet[cell_position].value is not None:
            cells_list.append(template_sheet[cell_position].value)
        else: break

    return cells_list

sectors_parameters_list = retrieve_parameters_cell_position_to_list(parameter_value='sectors parameters')
project_parameters_list = retrieve_parameters_cell_position_to_list(parameter_value='project parameters')

print(project_parameters_list)
for project in projects_data:

    for parameter in project_parameters_list:
        project_parameters_position = f'{project_parameters_position[0]}{int(project_parameters_position[1:])+1}'
        new_sheet[project_parameters_position] = project[parameter]
    
    project_parameters_position = f'{project_parameters_position[0]}{int(project_parameters_position[1:])+1}'

    for sector in project['sectors']:
        for detail in project['sectors'][sector]:
            for parameter in sectors_parameters_list:
                sectors_parameters_position = f'{sectors_parameters_position[0]}{int(sectors_parameters_position[1:])+1}'
                # print(f'detail parameter: {detail[parameter]}')
                new_sheet[sectors_parameters_position] = detail[parameter]
            # leave a space for the next set of details in this sector, if any...
            sectors_parameters_position = f'{sectors_parameters_position[0]}{int(sectors_parameters_position[1:])+1}'
        # leave another space for the next sector
        sectors_parameters_position = f'{sectors_parameters_position[0]}{int(sectors_parameters_position[1:])+1}' 


# save new workbook
new_workbook.save(filename='projects_data_autogenerated_sheet_all_fields.xlsx')