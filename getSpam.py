def getSpamEmails(subjects, spam_words):
    results = []
    for subject in subjects:
        count = 0
        for spam_word in spam_words or spam_word in spam_words.split():

            count += subject.lower().count(spam_word.lower())

        if count >= 2:
            results.append('spam')
        else:
            results.append('not spam')
    return results


def test_getSpamEmails():
    # Define some example inputs and expected outputs
    subjects = ["free prize worth millions", "Buy now and save!", "Urgent message: please read", "Free trial offer"]
    spam_words = ["free", "money", "win", "million"]
    expected_results = ["not spam", "spam", "spam", "spam"]

    # Call the function with the example inputs and check the output
    print(getSpamEmails(subjects, spam_words))


    # Test with an empty list of subjects and spam words
    subjects = []
    spam_words = []
    expected_results = []
    print(getSpamEmails(subjects, spam_words))

    # Test with a single subject that contains multiple spam words
    subjects = ["Buy now and save on this limited time offer!"]
    spam_words = ["buy", "offer"]
    expected_results = ["spam"]
    print(getSpamEmails(subjects, spam_words))

    # Test with a single subject that contains no spam words
    subjects = ["Important Meeting"]
    spam_words = ["urgent", "buy", "free", "offer"]
    expected_results = ["not spam"]
    print(getSpamEmails(subjects, spam_words))




def Test():
    print("test start...")  

    test_getSpamEmails()
   
    print("test end")    

if __name__ =="__main__":
    Test()    