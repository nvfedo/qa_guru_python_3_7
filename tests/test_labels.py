import allure
from allure_commons.types import Severity
import json
from selene.support import by
from selene.support.conditions import be
from selene.support.shared import browser
from allure import attachment_type


def test_dynamic_labels():
    allure.dynamic.tag("web")
    allure.dynamic.severity(Severity.BLOCKER)
    allure.dynamic.feature("Задачи в репозитории")
    allure.dynamic.story("Авторизованный пользователь может создать задачу в репозитории")
    allure.dynamic.link("https://github.com", name="testing")
    pass

@allure.tag("critical")
@allure.severity(Severity.CRITICAL)
@allure.label("owner", "fedotov")
@allure.feature("Задачи в репозитории")
@allure.story("Авторизованный пользователь может создать задачу в репозитории")
@allure.link("https://github.com", name="testing")
def test_decorator_labels():
    pass
