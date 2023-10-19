import re

whatsapp_phones = ["Avi, Nitzan, Yifat, אבישג, מייקרלאב, +972 52-354-2312, +972 50-588-2388, +972 54-498-0346, +972 54-548-3313, +972 52-356-9739, +972 53-284-0066, +972 58-730-3505, +972 52-484-6334, +972 54-436-8644, +972 54-677-4524, +972 50-585-0492, +972 53-825-7554, +972 54-475-3873, +972 54-263-1322, +972 52-667-7884, +972 52-838-2025, +972 52-556-5638, +972 50-935-1445, +972 50-554-8566, +972 52-618-0740, +972 52-555-5012, +972 52-865-6281, +972 54-535-5200, +972 55-254-4494, +972 52-319-6413, +972 52-808-8812, +972 54-478-7640, +972 54-793-0651, +972 52-830-9001, +972 53-525-6141, +972 50-776-8889, +972 52-315-1100, +972 54-558-8811, +972 54-566-4432, +972 52-555-6272, +972 50-315-5388, +972 50-693-8320, +972 54-654-3030, +972 54-639-5961, +972 52-424-8486, +972 52-447-3379, +972 50-673-4911, +972 50-730-0890, +972 50-233-2254, +972 50-296-3999, +972 50-313-7585, +972 50-432-1288, +972 50-451-8243, +972 50-506-8557, +972 50-546-9900, +972 50-572-2920, +972 50-595-2915, +972 50-621-0496, +972 50-622-0682, +972 50-623-6330, +972 50-624-2359, +972 50-648-6267, +972 50-655-4182, +972 50-670-9585, +972 50-721-5160, +972 50-722-3790, +972 50-731-3260, +972 50-736-5365, +972 50-736-7330, +972 50-769-4955, +972 50-774-9337, +972 50-779-7061, +972 50-854-4524, +972 50-878-5844, +972 50-889-5704, +972 50-978-9087, +972 52-212-2232, +972 52-222-1217, +972 52-237-0694, +972 52-243-6805, +972 52-250-3681, +972 52-250-9375, +972 52-255-2622, +972 52-276-2057, +972 52-296-2775, +972 52-312-8232, +972 52-321-6678, +972 52-336-2535, +972 52-352-9806, +972 52-356-4015, +972 52-357-4605, +972 52-357-6047, +972 52-358-1442, +972 52-360-7371, +972 52-364-0959, +972 52-364-5302, +972 52-365-5768, +972 52-379-8883, +972 52-382-2424, +972 52-392-7535, +972 52-397-4527, +972 52-400-1220, +972 52-423-6501, +972 52-445-2288, +972 52-457-0729, +972 52-457-9893, +972 52-460-7907, +972 52-462-6344, +972 52-478-4141, +972 52-482-4309, +972 52-526-3383, +972 52-539-0427, +972 52-544-4673, +972 52-544-6339, +972 52-546-0498, +972 52-626-8599, +972 52-654-3378, +972 52-656-9969, +972 52-720-6728, +972 52-836-9391, +972 52-870-2546, +972 52-924-7538, +972 52-927-7224, +972 52-946-5558, +972 53-223-4082, +972 53-334-7120, +972 53-422-6546, +972 53-458-0085, +972 53-555-9519, +972 53-734-6145, +972 53-951-2715, +972 54-213-1939, +972 54-220-7702, +972 54-222-8522, +972 54-232-2932, +972 54-234-7785, +972 54-242-2018, +972 54-323-0031, +972 54-336-6571, +972 54-397-5438, +972 54-423-2123, +972 54-433-4321, +972 54-441-6520, +972 54-447-1260, +972 54-449-7133, +972 54-464-6606, +972 54-466-5424, +972 54-469-5608, +972 54-523-2472, +972 54-524-3804, +972 54-525-6817, +972 54-535-5400, +972 54-537-4141, +972 54-544-6438, +972 54-545-5894, +972 54-547-8858, +972 54-548-1694, +972 54-548-2109, +972 54-551-5282, +972 54-555-3111, +972 54-563-7022, +972 54-571-1031, +972 54-580-0163, +972 54-592-6699, +972 54-630-3565, +972 54-635-6212, +972 54-648-2470, +972 54-654-2254, +972 54-660-8418, +972 54-661-0146, +972 54-682-8471, +972 54-688-4332, +972 54-730-0789, +972 54-738-0771, +972 54-751-6461, +972 54-757-1415, +972 54-774-2798, +972 54-776-0888, +972 54-777-4712, +972 54-779-9887, +972 54-780-1516, +972 54-788-7378, +972 54-797-7828, +972 54-805-1606, +972 54-805-3750, +972 54-888-5735, +972 54-892-8606, +972 54-940-1780, +972 54-977-3821, +972 54-998-6604, +972 55-503-0807, +972 55-688-5057, +972 58-454-0312, +972 58-514-0626, +972 58-627-2142, +972 58-664-0001, +972 58-714-1308, +972 58-727-4840, +972 58-786-6136, You"]
excel_phones = ["502768530,523576047,528088812,507300890,523542312,523564015,505850492,506938320,528382025,584540312,528724171,547774712,523640959,549986604,506220682,542347785,524579893,507365365,507215160,539512715,545355400,506211854,524236501,523569739,528309001,505068557,505469900,508544524,544646606,547081516,547516461,547930651,532234082,584540312,585140626,542631322,547516461,545553111,526677884,524607907,546482470,506276649,542228522,506777182,545232472,587866136,523151100,552544494,548051606,509351445,525533133,587141308,502963999,542422018,529247538,529465558,544334321,528656281,586272142,528461119,525565638,503155388,545374141,545483313,587303505,523196413,508785844,506734911,547571415,546610146,524846334,547760888,50313-7585,524626344,505722920,547452541,547452541,524784141,546356212,535256141,506486267,524784141,586640003,506292185,524473379,523128232,524473379,523581442,508895704,523822424,525555012,526268599,534226546,522762057,525263383,546302565,523645302,545446438,545355200,544665424,534580085,533347120,549401780,523655768,523607371,545243804,544797252,525446339,506210496,506567375,507819917,549773821,535559519,523362535,545515282,543366571,545800163,529661017,507694955,543230031,524001220,526543378,526543378,504518243,542207702,505882388,506242359,506242359,544232123,505952915,537346145,546774524,548053750,523529806,545481694,544404745,504321288,545711031,522962775,555648378,544368644,544471260,532840067,548885735,543975438,545926699,507693613,544753873,545256817,506236330,523339148,525838834,546395961,506709585,538257544,547300789,525390427,523574605,544695608,523798883,507768889,523557527,585258258,524824309,527206728,545588811,525556272,524226969,522221217,542322932,545215313,546828471,545664877,547380771,524570729,547799887,552764174,522552622,545637022,522552622,546543030,524248486,522370694,544787640,545874235,522552662,544980346,507797061,506202607,528369391,546884332,545482109,542131939,546542254,526180740,547930651,544416520,587274840,523736174,523736174,523736174,545664432,545455894,547977828,529277224,507740152,546608418,505548566,502332254,534500234,526569969,543214111,523927535,522503681,547742798,542951297,506554182,545478858,507313260,522509375,534500234,547887378,524452288,509789.87,523216678,507367330,556885057,525460498,523974527"]

#take the whatsapp list with a long string and devide it to a list of numbers seperated by a comma
#return a list of numbers
def turn_string_to_array(phones):
    phones = phones[0].split(",")
    return phones


#go over the list and delete the +972 and the spaces
#return a list of numbers
def format_numbers(phones):
    formatted_numbers = []
    for number in phones:
        formatted_number = re.sub(r'\D', '', number)
        if formatted_number.startswith('972'):
            formatted_number = formatted_number[3:]
        formatted_numbers.append(formatted_number)
    return formatted_numbers


#compare the two lists and return a list of numbers that are not in the excel list
def compare_lists(whatsapp_phones, excel_phones):
    return list(set(excel_phones) - set(whatsapp_phones))

#############
#test 
whatsapp_array = format_numbers(turn_string_to_array(whatsapp_phones))
excal_array = format_numbers(turn_string_to_array(excel_phones))

print(len(whatsapp_array))
print(len(excal_array))

print('phone numbers in whatsapp that are not in excal')
print(compare_lists(whatsapp_array, excal_array))
print(len(compare_lists(whatsapp_array, excal_array)))

print('phone numbers in excal that are not in whatsapp')
print(compare_lists(excal_array, whatsapp_array))
print(len(compare_lists(excal_array, whatsapp_array)))





