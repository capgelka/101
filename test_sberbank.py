import pytest
import allure
from collections import defaultdict
import sys
sys.path.append('.')

from driver.sberbank import WidgetFrame


params = defaultdict(list)
with open('test_data.csv', newline='') as csv:
    for line in csv.readlines():
        test_name, *data = line[:-1].split(',')
        params[test_name].append(data)



@pytest.yield_fixture
def page(request):
    page = WidgetFrame()
    yield page
    page.close()


@pytest.mark.parametrize(['check_name'], params['test_metals_active'])
def test_metals_active(page, check_name):
    assert not getattr(page, check_name)()
    page.click_metals()
    assert getattr(page, check_name)()


@pytest.mark.parametrize(['preactions', 'old', 'new'], 
                         params['test_new_page'])
def test_new_page(page, preactions, old, new):
    if preactions != '-':
        getattr(page, preactions)()
    assert page.url == old
    page.click_info()
    assert page.url == new
