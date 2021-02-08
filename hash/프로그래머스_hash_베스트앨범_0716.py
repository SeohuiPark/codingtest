import operator
import collections


def solution(genres, plays):
    genre_cnt_dict = {}
    for genre, play in zip(genres, plays):
        if genre in genre_cnt_dict.keys():
            genre_cnt_dict[genre] += play
        else:
            genre_cnt_dict[genre] = play
    print(genre_cnt_dict)

    info_dict = {}
    for idx, info in enumerate(zip(genres, plays)):
        genre, play_cnt = info[0], info[1]
        genre_cnt = genre_cnt_dict[genre]
        if genre in info_dict.keys():
            if len(info_dict[genre]) >= 2:
                info_dict[genre].append([genre_cnt, play_cnt, idx])
                info_dict[genre] = sorted(info_dict[genre], key=lambda x: -x[1])[:2]
            else:
                info_dict[genre].append([genre_cnt, play_cnt, idx])
        else:
            info_dict[genre] = [[genre_cnt, play_cnt, idx]]

    final_list = sum(info_dict.values(), [])
    ffinal_list = sorted(final_list, key=lambda x: (-x[0], -x[1], x[2]))

    return [i[2] for i in ffinal_list]

    answer = 0