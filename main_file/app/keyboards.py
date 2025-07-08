from aiogram.types import ReplyKeyboardMarkup, KeyboardButton, InlineKeyboardMarkup, InlineKeyboardButton



main = ReplyKeyboardMarkup(keyboard=[[KeyboardButton(text="Услуги"), KeyboardButton(text="О нас")],
                                     [KeyboardButton(text="Контакты"), KeyboardButton(text="Вопрос")]],
                           resize_keyboard=True, input_field_placeholder="Выберите кнопку")


services = InlineKeyboardMarkup(inline_keyboard=[
    [InlineKeyboardButton(text="Электромонтаж в квартирах и домах", callback_data="electricity_in_flats_and_houses")],
    [InlineKeyboardButton(text= "Электромонтаж в кафе и ресторанах", callback_data="electricity_in_cafe_and_restaurants")],
    [InlineKeyboardButton(text= "Увеличение электрической мощности", callback_data="High_electricity_power")],
    [InlineKeyboardButton(text= "Электромонтаж на торговых и промышленных объектах", callback_data="electric_works_in_business_objects")],
    [InlineKeyboardButton(text= "Проектирование", callback_data="projecting")],
    [InlineKeyboardButton(text= "Монтаж освещения", callback_data="light_works")],
    [InlineKeyboardButton(text= "Консультация в сфере энергетики", callback_data="consultation_about_electricity")],
    [InlineKeyboardButton(text= "Технологическое присоединение к электросетям", callback_data="tech_connect_to_electric_net")]
])

#Вопросы



questions = InlineKeyboardMarkup(inline_keyboard=[[InlineKeyboardButton(text="Общие вопросы", callback_data="any_q")],
                                                  [InlineKeyboardButton(text="Вопросы по электромонтажу в квартирах и домах", callback_data="r1_q")],
                                                  [InlineKeyboardButton(text="Вопросы по электромонтажу в кафе и ресторанах", callback_data="r2_q")],
                                                  [InlineKeyboardButton(text="По увеличению электрической мощности", callback_data="r3_q")],
                                                  [InlineKeyboardButton(text="По работам на торговых и промышленных объектах", callback_data="r3_q")],
                                                  [InlineKeyboardButton(text="По проектированию", callback_data="r5_q")],
                                                  [InlineKeyboardButton(text="По монтажу освещения", callback_data="r6_q")],
                                                  [InlineKeyboardButton(text="По консультированию", callback_data="r7_q")],
                                                  [InlineKeyboardButton(text="По технологическому присоединению", callback_data="r8_q")]])



#Подуслуги раздела электромонтажа в квартирах и домах
sub_services_1 = InlineKeyboardMarkup(inline_keyboard = [[InlineKeyboardButton(text="Монтаж установка УЗО, УЗМ, автомата", callback_data="montage_automat")],
                                                         [InlineKeyboardButton(text="Подключение бытовой техники", callback_data="connect_household")],
                                                         [InlineKeyboardButton(text="Замена и установка светильников", callback_data="changing_lamps")],
                                                         [InlineKeyboardButton(text="Замена розеток", callback_data="changing_outlets")],
                                                         [InlineKeyboardButton(text="Замена выключателей", callback_data="changing_switches")],
                                                         [InlineKeyboardButton(text="Монтаж и замена электрощита", callback_data="montage_electrical_panel")],
                                                         [InlineKeyboardButton(text="Замена проводки на кухне", callback_data="changing_wiring_kitchen")],
                                                         [InlineKeyboardButton(text="Электромонтаж в домах", callback_data="electric_installation_houses")],
                                                         [InlineKeyboardButton(text="Электромонтаж в квартирах", callback_data="electric_installation_flats")]])


#Подуслуги раздела электромонтажа в кафе и ресторанах
sub_services_2 = InlineKeyboardMarkup(inline_keyboard=[[InlineKeyboardButton(text="Монтаж освещения", callback_data="montage_light")],
                                                       [InlineKeyboardButton(text="Прокладка линий внутреннего электроснабжения", callback_data="electrical_inlines")],
                                                       [InlineKeyboardButton(text="Сборка и монтаж ВРУ (щитов)", callback_data="building_panels")]])


#Подуслуги раздела увеличение электрической мощности
sub_services_3 = InlineKeyboardMarkup(inline_keyboard=[[InlineKeyboardButton(text="Получение актов АТП", callback_data="receiving_certificates")],
                                                       [InlineKeyboardButton(text="Выполнение технических условий", callback_data="complete_tech")],
                                                       [InlineKeyboardButton(text="Разработка проекта однолинейной схемы", callback_data="project_one_line_system")],
                                                       [InlineKeyboardButton(text="Получение технических условий", callback_data="receiving_tech")],
                                                       [InlineKeyboardButton(text="Подготовка документов", callback_data="ready_documents")]])


#Подуслуги раздела электромонтажа на торговых и промышленных объектах
sub_services_4 = InlineKeyboardMarkup(inline_keyboard=[[InlineKeyboardButton(text="Монтаж освещения", callback_data="montage_lights")],
                                                       [InlineKeyboardButton(text="Прокладка линий внутреннего электроснабжения", callback_data="to_do_electrical_inlines")],
                                                       [InlineKeyboardButton(text="Сборка и монтаж ВРУ", callback_data="build_electric")],
                                                       [InlineKeyboardButton(text="Сборка и монтаж ГРЩ", callback_data="build_and_montage")],
                                                       [InlineKeyboardButton(text="Монтаж воздушных линий", callback_data="montage_airlines")],
                                                       [InlineKeyboardButton(text="Прокладка кабельных линий", callback_data="to_do_lines")]])

#Подуслуги раздела проектирования
sub_services_5 = InlineKeyboardMarkup(inline_keyboard=[[InlineKeyboardButton(text="Заземление", callback_data="grounding")],
                                                       [InlineKeyboardButton(text="Молниезащиты", callback_data="lightning_protection")],
                                                       [InlineKeyboardButton(text="Электроснабжения дома", callback_data="project_house")],
                                                       [InlineKeyboardButton(text="Наружного освещения", callback_data="project_out_light")],
                                                       [InlineKeyboardButton(text="Внутреннего электроснабжение", callback_data="project_in_electro")],
                                                       [InlineKeyboardButton(text="Внешнего электроснабжение", callback_data="project_out_electro")]])

#Подуслуги раздела монтажа освещения
sub_services_6 = InlineKeyboardMarkup(inline_keyboard=[[InlineKeyboardButton(text="В поселках и СНТ", callback_data="in_villages")],
                                                       [InlineKeyboardButton(text="Подсветки зданий", callback_data="light_of_buildings")],
                                                       [InlineKeyboardButton(text="Наружного освещения", callback_data="out_lighting")]])

#Подуслуги раздела технологического присоединения к электросетям
sub_services_8 = InlineKeyboardMarkup(inline_keyboard=[[InlineKeyboardButton(text="Получение договора электроснабжения", callback_data="receive_contract_electro")],
                                                       [InlineKeyboardButton(text="Получение актов АТП", callback_data="receive_certificates")],
                                                       [InlineKeyboardButton(text="Выполнение технических условий", callback_data="ready_tech")],
                                                       [InlineKeyboardButton(text="Разработка проекта однолинейной схемы", callback_data="create_project")],
                                                       [InlineKeyboardButton(text="Получение технических условий", callback_data="tech_conditions")],
                                                       [InlineKeyboardButton(text="Подключение к электросетям под ключ", callback_data="connection_to_electro")]])