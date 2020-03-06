*** Settings ***
Library     SeleniumLibrary
Library     ../web_objects/web_page_objects.py
Library     Collections
Variables   ../variables/ww_web_locators.py

*** Test Cases ***
validate weight watchers web page
    [Tags]      WW_REGRESSION
    [Documentation]   Validating UI web page
    Given user navigates to the address                  ${web_address_id}
    ${first_page_title}   user gets the title of the page
    And SHOULD BE EQUAL AS STRINGS                      ${first_page_title}   ${HOME_PAGE_TITLE}

    ${studio_btn_locator}  user clicks on studio button   ${studio_text_id}
    sleep                                                 ${20}
    Then dismiss popup                                    ${30}

    ${second_page_title}   user gets the title of the page     ${True}
    And SHOULD BE EQUAL AS STRINGS              ${second_page_title}    ${STUDIO_PAGE_TITLE}

    Then user inputs zipcode in search bar field    ${location_zip}   element_name=${search_bar_field_id}
    ${location_name}   get element by class         ${location_name_id}
    And user waits till the element visibles        ${location_name}

    ${location_text}   get text                     ${location_name}

    ${location_dist}    get element by class        ${location_distance_id}
    ${distance_text}        get_text                ${location_dist}

    Then user selects a location                    ${location_name_id}

    ${result_location}  get element by class        ${location_name_id}
    ${result_location_text}   get text              ${result_location}

    And SHOULD BE EQUAL AS STRINGS   ${result_location_text}    ${location_text}

    Then user drags the scroll bar              ${operating_hour_xpath}

    ${today_work_hours}         user gets operating hours or appointments   ${operating_hours_class}
    ${appointment_schedules}    user gets operating hours or appointments   ${employee_schedule_day}
    LOG TO CONSOLE          ${appointment_schedules}
    LOG TO CONSOLE          ${today_work_hours}
    sleep                   ${5}
    Then close web browser

*** Keywords ***
user navigates to the address
    [Arguments]   ${web_address}
    navigate_to_page     ${web_address}
    maximize_browser

user gets the title of the page
    [Arguments]     ${convert_uni}=${False}
    ${result_title}    get_page_title   ${convert_uni}
    [Return]  ${result_title}

user clicks on studio button
    [Arguments]   ${link_text}
    ${element_locator}  get_element_by_property   ${link_text}
    user waits till the element visibles        ${element_locator}
    click_button        ${element_locator}

user waits till the element visibles
    [Arguments]     ${element_id}
    wait_until_page_contains_element   ${element_id}

user inputs zipcode in search bar field
    [Arguments]   ${zip_address}   ${link_text}=${None}  ${element_name}=${None}
    ${search_locator}  get_element_by_property  ${link_text}    ${element_name}
    input_text          ${search_locator}   ${zip_address}
    submit_form         ${search_locator}

user drags the scroll bar
    [Arguments]   ${x_path}
    ${dest_element}  get_element_by_xpath   ${x_path}
    ${coords}  scroll_web_page   ${dest_element}
    [Return]  ${coords}

user gets xpath of dest coords
    [Arguments]   ${x_path}
    ${dest_element}  get_element_by_xpath   ${x_path}
    [Return]  ${dest_element}

user selects a location
    [Arguments]     ${class_name}
    ${idofdest}  get_element_by_class    ${class_name}
    click_button    ${idofdest}
    user waits till the element visibles  ${idofdest}

user gets operating hours or appointments
    [Arguments]     ${class_name}
    ${hours}    get_operating_hours_or_appointments   ${class_name}
    [Return]    ${hours}