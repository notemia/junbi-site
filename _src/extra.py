# Additions of 2026-11-27 to the privacy policy and support pages: the full-game purchase and Game Center (version 1.0.2).
# short: the new "short version" paragraph (the old one said "no in-app purchases"); buy, gc: (heading, paragraph) inserted after
# "What stays on your device"; restore: (question, answer) added to the support FAQ. build.py merges this into langs.L.
X = {}

X['en'] = dict(
 short='Junbi does not ask you to create an account. It has no advertising, no analytics and no tracking. Notemia does not collect, store or sell any personal data about you.',
 buy=('The full game', 'Junbi is free to download; the full game is one in-app purchase. It is made and billed by Apple through your Apple Account. We never see your name, Apple Account or payment details: the app only learns from the App Store whether the full game was bought, so it can unlock it and restore it on your other devices.'),
 gc=('Game Center (optional)', 'If you are signed in to Game Center, the game sends your ranking points, number of wins and achievements to Apple Game Center, where they appear in its leaderboards and achievements under your Game Center profile. Apple handles this under its own privacy policy; Notemia does not receive your Game Center profile. You can turn Game Center off in the settings of your device.'),
 restore=('I bought the full game. How do I get it on another device?', 'Sign in with the same Apple Account, open any locked mode and tap “Restore purchase”.'),
)
X['ru'] = dict(
 short='Junbi не просит создавать аккаунт. В игре нет рекламы, аналитики и слежения. Notemia не собирает, не хранит и не продаёт никаких персональных данных о вас.',
 buy=('Полная игра', 'Junbi скачивается бесплатно, полная игра — одна встроенная покупка. Её проводит и оплачивает Apple через ваш Apple Account. Мы не видим ни вашего имени, ни Apple Account, ни платёжных данных: приложение узнаёт от App Store только то, куплена ли полная игра, чтобы открыть её и восстановить на других ваших устройствах.'),
 gc=('Game Center (по желанию)', 'Если вы вошли в Game Center, игра отправляет в Apple Game Center очки рейтинга, число побед и достижения, и они появляются в его таблицах и достижениях под вашим профилем Game Center. Apple обрабатывает их по своей политике конфиденциальности; Notemia ваш профиль Game Center не получает. Game Center можно выключить в настройках устройства.'),
 restore=('Я купил полную игру. Как получить её на другом устройстве?', 'Войдите с тем же Apple Account, откройте любой закрытый режим и нажмите «Восстановить покупку».'),
)
X['fr'] = dict(
 short='Junbi ne vous demande pas de créer de compte. Il n’y a ni publicité, ni analyse, ni suivi. Notemia ne collecte, ne conserve et ne vend aucune donnée personnelle vous concernant.',
 buy=('Le jeu complet', 'Junbi se télécharge gratuitement ; le jeu complet est un achat intégré unique. Il est effectué et facturé par Apple via votre compte Apple. Nous ne voyons jamais votre nom, votre compte Apple ni vos données de paiement : l’application apprend seulement de l’App Store si le jeu complet a été acheté, afin de le débloquer et de le restaurer sur vos autres appareils.'),
 gc=('Game Center (facultatif)', 'Si vous êtes connecté à Game Center, le jeu envoie vos points de classement, votre nombre de victoires et vos succès à Apple Game Center, où ils apparaissent dans ses classements et succès sous votre profil Game Center. Apple les traite selon sa propre politique de confidentialité ; Notemia ne reçoit pas votre profil Game Center. Vous pouvez désactiver Game Center dans les réglages de votre appareil.'),
 restore=('J’ai acheté le jeu complet. Comment l’obtenir sur un autre appareil ?', 'Connectez-vous avec le même compte Apple, ouvrez un mode verrouillé et touchez « Restaurer l’achat ».'),
)
X['de'] = dict(
 short='Junbi verlangt kein Konto. Es gibt keine Werbung, keine Analyse und kein Tracking. Notemia erhebt, speichert und verkauft keine personenbezogenen Daten über dich.',
 buy=('Das volle Spiel', 'Junbi ist kostenlos; das volle Spiel ist ein einmaliger In-App-Kauf. Er wird von Apple über deinen Apple Account abgewickelt und abgerechnet. Wir sehen weder deinen Namen noch deinen Apple Account oder deine Zahlungsdaten: Die App erfährt vom App Store nur, ob das volle Spiel gekauft wurde, um es freizuschalten und auf deinen anderen Geräten wiederherzustellen.'),
 gc=('Game Center (optional)', 'Wenn du bei Game Center angemeldet bist, sendet das Spiel deine Ranglistenpunkte, die Zahl deiner Siege und deine Erfolge an Apple Game Center, wo sie in dessen Bestenlisten und Erfolgen unter deinem Game-Center-Profil erscheinen. Apple verarbeitet sie nach seiner eigenen Datenschutzrichtlinie; Notemia erhält dein Game-Center-Profil nicht. Du kannst Game Center in den Einstellungen deines Geräts ausschalten.'),
 restore=('Ich habe das volle Spiel gekauft. Wie bekomme ich es auf ein anderes Gerät?', 'Melde dich mit demselben Apple Account an, öffne einen gesperrten Modus und tippe auf „Kauf wiederherstellen“.'),
)
X['es'] = dict(
 short='Junbi no te pide crear una cuenta. No tiene publicidad, analítica ni seguimiento. Notemia no recopila, guarda ni vende ningún dato personal sobre ti.',
 buy=('El juego completo', 'Junbi se descarga gratis; el juego completo es una única compra dentro de la app. La realiza y la cobra Apple a través de tu cuenta de Apple. Nunca vemos tu nombre, tu cuenta de Apple ni tus datos de pago: la app solo sabe por el App Store si el juego completo está comprado, para desbloquearlo y restaurarlo en tus otros dispositivos.'),
 gc=('Game Center (opcional)', 'Si has iniciado sesión en Game Center, el juego envía tus puntos de clasificación, tu número de victorias y tus logros a Apple Game Center, donde aparecen en sus clasificaciones y logros con tu perfil de Game Center. Apple los trata según su propia política de privacidad; Notemia no recibe tu perfil de Game Center. Puedes desactivar Game Center en los ajustes del dispositivo.'),
 restore=('Compré el juego completo. ¿Cómo lo tengo en otro dispositivo?', 'Inicia sesión con la misma cuenta de Apple, abre cualquier modo bloqueado y toca «Restaurar compra».'),
)
X['pt-br'] = dict(
 short='O Junbi não pede para você criar uma conta. Não tem publicidade, análise nem rastreamento. A Notemia não coleta, não armazena e não vende nenhum dado pessoal sobre você.',
 buy=('O jogo completo', 'O Junbi é gratuito para baixar; o jogo completo é uma única compra dentro do app. Ela é feita e cobrada pela Apple através da sua Conta Apple. Nunca vemos seu nome, sua Conta Apple nem seus dados de pagamento: o app só sabe pela App Store se o jogo completo foi comprado, para desbloqueá-lo e restaurá-lo nos seus outros dispositivos.'),
 gc=('Game Center (opcional)', 'Se você estiver conectado ao Game Center, o jogo envia seus pontos de ranking, seu número de vitórias e suas conquistas para o Apple Game Center, onde aparecem nas classificações e conquistas dele no seu perfil do Game Center. A Apple os trata de acordo com a própria política de privacidade; a Notemia não recebe seu perfil do Game Center. Você pode desativar o Game Center nos ajustes do dispositivo.'),
 restore=('Comprei o jogo completo. Como tê-lo em outro dispositivo?', 'Entre com a mesma Conta Apple, abra qualquer modo bloqueado e toque em “Restaurar compra”.'),
)
X['pl'] = dict(
 short='Junbi nie wymaga zakładania konta. Nie ma reklam, analityki ani śledzenia. Notemia nie zbiera, nie przechowuje i nie sprzedaje żadnych Twoich danych osobowych.',
 buy=('Pełna gra', 'Junbi można pobrać za darmo; pełna gra to jeden zakup w aplikacji. Realizuje go i rozlicza Apple przez Twoje konto Apple. Nigdy nie widzimy Twojego imienia, konta Apple ani danych płatności: aplikacja dowiaduje się od App Store tylko tego, czy pełna gra została kupiona, aby ją odblokować i przywrócić na innych Twoich urządzeniach.'),
 gc=('Game Center (opcjonalnie)', 'Jeśli jesteś zalogowany w Game Center, gra wysyła Twoje punkty rankingowe, liczbę zwycięstw i osiągnięcia do Apple Game Center, gdzie pojawiają się w jego rankingach i osiągnięciach w Twoim profilu Game Center. Apple przetwarza je zgodnie z własną polityką prywatności; Notemia nie otrzymuje Twojego profilu Game Center. Game Center możesz wyłączyć w ustawieniach urządzenia.'),
 restore=('Kupiłem pełną grę. Jak mieć ją na innym urządzeniu?', 'Zaloguj się tym samym kontem Apple, otwórz dowolny zablokowany tryb i stuknij „Przywróć zakup”.'),
)
X['tr'] = dict(
 short='Junbi hesap açmanızı istemez. Reklam, analiz ve takip yoktur. Notemia sizinle ilgili hiçbir kişisel veriyi toplamaz, saklamaz ve satmaz.',
 buy=('Tam oyun', 'Junbi ücretsiz indirilir; tam oyun tek bir uygulama içi satın alımdır. Satın alma Apple tarafından Apple Hesabınız üzerinden yapılır ve ücretlendirilir. Adınızı, Apple Hesabınızı veya ödeme bilgilerinizi asla görmeyiz: uygulama App Store’dan yalnızca tam oyunun satın alınıp alınmadığını öğrenir; böylece onu açabilir ve diğer cihazlarınızda geri yükleyebilir.'),
 gc=('Game Center (isteğe bağlı)', 'Game Center’a giriş yaptıysanız oyun sıralama puanlarınızı, galibiyet sayınızı ve başarılarınızı Apple Game Center’a gönderir; bunlar Game Center profilinizle onun sıralamalarında ve başarılarında görünür. Apple bunları kendi gizlilik politikasına göre işler; Notemia Game Center profilinizi almaz. Game Center’ı cihazınızın ayarlarından kapatabilirsiniz.'),
 restore=('Tam oyunu satın aldım. Başka bir cihazda nasıl kullanırım?', 'Aynı Apple Hesabı ile giriş yapın, kilitli bir modu açın ve “Satın alımı geri yükle”ye dokunun.'),
)
X['ar'] = dict(
 short='لا يطلب منك Junbi إنشاء حساب. لا توجد إعلانات ولا تحليلات ولا تتبّع. لا تجمع Notemia أي بيانات شخصية عنك ولا تخزّنها ولا تبيعها.',
 buy=('اللعبة الكاملة', 'تنزيل Junbi مجاني، واللعبة الكاملة عملية شراء واحدة داخل التطبيق. تتم عملية الشراء ويُحصَّل ثمنها عن طريق Apple من خلال حساب Apple الخاص بك. لا نرى أبدًا اسمك ولا حساب Apple ولا بيانات الدفع: يعرف التطبيق من App Store فقط ما إذا كانت اللعبة الكاملة قد اشتُريت، ليفتحها ويستعيدها على أجهزتك الأخرى.'),
 gc=('Game Center (اختياري)', 'إذا كنت مسجّلًا الدخول إلى Game Center، ترسل اللعبة نقاط التصنيف وعدد الانتصارات والإنجازات إلى Apple Game Center، فتظهر في لوحات الصدارة والإنجازات فيه باسم ملفك في Game Center. تعالج Apple هذه البيانات وفق سياسة الخصوصية الخاصة بها، ولا تتلقى Notemia ملفك في Game Center. يمكنك إيقاف Game Center من إعدادات جهازك.'),
 restore=('اشتريت اللعبة الكاملة. كيف أحصل عليها على جهاز آخر؟', 'سجّل الدخول بحساب Apple نفسه، وافتح أي وضع مقفل، ثم اضغط «استعادة الشراء».'),
)
X['ko'] = dict(
 short='Junbi는 계정을 만들라고 요구하지 않습니다. 광고, 분석, 추적이 없습니다. Notemia는 귀하에 관한 어떤 개인 정보도 수집, 저장 또는 판매하지 않습니다.',
 buy=('정식 게임', 'Junbi는 무료로 다운로드할 수 있으며, 정식 게임은 한 번의 앱 내 구입입니다. 구입과 결제는 Apple이 귀하의 Apple 계정을 통해 처리합니다. 저희는 귀하의 이름, Apple 계정, 결제 정보를 볼 수 없습니다. 앱은 정식 게임을 잠금 해제하고 다른 기기에서 복원하기 위해 App Store에서 구입 여부만 확인합니다.'),
 gc=('Game Center (선택)', 'Game Center에 로그인되어 있으면 게임은 랭킹 점수, 승리 횟수, 도전 과제를 Apple Game Center로 보내며, 이는 귀하의 Game Center 프로필로 리더보드와 도전 과제에 표시됩니다. Apple은 이를 자체 개인정보 처리방침에 따라 처리하며, Notemia는 귀하의 Game Center 프로필을 받지 않습니다. 기기 설정에서 Game Center를 끌 수 있습니다.'),
 restore=('정식 게임을 구입했습니다. 다른 기기에서는 어떻게 하나요?', '같은 Apple 계정으로 로그인한 뒤 잠긴 모드를 열고 ‘구매 복원’을 누르세요.'),
)
X['zh-hans'] = dict(
 short='Junbi 不要求你创建账户。没有广告、没有分析、没有跟踪。Notemia 不收集、不存储、也不出售任何关于你的个人数据。',
 buy=('完整版游戏', 'Junbi 可免费下载，完整版游戏为一次性 App 内购买。购买由 Apple 通过你的 Apple 账户完成并收费。我们永远看不到你的姓名、Apple 账户或付款信息：App 只从 App Store 得知是否已购买完整版，以便解锁并在你的其他设备上恢复。'),
 gc=('Game Center（可选）', '如果你已登录 Game Center，游戏会将你的排名积分、胜场数和成就发送到 Apple Game Center，并以你的 Game Center 资料显示在其排行榜和成就中。Apple 按照其自身的隐私政策处理这些数据；Notemia 不会获得你的 Game Center 资料。你可以在设备的设置中关闭 Game Center。'),
 restore=('我买了完整版游戏，怎样在另一台设备上使用？', '使用同一个 Apple 账户登录，打开任一锁定的模式，然后轻点“恢复购买”。'),
)
X['zh-hant'] = dict(
 short='Junbi 不要求你建立帳號。沒有廣告、沒有分析、沒有追蹤。Notemia 不會收集、儲存或出售任何關於你的個人資料。',
 buy=('完整版遊戲', 'Junbi 可免費下載，完整版遊戲為一次性 App 內購買。購買由 Apple 透過你的 Apple 帳號完成並收費。我們永遠看不到你的姓名、Apple 帳號或付款資訊：App 只從 App Store 得知是否已購買完整版，以便解鎖並在你的其他裝置上恢復。'),
 gc=('Game Center（選用）', '如果你已登入 Game Center，遊戲會將你的排名積分、勝場數和成就傳送到 Apple Game Center，並以你的 Game Center 個人資料顯示在其排行榜和成就中。Apple 依其自身的隱私權政策處理這些資料；Notemia 不會取得你的 Game Center 個人資料。你可以在裝置的設定中關閉 Game Center。'),
 restore=('我買了完整版遊戲，要怎麼在另一台裝置上使用？', '使用同一個 Apple 帳號登入，打開任一鎖定的模式，然後點一下「恢復購買」。'),
)
