import schedule
from datetime import datetime
from database.insert import insert_data_mysql
from program.tvl import get_total_value_locked


def main():
    total_value_locked = get_total_value_locked('https://defillama.com/chain/Ethereum')
    print(total_value_locked)
    current_datetime = datetime.now().strftime('%H:%M %Y-%m-%d')
    # insert_data_mysql('ethereum', [current_datetime, total_value_locked])


if __name__ == '__main__':
    main()
    # schedule.every(1).minutes.do(main)
    # while True:
    #     schedule.run_pending()