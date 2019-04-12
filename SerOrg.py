# import guessit
# import os



# video = 'Greyss Anatomy S15E18 Add It Up 720p AMZN WEB-DL DDP5 1 H 264-NTb [eztv].mkv'
# m = guessit.guessit(video)

# print(m)


# def recursion(a, c):
#     tipo_season = ['season', 'temp', 'Season']
#     c = c + 1
#     for b in os.scandir(a):
#         if b.is_dir():
#             if len(b.name.split()) > 1:
#                 for temp in tipo_season:
#                     if temp in b.name.split()[0]:
#                         print(' '*c, '  |__ Season', b.name.split()[1])
#                     # else:
#                     #     print(' '*c, '  |__', b.name)
#                     #     recursion(b, c)
#             else:
#                 print(' '*c, '  |__ Season', b.name)

            
# dir = os.scandir('C:\\Users\\dotero\\Documents\\app\\Serie')

# for a in dir:
#     c = 0
#     if a.is_dir():
#         print(a.name)
#         recursion(a, c)
