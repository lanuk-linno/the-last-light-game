import time
import sys

# მოთამაშის მდგომარეობა
game_state = {
    "sanity": 100,
    "inventory": [],
    "has_robot_no": False,
    "rael_trust": 0,
}

def print_slow(text, delay=0.03):
    for char in text:
        sys.stdout.write(char)
        sys.stdout.flush()
        time.sleep(delay)
    print()

def print_whisper(text, delay=0.04):
    print("\033[36m", end="")  # ცისფერი ფერი შინაგანი ხმისთვის
    for char in text:
        sys.stdout.write(char)
        sys.stdout.flush()
        time.sleep(delay)
    print("\033[0m")

def print_city_voice(text, delay=0.02):
    print("\033[31m", end="")  # წითელი ფერი
    for char in text:
        sys.stdout.write(char)
        sys.stdout.flush()
        time.sleep(delay)
    print("\033[0m")

def show_status():
    print(f"\n[ 🧠 ფსიქიკური მდგრადობა: {game_state['sanity']}% | ინვენტარი: {', '.join(game_state['inventory']) if game_state['inventory'] else 'ცარიელია'} ]\n")

def start_game():
    print("==================================================")
    print("           THE LAST LIGHT: VOICES OF NEON          ")
    print("   (ფსიქოლოგიური თავსატეხი / ლანა დოლიძის წიგნი)   ")
    print("==================================================")
    time.sleep(1)
    
    print_slow("\nსიბნელე. ნეონის ცივი ნათება მილიონობით ტელეეკრანიდან...")
    print_city_voice('»» "სტაბილურობა უსაფრთხოებაა. ქალაქი გიცავთ თქვენ." ««')
    
    print_whisper('\n(ხმა შენს თავში): "ნუთუ ესაა ერთადერთი რეალობა? რატომ მეჩვენება, რომ ეს ცა ყალბია?"')
    time.sleep(1)
    
    chapter_1_workshop()

def chapter_1_workshop():
    show_status()
    print_slow("\n--- თავი 1: მამის მიტოვებული სახელოსნო ---")
    print_slow("ოთახში მანქანის ზეთისა და დამწვარი ელექტრონიკის სუნია. მტვერი ფარავს იატაკს.")
    
    print_whisper('(შინაგანი ხმა): "მამა აქ იყო... სამი წლის წინ გაქრა. მათ თქვეს, რომ ავარია მოხდა. იტყუებიან..."')
    print_whisper('(მამის შორეული მოგონება): "ლინა... სიმართლე იატაკის ქვეშაა, სადაც შუქი ვერ აღწევს..."')
    
    puzzle_1_floor()

def puzzle_1_floor():
    print("\n[გონების თავსატეხი: იატაკის საიდუმლო]")
    print_slow("იატაკზე რამდენიმე ლითონის ფილაა. ერთ-ერთი ოდნავ არათანაბრადაა.")
    print_slow("ფილაზე ამოტვიფრულია სამი სიმბოლო: [ ☀️️ მზე ]  [ ⚙️ ოსტატი ]  [ 🌧️ წვიმა ]")
    
    print_whisper('\n(შინაგანი ხმა): "მამას უყვარდა ბუნება... რა უძღვის წინ სიცოცხლის გაღვიძებას?"')
    
    choice = input("\nრომელ სიმბოლოს დააჭერ პირველად? (1: მზე, 2: ოსტატი, 3: წვიმა): ")
    
    if choice == "1":
        print_slow("\nწკაპ! ფილა ჩავიდა. შიგნით იპოვე დამწვარი წერილი!")
        print_whisper('(შინაგანი ხმა): "ეს მამის ხელია! \'როდესაც უკანასკნელი სინათლე გამოჩნდება...\'"')
        game_state["inventory"].append("დამწვარი წერილი")
        chapter_1_escape()
    else:
        print_slow("\nარაფერი მოხდა. ფილა ჩაიკეტა.")
        print_whisper('(შინაგანი ხმა): "არა... დაფიქრდი, ლინა!"')
        game_state["sanity"] -= 10
        puzzle_1_floor()

def chapter_1_escape():
    show_status()
    print_city_voice("\n⚠️ WARNING: UNAUTHORIZED ACCESS DETECTED! ALL UNITS REPORT!")
    print_slow("განგაშის საირენა სულს გიფორთხიალებს. დრონების პროპელერების ხმა უახლოვდება ფანჯარას.")
    
    print_whisper('(შინაგანი შიში): "ისინი მომაგნებენ! გაიქეცი!"')
    
    puzzle_2_escape()

def puzzle_2_escape():
    print("\n[გონების თავსატეხი: გაქცევის მარშრუტი]")
    print_slow("A) მთავარი ლიფტი — სწრაფია, მაგრამ სენსორებით კონტროლდება.")
    print_slow("B) ტექნიკური შახტა — ბნელია, ჟანგიანი, მაგრამ უსაფრთხო.")
    
    choice = input("\nრომელ გზას ირჩევ? (A თუ B): ").upper()
    
    if choice == "B":
        print_slow("\nშენ ჩახტი ტექნიკურ შახტაში. სიბნელე გშლაპავს...")
        print_whisper('(შინაგანი ხმა): "სიბნელე შენი მოკავშირეა, როცა სინათლე ყალბია..."')
        chapter_2_robot_no()
    elif choice == "A":
        print_slow("\nლიფტი შუა გზაში გაჩერდა! დრონებმა დენი გათიშეს.")
        game_state["sanity"] -= 25
        print_whisper('(შინაგანი ეჭვი): "შეცდომა დაუშვი..."')
        chapter_2_robot_no()
    else:
        puzzle_2_escape()

def chapter_2_robot_no():
    show_status()
    print_slow("\n--- თავი 2: BEEP სიბნელეში ---")
    print_slow("ღრმად მიწისქვეშეთში ხარ. უეცრად სიბნელეში ლურჯი შუქი აინთო: BEEP... BEEP!")
    
    print_whisper('(შინაგანი ხმა): "მანქანაა... საქალაქო დრონი ხომ არ არის?"')
    print_slow("პატარა რობოტი კედელზე ლურჯი სხივით გვირაბის რუკას გიხატავს.")
    print_whisper('(მამის ხმა): "ზოგჯერ ყველაზე პატარა მექანიზმს ყველაზე დიდი გული აქვს..."')
    
    print_slow("\nშენ იღიმები. მას 'No' დაარქვი!")
    game_state["has_robot_no"] = True
    game_state["inventory"].append("რობოტი No")
    
    chapter_3_ghost_garden()

def chapter_3_ghost_garden():
    show_status()
    print_slow("\n--- თავი 3: GHOST GARDEN & THE HUNTER IN RED ---")
    print_slow("გვირაბი იხსნება... შენს წინაშეა უზარმაზარი მიწისქვეშა ბაღი! მწვანე ბალახი. ნამდვილი ხეები.")
    
    print_whisper('\n(შინაგანი ხმა): "მწვანე სამყარო ცოცხალია!"')
    print_slow("ხის ფესვებში იპოვე ცილინდრი მამის წერილით: 'ბუნება თავისუფლებაა, ლინა...'")
    game_state["inventory"].append("მამის წერილი ბაღიდან")
    
    print_slow("\nუეცრად, ჰაერში მძიმე ნაბიჯების ხმა ისმის. ჩრდილიდან გამოდის RAEL — კიბორგი მონადირე წითელი თვალით!")
    print_city_voice('»» "LINA ARDEN. TARGET IDENTIFIED." ««')
    
    print_whisper('(შინაგანი შიში): "ეს მონადირეა! მოგვკლავს!"')
    print_whisper('(სიღრმისეული ხმა): "შეხედე მის თვალებს... მასში მანქანის მიღმა რაღაც სხვას ხედავ?"')
    
    puzzle_3_rael()

def puzzle_3_rael():
    print("\n[გონების თავსატეხი: ნდობის არჩევანი]")
    print("1. იყვირო და No ზურგს უკან დაიმალო.")
    print("2. ჰკითხო მშვიდად: 'შენ მამაჩემს იცნობდი, ხომ?'")
    
    choice = input("\nრას ირჩევ? (1 ან 2): ")
    
    if choice == "2":
        print_slow("\nრელის წითელი თვალი ოდნავ ჩაქრა:")
        print_slow('"ელიას არდენმა შემეკეთა... მან დამიბრუნა სული. მე შენი დაცვა აღვთქვი."')
        game_state["rael_trust"] += 1
    else:
        print_slow("\nრელი ნელა დგამს ნაბიჯს: 'ნუ გეშინია, ბავშვო. მამაშენმა მასწავლა, რა არის ადამიანობა.'")
        
    print_slow("\nანაზდად, დრონები თავს გესხმიან! რელი თავისი ენერგო-ფარით გეფარებათ.")
    chapter_4_wall_of_clouds()

def chapter_4_wall_of_clouds():
    show_status()
    print_slow("\n--- თავი 4: WALL OF CLOUDS & REAL STARS ---")
    print_slow("რელის დახმარებით გადალახეთ ქალაქის საზღვარი. ქარიშხალი და ტოქსიკური ნისლი უკან რჩება.")
    print_slow("პირველად შენს ცხოვრებაში, მაღლა იხედები...")
    
    print_whisper('\n(შინაგანი აღტაცება ცრემლებით): "ღმერთო ჩემო... არანაირი ჰოლოგრამა. ეს... ვარსკვლავებია. ნამდვილი ვარსკვლავები!"')
    
    print_slow("\nNo ჰოლოგრაფიულ კოორდინატებს აპროექტებს. რელი ამბობს:")
    print_slow('"რუკა წერილში კი არ იყო... ის No-ს მეხსიერების ბირთვშია ჩაწერილი! მწვანე ქალაქისკენ მივდივართ!"')
    
    chapter_5_final_spire()

def chapter_5_final_spire():
    show_status()
    print_slow("\n--- თავი 5: THE LAST LIGHT (ფინალური ბრძოლა) ---")
    print_slow("მიაღწიეთ მწვანე ხეობას! ცენტრში დგას გიგანტური კრისტალური კოშკი (Spire).")
    print_slow("მაგრამ ცა იხლიჩება — საქალაქო სამხედრო ხომალდები ეშვებიან სანქტუარიუმის განადგურებისთვის!")
    
    print_slow("\nრელი კარს კეტავს და თავისი რეაქტორის გადატვირთვით მტრებს გზას უღობავს:")
    print_slow('"გაიქეცი, ლინა! მე დროს მოგიგებ! ჩემი დანიშნულება წარსულის დანგრევა იყო, ახლა მომავლისთვის ვიბრძვი!"')
    
    print_whisper('\n(შინაგანი შიში): "რელი იქ დარჩება... No უნდა ავტვირთო კოშკში!"')
    
    puzzle_4_spire()

def puzzle_4_spire():
    print("\n[ფინალური თავსატეხი: მეხსიერების ბირთვის გააქტიურება]")
    print_slow("შენ აერთებ No-ს კოშკის ცენტრალურ პანელთან.")
    print_slow("ეკრანზე წერია: 'ENTER PASSCODE TO RESTORE GREEN SANCTUARY'")
    
    print_whisper('(მამის ხმა შენს გონებაში): "გახსოვს, ლინა? რას ვერ ჩააქრობს ვერასდროს ვერავინ?"')
    print("მინიშნება: წიგნის მთავარი ფრაზა — [ 1: STABILITY | 2: CONTROL | 3: YOUR LIGHT ]")
    
    choice = input("\nრომელ კოდს აირჩევ? (1, 2 ან 3): ")
    
    if choice == "3":
        print_slow("\n100% COMPLETE! 'LAST LIGHT BEACON: ACTIVATED!'")
        print_slow("\nზურმუხტისფერი მწვანე ენერგიის სხივი გაიტყორცნა ცაში!")
        print_slow("ენერგიამ მოშალა მტრის მანქანები, გადაუარა ქალაქს, დაშალა ბეტონი და ნეონის კოშკებზე მწვანე მცენარეები აღმოცენდა!")
        
        print_whisper('\n(შინაგანი სიმშვიდე): "სიბნელე დასრულდა... სამყარომ ისევ გაიღვიძა."')
        print_slow("\nწლების შემდეგ: ლინა, No და გადარჩენილი Rael ერთად უყურებენ ნამდვილ მზის ამოსვლას.")
        print("\n==================================================")
        print("                 THE END (დასასრული)               ")
        print("==================================================")
    else:
        print_slow("\nკოდი არასწორია! სცადე თავიდან.")
        puzzle_4_spire()

if __name__ == "__main__":
    start_game()