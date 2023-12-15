def decrypt(first_a, first_b, second_b, second_c, secret_c):
    # Création des dictionnaires de substitution entre les alphabets
    dict_b_to_a = {b: a for a, b in zip(first_a, first_b)}
    dict_c_to_b = {c: b for b, c in zip(second_b, second_c)}

    # Reconstruction de la substitution entre les alphabets A et C
    dict_c_to_a = {c: dict_b_to_a[dict_c_to_b[c]] for c in secret_c}

    # Déchiffrage du message secret_c vers l'alphabet A
    message = ''.join(dict_c_to_a[c] if c in dict_c_to_a else c for c in secret_c)
    return message


first_a = "JACKIE WILL BUDGET FOR THE MOST EXPENSIVE ZOOLOGY EQUIPMENT"
first_b = "DAOFJK XJCC PVQNKW STH WUK RTBW KYZKLBJGK MTTCTNI KEVJZRKLW"
second_b = "ZELDA MIGHT FIX THE JOB GROWTH PLANS VERY QUICKLY ON MONDAY"
second_c = "XSFIY TANBD QAO DBS MPR NJPLDB GFYCK USJW HEAZVFW PC TPCIYW"
secret_c = "RDJV VZVJVFLR YBV UFRLYGZV M FVVH LD MFNVRLMCYLV JDBV"

result = decrypt(first_a, first_b, second_b, second_c, secret_c)
print(result)
