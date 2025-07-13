
import phonenumbers
from phonenumbers import geocoder, carrier, timezone
import sys

def analyze_number(number_str):
    try:
        parsed_number = phonenumbers.parse(number_str)
    except phonenumbers.phonenumberutil.NumberParseException:
        return ["❌ خطأ: الرقم غير صالح. تأكد من كتابته بصيغة دولية (مثال: +9665xxxxxxx)"]

    if not (phonenumbers.is_possible_number(parsed_number) and phonenumbers.is_valid_number(parsed_number)):
        return ["❌ الرقم غير صالح أو غير ممكن."]

    info = [
        f"📞 رقم الهاتف: {number_str}",
        f"🌐 التنسيق الدولي: {phonenumbers.format_number(parsed_number, phonenumbers.PhoneNumberFormat.INTERNATIONAL)}",
        f"🌍 الدولة: {geocoder.description_for_number(parsed_number, 'en')}",
        f"📡 شركة الاتصالات: {carrier.name_for_number(parsed_number, 'en')}",
        f"🕒 المنطقة الزمنية: {', '.join(timezone.time_zones_for_number(parsed_number))}",
    ]

    # روابط البحث
    info += [
        "\n--- روابط OSINT ---",
        f"🔎 Google: https://www.google.com/search?q={number_str}",
        f"📘 Facebook: https://www.facebook.com/search/top/?q={number_str}",
        f"🐦 Twitter: https://twitter.com/search?q={number_str}",
        f"📷 Instagram: https://www.instagram.com/{number_str.strip('+')}",
        f"📱 Truecaller: https://www.truecaller.com/search/{parsed_number.country_code}/{parsed_number.national_number}",
    ]
    
    return info

if __name__ == "__main__":
    if len(sys.argv) < 2:
        print("📌 الاستخدام: python3 phonehunter.py +9665xxxxxxx")
        sys.exit()

    phone = sys.argv[1]
    results = analyze_number(phone)

    with open("results.txt", "w", encoding="utf-8") as file:
        for line in results:
            print(line)
            file.write(line + "\n")

    print("\n✅ تم حفظ النتائج في results.txt")
