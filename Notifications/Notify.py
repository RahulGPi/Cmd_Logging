from win11toast import notify

class noti:
    def check(cleanedlist:list):
        if(cleanedlist[1] == 'HIGH'):
            notify(app_id='COMMAND_LOG',title='ALERT!!!',body=f'Take Action Immediately\n{cleanedlist[0]}') 