def compare(file_data_obj_1, file_data_obj_2):
    report = []
    non_consistent_data_report: [str] = []
    missing_data_report: [str] = []
    first_dataset = file_data_obj_1.data
    second_dataset = file_data_obj_2.data

    found = False
    for data1 in first_dataset:
        if data1[-1] == 0 and data1[-2] == 0:
            continue
        for data2 in second_dataset:
            if data1[-1] == 0 and data1[-2] == 0:
                continue
            if str(data1[1]).lower() == str(data2[1]).lower():
                deep_compare_result = deep_compare(data1, data2)
                if deep_compare_result != None:
                    non_consistent_data_report.append(deep_compare_result)
                found = True
                break
        if found:
            found = False
        else:
            missing_data_report.append(f'студент не найден в одном из документов{data1}')

    for data1 in second_dataset:
        if data1[-1] == 0 and data1[-2] == 0:
            continue
        for data2 in first_dataset:
            if data1[-1] == 0 and data1[-2] == 0:
                continue
            if str(data1[1]).lower() == str(data2[1]).lower():
                found = True
                break
        if found:
            found = False
        else:
            missing_data_report.append(f'студент не найден в одном из документов{data1}')

    with open('compare_report.txt','w', encoding='utf-8') as file:
        file.write('\n'.join(non_consistent_data_report) + '\n' +'\n'.join(missing_data_report))

def deep_compare(data1_tuple, data2_tuple):
    ignore_index = {0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10}
    result_str = ''
    for i in range(len(data1_tuple)):
        if data1_tuple[i] != data2_tuple[i] and not (i in ignore_index):
            result_str += f'позиция №{i} ({data1_tuple[i]} - {data2_tuple[i]})'
    if result_str == '':
        return None
    else:
        return f"найдены несовпадения данных {data1_tuple[1]}  и {data2_tuple[1]} в позициях:  " + result_str