from selenium.webdriver.common.by import By

#EXCHANGE_RATES_WIDGET = (By.CLASS_NAME, "bp-container sbt-springboard-container 4")

WIDGET_PARENT = (By.CSS_SELECTOR, ".bp-container.sbt-springboard-container")
EXCHANGE_RATES_WIDGET = (By.XPATH, )


# driver.find_elements_by_xpath("//*[contains(text(), 'My Button')]")

# <div class="flip-container">
# <div class="flipper">
# <div class="sbt-springboard-area bp-area front">
# <div data-pid="personalRates" class="bp-widget aa-widget personalized-widget bp-ui-dragRoot">
# <div class="bp-widget-head personalized-widget-head bp-ui-dragGrip">
# <span class="personalized-widget-title aa-widget-head-draggable rates-icon">
#             Курсы
#         </span><span class="widget-icons">
#         <a class="minimize-w" data-action="widget-minimize"><i>^</i><
#         /a><a class="remove-w" data-action="sbrf-widget-remove"><i>X</i></a>
#         <a class="catalog-w" data-action="sbrf-widget-catalog"><i>*</i><
#         /a></span><span class="widget-icon-hider"><
#         a class="hide-i" data-action="widget-icons-hide" onclick="$(this).closest('.personalized-widget-head').find('.widget-icons').toggleClass('visible');">
#         <i>...</i></a></span></div><div class="bp-widget-body">
#         <div g:onload="window.SBT.personalRates.init(__WIDGET__)" 
#         g:onprefmodified="window.SBT.personalRates.init(__WIDGET__)"><
#         div class="personal-rates" data-reactid=".u"><
#         ul class="tabs" data-reactid=".u.0">
#         <li data-type="currency" class="active" data-reactid=".u.0.0">
#         <span data-reactid=".u.0.0.0">Валюты</span></li><
#         li data-type="metal" class="" data-reactid=".u.0.1"><
#         span data-reactid=".u.0.1.0">Металлы</span></li></ul>
#         <a href="/ru/quotes/converter/" class="currency-section currency" data-reactid=".u.1">
#         <table data-reactid=".u.1.0"><thead data-reactid=".u.1.0.0"><tr
#          data-reactid=".u.1.0.0.0"><td data-reactid=".u.1.0.0.0.0">15.09.2016</td><t
#          d data-reactid=".u.1.0.0.0.1">Покупка</td><td data-reactid=".u.1.0.0.0.2">Продажа
#          </td></tr></thead></table><div class="currency-body" data-reactid=".u.1.1"><span 
#          class="form_input_note" data-reactid=".u.1.1.0"><span class="sbr-tooltip-icon" d
#          ata-reactid=".u.1.1.0.0">?</span></span><p data-reactid=".u.1.1.1">Дистанционные к
#          аналы, карты</p><table data-reactid=".u.1.1.2"><tbody data-reactid=".u.1.1.2.0"><
#          tr data-reactid=".u.1.1.2.0.0"><td data-reactid=".u.1.1.2.0.0.0">Доллар США</td>
#          <td data-reactid=".u.1.1.2.0.0.1"><strong class="currency-decrease" data-reactid
#          =".u.1.1.2.0.0.1.0">63.81</strong></td><td data-reactid=".u.1.1.2.0.0.2"><stron
#          g class="currency-decrease" data-reactid=".u.1.1.2.0.0.2.0">65.99</strong></td>
#          </tr><tr data-reactid=".u.1.1.2.0.1"><td data-reactid=".u.1.1.2.0.1.0">Евро</td
#          ><td data-reactid=".u.1.1.2.0.1.1"><strong class="currency-decrease" data-reacti
#          d=".u.1.1.2.0.1.1.0">71.74</strong></td><td data-reactid=".u.1.1.2.0.1.2"><stron
#          g class="currency-decrease" data-reactid=".u.1.1.2.0.1.2.0">74.18</strong></td><
#          /tr></tbody></table><p data-reactid=".u.1.1.3">Отделения банка</p><table data-re
#          actid=".u.1.1.4"><tbody data-reactid=".u.1.1.4.0"><tr data-reactid=".u.1.1.4.0.0
#          "><td data-reactid=".u.1.1.4.0.0.0">Доллар США</td><td data-reactid=".u.1.1.4.0.
#          0.1"><strong class="currency-decrease" data-reactid=".u.1.1.4.0.0.1.0">63.34</s
#          trong></td><td data-reactid=".u.1.1.4.0.0.2"><strong class="currency-decrease" 
#          data-reactid=".u.1.1.4.0.0.2.0">66.46</strong></td></tr><tr data-reactid=".u.1.1
#          .4.0.1"><td data-reactid=".u.1.1.4.0.1.0">Евро</td><td data-reactid=".u.1.1.4.0
#          .1.1"><strong class="currency-decrease" data-reactid=".u.1.1.4.0.1.1.0">71.21</
#          strong></td><td data-reactid=".u.1.1.4.0.1.2"><strong class="currency-decrease
#          " data-reactid=".u.1.1.4.0.1.2.0">74.71</strong></td></tr></tbody></table></di
#          v></a></div></div></div></div></div><
#         div class="sbt-springboard-area back"></div></div></div>