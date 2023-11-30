#quiz tentang sejarah indonesia
def check_guess(guess, jawaban):
    global score
    still_guessing = True
    attempt = 0
    while still_guessing and attempt < 3:
        if guess.lower() == jawaban.lower():
            print("Jawaban Benar")
            score = score + 1
            still_guessing = False
        else:
            if attempt < 2:
                guess = input("Mohon maaf Jawaban anda salah, coba lagi")
            attempt = attempt + 1
    if attempt == 3:
        print("Jawaban yang benar adalah ",jawaban )
    
score = 0
print("Tebakan Sejarah")
guess1 = input("Siapa Raja Paling Makmur Majapahit ? ")
check_guess(guess1, "hayam wuruk")
guess2 = input("Tahun Berapa Indonesia Merdeka ? ")
check_guess(guess2, "1945")
guess3 = input("Siapakah yang mengkumandangkan semangat melawan nica datang ke surabaya ?")
check_guess(guess3, "bung tomo")
print("Skor Anda adalah "+ str(score))