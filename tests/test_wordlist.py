import pathlib

# Ensure that the modified line contains the correct spelling

def test_wordlist_string_correct():
    file_path = pathlib.Path('Araclar/wordlist.py')
    content = file_path.read_text(encoding='utf-8')
    assert "figlet WORDLIST R00T" in content
    assert "WORLDLIST" not in content
