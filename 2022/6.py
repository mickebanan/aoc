import collections
from itertools import islice


buffer = 'plhlsssjsrscspsffmrffwvfvrvvmbbnjnrnrfnndlnlznlznlnccdbbhvbvgvmvzmzvmzmbbrcclsslzslzzsztzftzzhggnjgnjnhnmnqnqqfdfnnrwnwsnwwvgvqqgpptvtrvvfmmzjzmmjssmwsmmhzzvvwzwcwrcrllpbppdgdvvwqvvsnsrnsncnwntnggwqgqhqrqprqrddjvddqsqhshchfffzddswdsshhcnhnqqfjffvlvwvssdqqwrwvrvhrvrzzgwggcjcgclcwchhzvzmzrrjwjqwwvbwwrmmvmpmzpzgpgsghgrrtmmlfmmnzzmpzzvmvjjsqqshqshsqqgtqggpvvrtttwbbhnbnlbnlnhnthtjhjshhrmrjjlclpprmrnrsrwrbwrwwjnwnbwbhbmbggdbgghllcvlvddzbdbdvdwvdvjvqvcvczvcvclvvrggrngrrwcwbcczgghnhznhnttbcbvcvttrrpbrppndppvvvgvtgvvhfvhhttppjmjllznlnldnldlwlnwlnlttgzzcfcggwmgmqgmmshmhqqdfqfpfqppprzrhrnrhnrrtsrrgpgnpngnqnmmrtrvtrrfccszszffvlfvlvssvdvvpggvcvscvvpmpgpqpfqqhttrhhsbhbqhhzggzrgrqrfqffwllggrgqqjzqzzsgglvgllsgllptltblbggvrggctczzllvsvcscrrzjrzzjnnbvvtntpntnvtntcntcnnwsnnnvjnnsccsddcvvgzgwggbnbwnwbwmwttzzsgzzjpzztwztwwhhzggplgplggwwwphpmmhchsccmwmttvjtjftffzbfffjljbbqvvstsggbbqrbqrbrhbbrmbmppvrpphptpggqgddtmdtmdmbbbcdbbgssmzzthhtjjrgjrgrzzchzhttgddjnjrjmjllrcrqqsvsjjjhvvphhgjhgjhjccwmcmjcmjmhmzznmmcbcscddcsssnppsnpnmnqmmtztftqtjtqqgvgvjjfnjffqbqbfqqwfqfcfsfttvccnssjvvpfvpvttvpvccwhwfwlwlclljqqststllgqgzqqfpflpplpssnntstqqpnnsrnsrrsvrsvsrvsrrtztmtptpcpssgnnfvflffscsqszzsppfnftfptfpfnfbbwzbzfbbtggrzrnntztnznhnnlbnbrbdddjhjchhdshhnzhnnsrnrrqwrrdsdlsstdsslqsqdqvqzvqvwqqlmmwzmwzwztzlzczhqfrclvgvnlchrggsrjhntctdbpfdcffwjngdvdrjmgvwvptlvlhvhshqphmrdznqbtchcvrwfrpvwhzmrwlcjwnrsgrqcbsgpwjthstvqzlwjjmqbvhhdfdsmqnmnswmwjtpgjhdpgcnvmlcjwjzrjhmrqmqnrqrmgdnbdgznwhgzncmcbzpntcdflvrbfdzwgpnqjqmrcqpbrzwhwdgtgshhmrwvhnrwslvcswjvdgglfrdvmqdspppwmvfzvdbvpcnhmvgfqwnvjvvzrvttwvbjrbjlllmwtlcltvqmwshnqsdtjrptvqjvdjgzwgzzhcdbwjzhdgsptfrtmmqvhsnsnpgwbncbnnvwmmrrjgfccbzcpcjmqvqsbvjrstzblsrngphwndfdswjnnnfdgpcbslvbjglqqnbbtjljsmdgcslmwlvgwpsqthlmmqfgpgmcvrpvvtzcjdrwcjgrbwthblwpwpbzvjvhzsphmfhfwvsthlfnhhfcmpsnmgrvrntlzpdvqwtrghnslnfhcjwrsvrngqqtwvcsfhbjwmsnmsmgvdhnzjgljtchbtwlfppvbtdclbdjdmwzcntvgfjlcwdplnjwqnzqhnfgcnbrgftqpdmqzrrhglbzzvjcdnbtfnvmsrbjdzhbqmhnsmprgvjzzgvllhqnzgpstqzcnlgsrcwzlhwqvcjlwnnjslmdtwqcpbrntrmrmmtscjwwtzjhghtqvvpldzvhtmspzlnlfgrfhmsndbdgpgvphwwgqhrtlwztgqqsrwnrnqphqfsrtbztqbrgmfbtpjwhhrglhbzmmjptppnfdzlpbqfcbdwzdtqbrvfmtdzdjlnzvqfnzmttpqgzgmrqwmdtmdzrttffpdlgwdhnlrhnnztphvrbzcrlvcpswlngcjhdzqwwwpzdmhhwpnzwgjsdsdbdvpfsrwmwvsggpcqbchwjpgljnbtpvjzbbvgsbsbjmtwtbjtzzsfvrmfvnmcngvvdsvljvjbrlfgstjrhtjplttzhjfbmphvbqdsmwfwspqpcvmgzgjnqlphshlgdwcvtmpwcfgdcbqwpnshfgrfjvlrtqbffwwtbnwtvjlsdgwgfmhlrsmfrjzcwccdzfwwdwhwdsjbllhjsqmnqvngvdmbvbssfjtjfbtngrdwgldcrtpmvrbrmpvwwsfrlnbqsqzfnftpbhslqccnbqwgbdbfpblpmwbgjzmnptnhdjzqjhdrhqbtfhsrdqwlmwzqlsmmslgfzpvtgtsrlszvqrhrzclbqhzzwwfmhrrvsrnsjbdjsqqlsmgdmgbdtmvfjmsbwjqmqrvrhqbchpqrwvlvwpvhjlbdzfjvrwmchccrsrfvhzmpfjqwnrbvqmgwjcbndjdtfgnrzrqwgzhrdvghdrvgtplcrthgchmvwtdrchfwpdszzzhqpmrlzvfdnfnlwghmmwvsscbrdbchhgttsnbzdbqgddqfvcgvqwltnqtcwrmhtftnlwvlglsvvctccnntznsjnmmgqlzmplsdspnjtmzlbvrfzfclnhgjzmvntdwhspqwtpgndspnjqjqwrpwhjhpvjwfptpndnwvcjdwsvdtcrtwpsprgmrspgmcsdgtjbbgsgvcjhrcldlvgvqwqwthplzgwbzmszjfrlnznvgphnqzcwsztvvljlrlzrndbzccstprhntnlmshhclnrsmsvvvsbmpfdjsmspwcqtmlrrdmfzjjjhmsmdfqddzpgtbzbsnhhhpsfrdrdvpvpnjmvnhdrzrqggrpqdcmctvqfrtfmjjqjwgzzbrdfplhzjbnqlmjlcgvmsbpgdlfjmbgqtrvzzdgtlmbqthjrdtlstqtzqvfjvmmstsmtsbnjvstjjvrrjqcbjvhfpslpvjmdznrcnsvlpbpzmslqtpczmvhdwzrhwbwtfvrrmbszvrhwsjrclcscgngwvblbbrqprgshwzhlqgwmpfsmqsvpjbdccdmtnnhqfwvlgjlszmmmdmtmpzwhplzsjztrnwngbvspqqbmghwzgvfjdrblfmtwcvnczsrflmsjmrsvzldmttjwcmnvwcbjfvznhgntnqfbfchcqqshhjldgltqhdlqldlpfjnjvtbvbntzdjzstcqbzdnmsvcdgvjmmvtdfvdplqfndqqlzlspmjgdfbgsvwzqzsvvbbldltbtzwzpqrzfmfzgdbpqnwtrfcgwmlbpzrgscbjvfdwnjzjdfzltsbppnljzrgggplmttpmgwnhdlwfhwzsrcflnrqqzwsbqllwjqlrgwbhvcvqdvjvpbzgnfbbbtccvplzggplbrsbldllwmttwtvltsfljfbbprtvlfshhwdhdgvzfzjttvnphpnjnzsbvfwflfpqwnhvwjdsrtbwsjzqhgfldnssfbbzzqqrwtjvwjschmndgqzjtpsbfhwtmqbtfstrbghgtnldjqtshdnrwzvwddchhvdbsfjnqzfjdpvhvwwjspftgbtgwzdfgzzhpvjpdlrrdfnpftshthwzjzmzdghnfdqcbmjhfdgzrcgrzbrjtmhwbjhcpgjdsmnqzncdlwhqqzqblgdbbdsmrqgbdbmdczvvpnbbjdwrlmrwgnnbbzpcnsjgcmshgzwnjzwjlrdmvmhvjrzphgpczppqvwjthcdphprhhrggjdpzmgtpjjfvpczzrvsssfrrptnzlstrhmbhvzmwjnddshrrtgspbllvqlsptrtvtldsgnjjbwtfmtbjdvmgbptjlzhpttjmvpgnjphswhtdq'
# buffer = 'zcfzfwzzqfrljwzlrfnpqdbhtmscgvjw'


def sliding_window(iterable, n):
    # sliding_window('ABCDEFG', 4) --> ABCD BCDE CDEF DEFG
    it = iter(iterable)
    window = collections.deque(islice(it, n), maxlen=n)
    if len(window) == n:
        yield tuple(window)
    for x in it:
        window.append(x)
        yield tuple(window)


for i, window in enumerate(sliding_window(buffer, 14), 14):
    if len(window) == len(set(window)):
        print('start!', window, i)
        break