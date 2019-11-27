
# # ------------------------------------------------------------------------------

# Function Description

# Complete the makeAnagram function in the editor below. It must return an integer representing the minimum total characters that must be deleted to make the strings anagrams.
# https://www.hackerrank.com/challenges/ctci-making-anagrams/problem?h_l=interview&playlist_slugs%5B%5D=interview-preparation-kit&playlist_slugs%5B%5D=strings


# def create_freq_table(my_str):
#     my_str_dict = {}
#     for ch in my_str:
#         if ch in my_str_dict:
#             my_str_dict[ch] += 1
#         else:
#             my_str_dict[ch] = 1
#     return my_str_dict

# def makeAnagram(a, b):
#     a_dict = create_freq_table(a)
#     b_dict = create_freq_table(b)

#     first = b_dict
#     second = a_dict
#     count = 0
#     if(len(b_dict.keys()) > len(a_dict.keys())):
#         first = a_dict
#         second = b_dict

#     for key in first:
#         if key in second:
#             if (first[key] != second[key]):
#                 count += abs(first[key] - second[key])
#             second.pop(key, None)
#         else:
#             count += first[key]
#         # first.pop(key, None)

#     for key in second:
#         count += second[key]
#     return count


# def test(a, b, ans):
#     print("SUCCESS" if makeAnagram(a, b) == ans else "FAILURE")


# test("cde", "abc", 4)
# test("abcde", "abc", 2)
# test("abde", "abc", 3)


# ------------------------------------------------------------------------------

# ## check if the note can be created using words from magzine
# def checkMagazine1(magazine, note):
#     all_found = True
#     for word in note:
#         if word not in magazine:
#             all_found = False
#             break
#         else:
#             magazine.remove(word)

#     print("Yes" if all_found else "No")


# def checkMagazine(magazine, note):
#     mag_dict = {}
#     for word in magazine.split():
#         if word in mag_dict:
#             mag_dict[word] += 1
#         else:
#             mag_dict[word] = 1
#     all_found = True
#     for word in note.split():
#         if word in mag_dict:
#             mag_dict[word] -= 1
#             if mag_dict[word] == 0:
#                 mag_dict.pop(word, None)
#         else:
#             all_found = False
#             break
#     result = "Yes" if all_found else "No"
#     print(result)
#     return result


# # n, m = map(int, input().split())
# # magazine = input().rstrip().split()
# # note = input().rstrip().split()

# print("SUCCESS" if checkMagazine("ive got a lovely bunch of coconuts",
#                                  "ive got some coconuts") == "No" else "FAILURE")
# print("SUCCESS" if checkMagazine("give me one grand today night",
#                                  "give one grand today") == "Yes" else "FAILURE")
# print("SUCCESS" if checkMagazine("two times three is not four",
#                                  "two times two is four") == "No" else "FAILURE")
