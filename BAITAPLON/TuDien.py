class Dictionary:
    def __init__(self):
        self.words = {}

    def add_word(self, base_word, entries):
        if base_word not in self.words:
            self.words[base_word] = []
        self.words[base_word].extend(entries)
        print(f"Thêm từ '{base_word}' thành công.")

    def remove_word(self, base_word):
        if base_word in self.words:
            del self.words[base_word]
            print(f"Xóa từ '{base_word}' thành công.")
        else:
            print(f"Từ '{base_word}' không tồn tại.")

    def lookup_word(self, base_word):
        if base_word in self.words:
            return self.words[base_word]
        return None

    def save_to_file(self, filename):
        with open(filename, 'w', encoding='utf-8') as file:
            for base_word, entries in self.words.items():
                file.write(f"{base_word}\n")
                for entry in entries:
                    line = f"{entry['word']} ({entry['part_of_speech']}) - {entry['meaning']}"
                    if 'example' in entry:
                        line += f" - VD: {entry['example']}"
                    file.write(f"{line}\n")
        print(f"Lưu từ điển vào tập tin '{filename}' thành công.")

    def load_from_file(self, filename):
        self.words = {}
        with open(filename, 'r', encoding='utf-8') as file:
            lines = file.readlines()
            base_word = None
            for line in lines:
                line = line.strip()
                if not line:
                    continue
                if ' (' not in line:
                    base_word = line
                    self.words[base_word] = []
                else:
                    parts = line.split(' - ')
                    word_pos = parts[0]
                    meaning = parts[1]
                    word, pos = word_pos.split(' (')
                    pos = pos.rstrip(')')
                    entry = {'word': word.strip(), 'part_of_speech': pos.strip(), 'meaning': meaning.strip()}
                    if len(parts) > 2:
                        entry['example'] = parts[2].split('VD:')[1].strip()
                    self.words[base_word].append(entry)
        print(f"Nạp từ điển từ tập tin '{filename}' thành công.")

def display_menu():
    print("\nChức năng từ điển:")
    print("1. Thêm một mục từ mới vào từ điển")
    print("2. Loại bỏ một mục từ của từ điển")
    print("3. Tra cứu các nghĩa của một mục từ trong từ điển")
    print("4. Lưu từ điển vào các tập tin")
    print("5. Nạp từ điển từ các tập tin")
    print("6. Kết thúc chương trình")

def main():
    dictionary = Dictionary()
    filename = "N21DCDT073_mang.txt"

    while True:
        display_menu()
        choice = input("Chọn chức năng: ")

        if choice == '1':
            base_word = input("Nhập từ chính: ")
            entries = []
            while True:
                word = input("Nhập từ: ")
                pos = input("Nhập loại từ (danh từ, động từ, tính từ,...): ")
                meaning = input("Nhập nghĩa: ")
                example = input("Nhập ví dụ (hoặc bỏ qua nếu không có): ")
                entry = {'word': word, 'part_of_speech': pos, 'meaning': meaning}
                if example:
                    entry['example'] = example
                entries.append(entry)
                more = input("Bạn có muốn thêm nghĩa khác cho từ này không? (y/n): ")
                if more.lower() != 'y':
                    break
            dictionary.add_word(base_word, entries)

        elif choice == '2':
            base_word = input("Nhập từ cần xóa: ")
            dictionary.remove_word(base_word)

        elif choice == '3':
            base_word = input("Nhập từ cần tra cứu: ")
            definitions = dictionary.lookup_word(base_word)
            if definitions:
                print(f"Định nghĩa của từ '{base_word}':")
                for definition in definitions:
                    line = f" - {definition['word']} ({definition['part_of_speech']}) - {definition['meaning']}"
                    if 'example' in definition:
                        line += f" - VD: {definition['example']}"
                    print(line)
            else:
                print(f"Không tìm thấy từ '{base_word}' trong từ điển.")

        elif choice == '4':
            dictionary.save_to_file(filename)

        elif choice == '5':
            dictionary.load_from_file(filename)

        elif choice == '6':
            print("Kết thúc chương trình.")
            break

        else:
            print("Lựa chọn không hợp lệ, vui lòng chọn lại.")

if __name__ == "__main__":
    main()
