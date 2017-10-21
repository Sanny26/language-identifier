from identifier import *


def get_lang_label(profile, lprofiles):
    lang_label = -1
    min_dist = 99999

    for key, lprofile in lprofiles.items():
      dist = 0
      for i, val in enumerate(profile):
        if val in lprofile:
            dist+=abs(i-lprofile.index(val))
        else:
            dist+=len(lprofile)

        if dist < min_dist:
            min_dist = dist
            lang_label = key

    return lang_label 

if __name__ =='__main__':

   test_file = raw_input('Enter file path to be identified: ')

   profile = get_file_lprofile(test_file)
   profile = [each[0] for each in profile.most_common(top_k_val)]   

   lprofiles = pickle.load(open('lprofiles.txt', 'rb'))

   lang_label = get_lang_label(profile, lprofiles)

   print lang_label

