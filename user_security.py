import random
import string

def generate_password_core():
    core = ''.join(random.choices(string.ascii_lowercase + string.digits, k=8))
    return core

def generate_related_passwords(core, num_passwords):
    passwords = [f"{core}{i}" for i in range(1, num_passwords + 1)]
    return passwords

def simulate_password_attack(passwords, guess_attempts, hint_probability):
    successful_guesses = 0
    for _ in range(guess_attempts):
        if random.random() < hint_probability:
            # Include a hint by using the core password as a guess
            guess = passwords[0]
        else:
            guess = ''.join(random.choices(string.ascii_lowercase + string.digits, k=len(passwords[0])))
        if guess in passwords:
            successful_guesses += 1
    success_rate = (successful_guesses / guess_attempts) * 100
    return success_rate

# Example usage:
core_password = generate_password_core()
related_passwords = generate_related_passwords(core_password, 10)
attack_success_rate = simulate_password_attack(related_passwords, 10000, 0.1)  # Set hint_probability to 0.1 (10%)

print(f"Core Password: {core_password}")
print(f"Related Passwords: {related_passwords}")
print(f"Attack Success Rate: {attack_success_rate:.2f}%")
