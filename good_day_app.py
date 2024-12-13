from datetime import datetime
import sys
from flask import Flask
from freezegun import freeze_time

app = Flask(__name__)

weekdays_list = ['понедельник','вторник','среда','четверг','пятница','суббота', 'воскресенье']
weekdays_tuple = ('понедельник','вторник','среда','четверг','пятница','суббота', 'воскресенье')
weekdays_dict = {i: weekdays_list[i] for i in range(len(weekdays_list))}
# print(weekdays_dict)
# print(sys.getsizeof(weekdays_list))
# print(sys.getsizeof(weekdays_tuple))
# print(sys.getsizeof(weekdays_dict))
#кортеж весит меньше
@freeze_time('2024-12-12')
def get_weekday():
    weekday = datetime.today().weekday()
    if weekday in [0, 1, 3]:
        return f'Хорошего {weekdays_tuple[weekday]}a'
    elif weekday == 6:
        return f'Хорошего {weekdays_tuple[weekday][0:-1]}я'
    else:
        return f'Хорошей {weekdays_tuple[weekday][0:-1]}ы'
# print(get_weekday())

@app.route("/good_day/<user>")
def good_day(user):
    text = f'Привет {user}! '+ get_weekday()
    return text
if __name__ == '__main__':
    app.run(debug=True)
