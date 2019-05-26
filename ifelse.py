# isCNICValid = input('Do you have CNIC which is not expired!')
# if isCNICValid.lower() == 'yes':
#     gender = input('Please specify gender!')
#     if gender.lower() == 'male':
#         print('Please go to Booth A')
#     elif gender.lower() == 'female':
#         print('Please go to Booth B')
# else:
#     print('Thank you aap ka Vote BHAI ka hua go home')
bio_marks = int(input('Please provide Biology Marks!'))
chem_marks = int(input('Please provide Chemistry Marks!'))
if bio_marks < 0 or bio_marks > 100 or chem_marks < 0 or chem_marks > 100:
    print('Invalid bio marks input')
if chem_marks < 0 or chem_marks > 100:
    print('Invalid chemistry marks input')
