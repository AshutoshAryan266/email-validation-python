# EMAIL VALIDATION RULES

# 1. No spaces are allowed anywhere in the email. // done

# 2. The email must contain exactly ONE '@' symbol. // done

# 3. Local part (before '@'):
#    - Must not be empty. // done
#    - The first character must be an alphabet (A-z,a–z).//done
#    - Allowed characters are:
#        • lowercase alphabets (a–z)//done
#        • uppercase alphabets (A–Z)//done
#        • digits (0–9)//done
#        • underscore (_)//done
#        • dot (.)//done
#        • dollar sign ($)//done
#    - No consecutive dots ('..') are allowed.//done
#    - The local part must not start or end with a dot. //done

# 4. Domain part (after '@'):
#    - Must not be empty.//done
#    - Must contain at least one dot (.).//done
#    - There must be at least one character between '@' and the first dot.//done
#    - No consecutive dots ('..') are allowed//done
#    - The domain must not start or end with a dot.//done

# 5. Top-Level Domain (TLD):
#    - The part after the last dot must be at least 2 characters long.//done
#    - It must contain only alphabets (a–z).//done
#    - Examples: .com, .in, .org, .edu//done

# 6. Any character not explicitly allowed above should make the email invalid.


# Taking input from the user
email = input("Enter your email address: ")

# minimum length requirement  # g@g.in  ,, so min 6 characters

if len(email) >= 6:
    
    if ' ' not in email:
        if '@' in email and email.count('@') == 1:
            local_part = email.split('@')[0]
            domain_part = email.split('@')[1]
            #for local part validation
            if local_part.strip() != '':
                if '..' not in local_part:
                
                    if local_part[0].isalpha() and local_part[0] != '.' and local_part[-1] != '.':
                          # Allowed characters check
                        for char in local_part:
                            if not(char.isalnum() or char in ['_','$','.']):
                               print("Wrong Email Format: Invalid character in local part.")
                               break
                            else:
                               continue          
                    else:
                     print("Wrong Email Format: First character of local part must be an alphabet and last character must not be a dot.")
                     exit()
                else:
                    print("Wrong Email Format: Consecutive dots are not allowed in local part.")
                    exit()
            else:
               print("Wrong Email Format: Local part must not be empty.")
               exit()
            #for domain part validation
            if domain_part.strip() != '':
                if domain_part.count('.')>=1:
                    if domain_part[0] != '.' and domain_part[-1] != '.':
                        if '..' not in domain_part:
                            TLD = domain_part.split('.')[-1]
                            if len(TLD) >=2:
                                if TLD.isalpha():
                                    print("Valid Email Address.")
                                else:
                                    print("Wrong Email Format: Top-Level Domain (TLD) must contain only alphabets.")
                                    exit()
                            else:
                                print("Wrong Email Format: Top-Level Domain (TLD) must be at least 2 characters long.")
                                exit()
                        else:
                            print("Wrong Email Format: Consecutive dots are not allowed in domain part.")
                            exit()
                    else:
                        print("Wrong Email Format: Domain part must not start(at least one character or word between @ and '.') or end with a dot.")
                        exit()
                else:
                    print("Wrong Email Format: Domain part must contain at least one dot ('.').")
                    exit()
            else:
                print("Wrong Email Format: Domain part must not be empty.")
                exit()
                
        else:
            print("Wrong Email Format: Email must contain exactly one '@' symbol.")
            exit()
    else:
        print("Wrong Email Format: Email must not contain spaces.")
        exit()
        
else:
    print("Wrong Email Format: Email should be at least 6 characters long.")
    exit()