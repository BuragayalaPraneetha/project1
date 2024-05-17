def enter_key_value_pairs():
    # Initialize an empty dictionary to store key-value pairs
    key_value_pairs = {}
    
    while True:
        key = input("Enter key (or type 'stop' to finish): ").strip()
        
        # Check if the user wants to stop entering values
        if key.lower() == 'stop':
            break
        
        value = input("Enter value for {}: ".format(key)).strip()
        
        # Store the key-value pair in the dictionary
        key_value_pairs[key] = value
    
    return key_value_pairs


pairs = enter_key_value_pairs()


print("\nEntered key-value pairs:")
for key, value in pairs.items():
    print("Key:", key)
    print("Value:", value)
