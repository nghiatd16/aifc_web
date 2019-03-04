from .models import Challenge, Member, Submission
from django.db.models import Max


def ranking(challenge):
    lst_sub = Submission.objects.all().filter(challenge=challenge)
    lst_sub = lst_sub.exclude(result__isnull=True)
    lst_mem = Member.objects.all()
    no_sub = []
    lst_best_sub = []
    for mem in lst_mem:
        mem_sub = lst_sub.filter(member=mem)
        if len(mem_sub) == 0:
            no_sub.append(mem)
            continue
        max_sub = mem_sub.aggregate(Max('result'))
        lst_best_sub.append(mem_sub.filter(result=max_sub['result__max']).latest(field_name='time'))
    sorted_lst_sub = sorted(lst_best_sub, key=lambda sub: sub.result, reverse=True)
    final_rank = []
    for idx, submit in enumerate(sorted_lst_sub):
        mem = submit.member
        if mem.id == 2:
            lst_data = [str(idx+1), mem.get_show_name(), str(mem.gen), "{}".format(submit.result), 'black']
        elif mem.id == 1:
            lst_data = [str(idx+1), mem.get_show_name(), str(mem.gen), "{}".format(submit.result), 'red']
        else:
            lst_data = [str(idx+1), mem.get_show_name(), str(mem.gen), "{}".format(submit.result), 'blue']
        final_rank.append(lst_data)
    for mem in no_sub:
        if mem.id == 2:
            final_rank.append(["Unranking", mem.get_show_name(), str(mem.gen), "No Submission Judged", 'black'])
        elif mem.id == 1:
            final_rank.append(["Unranking", mem.get_show_name(), str(mem.gen), "No Submission Judged", 'red'])
        else:
            final_rank.append(["Unranking", mem.get_show_name(), str(mem.gen), "No Submission Judged", 'blue'])
    # print(final_rank)
    return final_rank
