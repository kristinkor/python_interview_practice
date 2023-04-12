def getPasswordStrength(passwords, common_words):
    def is_numbers(password):
        return all(char in '0123456789' for char in password)

    def is_uppercase(password):
        return all(char.isupper() for char in password)

    def is_lowercase(password):
        return all(char.islower() for char in password)

    def is_weak_password(password):
        for word in common_words:
            if word in password or word in password.split():
                return True
        for word in common_words:
            if word in password:
                return True
        if is_numbers(password):
            return True
        if is_uppercase(password) or is_lowercase(password):
            return True
        if len(password) < 6:
            return True
        return False

    results = []
    for password in passwords:
        if is_weak_password(password):
            results.append('weak')
        else:
            results.append('strong')
    return results


def Test():
    print("test start...")  
    s1 = {"iliketocode","abraCadardra", "pasSwprd", "blackcoffeeGG", "123454546", "teaMAKEmehappy"}
    s2 = {"coffee","coding", "happy"}
    print(getPasswordStrength(s1,s2))
   
    print("test end")    

if __name__ =="__main__":
    Test()     