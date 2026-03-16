import breakfast_sheet
import time

if __name__ == '__main__':
    try:
        monthyear = time.strftime('%B_%Y')
        date = time.strftime('%Y%m%d')
        breakfast_sheet.generate_daily_sheet(monthyear, date)
    except Exception as e:
        with open('./error.txt', 'a') as errfile:
            errfile.write(f'{time.strftime('%m_%d_%y %H:%M:%S')}: {e}\n')

# for i in range(1, 15):
#     day = f'2026030{i}' if i < 10 else f'202603{i}'
#     breakfast_sheet.generate_daily_sheet('March_2026', day)