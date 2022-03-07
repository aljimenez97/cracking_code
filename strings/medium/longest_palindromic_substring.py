# https://leetcode.com/problems/longest-palindromic-substring/
# Given a string s, return the longest palindromic substring in s.

def get_longest_palindrome(word):
    res = ""
    max_len = 0

    for i in range(len(word)):
        # Odd length palyndromes
        l, r = i, i
        while l >= 0 and r < len(word) and word[l] == word[r]:
                if (r - l + 1) > max_len:
                    res = word[l:r+1]
                    max_len = r - l + 1
                l -= 1
                r += 1
        # Even length palyndromes
        l, r = i, i+1
        while l >= 0 and r < len(word) and word[l] == word[r]:
                if (r - l + 1) > max_len:
                    res = word[l:r+1]
                    max_len = r - l + 1
                l -= 1
                r += 1
    return res                


if __name__ == "__main__":
    word = "iekmafcuinxsmkiaoqvgrlnmkgrevbkikaadcuuenrudjcvwslolsvvmykfrjveasenkoqvljkynevupgebavzurjgsbvxgqqlrmbyldqpnwuykqvebmehoglzdqgnnqrhpiqqvcvqwnhoounutqqghmvviezjrpjbxiizbfjdstavsvnfxmxnlyodntuwtaiawodrbqlokgfkvnwjmjfargyoxrecsfyeqirkpjhditwrpwdhgacrumguwkcevchntenjlcvgcdwvuymbdbfvmtyjppxndqxdcqbazrsgptfktfyarvtqinkeqnfzraqxxytngmpmfpekjlrdzhgpldpvwnbdaduntbqkyoocbzyogqhcvxcgyggdhyvrrgkjeipxlkrirpityizzeletevmlujdjtahzewtpgajdmyolaizyvhjlvxetweolftsrktimsntzxyxbuttubxyxztnsmitkrstfloewtexvljhvyzialoymdjagptwezhatjdjulmvetelezziytiprirklxpiejkgrrvyhdggygcxvchqgoyzbcooykqbtnudadbnwvpdlpghzdrljkepfmpmgntyxxqarzfnqekniqtvrayftkftpgsrzabqcdxqdnxppjytmvfbdbmyuvwdcgvcljnetnhcveckwugmurcaghdwprwtidhjpkriqeyfscerxoygrafjmjwnvkfgkolqbrdowaiatwutndoylnxmxfnvsvatsdjfbziixbjprjzeivvmhgqqtunuoohnwqvcvqqiphrqnngqdzlgohembevqkyuwnpqdlybmrlqqgxvbsgjruzvabegpuvenykjlvqoknesaevjrfkymvvslolswvcjdurneuucdaakikbvergkmnlrgvqoaikmsxniucfamkei"
    word = "oyxshtfvhudhhsnstwfxhdlhieqwaujxubhymmmuhpzjmjrwlapdlrnmzxprwkykmhcjozlivieafymrnixadlyomwvmoextitacntoopnldbhhzqsxkatwjmyzrvkhrwltapztwverlrnbownqhhdmuzwzynfdzdzgcjjxbwmziemkxhgsppdwureforlajyhucagmnxngmcxtzwrevgzdwzpbuxgkzdablbgzmjhnuvdaeonsotcwmazcpziuwjzgweygfvlqajzgujxsskaaduicsjyevqiwivrfvntmmbadqawskzrszhekrbdgdmfvszsypxhsaqeenogzegehuxifpkusuukrddouzshamsjukhagruhmwvrrrrvwmhurgahkujsmahszuoddrkuusukpfixuhegezgoneeqashxpyszsvfmdgdbrkehzsrzkswaqdabmmtnvfrviwiqveyjsciudaakssxjugzjaqlvfgyewgzjwuizpczamwctosnoeadvunhjmzgblbadzkgxubpzwdzgverwztxcmgnxnmgacuhyjalroferuwdppsghxkmeizmwbxjjcgzdzdfnyzwzumdhhqnwobnrlrevwtzpatlwrhkvrzymjwtakxsqzhhbdlnpootncatitxeomvwmoyldaxinrmyfaeivilzojchmkykwrpxzmnrldpalwrjmjzphummmyhbuxjuawqeihldhxfwtsnshhduhvfthsxyo"
    #word = "Alfonsoso"
    longest_palindrome = get_longest_palindrome(word)
    print(longest_palindrome)


