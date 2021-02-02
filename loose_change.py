def loose_change(cents):
    
    change_dict = {'Quarters': 0, 'Dimes': 0, 'Nickels': 0, 'Pennies': 0}

    if isinstance(cents, (float, int)) and cents > 0:

        conversion_dict = {'Quarters': 25, 'Dimes': 10, 'Nickels': 5, 'Pennies': 1}
        remainder = int(cents)

        for k, v in change_dict.items():
            
            change_dict[k] = remainder // conversion_dict[k]
            remainder = remainder % conversion_dict[k]

    return change_dict
