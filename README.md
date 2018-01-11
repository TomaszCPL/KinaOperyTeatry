# KinaOperyTeatry

-EN-
Main purpose of KinaOperyTeatry is to deliver information about cultural events in Cracow. To accomplish this we use Scrapy to retrieve data from other websites such us http://www.opera.krakow.pl. Collected data are stored in PostgreSQL database. In KinoOperyTeatry we used Django-REST-framwork to communicate between front and back-end. In the near future we are going to add scrappers and make interface more user friendly.


-PL-
  Głównym założeniem projektu jest stworzenie portalu przedstawiającego dane dotyczące wydarzeń związanych z kulturą na terenie Krakowa. Obecnie aplikacja pobiera dane z Opery Krakowskiej i prezentuje ją na mapie przy użyciu biblioteki Leaflet.

  Projekt opiera się na danych pozyskanych za pomocą scrapperów (biblioteka Scrapy) oraz wprowadzonych ręcznie przez administratora. Zastosowanie webscrappingu pozwala zmiejszyć nakład wymaganej pracy koniecznej do prezentacji aktualnych informacji z wielu źródeł. Pobrane dane gromadzone są w bazie danych PostgreSQL, które następnie przy użyciu Django Rest API są Udostępniane. Wykorzystanie wspomnianej technologii REST umożliwia oddzielenie części front-endowej od back-endu, co pozytywnie wpływa na utrzymanie oraz przyszły rozwój projektu. W najbliższej przyszłości (grudzień 2017) zostanie udoskonalony interface użytkownika o możliwość wyboru dnia. Dodatkowo planowane jest wprowadzenie kolejnego scrappera. Następnie zostanie wprowadzony moduł odpowiedzialny za rejstrację użytkowników oraz dodawanie przez nich treści.

![Alt text](https://github.com/jrkapciak/KinaOperyTeatry/blob/master/demo_screenshot.png)

