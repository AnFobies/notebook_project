import function as func
import UI


def start():
    input_from_user = ''
    while input_from_user != 7:
        UI.menu()
        input_from_user = input().strip()
        if input_from_user == '1':
            func.show('all')
        if input_from_user == '2':
            func.add()
        if input_from_user == '3':
            func.show('all')
            func.id_edit_delite_show('del')
        if input_from_user == '4':
            func.show('all')
            func.id_edit_delite_show('edit')
        if input_from_user == '5':
            func.show('date')
        if input_from_user == '6':
            func.show('id')
            func.id_edit_delite_show('show')
        if input_from_user == '7':
            UI.goodbye()
            break
