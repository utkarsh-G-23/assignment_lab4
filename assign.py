class Table:
    def _init_(self, p_id, name, start_time, priority):
        self.p_id = p_id
        self.name = name
        self.start_time = start_time
        self.priority = priority

class ProcessTable:
    def _init_(self):
        self.pro = []

    def add_process(self, process):
        self.pro.append(process)

    def sort_by_pid(self):
        n = len(self.pro)
        for i in range(n - 1):
            for j in range(0, n - i - 1):
                if self.pro[j].p_id > self.pro[j + 1].p_id:
                    self.pro[j], self.pro[j + 1] = self.pro[j + 1], self.pro[j]

    def sort_by_start_time(self):
        n = len(self.pro)
        for i in range(n - 1):
            for j in range(0, n - i - 1):
                if self.pro[j].start_time > self.pro[j + 1].start_time:
                    self.pro[j], self.pro[j + 1] = self.pro[j + 1], self.pro[j]

    def sort_by_priority(self):
        priority_order = {"Low": 0, "MID": 1, "High": 2}
        n = len(self.pro)
        for i in range(n - 1):
            for j in range(0, n - i - 1):
                if priority_order[self.pro[j].priority] > priority_order[self.pro[j + 1].priority]:
                    self.pro[j], self.pro[j + 1] = self.pro[j + 1], self.pro[j]

    def print_table(self):
        for process in self.pro:
            print(f"P_ID: {process.p_id}, Process: {process.name}, Start Time: {process.start_time},Priority:{process.priority}")

def main():
    table = ProcessTable()

    table.add_process(Table("P1", "VSCode", 100, "MID"))
    table.add_process(Table("P23", "Eclipse", 234, "MID"))
    table.add_process(Table("P93", "Chrome", 189, "High"))
    table.add_process(Table("P42", "JDK", 9, "High"))
    table.add_process(Table("P9", "CMD", 7, "High"))
    table.add_process(Table("P87", "NotePad", 23, "Low"))

    print("Sorting Options:")
    print("1. Sort by P_ID")
    print("2. Sort by Start Time")
    print("3. Sort by Priority")

    choice = int(input("Enter your choice: "))

    if choice == 1:
        table.sort_by_pid()
    elif choice == 2:
        table.sort_by_start_time()
    elif choice == 3:
        table.sort_by_priority()
    else:
        print("Invalid choice!")

    table.print_table()


main()