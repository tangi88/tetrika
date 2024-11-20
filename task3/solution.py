

def appearance(intervals: dict[str, list[int]]) -> int:
    lesson = intervals['lesson']
    pupil = intervals['pupil']
    tutor = intervals['tutor']
    start_lesson = lesson[0]
    finish_lesson = lesson[1]

    lst_pupil = []
    for j in range(0, len(pupil), 2):
        lst_pupil.extend(list(range(pupil[j], pupil[j + 1])))

    lst_tutor = []
    for j in range(0, len(tutor), 2):
        lst_tutor.extend(list(range(tutor[j], tutor[j + 1])))

    res = 0

    for k in range(start_lesson, finish_lesson):
        if k in lst_pupil and k in lst_tutor:
            res += 1

    return res

