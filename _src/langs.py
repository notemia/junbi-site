# Site copy for the Junbi privacy and support pages. One dict per language.
# 'sections' of the privacy policy: (heading, [paragraphs]); '{unity}' becomes the Unity privacy-policy link, '{mail}' the address.
L = {}

L['en'] = dict(
 name='Junbi', tag='Olympic taekwondo', home='Home', privacy='Privacy Policy', support='Support', updated='Last updated: 25 November 2026',
 lead='Junbi is a taekwondo game played by the rules of World Taekwondo: electronic scoring, three rounds, fighters from different countries and a realistic kicking technique.',
 features=['Championship, world ranking, training with a coach and a quick single bout', 'Fight a friend online with a short code', 'Fighters from different countries, each with a signature combo', 'No account, no ads, no tracking'],
 priv_title='Privacy Policy', priv_intro='This policy describes how the app Junbi: Olympic Taekwondo (by Notemia) treats your data.',
 sections=[
  ('The short version', ['Junbi does not ask you to create an account. It has no advertising, no analytics, no tracking and no in-app purchases. Notemia does not collect, store or sell any personal data about you.']),
  ('What stays on your device', ['Your progress, settings, chosen fighter, ranking and saved replays are stored only on your device. We cannot see them. Deleting the app deletes them.']),
  ('Fight a Friend (optional)', ['Online play starts only when you choose it. To connect two players the game uses Unity Gaming Services (Authentication and Relay), provided by Unity Technologies. When you use it, Unity creates an anonymous player ID, issues a short join code and processes network data such as your IP address in order to connect you to your friend and pass the match between your devices. Notemia does not receive or store this data. How Unity handles it is described in the {unity}.', 'If you never use Fight a Friend, none of this happens.']),
  ('Children', ['Junbi does not knowingly collect personal information from anyone, including children. The game has no chat, no profiles and no way to share personal information.']),
  ('Changes to this policy', ['If this policy changes, the new version will be published on this page with a new date.']),
  ('Contact', ['Questions about privacy: {mail}.']),
 ], unity_label='Unity Privacy Policy',
 sup_title='Support', sup_intro='Need help with Junbi? Write to us and we will answer as soon as we can.', sup_mail='Email', sup_faq='Common questions',
 faq=[
  ('How do I play against a friend online?', 'Open “Fight a Friend”. One player creates a match and shares the short code, the other enters it. Both devices need an internet connection.'),
  ('The friend code does not work.', 'Check that the code is typed exactly and was created recently. If it still fails, create a new match and share the new code. Switching the network (Wi-Fi or cellular) sometimes helps.'),
  ('Can I move my progress to another device?', 'Progress is stored only on the device. There is no account or cloud sync, so it cannot be moved automatically, and deleting the app erases it.'),
  ('How do I change the language?', 'Open Settings in the main menu and choose a language from the list.'),
  ('How do I report a problem?', 'Email us your device model, system version and a short description of what happened. A screenshot helps.'),
 ], more_priv='What data does the game use? Read the Privacy Policy.', lang_label='Language',
)

L['ru'] = dict(
 name='Junbi', tag='Олимпийское тхэквондо', home='Главная', privacy='Политика конфиденциальности', support='Поддержка', updated='Обновлено: 25 ноября 2026',
 lead='Junbi — игра про тхэквондо по правилам World Taekwondo: электронные жилеты, три раунда, бойцы из разных стран и реалистичная техника ударов.',
 features=['Чемпионат, мировой рейтинг, тренировка с тренером и быстрый бой', 'Бой с другом по сети по короткому коду', 'Бойцы из разных стран, у каждого своя коронка', 'Без аккаунта, без рекламы, без слежки'],
 priv_title='Политика конфиденциальности', priv_intro='Здесь описано, как приложение «Junbi: Олимпийское тхэквондо» (Notemia) обращается с вашими данными.',
 sections=[
  ('Коротко', ['Junbi не просит создавать аккаунт. В игре нет рекламы, аналитики, слежения и встроенных покупок. Notemia не собирает, не хранит и не продаёт никаких персональных данных о вас.']),
  ('Что остаётся на устройстве', ['Прогресс, настройки, выбранный боец, рейтинг и сохранённые повторы хранятся только на вашем устройстве. Мы их не видим. При удалении приложения они удаляются.']),
  ('Бой с другом (по желанию)', ['Игра по сети начинается только тогда, когда вы сами её выбрали. Чтобы соединить двух игроков, игра использует Unity Gaming Services (Authentication и Relay) от Unity Technologies. При этом Unity создаёт анонимный идентификатор игрока, выдаёт короткий код подключения и обрабатывает сетевые данные, например IP-адрес, чтобы соединить вас с другом и передавать матч между вашими устройствами. Notemia эти данные не получает и не хранит. Как с ними обращается Unity, описано в документе «{unity}».', 'Если вы не пользуетесь боем с другом, ничего из этого не происходит.']),
  ('Дети', ['Junbi сознательно не собирает личную информацию ни у кого, в том числе у детей. В игре нет чата, профилей и способов поделиться личными данными.']),
  ('Изменения политики', ['Если политика изменится, новая версия появится на этой странице с новой датой.']),
  ('Связь', ['Вопросы о конфиденциальности: {mail}.']),
 ], unity_label='Политика конфиденциальности Unity',
 sup_title='Поддержка', sup_intro='Нужна помощь с Junbi? Напишите нам, и мы ответим как можно скорее.', sup_mail='Почта', sup_faq='Частые вопросы',
 faq=[
  ('Как сыграть с другом по сети?', 'Откройте «С другом». Один игрок создаёт матч и называет короткий код, другой вводит его. На обоих устройствах нужен интернет.'),
  ('Код друга не подходит.', 'Проверьте, что код введён точно и создан недавно. Если не помогло, создайте новый матч и отправьте новый код. Иногда помогает смена сети (Wi-Fi или мобильная).'),
  ('Можно ли перенести прогресс на другое устройство?', 'Прогресс хранится только на устройстве. Аккаунта и облака нет, поэтому автоматически перенести его нельзя, а при удалении приложения он стирается.'),
  ('Как сменить язык?', 'Откройте «Настройки» в главном меню и выберите язык из списка.'),
  ('Как сообщить о проблеме?', 'Напишите нам модель устройства, версию системы и коротко опишите, что произошло. Поможет скриншот.'),
 ], more_priv='Какие данные использует игра? Читайте политику конфиденциальности.', lang_label='Язык',
)

L['fr'] = dict(
 name='Junbi', tag='Taekwondo olympique', home='Accueil', privacy='Politique de confidentialité', support='Assistance', updated='Dernière mise à jour : 25 novembre 2026',
 lead='Junbi est un jeu de taekwondo selon les règles de World Taekwondo : plastrons électroniques, trois rounds, combattants de différents pays et technique de frappe réaliste.',
 features=['Championnat, classement mondial, entraînement avec un coach et combat rapide', 'Combat en ligne contre un ami avec un code court', 'Des combattants de différents pays, chacun avec sa combinaison signature', 'Sans compte, sans publicité, sans suivi'],
 priv_title='Politique de confidentialité', priv_intro='Cette politique explique comment l’application Junbi : Taekwondo olympique (Notemia) traite vos données.',
 sections=[
  ('En bref', ['Junbi ne vous demande pas de créer de compte. Il n’y a ni publicité, ni analyse, ni suivi, ni achat intégré. Notemia ne collecte, ne conserve et ne vend aucune donnée personnelle vous concernant.']),
  ('Ce qui reste sur votre appareil', ['Votre progression, vos réglages, le combattant choisi, le classement et les replays enregistrés restent uniquement sur votre appareil. Nous ne pouvons pas les voir. Supprimer l’application les supprime.']),
  ('Combat contre un ami (facultatif)', ['Le jeu en ligne ne démarre que si vous le choisissez. Pour relier deux joueurs, le jeu utilise Unity Gaming Services (Authentication et Relay), fournis par Unity Technologies. Unity crée alors un identifiant de joueur anonyme, délivre un code de connexion court et traite des données réseau, comme votre adresse IP, afin de vous connecter à votre ami et de transmettre le match entre vos appareils. Notemia ne reçoit ni ne conserve ces données. Le traitement par Unity est décrit dans la {unity}.', 'Si vous n’utilisez jamais le combat contre un ami, rien de tout cela n’a lieu.']),
  ('Enfants', ['Junbi ne collecte sciemment aucune information personnelle, y compris auprès des enfants. Le jeu n’a ni chat, ni profil, ni moyen de partager des informations personnelles.']),
  ('Modifications', ['En cas de modification, la nouvelle version sera publiée sur cette page avec une nouvelle date.']),
  ('Contact', ['Questions sur la confidentialité : {mail}.']),
 ], unity_label='politique de confidentialité d’Unity',
 sup_title='Assistance', sup_intro='Besoin d’aide avec Junbi ? Écrivez-nous, nous répondrons dès que possible.', sup_mail='E-mail', sup_faq='Questions fréquentes',
 faq=[
  ('Comment jouer en ligne contre un ami ?', 'Ouvrez « Contre un ami ». Un joueur crée un match et partage le code court, l’autre le saisit. Les deux appareils ont besoin d’une connexion internet.'),
  ('Le code de l’ami ne fonctionne pas.', 'Vérifiez que le code est saisi exactement et qu’il a été créé récemment. Sinon, créez un nouveau match et partagez le nouveau code. Changer de réseau (Wi-Fi ou mobile) aide parfois.'),
  ('Puis-je transférer ma progression sur un autre appareil ?', 'La progression n’est stockée que sur l’appareil. Il n’y a ni compte ni synchronisation cloud : elle ne peut pas être transférée automatiquement et la suppression de l’application l’efface.'),
  ('Comment changer la langue ?', 'Ouvrez les réglages dans le menu principal et choisissez une langue dans la liste.'),
  ('Comment signaler un problème ?', 'Envoyez-nous le modèle de votre appareil, la version du système et une courte description. Une capture d’écran aide.'),
 ], more_priv='Quelles données le jeu utilise-t-il ? Lisez la politique de confidentialité.', lang_label='Langue',
)

L['de'] = dict(
 name='Junbi', tag='Olympisches Taekwondo', home='Startseite', privacy='Datenschutzerklärung', support='Support', updated='Zuletzt aktualisiert: 25. November 2026',
 lead='Junbi ist ein Taekwondo-Spiel nach den Regeln von World Taekwondo: elektronische Westen, drei Runden, Kämpfer aus verschiedenen Ländern und eine realistische Trittechnik.',
 features=['Meisterschaft, Weltrangliste, Training mit Coach und schneller Einzelkampf', 'Online gegen einen Freund mit kurzem Code', 'Kämpfer aus verschiedenen Ländern, jeder mit eigener Signatur-Kombination', 'Kein Konto, keine Werbung, kein Tracking'],
 priv_title='Datenschutzerklärung', priv_intro='Diese Erklärung beschreibt, wie die App Junbi: Olympisches Taekwondo (Notemia) mit Ihren Daten umgeht.',
 sections=[
  ('Kurzfassung', ['Junbi verlangt kein Konto. Es gibt keine Werbung, keine Analyse, kein Tracking und keine In-App-Käufe. Notemia erhebt, speichert und verkauft keine personenbezogenen Daten über Sie.']),
  ('Was auf Ihrem Gerät bleibt', ['Ihr Fortschritt, Ihre Einstellungen, der gewählte Kämpfer, die Rangliste und gespeicherte Wiederholungen liegen nur auf Ihrem Gerät. Wir können sie nicht sehen. Beim Löschen der App werden sie gelöscht.']),
  ('Kampf gegen einen Freund (optional)', ['Das Online-Spiel startet nur, wenn Sie es wählen. Um zwei Spieler zu verbinden, nutzt das Spiel die Unity Gaming Services (Authentication und Relay) von Unity Technologies. Dabei erstellt Unity eine anonyme Spieler-ID, vergibt einen kurzen Beitrittscode und verarbeitet Netzwerkdaten wie Ihre IP-Adresse, um Sie mit Ihrem Freund zu verbinden und den Kampf zwischen Ihren Geräten zu übertragen. Notemia erhält und speichert diese Daten nicht. Wie Unity sie behandelt, steht in der {unity}.', 'Wenn Sie den Kampf gegen einen Freund nie nutzen, passiert nichts davon.']),
  ('Kinder', ['Junbi erhebt wissentlich von niemandem personenbezogene Daten, auch nicht von Kindern. Das Spiel hat keinen Chat, keine Profile und keine Möglichkeit, persönliche Daten zu teilen.']),
  ('Änderungen', ['Ändert sich diese Erklärung, wird die neue Fassung mit neuem Datum auf dieser Seite veröffentlicht.']),
  ('Kontakt', ['Fragen zum Datenschutz: {mail}.']),
 ], unity_label='Datenschutzerklärung von Unity',
 sup_title='Support', sup_intro='Brauchen Sie Hilfe mit Junbi? Schreiben Sie uns, wir antworten so schnell wie möglich.', sup_mail='E-Mail', sup_faq='Häufige Fragen',
 faq=[
  ('Wie spiele ich online gegen einen Freund?', 'Öffnen Sie „Mit Freund“. Ein Spieler erstellt ein Match und teilt den kurzen Code, der andere gibt ihn ein. Beide Geräte brauchen eine Internetverbindung.'),
  ('Der Freundescode funktioniert nicht.', 'Prüfen Sie, ob der Code genau eingegeben und erst kürzlich erstellt wurde. Sonst erstellen Sie ein neues Match und teilen den neuen Code. Ein Netzwechsel (WLAN oder Mobilfunk) hilft manchmal.'),
  ('Kann ich meinen Fortschritt auf ein anderes Gerät übertragen?', 'Der Fortschritt liegt nur auf dem Gerät. Es gibt weder Konto noch Cloud-Sync, daher ist keine automatische Übertragung möglich; beim Löschen der App wird er gelöscht.'),
  ('Wie ändere ich die Sprache?', 'Öffnen Sie im Hauptmenü die Einstellungen und wählen Sie eine Sprache aus der Liste.'),
  ('Wie melde ich ein Problem?', 'Senden Sie uns Gerätemodell, Systemversion und eine kurze Beschreibung. Ein Screenshot hilft.'),
 ], more_priv='Welche Daten nutzt das Spiel? Lesen Sie die Datenschutzerklärung.', lang_label='Sprache',
)

L['es'] = dict(
 name='Junbi', tag='Taekwondo olímpico', home='Inicio', privacy='Política de privacidad', support='Soporte', updated='Última actualización: 25 de noviembre de 2026',
 lead='Junbi es un juego de taekwondo con las reglas de World Taekwondo: petos electrónicos, tres asaltos, luchadores de distintos países y una técnica de patadas realista.',
 features=['Campeonato, ranking mundial, entrenamiento con entrenador y combate rápido', 'Combate en línea contra un amigo con un código corto', 'Luchadores de distintos países, cada uno con su combo característico', 'Sin cuenta, sin anuncios, sin rastreo'],
 priv_title='Política de privacidad', priv_intro='Esta política describe cómo la app Junbi: Taekwondo olímpico (Notemia) trata tus datos.',
 sections=[
  ('En resumen', ['Junbi no te pide crear una cuenta. No tiene publicidad, analítica, rastreo ni compras integradas. Notemia no recopila, almacena ni vende ningún dato personal sobre ti.']),
  ('Lo que queda en tu dispositivo', ['Tu progreso, ajustes, luchador elegido, ranking y repeticiones guardadas se almacenan solo en tu dispositivo. No podemos verlos. Al borrar la app se borran.']),
  ('Combate con un amigo (opcional)', ['El juego en línea solo empieza si tú lo eliges. Para conectar a dos jugadores, el juego usa Unity Gaming Services (Authentication y Relay), de Unity Technologies. Unity crea un identificador de jugador anónimo, emite un código de unión corto y procesa datos de red, como tu dirección IP, para conectarte con tu amigo y pasar el combate entre vuestros dispositivos. Notemia no recibe ni almacena estos datos. Cómo los trata Unity se describe en la {unity}.', 'Si nunca usas el combate con un amigo, nada de esto ocurre.']),
  ('Menores', ['Junbi no recopila a sabiendas información personal de nadie, incluidos los menores. El juego no tiene chat, perfiles ni forma de compartir datos personales.']),
  ('Cambios', ['Si esta política cambia, la nueva versión se publicará en esta página con una nueva fecha.']),
  ('Contacto', ['Preguntas sobre privacidad: {mail}.']),
 ], unity_label='política de privacidad de Unity',
 sup_title='Soporte', sup_intro='¿Necesitas ayuda con Junbi? Escríbenos y responderemos lo antes posible.', sup_mail='Correo', sup_faq='Preguntas frecuentes',
 faq=[
  ('¿Cómo juego en línea contra un amigo?', 'Abre «Con un amigo». Un jugador crea la partida y comparte el código corto, el otro lo introduce. Ambos dispositivos necesitan internet.'),
  ('El código del amigo no funciona.', 'Comprueba que el código esté escrito exactamente y se haya creado hace poco. Si sigue fallando, crea una partida nueva y comparte el nuevo código. A veces ayuda cambiar de red (Wi-Fi o datos).'),
  ('¿Puedo pasar mi progreso a otro dispositivo?', 'El progreso se guarda solo en el dispositivo. No hay cuenta ni sincronización en la nube, así que no se puede mover automáticamente y al borrar la app se pierde.'),
  ('¿Cómo cambio el idioma?', 'Abre Ajustes en el menú principal y elige un idioma de la lista.'),
  ('¿Cómo informo de un problema?', 'Envíanos el modelo del dispositivo, la versión del sistema y una breve descripción. Una captura de pantalla ayuda.'),
 ], more_priv='¿Qué datos usa el juego? Lee la política de privacidad.', lang_label='Idioma',
)

L['pt-br'] = dict(
 name='Junbi', tag='Taekwondo olímpico', home='Início', privacy='Política de privacidade', support='Suporte', updated='Última atualização: 25 de novembro de 2026',
 lead='Junbi é um jogo de taekwondo com as regras da World Taekwondo: coletes eletrônicos, três rounds, lutadores de vários países e uma técnica de chutes realista.',
 features=['Campeonato, ranking mundial, treino com treinador e luta rápida', 'Luta online contra um amigo com um código curto', 'Lutadores de vários países, cada um com seu combo característico', 'Sem conta, sem anúncios, sem rastreamento'],
 priv_title='Política de privacidade', priv_intro='Esta política descreve como o app Junbi: Taekwondo olímpico (Notemia) trata os seus dados.',
 sections=[
  ('Resumo', ['O Junbi não pede que você crie uma conta. Não há publicidade, análise, rastreamento nem compras no app. A Notemia não coleta, armazena nem vende nenhum dado pessoal sobre você.']),
  ('O que fica no seu dispositivo', ['Seu progresso, configurações, lutador escolhido, ranking e replays salvos ficam apenas no seu dispositivo. Nós não conseguimos vê-los. Ao excluir o app, eles são apagados.']),
  ('Luta com um amigo (opcional)', ['O jogo online só começa se você escolher. Para conectar dois jogadores, o jogo usa o Unity Gaming Services (Authentication e Relay), da Unity Technologies. A Unity cria um ID de jogador anônimo, emite um código de entrada curto e processa dados de rede, como seu endereço IP, para conectar você ao seu amigo e passar a luta entre os dispositivos. A Notemia não recebe nem armazena esses dados. Como a Unity os trata está descrito na {unity}.', 'Se você nunca usar a luta com um amigo, nada disso acontece.']),
  ('Crianças', ['O Junbi não coleta intencionalmente informações pessoais de ninguém, inclusive de crianças. O jogo não tem chat, perfis nem forma de compartilhar dados pessoais.']),
  ('Alterações', ['Se esta política mudar, a nova versão será publicada nesta página com uma nova data.']),
  ('Contato', ['Dúvidas sobre privacidade: {mail}.']),
 ], unity_label='política de privacidade da Unity',
 sup_title='Suporte', sup_intro='Precisa de ajuda com o Junbi? Escreva para nós e responderemos assim que possível.', sup_mail='E-mail', sup_faq='Perguntas frequentes',
 faq=[
  ('Como jogo online contra um amigo?', 'Abra “Com um amigo”. Um jogador cria a partida e compartilha o código curto, o outro o digita. Os dois dispositivos precisam de internet.'),
  ('O código do amigo não funciona.', 'Confira se o código foi digitado exatamente e criado há pouco. Se continuar falhando, crie uma nova partida e compartilhe o novo código. Trocar de rede (Wi-Fi ou dados móveis) às vezes ajuda.'),
  ('Posso levar meu progresso para outro dispositivo?', 'O progresso fica apenas no dispositivo. Não há conta nem sincronização na nuvem, então ele não pode ser movido automaticamente, e excluir o app o apaga.'),
  ('Como mudo o idioma?', 'Abra Configurações no menu principal e escolha um idioma na lista.'),
  ('Como relato um problema?', 'Envie o modelo do dispositivo, a versão do sistema e uma breve descrição. Uma captura de tela ajuda.'),
 ], more_priv='Que dados o jogo usa? Leia a política de privacidade.', lang_label='Idioma',
)

L['pl'] = dict(
 name='Junbi', tag='Taekwondo olimpijskie', home='Strona główna', privacy='Polityka prywatności', support='Wsparcie', updated='Ostatnia aktualizacja: 25 listopada 2026',
 lead='Junbi to gra o taekwondo według zasad World Taekwondo: elektroniczne ochraniacze, trzy rundy, zawodnicy z różnych krajów i realistyczna technika kopnięć.',
 features=['Mistrzostwa, ranking światowy, trening z trenerem i szybka walka', 'Walka online z przyjacielem za pomocą krótkiego kodu', 'Zawodnicy z różnych krajów, każdy z własną kombinacją', 'Bez konta, bez reklam, bez śledzenia'],
 priv_title='Polityka prywatności', priv_intro='Ta polityka opisuje, jak aplikacja Junbi: Taekwondo olimpijskie (Notemia) traktuje Twoje dane.',
 sections=[
  ('W skrócie', ['Junbi nie wymaga zakładania konta. Nie ma reklam, analityki, śledzenia ani zakupów w aplikacji. Notemia nie zbiera, nie przechowuje i nie sprzedaje żadnych danych osobowych o Tobie.']),
  ('Co zostaje na urządzeniu', ['Twój postęp, ustawienia, wybrany zawodnik, ranking i zapisane powtórki są przechowywane wyłącznie na Twoim urządzeniu. Nie mamy do nich wglądu. Usunięcie aplikacji je usuwa.']),
  ('Walka z przyjacielem (opcjonalnie)', ['Gra online rusza tylko wtedy, gdy ją wybierzesz. Do połączenia dwóch graczy gra korzysta z Unity Gaming Services (Authentication i Relay) firmy Unity Technologies. Unity tworzy wtedy anonimowy identyfikator gracza, wydaje krótki kod dołączenia i przetwarza dane sieciowe, takie jak adres IP, aby połączyć Cię z przyjacielem i przekazywać walkę między urządzeniami. Notemia nie otrzymuje ani nie przechowuje tych danych. Sposób ich przetwarzania opisuje {unity}.', 'Jeśli nigdy nie korzystasz z walki z przyjacielem, nic z tego się nie dzieje.']),
  ('Dzieci', ['Junbi świadomie nie zbiera danych osobowych od nikogo, także od dzieci. W grze nie ma czatu, profili ani możliwości dzielenia się danymi osobowymi.']),
  ('Zmiany', ['Jeśli polityka się zmieni, nowa wersja pojawi się na tej stronie z nową datą.']),
  ('Kontakt', ['Pytania o prywatność: {mail}.']),
 ], unity_label='polityka prywatności Unity',
 sup_title='Wsparcie', sup_intro='Potrzebujesz pomocy z Junbi? Napisz do nas, odpowiemy najszybciej, jak się da.', sup_mail='E-mail', sup_faq='Częste pytania',
 faq=[
  ('Jak zagrać online z przyjacielem?', 'Otwórz „Z przyjacielem”. Jeden gracz tworzy mecz i podaje krótki kod, drugi go wpisuje. Oba urządzenia potrzebują internetu.'),
  ('Kod przyjaciela nie działa.', 'Sprawdź, czy kod jest wpisany dokładnie i został utworzony niedawno. Jeśli nadal nie działa, utwórz nowy mecz i wyślij nowy kod. Czasem pomaga zmiana sieci (Wi-Fi lub komórkowa).'),
  ('Czy mogę przenieść postęp na inne urządzenie?', 'Postęp jest przechowywany tylko na urządzeniu. Nie ma konta ani synchronizacji w chmurze, więc nie można go przenieść automatycznie, a usunięcie aplikacji go kasuje.'),
  ('Jak zmienić język?', 'Otwórz Ustawienia w menu głównym i wybierz język z listy.'),
  ('Jak zgłosić problem?', 'Wyślij nam model urządzenia, wersję systemu i krótki opis. Pomoże zrzut ekranu.'),
 ], more_priv='Jakich danych używa gra? Przeczytaj politykę prywatności.', lang_label='Język',
)

L['tr'] = dict(
 name='Junbi', tag='Olimpik tekvando', home='Ana sayfa', privacy='Gizlilik Politikası', support='Destek', updated='Son güncelleme: 25 Kasım 2026',
 lead='Junbi, World Taekwondo kurallarına göre oynanan bir tekvando oyunudur: elektronik koruyucular, üç raunt, farklı ülkelerden dövüşçüler ve gerçekçi tekme tekniği.',
 features=['Şampiyona, dünya sıralaması, antrenörle antrenman ve hızlı maç', 'Kısa bir kodla arkadaşınla çevrimiçi dövüş', 'Farklı ülkelerden dövüşçüler, her birinin kendine özgü kombinasyonu', 'Hesap yok, reklam yok, takip yok'],
 priv_title='Gizlilik Politikası', priv_intro='Bu politika, Junbi: Olimpik Tekvando uygulamasının (Notemia) verilerinizi nasıl ele aldığını açıklar.',
 sections=[
  ('Kısaca', ['Junbi hesap oluşturmanızı istemez. Reklam, analiz, takip ve uygulama içi satın alma yoktur. Notemia hakkınızda hiçbir kişisel veri toplamaz, saklamaz veya satmaz.']),
  ('Cihazınızda kalanlar', ['İlerlemeniz, ayarlarınız, seçtiğiniz dövüşçü, sıralamanız ve kaydedilen tekrarlar yalnızca cihazınızda saklanır. Onları göremeyiz. Uygulamayı silmek bunları siler.']),
  ('Arkadaşla Dövüş (isteğe bağlı)', ['Çevrimiçi oyun yalnızca siz seçtiğinizde başlar. İki oyuncuyu bağlamak için oyun, Unity Technologies’in Unity Gaming Services (Authentication ve Relay) hizmetlerini kullanır. Bu sırada Unity anonim bir oyuncu kimliği oluşturur, kısa bir katılım kodu verir ve sizi arkadaşınıza bağlamak ve maçı cihazlarınız arasında aktarmak için IP adresiniz gibi ağ verilerini işler. Notemia bu verileri almaz ve saklamaz. Unity’nin bunları nasıl ele aldığı {unity} içinde açıklanır.', 'Arkadaşla Dövüş’ü hiç kullanmazsanız bunların hiçbiri gerçekleşmez.']),
  ('Çocuklar', ['Junbi, çocuklar dahil hiç kimseden bilerek kişisel bilgi toplamaz. Oyunda sohbet, profil veya kişisel bilgi paylaşma yolu yoktur.']),
  ('Değişiklikler', ['Bu politika değişirse yeni sürüm bu sayfada yeni bir tarihle yayımlanır.']),
  ('İletişim', ['Gizlilikle ilgili sorular: {mail}.']),
 ], unity_label='Unity Gizlilik Politikası',
 sup_title='Destek', sup_intro='Junbi ile ilgili yardıma mı ihtiyacınız var? Bize yazın, en kısa sürede yanıtlayalım.', sup_mail='E-posta', sup_faq='Sık sorulan sorular',
 faq=[
  ('Arkadaşımla çevrimiçi nasıl oynarım?', '“Arkadaşla” bölümünü açın. Bir oyuncu maç oluşturup kısa kodu paylaşır, diğeri kodu girer. İki cihazın da internete ihtiyacı vardır.'),
  ('Arkadaş kodu çalışmıyor.', 'Kodun tam olarak yazıldığından ve yakın zamanda oluşturulduğundan emin olun. Yine olmazsa yeni bir maç oluşturup yeni kodu paylaşın. Ağı değiştirmek (Wi-Fi veya hücresel) bazen yardımcı olur.'),
  ('İlerlememi başka bir cihaza taşıyabilir miyim?', 'İlerleme yalnızca cihazda saklanır. Hesap veya bulut senkronizasyonu yoktur; bu yüzden otomatik taşınamaz ve uygulamayı silmek onu siler.'),
  ('Dili nasıl değiştiririm?', 'Ana menüde Ayarlar’ı açın ve listeden bir dil seçin.'),
  ('Sorunu nasıl bildiririm?', 'Bize cihaz modelinizi, sistem sürümünüzü ve kısa bir açıklama gönderin. Ekran görüntüsü yardımcı olur.'),
 ], more_priv='Oyun hangi verileri kullanır? Gizlilik Politikası’nı okuyun.', lang_label='Dil',
)

L['ar'] = dict(
 dir='rtl', name='Junbi', tag='التايكوندو الأولمبي', home='الرئيسية', privacy='سياسة الخصوصية', support='الدعم', updated='آخر تحديث: 25 نوفمبر 2026',
 lead='Junbi لعبة تايكوندو وفق قواعد الاتحاد العالمي للتايكوندو: أدوات حماية إلكترونية، ثلاث جولات، مقاتلون من بلدان مختلفة وتقنية ركلات واقعية.',
 features=['البطولة والتصنيف العالمي والتدريب مع مدرب ونزال سريع', 'نزال عبر الإنترنت ضد صديق برمز قصير', 'مقاتلون من بلدان مختلفة، ولكل منهم تركيبته المميزة', 'بلا حساب وبلا إعلانات وبلا تتبع'],
 priv_title='سياسة الخصوصية', priv_intro='توضح هذه السياسة كيف يتعامل تطبيق Junbi: التايكوندو الأولمبي (من Notemia) مع بياناتك.',
 sections=[
  ('باختصار', ['لا يطلب Junbi منك إنشاء حساب. لا توجد إعلانات ولا تحليلات ولا تتبع ولا مشتريات داخل التطبيق. لا تجمع Notemia أي بيانات شخصية عنك ولا تخزنها ولا تبيعها.']),
  ('ما يبقى على جهازك', ['يُحفظ تقدمك وإعداداتك والمقاتل الذي اخترته والتصنيف والإعادات المحفوظة على جهازك فقط. لا يمكننا رؤيتها. وحذف التطبيق يحذفها.']),
  ('نزال ضد صديق (اختياري)', ['لا يبدأ اللعب عبر الإنترنت إلا إذا اخترته. لربط لاعبين تستخدم اللعبة خدمات Unity Gaming Services (Authentication وRelay) التي تقدمها Unity Technologies. عندها تنشئ Unity معرّف لاعب مجهولًا وتصدر رمز انضمام قصيرًا وتعالج بيانات الشبكة مثل عنوان IP لربطك بصديقك ونقل النزال بين جهازيكما. لا تتلقى Notemia هذه البيانات ولا تخزنها. وتوضح {unity} كيف تتعامل Unity معها.', 'إذا لم تستخدم النزال ضد صديق فلن يحدث شيء من ذلك.']),
  ('الأطفال', ['لا يجمع Junbi عن علم معلومات شخصية من أي شخص، بمن فيهم الأطفال. ولا توجد في اللعبة دردشة ولا ملفات شخصية ولا وسيلة لمشاركة المعلومات الشخصية.']),
  ('التغييرات', ['إذا تغيرت هذه السياسة فستُنشر النسخة الجديدة في هذه الصفحة بتاريخ جديد.']),
  ('التواصل', ['أسئلة الخصوصية: {mail}.']),
 ], unity_label='سياسة الخصوصية لدى Unity',
 sup_title='الدعم', sup_intro='هل تحتاج مساعدة في Junbi؟ راسلنا وسنرد في أقرب وقت.', sup_mail='البريد', sup_faq='أسئلة شائعة',
 faq=[
  ('كيف ألعب عبر الإنترنت ضد صديق؟', 'افتح «مع صديق». ينشئ أحد اللاعبين مباراة ويشارك الرمز القصير ويدخله الآخر. يحتاج الجهازان إلى اتصال بالإنترنت.'),
  ('رمز الصديق لا يعمل.', 'تأكد من كتابة الرمز كما هو وأنه أُنشئ حديثًا. وإن استمرت المشكلة فأنشئ مباراة جديدة وشارك الرمز الجديد. وأحيانًا يفيد تغيير الشبكة (واي فاي أو بيانات الجوال).'),
  ('هل يمكنني نقل تقدمي إلى جهاز آخر؟', 'يُحفظ التقدم على الجهاز فقط. لا يوجد حساب ولا مزامنة سحابية، لذلك لا يمكن نقله تلقائيًا، وحذف التطبيق يمحوه.'),
  ('كيف أغيّر اللغة؟', 'افتح الإعدادات من القائمة الرئيسية واختر لغة من القائمة.'),
  ('كيف أبلغ عن مشكلة؟', 'أرسل لنا طراز جهازك وإصدار النظام ووصفًا مختصرًا لما حدث. ولقطة الشاشة تفيد.'),
 ], more_priv='ما البيانات التي تستخدمها اللعبة؟ اقرأ سياسة الخصوصية.', lang_label='اللغة',
)

L['ko'] = dict(
 name='Junbi', tag='올림픽 태권도', home='홈', privacy='개인정보 처리방침', support='지원', updated='최종 업데이트: 2026년 11월 25일',
 lead='Junbi는 월드태권도(WT) 규칙으로 즐기는 태권도 게임입니다. 전자 호구, 3라운드, 여러 나라의 선수, 사실적인 발차기 기술을 담았습니다.',
 features=['챔피언십, 세계 랭킹, 코치와 함께하는 훈련, 빠른 단판 경기', '짧은 코드로 친구와 온라인 대결', '나라별 선수, 선수마다 고유한 콤보', '계정 없음, 광고 없음, 추적 없음'],
 priv_title='개인정보 처리방침', priv_intro='이 방침은 앱 Junbi: 올림픽 태권도(Notemia)가 여러분의 데이터를 어떻게 다루는지 설명합니다.',
 sections=[
  ('요약', ['Junbi는 계정 생성을 요구하지 않습니다. 광고, 분석, 추적, 인앱 결제가 없습니다. Notemia는 여러분에 대한 어떤 개인정보도 수집, 저장, 판매하지 않습니다.']),
  ('기기에 남는 정보', ['진행 상황, 설정, 선택한 선수, 랭킹, 저장한 리플레이는 여러분의 기기에만 저장됩니다. 저희는 볼 수 없습니다. 앱을 삭제하면 함께 삭제됩니다.']),
  ('친구와 대결 (선택)', ['온라인 플레이는 여러분이 선택할 때만 시작됩니다. 두 플레이어를 연결하기 위해 게임은 Unity Technologies의 Unity Gaming Services(Authentication 및 Relay)를 사용합니다. 이때 Unity는 익명 플레이어 ID를 만들고 짧은 참가 코드를 발급하며, 친구와 연결하고 기기 간에 경기를 전달하기 위해 IP 주소 같은 네트워크 데이터를 처리합니다. Notemia는 이 데이터를 받거나 저장하지 않습니다. Unity가 이를 처리하는 방식은 {unity}에 설명되어 있습니다.', '친구와 대결을 사용하지 않으면 위의 일은 일어나지 않습니다.']),
  ('어린이', ['Junbi는 어린이를 포함해 누구로부터도 개인정보를 고의로 수집하지 않습니다. 게임에는 채팅, 프로필, 개인정보를 공유할 방법이 없습니다.']),
  ('방침 변경', ['방침이 바뀌면 새 버전이 새 날짜와 함께 이 페이지에 게시됩니다.']),
  ('문의', ['개인정보 관련 문의: {mail}.']),
 ], unity_label='Unity 개인정보 처리방침',
 sup_title='지원', sup_intro='Junbi에 도움이 필요하신가요? 메일을 보내 주시면 최대한 빨리 답변드리겠습니다.', sup_mail='이메일', sup_faq='자주 묻는 질문',
 faq=[
  ('친구와 온라인으로 어떻게 대결하나요?', '“친구와”를 엽니다. 한 사람이 경기를 만들어 짧은 코드를 공유하고, 상대가 그 코드를 입력합니다. 두 기기 모두 인터넷이 필요합니다.'),
  ('친구 코드가 작동하지 않습니다.', '코드를 정확히 입력했는지, 최근에 만든 코드인지 확인하세요. 계속 안 되면 새 경기를 만들어 새 코드를 공유하세요. 네트워크(Wi-Fi 또는 모바일)를 바꾸면 도움이 될 때가 있습니다.'),
  ('진행 상황을 다른 기기로 옮길 수 있나요?', '진행 상황은 기기에만 저장됩니다. 계정이나 클라우드 동기화가 없어 자동으로 옮길 수 없으며, 앱을 삭제하면 지워집니다.'),
  ('언어는 어떻게 바꾸나요?', '메인 메뉴에서 설정을 열고 목록에서 언어를 선택하세요.'),
  ('문제는 어떻게 알리나요?', '기기 모델, 시스템 버전, 간단한 설명을 메일로 보내 주세요. 스크린샷이 도움이 됩니다.'),
 ], more_priv='게임은 어떤 데이터를 사용하나요? 개인정보 처리방침을 읽어 보세요.', lang_label='언어',
)

L['zh-hans'] = dict(
 name='Junbi', tag='奥林匹克跆拳道', home='首页', privacy='隐私政策', support='支持', updated='最后更新：2026年11月25日',
 lead='Junbi 是一款按世界跆拳道联盟规则进行的跆拳道游戏：电子护具、三个回合、来自不同国家的选手，以及逼真的踢击技术。',
 features=['锦标赛、世界排名、教练训练和快速单场比赛', '通过短代码与好友在线对战', '来自不同国家的选手，各有招牌连招', '无需账号、没有广告、不做追踪'],
 priv_title='隐私政策', priv_intro='本政策说明应用 Junbi：奥林匹克跆拳道（Notemia）如何处理你的数据。',
 sections=[
  ('简而言之', ['Junbi 不要求你创建账号。没有广告、分析、追踪，也没有应用内购买。Notemia 不会收集、存储或出售任何与你有关的个人数据。']),
  ('留在你设备上的内容', ['你的进度、设置、所选选手、排名和已保存的回放只存储在你的设备上，我们无法查看。删除应用即会删除这些内容。']),
  ('与好友对战（可选）', ['只有当你选择时才会开始在线游戏。为连接两位玩家，游戏使用 Unity Technologies 提供的 Unity Gaming Services（Authentication 和 Relay）。此时 Unity 会创建匿名玩家 ID、发放短加入代码，并处理 IP 地址等网络数据，以便把你与好友连接起来并在你们的设备之间传递比赛。Notemia 不会接收或存储这些数据。Unity 如何处理这些数据，请见{unity}。', '如果你从不使用“与好友对战”，以上这些都不会发生。']),
  ('儿童', ['Junbi 不会有意收集任何人（包括儿童）的个人信息。游戏中没有聊天、个人资料，也无法分享个人信息。']),
  ('政策变更', ['如本政策有变更，新版本将连同新日期发布在此页面。']),
  ('联系我们', ['隐私相关问题：{mail}。']),
 ], unity_label='Unity 隐私政策',
 sup_title='支持', sup_intro='需要 Junbi 方面的帮助？给我们写信，我们会尽快回复。', sup_mail='邮箱', sup_faq='常见问题',
 faq=[
  ('如何与好友在线对战？', '打开“与好友”。一位玩家创建比赛并分享短代码，另一位输入该代码。两台设备都需要联网。'),
  ('好友代码无法使用。', '请确认代码输入准确且是刚刚创建的。仍不行就新建一场比赛并分享新代码。有时切换网络（Wi-Fi 或蜂窝）会有帮助。'),
  ('可以把进度转移到另一台设备吗？', '进度只保存在设备上。没有账号或云同步，因此无法自动转移，删除应用会清除进度。'),
  ('如何切换语言？', '在主菜单中打开“设置”，从列表中选择语言。'),
  ('如何反馈问题？', '请把设备型号、系统版本和简短描述发给我们，附上截图更有帮助。'),
 ], more_priv='游戏使用哪些数据？请阅读隐私政策。', lang_label='语言',
)

L['zh-hant'] = dict(
 name='Junbi', tag='奧林匹克跆拳道', home='首頁', privacy='隱私權政策', support='支援', updated='最後更新：2026年11月25日',
 lead='Junbi 是一款依世界跆拳道聯盟規則進行的跆拳道遊戲：電子護具、三個回合、來自不同國家的選手，以及逼真的踢擊技術。',
 features=['錦標賽、世界排名、教練訓練與快速單場比賽', '透過短代碼與好友線上對戰', '來自不同國家的選手，各有招牌連招', '無需帳號、沒有廣告、不做追蹤'],
 priv_title='隱私權政策', priv_intro='本政策說明應用程式 Junbi：奧林匹克跆拳道（Notemia）如何處理你的資料。',
 sections=[
  ('簡而言之', ['Junbi 不要求你建立帳號。沒有廣告、分析、追蹤，也沒有應用程式內購買。Notemia 不會蒐集、儲存或出售任何與你有關的個人資料。']),
  ('留在你裝置上的內容', ['你的進度、設定、所選選手、排名與已儲存的重播只儲存在你的裝置上，我們無法查看。刪除應用程式即會刪除這些內容。']),
  ('與好友對戰（選用）', ['只有在你選擇時才會開始線上遊戲。為連接兩位玩家，遊戲使用 Unity Technologies 提供的 Unity Gaming Services（Authentication 與 Relay）。此時 Unity 會建立匿名玩家 ID、發出短加入代碼，並處理 IP 位址等網路資料，以便把你與好友連線並在你們的裝置之間傳遞比賽。Notemia 不會接收或儲存這些資料。Unity 如何處理這些資料，請見{unity}。', '如果你從不使用「與好友對戰」，以上這些都不會發生。']),
  ('兒童', ['Junbi 不會刻意蒐集任何人（包括兒童）的個人資訊。遊戲中沒有聊天、個人檔案，也無法分享個人資訊。']),
  ('政策變更', ['若本政策有變更，新版本將連同新日期發布於此頁面。']),
  ('聯絡我們', ['隱私相關問題：{mail}。']),
 ], unity_label='Unity 隱私權政策',
 sup_title='支援', sup_intro='需要 Junbi 方面的協助？寫信給我們，我們會盡快回覆。', sup_mail='電子郵件', sup_faq='常見問題',
 faq=[
  ('如何與好友線上對戰？', '開啟「與好友」。一位玩家建立比賽並分享短代碼，另一位輸入該代碼。兩台裝置都需要連線網際網路。'),
  ('好友代碼無法使用。', '請確認代碼輸入正確且是剛建立的。仍不行就建立新比賽並分享新代碼。有時切換網路（Wi-Fi 或行動網路）會有幫助。'),
  ('可以把進度轉移到另一台裝置嗎？', '進度只儲存在裝置上。沒有帳號或雲端同步，因此無法自動轉移，刪除應用程式會清除進度。'),
  ('如何切換語言？', '在主選單中開啟「設定」，從清單中選擇語言。'),
  ('如何回報問題？', '請把裝置型號、系統版本與簡短描述寄給我們，附上螢幕截圖更有幫助。'),
 ], more_priv='遊戲使用哪些資料？請閱讀隱私權政策。', lang_label='語言',
)
