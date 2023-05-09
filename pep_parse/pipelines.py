import csv
from datetime import datetime
from pathlib import Path

BASE_DIR = Path(__file__).parent.parent


class PepParsePipeline:
    def open_spider(self, spider):
        self.status_counter = {}

    def process_item(self, item, spider):
        status = item['status']
        self.status_counter[status] = self.status_counter.get(status, 0) + 1
        return item

    def close_spider(self, spider):
        time = datetime.now().strftime('%Y-%m-%dT%H-%M-%S')
        filename = BASE_DIR / f'results/status_summary_{time}.csv'

        with open(filename, mode='w', encoding='utf-8', newline='') as file:
            writer = csv.writer(file)
            writer.writerow(['Статус' + ',' + 'Количество'])
            writer.writerows(self.status_counter.items())
            writer.writerow([f'Total,{sum(self.status_counter.values())}'])
