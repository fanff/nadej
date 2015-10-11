
@then(u'the html result contains {nocare} "{domelem}" Element')
def step_impl(context,domelem,nocare):
    from bs4 import BeautifulSoup
    print("src",context.nadej_collected)
    soup = BeautifulSoup(context.nadej_collected, 'html.parser')
    
    res = soup.find_all(domelem)

    print("lol",soup.prettify())
    assert len(res) == 1

@then(u'the html result contains {some} "{domelem}" Elements')
def step_impl(context,some,domelem):
    from bs4 import BeautifulSoup
    soup = BeautifulSoup(context.nadej_collected, 'html.parser')
    
    res = soup.find_all(domelem)
    assert len(res) == int(some)


