from postinumerot import get_data
import postinumerot
import postinumerot2

test_data = get_data()

#OSA 1

def test_one_result():
    data = postinumerot.rearrangeData(test_data)

    result = data["SMARTPOST"]
    assert len(result) == 1 #palauttaa failed testin -- en tiedä millä postitoimipaikalla on yksi postinumero

def test_multiple_results():
    data = postinumerot2.rearrangeData(test_data)

    result = data["HELSINKI"]

    assert len(result) > 1


#OSA 2

#smartposteja on 812 kappaletta, 816 jos poistaa välimerkit

    #testi bugisella tiedostolla
def test_smartpost_without_removing_spaces():
    data = postinumerot.rearrangeData(test_data)

    result = data["SMARTPOST"]
    assert len(result) > 812

    #testi bugi korjattuna
def test_smart_post_with_removing_spaces():
    data = postinumerot2.rearrangeData(test_data)

    result = data["SMARTPOST"]

    assert len(result) == 816





