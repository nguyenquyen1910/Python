class MonThi:
    def __init__(self, idSub="", nameSub="", typeSub=""):
        self.idSub = idSub
        self.nameSub = nameSub
        self.typeSub = typeSub


class CaThi:
    def __init__(self, i, date="", time="", idRoom=""):
        self.idCa = f"C{i:03d}"
        self.date = date
        self.time = time
        self.idRoom = idRoom


class LichThi:
    def __init__(self, idCa="", idSub="", idGroup="", students=0):
        self.idCa = idCa
        self.idSub = idSub
        self.idGroup = idGroup
        self.students = students


def read_monthi(file_name):
    with open(file_name, "r", encoding="utf-8") as f:
        n = int(f.readline().strip())
        subjects = []
        for _ in range(n):
            id_mon = f.readline().strip()
            name_mon = f.readline().strip()
            type_mon = f.readline().strip()
            subjects.append(MonThi(id_mon, name_mon, type_mon))
        return subjects


def read_cathi(file_name):
    with open(file_name, "r", encoding="utf-8") as f:
        n = int(f.readline().strip())
        sessions = []
        for i in range(n):
            date = f.readline().strip()
            time = f.readline().strip()
            id_room = f.readline().strip()
            sessions.append(CaThi(i + 1, date, time, id_room))
        return sessions


def read_lichthi(file_name):
    with open(file_name, "r", encoding="utf-8") as f:
        n = int(f.readline().strip())
        schedule = []
        for _ in range(n):
            line = f.readline().strip().split()
            id_ca = line[0]
            id_mon = line[1]
            id_group = line[2]
            students = int(line[3])
            schedule.append(LichThi(id_ca, id_mon, id_group, students))
        return schedule


def main():
    subjects = read_monthi("MONTHI.in")
    sessions = read_cathi("CATHI.in")
    schedule = read_lichthi("LICHTHI.in")

    full_schedule = []

    for i in schedule:
        for j in subjects:
            for k in sessions:
                if i.idCa == k.idCa and i.idSub == j.idSub:
                    full_schedule.append(
                        (
                            k.date,
                            k.time,
                            k.idRoom,
                            i.idCa,
                            j.nameSub,
                            i.idGroup,
                            i.students,
                        )
                    )

    full_schedule.sort(key=lambda x: (x[0], x[1], x[3]))

    for entry in full_schedule:
        date, time, idRoom, i.idCa, subject_name, group, students = entry
        print(f"{date} {time} {idRoom} {subject_name} {group} {students}")


if __name__ == "__main__":
    main()
