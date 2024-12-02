# Mendefinisikan karakter
define b = Character("Bima", image="characters/MC_Default.png")
define ibu = Character("Ibunda Bima", color="#ff9999")
define pe = Character("Politisi Senior A", color="#9999ff")
define ps = Character("Politisi Senior B", color="#6666cc")
define asisten = Character("Asisten Parlemen", color="#66cc66")
define mp = Character("Anggota Parlemen Muda", color="#ffcc00")
define bp = Character("Buruh", color="#cc9966")
define bu = Character("Buruh Senior", color="#9966cc")
define be = Character("Buruh E", color="#cc6666")

#Character expressions
image b default = "characters/MC_Default.png"
image b happy = "characters/MC_Happy.png"
image b angry = "characters/MC_angry"
image b worried = "characters/MC_worried"

# Background Definitions'
image bg parliament_hall = im.Scale("backgrounds/parliament_chamber.jpg", 1920, 1080)
image bg bima_office_sore = im.Scale("backgrounds/bima_office_sore.jpg", 1920, 1080)
image bg bima_office_pagi = im.Scale("backgrounds/bima_office_pagi.jpg", 1920, 1080)


# Scene pertama dengan background
label start:

    # Scene 1: Rumah Bima - Refleksi Masa Lalu
    scene bg living_room with fade  # Background: ruang tamu
    show b default at Position(xpos=0.3, ypos=2.0) with dissolve

    "Di malam yang tenang, Bima duduk di depan meja. Pikirannya melayang ke masa lalu—sebuah masa penuh luka dan kehilangan yang membentuk dirinya hingga hari ini."
    
    # Flashback ke masa lalu
    show bg small_village with dissolve  # Background: pemukiman kecil
    ibu "Cepat, Bima! Kita harus keluar sebelum mereka datang!"
    b "Tapi Ibu, kenapa kita harus pergi? Ini rumah kita!"
    "Bima muda tidak pernah melupakan malam itu—malam di mana keluarganya kehilangan segalanya karena keputusan segelintir orang di atas."
    
    # Kembali ke masa kini
    show bg living_room with fade
    b "Ayah, malam itu aku tidak bisa melakukan apa-apa. Tapi sekarang aku punya kesempatan untuk melawan mereka yang mengambil segalanya dari kita."

    # Scene 2: Kantor Parlemen - Hari Pertama Bima
    scene bg parliament_office at truecenter with dissolve # Background: kantor parlemen
    "Hari pertama di parlemen. Bima tahu, ini bukan hanya pekerjaan. Ini adalah perjuangan untuk mereka yang tidak memiliki suara."
    asisten "Pak Bima, selamat datang. Rapat pertama Anda akan dimulai dalam satu jam. Semua anggota sudah tidak sabar mendengar ide-ide segar Anda."
    b "Terima kasih. Saya akan memastikan mereka mendengar apa yang perlu mereka dengar."

    # Scene 3: Sidang Parlemen - Idealisme yang Ditantang
    scene bg parliament_chamber at truecenter with dissolve # Background: ruang sidang
    show b with dissolve
    pe "Saudara Bima, itu pidato yang indah. Tapi izinkan saya bertanya: apakah Anda tahu betapa sulitnya membawa perubahan dalam sistem yang sudah mapan ini?"
    
    menu:
        "Menjawab dengan sopan namun percaya diri":
            b "Saya mengerti bahwa perubahan itu sulit. Tapi saya percaya, setiap langkah kecil bisa membawa kita ke arah yang lebih baik. Saya di sini untuk memulai langkah itu."
            pe "Hmph, langkah kecil tidak akan berarti apa-apa jika Anda tidak memiliki dukungan yang cukup."
            b "Dukungan? Kalau begitu, aku harus membuktikan diriku terlebih dahulu."
        
        "Menegaskan pendapat dengan berani":
            b "Sistem ini mapan, tapi tidak sempurna. Tugas kita bukan untuk menerima kenyataan, melainkan untuk memperbaikinya. Saya yakin, jika kita bekerja sama, kita bisa membawa perubahan."
            pe "Berani sekali bicara seperti itu di hari pertama Anda. Kita lihat apakah Anda masih bisa bicara besar setelah satu tahun di sini."
            b "Mungkin aku baru di sini, tapi aku tidak akan membiarkan intimidasi menghentikan langkahku."

    # Debat Parlemen: Kebijakan Tenaga Kerja
    ps "Rancangan ini penting untuk meningkatkan daya saing tenaga kerja kita di pasar internasional. Fleksibilitas jam kerja dan efisiensi tenaga kerja akan memberikan keuntungan besar bagi ekonomi kita."
    b "Keuntungan ekonomi? Bagaimana dengan nasib para buruh yang jam kerjanya diperpanjang tanpa perlindungan?"
    
    menu:
        "Memprotes langsung rancangan tersebut dengan argumen yang tajam":
            b "Maaf, tapi saya tidak bisa mendukung rancangan ini. Apakah kita mempertimbangkan bagaimana fleksibilitas ini akan mempengaruhi para buruh? Mereka sudah bekerja terlalu keras untuk upah yang tidak layak. Menambah jam kerja hanya akan memperburuk keadaan mereka."
            ps "Saudara Bima, ini bukan hanya tentang buruh. Ini tentang ekonomi negara kita. Jika buruh tidak kompetitif, siapa yang akan berinvestasi di sini?"
            b "Dan apa gunanya investasi jika masyarakat yang kita wakili hidup dalam penderitaan? Prioritas kita harus selalu rakyat, bukan angka di laporan ekonomi."

        "Mengajukan pertanyaan untuk menggiring diskusi ke isu buruh":
            b "Saya punya pertanyaan. Bagaimana rancangan ini memastikan bahwa hak buruh tetap terlindungi? Apakah ada mekanisme untuk mencegah eksploitasi tenaga kerja?"
            ps "Hmm, tentu saja, ada regulasi tambahan yang akan kita bahas nanti. Tapi fokus kita sekarang adalah pada daya saing."
            b "Kalau begitu, saya berharap pembahasan itu menjadi prioritas. Daya saing tidak ada artinya jika tenaga kerja kita diperlakukan seperti mesin tanpa batas."

    # Scene 4: Ruang Kerja Bima - Penemuan Masalah Awal
    scene bg bima_office_sore with fade  # Background: ruang kerja Bima
    show b with dissolve
    b "Hari pertama setelah sidang penuh tantangan, Bima kembali ke ruang kerjanya. Di sini, ia mulai menelaah laporan-laporan yang disampaikan oleh masyarakat. Setiap lembar laporan adalah gambaran tentang ketidakadilan yang masih terjadi di luar sana."
    b "Gaji di bawah standar, jam kerja panjang, dan tidak ada jaminan perlindungan bagi pekerja. Bahkan, laporan ini menyebutkan beberapa pekerja dipecat karena mencoba menyuarakan hak mereka. Ini tidak bisa dibiarkan."
    b "Saya akan menghubungi tim konstituen di daerah asal saya."

    # Diskusi dengan Tim Konstituen
    bp "Pak Bima, terima kasih sudah meluangkan waktu untuk kami. Saya bekerja di pabrik itu hampir 10 tahun. Belakangan ini, kondisi kami semakin buruk. Jam kerja bertambah, tapi gaji tetap kecil. Beberapa teman saya bahkan dipecat setelah mencoba mengajukan protes."
    b "Saya mendengar masalah ini dari laporan. Tapi saya ingin memastikan, apa Anda memiliki bukti, atau ada orang lain yang bisa mendukung cerita ini?"
    bp "Kami punya dokumen slip gaji dan daftar jam kerja yang tidak sesuai dengan kontrak. Tapi kalau kami ketahuan, risikonya terlalu besar. Tolong bantu kami, Pak."
    b "Tenang. Saya akan datang ke tempat Anda dalam beberapa hari. Kita akan bertemu secara aman dan mendiskusikan ini lebih jauh."

    # Scene 5: Pabrik Buruh - Investigasi Awal
    scene bg industrial_area with fade  # Background: kawasan industri
    show b with dissolve
    b "Dengan bantuan tim konstituennya, Bima berhasil mengatur pertemuan rahasia dengan beberapa buruh pabrik. Meski pertemuan ini sederhana, bagi para buruh, ini adalah momen penuh harapan."
    b "Saya harus mendengar langsung apa yang mereka alami."

    # Perjalanan menuju gudang tempat pertemuan
    scene bg warehouse with fade  # Background: gudang
    show b with dissolve
    b "Bima berjalan melewati lorong sempit menuju sebuah gudang kosong di belakang pabrik, tempat pertemuan akan diadakan. Sekelompok buruh menunggu di sana, wajah mereka menunjukkan kelelahan dan kecemasan."

    # Pertemuan dengan buruh
    bp "Pak Bima, terima kasih sudah meluangkan waktu untuk bertemu dengan kami. Kami tidak tahu harus bicara ke siapa lagi. Kami sudah mencoba menyampaikan keluhan, tapi tidak ada yang peduli."
    b "Saya sudah membaca laporan kalian, tapi saya ingin mendengar lebih rinci. Apa ada bukti yang bisa membantu kita memperkuat argumen ini? Dokumen atau catatan yang menunjukkan pelanggaran mereka?"
    bu "Ada, Pak. Beberapa teman kami diam-diam mencatat jam kerja yang tidak sesuai kontrak. Tapi kami takut, Pak. Kalau ketahuan, kami bisa dipecat."
    b "Saya mengerti. Kalian punya alasan untuk khawatir. Tapi kita harus hati-hati. Bukti ini sangat penting untuk membawa kasus kalian ke tingkat yang lebih tinggi."

    # Buruh yang skeptis
    be "Apa gunanya semua ini, Pak Bima? Kami sudah mencoba protes sebelumnya, tapi malah diberhentikan! Bos hanya peduli pada keuntungan. Tidak ada yang peduli dengan kami!"
    b "Saya tahu kalian merasa putus asa. Tapi percayalah, jika kita bergerak bersama dengan bukti yang kuat, kita bisa membawa masalah ini ke meja hukum. Saya tidak akan membiarkan mereka lolos begitu saja."

    menu:
        "Mengumpulkan bukti melalui wawancara dan dokumen":
            b "Kita mulai dari langkah kecil. Kumpulkan semua dokumen yang menunjukkan pelanggaran: slip gaji, jam kerja, atau kontrak yang tidak dipatuhi. Saya akan mengatur agar semua ini tetap aman."
            bp "Tapi, bagaimana kalau mereka tahu, Pak? Kami bisa kehilangan pekerjaan."
            b "Saya akan memastikan kalian tidak sendirian. Jika kalian bersatu, suara kalian akan lebih kuat. Percayalah, saya di sini untuk melindungi kalian."
        
        "Mengorganisir buruh untuk memulai protes besar":
            b "Jika kita ingin perubahan cepat, kita harus bersatu. Kita bisa mengorganisir protes damai untuk menunjukkan bahwa suara kalian tidak bisa diabaikan."
            bu "Protes? Itu berisiko besar, Pak. Mereka bisa memanggil polisi untuk membubarkan kami."
            b "Risiko itu ada, tapi kita akan melakukannya dengan cara yang aman. Kita libatkan media dan organisasi HAM untuk memastikan bahwa mereka tidak bisa bertindak semena-mena. Ini bukan hanya tentang kalian, tapi tentang ribuan buruh lain yang menghadapi masalah serupa."

    # Narasi Akhir Scene 5
    b "Setelah diskusi panjang, sebagian buruh setuju untuk mulai mengorganisir protes. Namun, rasa takut tetap ada di antara mereka."
    b "Malam itu, Bima meninggalkan kawasan pabrik dengan membawa dokumen dan kesaksian buruh. Di pikirannya, dia tahu ini hanya awal dari perjuangan yang panjang. Tapi dia juga tahu, setiap langkah kecil membawa harapan untuk perubahan."


    # Narasi penutup untuk Arc 1
    b "Ini baru awal. Masalah ini lebih besar dari yang aku bayangkan. Tapi aku sudah siap untuk melangkah lebih jauh."
    
    return
#ARC 2
# The script of the game goes in this file.

# Declare characters used by this game. The color argument colorizes the
# name of the character.

define b = Character("Bima")
define n = Character(" ")
define ks = Character("Ketua Sidang")
define psa = Character("Politisi Senior A")
define psb = Character("Politisi Senior B")
define ka = Character("Kolega A")
define kb = Character("Kolega B")
define pk = Character("Pejabat Korup")
define ba = Character("Buruh A")
define ah = Character("Aktivis HAM")
define ppk = Character("Politisi Pendukung Kebijakan")
define a = Character("Asisten")
define ap = Character("Asisten Pengusaha")
define pt = Character("Pengusaha Tamak")
define h = Character("Hardi")
define wi = Character("Wartawan Independen")
define mp = Character("Mantan Pekerja")

# The game starts here.

label start:
    #Scene 1a: Sidang Parlemen - Meningkatkan Taruhan
    n "Setelah pernyataan beraninya di sidang sebelumnya, Bima kini menghadapi ujian yang lebih berat. Rancangan kebijakan yang memihak pengusaha telah kembali ke meja parlemen, dan tekanan untuk diam semakin besar."
    ks "Sidang hari ini akan membahas finalisasi rancangan kebijakan tenaga kerja. Kami meminta anggota yang ingin berbicara untuk mengajukan pendapat mereka."
    n "Bima tahu, ini adalah momen penting. Tetapi dia juga sadar bahwa setiap kata yang diucapkannya bisa membawa risiko besar."
    b "(Dalam hati): Mereka sedang menunggu aku membuat kesalahan. Tapi aku tidak boleh diam. Rakyat membutuhkan suara ini."
    menu:
        "Berbicara dengan tenang dan penuh perhitungan.":
            jump pilihan1_1a
        "Langsung menyerang dengan bukti awal yang dimiliki.":
            jump pilihan2_1a
    label pilihan1_1a:
        b "Terima kasih atas kesempatannya. Saya ingin mengingatkan bahwa kebijakan ini harus melindungi semua pihak, termasuk buruh yang menjadi tulang punggung ekonomi kita. Jika kita hanya memihak pengusaha, kita akan menciptakan ketimpangan yang lebih dalam."
        psa "Pak Bima, Anda berbicara tentang ketimpangan, tetapi apakah Anda memahami kebutuhan investasi? Kita butuh investor untuk menciptakan lapangan kerja."
        b "Saya paham pentingnya investasi. Namun, investasi yang dibangun di atas ketidakadilan hanya akan merusak fondasi bangsa kita. Kita bisa mendukung pengusaha tanpa mengorbankan hak buruh."
        n "Pendekatan Bima yang tenang berhasil menarik perhatian beberapa anggota parlemen. Namun, skeptisisme tetap kuat, terutama dari pihak pendukung kebijakan."
        jump choices1_common_1b
    label pilihan2_1a:
        b "Rancangan kebijakan ini bukan hanya soal ekonomi, tetapi juga soal moralitas. Saya telah melihat sendiri bagaimana pengusaha besar menggunakan kekuasaan mereka untuk menindas buruh, dan bukti ini hanya sebagian kecil dari apa yang saya temukan."
        n "Bima menunjukkan dokumen awal yang mengungkap pelanggaran jam kerja dan gaji minimum di pabrik besar. Ruangan sidang menjadi sunyi, namun ketegangan meningkat."
        psb "Apa maksud Anda dengan ini? Tuduhan ini tidak berdasar. Anda hanya mencoba memancing perhatian."
        b "Kalau memang tidak berdasar, kenapa Anda terlihat begitu defensif? Saya hanya menginginkan transparansi. Jika kebijakan ini sah, maka tidak ada yang perlu disembunyikan."
        hide bima
        n "Strategi Bima berhasil memancing reaksi keras dari pihak pendukung kebijakan, tetapi juga menarik dukungan dari beberapa anggota parlemen independen."
        jump choices1_common_1b
    
    

    #Scene 1b: Konflik Internal-Rekan Parlemen Ragu
    label choices1_common_1b:
        scene bg ruangkerjapagi
        show bima marah
        ka "Bima, apa yang kamu lakukan? Kamu tahu mereka tidak akan tinggal diam. Mereka punya kekuatan untuk menjatuhkanmu."
        b "Kalau aku diam, lalu siapa yang akan bicara untuk rakyat? Aku tidak peduli risiko ini, selama aku tahu aku berada di pihak yang benar."
        kb "Hati-hati, Bima. Kita mendukungmu, tapi jangan membuat mereka merasa terlalu terpojok. Mereka bisa balas menyerang."

    #Scene 1c: Konfrontasi dengan antagonis
    pk "Pak Bima, saya memahami semangat Anda sebagai anggota baru di parlemen. Namun, izinkan saya memberi sedikit masukan. Dunia politik tidak sesederhana yang Anda bayangkan. Terkadang, kompromi adalah jalan terbaik untuk mencapai tujuan besar."
    b "Kompromi? Apa yang Anda maksud dengan kompromi, Pak? Membiarkan rakyat terus menderita demi menjaga keuntungan segelintir pihak?"
    pk "Anda salah paham. Tidak ada yang ingin rakyat menderita. Namun, kita juga harus berpikir realistis. Dunia tidak bekerja dengan idealisme, Pak Bima. Anda perlu memahami bahwa roda ekonomi harus terus berputar, dan itu membutuhkan keseimbangan, meskipun terkadang ada yang harus berkorban."
    b "(Dalam Hati): Dia berbicara tentang keseimbangan, tetapi jelas ini hanyalah pembenaran untuk membiarkan ketidakadilan terus terjadi. Aku harus memilih kata-kataku dengan hati-hati."
    menu:
        "Menanggapi dengan sopan dan logis.":
            jump pilihan1_1c
        "Menyerang balik dengan mempertanyakan integritasnya.":
            jump pilihan2_1c
    label pilihan1_1c:
        b "Saya menghargai masukan Anda, Pak. Memang benar bahwa dunia tidak sempurna, dan terkadang kita harus membuat keputusan sulit. Namun, saya percaya bahwa keputusan sulit tidak boleh mengorbankan prinsip dasar keadilan."
        pk "Prinsip dasar keadilan? Prinsip itu bagus di atas kertas, tapi kita bekerja di dunia nyata, Pak Bima. Kalau kita terlalu berpihak pada satu sisi, sisi lainnya akan runtuh."
        b "Tugas kita di sini adalah menjaga agar tidak ada yang runtuh, Pak. Jika kita memihak buruh, bukan berarti kita menolak pengusaha. Kita hanya meminta mereka untuk memenuhi kewajiban mereka, yang seharusnya tidak menjadi beban besar bagi mereka."
        pk "Menarik sekali, Pak Bima. Anda berbicara seperti orang yang tidak pernah bekerja dengan anggaran besar atau tekanan investor. Apa Anda yakin bisa memahami kompleksitas masalah ini?"
        b "Saya mungkin belum pernah bekerja dengan investor besar, tapi saya bekerja dengan rakyat kecil setiap hari. Saya mendengar keluhan mereka, dan itu cukup untuk memahami bahwa sistem ini perlu diperbaiki, bukan dipertahankan."
        n "Pendekatan diplomatis Bima menarik perhatian beberapa anggota parlemen. Beberapa terlihat mengangguk setuju, meskipun ketegangan dengan pejabat korup itu tidak berkurang."
        jump choices1_common_1c
    label pilihan2_1c:
        b "Pak, maaf kalau saya salah paham, tapi dari cara Anda berbicara, sepertinya yang Anda maksud dengan keseimbangan adalah membiarkan ketidakadilan terus terjadi demi keuntungan segelintir pihak."
        pk "Anda menuduh tanpa bukti, Pak Bima. Hati-hati dengan kata-kata Anda. Tuduhan seperti ini bisa berbalik kepada Anda." #nada dingin
        b "Saya tidak menuduh, Pak. Saya hanya bertanya. Jika kebijakan ini benar-benar adil, mengapa buruh di lapangan mengatakan bahwa mereka tidak pernah dilibatkan dalam diskusi? Mengapa ada begitu banyak pelanggaran terhadap hak dasar mereka yang dibiarkan begitu saja?"
        pk "Pak Bima, dunia ini tidak hanya hitam dan putih. Kalau Anda terus mendesak seperti ini, Anda akan menemukan banyak musuh. Apa Anda siap menghadapi itu?" #nada mengancam
        b "Jika membela rakyat kecil membuat saya punya banyak musuh, maka biarlah begitu. Saya lebih baik kalah dengan prinsip daripada menang dengan cara mengkhianati mereka yang mempercayakan suara mereka kepada saya." #tegas
        n "Pernyataan Bima membuat ruangan menjadi sunyi. Beberapa anggota parlemen mulai memandangnya dengan kagum, sementara pejabat korup itu tersenyum tipis, menyembunyikan rasa tidak senangnya."
        pk "(Dalam hati): Anak muda ini terlalu berani. Kita lihat sampai kapan dia bisa bertahan." 
        jump choices1_common_1c
    label choices1_common_1c:
        n "Pertukaran kata-kata antara Bima dan pejabat korup itu menjadi momen penting di sidang hari itu. Bima tahu bahwa dia telah membuat lawannya merasa terancam, tetapi dia juga menyadari bahwa serangan balik dari pihak mereka tidak akan lama lagi."
    
    #Scene 2a: Investigasi Lapangan - Menyusun Bukti 
        #Visual: Malam hari di luar pabrik buruh, dengan suasana yang penuh kewaspadaan. Bima dan timnya bertemu dengan buruh yang telah mengumpulkan bukti pelanggaran.
    ba "Pak Bima, ini semua dokumen yang kami punya. Slip gaji, laporan jam kerja, dan foto kondisi tempat kerja kami. Tapi hati-hati, dokumen ini bisa membuat mereka marah jika mereka tahu kami yang menyerahkannya."
    b "Kalian sudah melakukan hal yang luar biasa. Saya akan memastikan bukti ini digunakan dengan hati-hati. Tidak ada yang akan tahu siapa yang memberikan ini."
    ah "Pak Bima, kita punya cukup bukti untuk menekan parlemen. Tapi saya tahu para pejabat yang terkait pasti akan menyerang balik. Kita harus bersiap."
    b "Saya tidak akan mundur. Saya akan membawa ini ke meja parlemen, apa pun risikonya."
    n "Dengan bukti di tangan, Bima tahu langkah berikutnya adalah mempresentasikan kasus ini di parlemen. Namun, ia juga sadar bahwa musuhnya, terutama pejabat korup dan pengusaha besar, tidak akan tinggal diam."
        #Visual: Bima kembali ke kantor parlemen larut malam, melihat dokumen di mejanya dengan wajah penuh tekad.
    b "(Dalam hati): Bukti ini kuat, tapi akan sulit untuk membuat semua pihak mendengar. Aku harus melangkah hati-hati, karena musuhku ada di sini, di ruang parlemen ini sendiri."
        #Visual: Ruang sidang parlemen di siang hari berikutnya. Para anggota parlemen duduk di kursi mereka, dengan suasana yang tegang. Ketua sidang memberi kesempatan kepada Bima untuk berbicara.
    ks "Anggota Bima, Anda meminta waktu untuk menyampaikan pendapat Anda tentang rancangan kebijakan ini. Silakan."
    n "Bima berdiri, membawa dokumen dari investigasi lapangannya. Ia mengambil napas dalam-dalam sebelum mulai berbicara."
    b "Terima kasih, Ketua Sidang. Hari ini, saya ingin membahas apa yang sering kali terabaikan dalam rancangan kebijakan ini: nasib buruh. Selama beberapa minggu terakhir, saya telah turun langsung ke lapangan untuk mendengar suara mereka."
    b "Yang saya temukan sungguh mengkhawatirkan. Jam kerja yang melebihi batas hukum, gaji yang jauh di bawah standar, dan tempat kerja yang tidak aman. Semua ini adalah pelanggaran yang nyata terhadap hak asasi manusia."
    n "Bima menunjukkan dokumen-dokumen yang dibawanya kepada anggota parlemen lain."
    ppk "Apa yang Anda bawa ini hanya laporan sepihak. Kita tidak bisa menyusun kebijakan berdasarkan cerita yang tidak terverifikasi, Pak Bima."
    "Laporan ini bukan sekadar cerita. Ini bukti. Dokumen ini menunjukkan pemotongan gaji ilegal, laporan medis buruh yang terluka akibat kondisi kerja, dan catatan jam kerja yang melebihi batas hukum. Apa ini masih Anda anggap cerita sepihak?"
        #Pejabat Korup, yang sejak tadi diam, akhirnya bangkit berdiri. Ia tersenyum kecil, mencoba mencairkan suasana.
    pk "Pak Bima, saya menghormati upaya Anda. Tapi mari kita pikirkan bersama: apakah kebijakan ini benar-benar hanya untuk menguntungkan pengusaha? Kita semua di sini sepakat bahwa investasi itu penting, bukan?"
    b "Saya tidak menentang investasi, Pak. Yang saya tentang adalah investasi yang dibangun di atas penderitaan buruh. Kita bisa menarik investasi tanpa mengorbankan mereka yang bekerja paling keras untuk mendukung perekonomian kita."
    pk "Anda berbicara dengan semangat yang luar biasa. Tapi izinkan saya bertanya: apakah Anda paham betapa sulitnya mengatur keseimbangan antara kebutuhan pengusaha dan hak buruh? Dunia ini tidak hanya hitam dan putih, Pak Bima."
    menu:
        "Menanggapi dengan sopan dan logis.":
            jump pilihan1_2a
        "Menyerang balik dengan mempertanyakan integritasnya.":
            jump pilihan2_2a
    label pilihan1_2a:
        b "Saya paham bahwa ini tidak mudah, Pak. Tapi tugas kita di sini adalah membuat keputusan yang adil untuk semua pihak, bukan hanya untuk mereka yang memiliki kuasa. Jika keseimbangan yang Anda maksud adalah terus membiarkan pelanggaran ini, maka saya rasa itu bukan keseimbangan, melainkan ketidakadilan."
        pk "Tuduhan Anda terlalu berat untuk sesuatu yang Anda anggap 'ketidakadilan'. Hati-hati, Pak Bima. Anda bisa melangkah terlalu jauh."
        jump choices1_common_2a
    label pilihan2_2a:
        b "Keseimbangan? Apa yang Anda maksud dengan keseimbangan adalah memberikan kekuasaan mutlak kepada pengusaha dan membiarkan buruh menjadi korban? Kalau begitu, saya tidak ingin menjadi bagian dari keseimbangan itu." #tegas
        pk "Kata-kata Anda keras, Pak Bima. Tapi keras kepala saja tidak cukup untuk membuat perubahan. Apa Anda yakin bisa menghadapi konsekuensi dari ucapan Anda?" #menyeringai
        b "Kalau memperjuangkan keadilan membawa konsekuensi, maka saya akan menerimanya. Yang tidak bisa saya terima adalah diam melihat rakyat terus menderita."
        jump choices1_common_2a
    label choices1_common_2a:
        n "Dialog itu menjadi momen puncak dalam sidang hari itu. Bima telah membuat musuhnya merasa terpojok, tetapi ia juga tahu bahwa serangan balik dari mereka tidak akan lama lagi. Pejabat korup itu duduk kembali dengan senyum tipis, merencanakan langkah selanjutnya."
        #visual: Bima duduk di kursinya dengan tenang, sementara kamera menyorot wajah-wajah anggota parlemen yang mulai terpecah antara mendukung atau melawan argumen Bima.
        n "Dengan bukti yang kuat dan dukungan yang mulai tumbuh, Bima harus bersiap menghadapi langkah selanjutnya. Lawannya, pejabat korup dan pengusaha besar, pasti akan mencoba membalas serangan ini. Namun, Bima tahu, perjuangannya baru dimulai."
        #visual: Bima berjalan keluar dari ruang sidang, membawa dokumen di tangannya dengan tatapan penuh tekad.
    
    #Scene 3a: Munculnya Pengusaha Tamak
    #Visual: Sebuah kantor mewah dengan jendela besar yang menghadap ke kota. Pengusaha Tamak duduk di kursinya, dengan tumpukan dokumen di meja. Seorang asisten datang membawa berita tentang sidang parlemen yang baru saja berlangsung.
    a "Pak, Anda mungkin ingin melihat ini. Anggota parlemen baru, Bima, baru saja mempresentasikan bukti tentang pelanggaran di pabrik Anda dalam sidang tadi."
    pt "Bima, ya? Anak baru yang penuh idealisme itu? Aku sudah mendengar tentangnya. Dia terlalu bersemangat untuk kebaikannya sendiri."
    a "Bukti yang dia tunjukkan cukup kuat, Pak. Jika ini terus berlanjut, reputasi Anda bisa terancam, dan kebijakan kita mungkin akan diblokir."
    pt "Hmph, aku tidak sampai di sini dengan membiarkan bocah seperti dia menghancurkan semuanya. Kita lihat apakah dia tetap idealis setelah diajak bicara. Hubungi orang-orang kita di parlemen dan atur pertemuan dengannya."
    n "Pengusaha itu tahu bahwa mengabaikan ancaman seperti Bima bisa berbahaya. Dia memutuskan untuk mengambil langkah langsung untuk mengontrol situasi."

    #Visual: Malam hari di kantor Bima. Telepon berdering saat Bima sedang meninjau dokumen baru dari buruh.
    b "Halo, ini Bima."
    ap "Pak Bima, nama saya Indra. Saya asisten dari Pak Hardi, salah satu pemilik pabrik di kawasan industri yang Anda investigasi. Bos saya ingin bertemu dengan Anda untuk mendiskusikan laporan Anda."
    b "Pak Hardi? Saya tidak menyangka dia akan merespons secepat ini."
    ap "Pak Hardi merasa bahwa ada kesalahpahaman yang perlu diluruskan. Dia ingin bertemu di kantornya besok malam. Ini akan menjadi pertemuan pribadi dan informal."
    menu:
        "Menerima undangan untuk bertemu langsung.":
            jump pilihan1_3a
        "Menolak bertemu dan meminta semua komunikasi dilakukan secara resmi.":
            jump pilihan2_3a
    label pilihan1_3a:
        b "Baik, saya akan datang. Tapi saya harap ini adalah diskusi terbuka dan jujur. Jika ada sesuatu yang perlu dijelaskan, saya ingin mendengarnya langsung."
        ap "Tentu saja, Pak. Bos saya sangat menghormati posisi Anda."
        #Visual: Bima mengakhiri panggilan dengan ekspresi serius, mempersiapkan dirinya untuk pertemuan yang penuh risiko.
        jump choices1_common_3a
    label pilihan2_3a:
        b "Terima kasih atas undangannya, tapi saya rasa semua diskusi tentang isu ini harus dilakukan secara resmi. Saya tidak ingin ada yang disalahartikan."
        ap "Saya mengerti, Pak. Tapi ini adalah kesempatan baik untuk menyelesaikan kesalahpahaman sebelum masalah ini menjadi lebih besar."
        b "Saya akan tetap pada pendirian saya. Jika Pak Hardi ingin berbicara, dia bisa menghadapi saya di parlemen atau melalui jalur resmi lainnya."
        jump choices2_common_3a
    label choices1_common_3a:
        #Visual: Kantor mewah dengan lantai marmer, jendela besar menghadap ke kota, dan meja kayu besar dengan dokumen tertata rapi. Hardi duduk di kursinya, memandang Bima dengan senyum licik, sementara Bima duduk di kursi tamu dengan tatapan serius.
        h "Pak Bima, pertama-tama, saya ingin mengucapkan terima kasih atas waktu Anda. Tidak banyak anggota parlemen yang mau repot-repot mendengar langsung dari pelaku usaha seperti saya."
        b "Terima kasih atas undangannya, Pak. Saya di sini untuk memastikan bahwa kebenaran muncul dan keadilan ditegakkan. Saya harap diskusi ini bisa bermanfaat."
        h "Ah, keadilan, kata yang indah. Tapi, Anda harus tahu bahwa keadilan sering kali bersifat relatif, tergantung dari mana Anda melihatnya. Dunia ini penuh nuansa, Pak Bima, bukan hitam putih seperti yang sering digambarkan."
        menu:
            "Tetap sopan dan mendengarkan argumen Hardi.":
                jump pilihan1_cc_3a
            "Langsung mempertanyakan integritas Hardi.":
                jump pilihan2_cc_3a
        label pilihan1_cc_3a:
            b "Saya setuju bahwa dunia tidak selalu hitam dan putih, Pak. Namun, jika kita membiarkan prinsip keadilan menjadi terlalu fleksibel, kita berisiko mengabaikan mereka yang paling rentan."
            h "Pernyataan yang bagus. Tapi izinkan saya bertanya: apa Anda tahu bagaimana sulitnya menjalankan bisnis di negeri ini? Pajak yang tinggi, regulasi yang tumpang tindih, tekanan dari investor. Semua itu memaksa pengusaha seperti saya untuk membuat keputusan yang, terkadang, tidak ideal."
            b "Keputusan tidak ideal yang Anda maksud, apakah itu termasuk pemotongan gaji buruh dan pelanggaran jam kerja?"
            h "Ah, saya lihat Anda datang dengan membawa tuduhan berat. Tapi percayalah, masalah ini sering kali disebabkan oleh manajemen di lapangan, bukan kebijakan saya. Saya tidak pernah berniat merugikan pekerja saya." #tersenyum kecil
            b "Kalau begitu, saya harap Anda siap bekerja sama untuk memperbaiki masalah ini. Para buruh Anda berhak mendapatkan keadilan."
            jump lanjutan_3a
        label pilihan2_cc_3a:
            b "Relatif atau tidak, keadilan tetaplah keadilan, Pak. Apa yang terjadi di pabrik Anda adalah pelanggaran nyata terhadap hukum dan hak asasi manusia. Jika Anda tahu tentang ini, Anda seharusnya bertindak lebih cepat."
            h "Hati-hati dengan tuduhan Anda, Pak Bima. Saya menghormati posisi Anda, tetapi saya tidak akan menerima fitnah tanpa dasar."
            b "Ini bukan fitnah. Saya punya bukti yang menunjukkan pemotongan gaji ilegal, pelanggaran jam kerja, dan kondisi kerja yang tidak aman. Semua ini terjadi di pabrik Anda."
            h "Kalau begitu, mari kita selidiki bersama. Saya akan membentuk tim internal untuk menyelesaikan ini. Tapi, Anda juga harus memahami bahwa kesalahan seperti ini sering kali berasal dari manajemen tingkat bawah."
            b "Saya akan menunggu hasil investigasi Anda, tapi saya tidak akan tinggal diam jika masalah ini tidak segera ditangani."
            jump lanjutan_3a
        label lanjutan_3a:
            h "Pak Bima, izinkan saya berbicara jujur. Anda adalah orang baru di dunia politik, penuh dengan semangat dan idealisme. Itu bagus. Tapi Anda juga harus belajar bahwa dunia ini tidak berjalan hanya dengan moral. Kadang kita harus berkompromi."
            menu:
                "Menyatakan bahwa prinsip lebih penting daripada kompromi.":
                    jump pilihan1_lanjutan_3a
                "Mengakui bahwa kompromi kadang diperlukan, tetapi tidak untuk melanggar hak asasi.":
                    jump pilihan2_lanjutan_3a
            label pilihan1_lanjutan_3a:
                b "Mungkin Anda benar bahwa kompromi penting dalam beberapa hal. Tapi untuk pelanggaran hak asasi manusia, saya tidak akan pernah berkompromi. Keadilan adalah hal yang tidak bisa ditawar."
                h "Pendekatan seperti itu mungkin ideal, tapi tidak realistis. Jika Anda terus bertahan dengan pandangan itu, Anda akan menghadapi lebih banyak musuh daripada teman di dunia ini."
                b "Kalau mempertahankan prinsip membuat saya punya lebih banyak musuh, maka itu risiko yang saya terima. Lebih baik saya kalah dengan integritas daripada menang dengan mengkhianati rakyat."
                jump cc_lanjutan_3a
            label pilihan2_lanjutan_3a:
                b "Saya paham bahwa kompromi kadang diperlukan, Pak. Tapi saya tidak percaya bahwa kompromi bisa menjadi alasan untuk melanggar hak asasi manusia. Ada batasan yang tidak boleh dilanggar."
                h "Batasan, ya? Kalau begitu, izinkan saya menanyakan ini: apa batasan Anda? Apa Anda siap kehilangan dukungan politik hanya karena Anda tidak mau sedikit melonggarkan prinsip Anda?"
                b "Kalau prinsip saya harus dilonggarkan untuk mendukung ketidakadilan, maka saya lebih baik kehilangan dukungan itu."
                jump cc_lanjutan_3a
            label cc_lanjutan_3a:
                h "Pak Bima, izinkan saya memberi saran. Jika Anda terus maju seperti ini, Anda tidak hanya melawan saya. Anda melawan sistem. Apakah Anda yakin siap untuk itu?"
                menu:
                    "Menghadapi ancaman Hardi dengan tegas.":
                        jump pilihan1_cc_lanjutan_3a
                    "Memanfaatkan situasi untuk mendapatkan lebih banyak informasi.":
                        jump pilihan2_cc_lanjutan_3a
                label pilihan1_cc_lanjutan_3a:
                    b "Kalau memperjuangkan rakyat berarti melawan sistem, maka itu yang akan saya lakukan. Saya tidak takut pada ancaman Anda, Pak Hardi."
                    h "Baiklah, kita lihat sampai kapan idealisme Anda bisa bertahan. Tapi jangan bilang saya tidak memperingatkan Anda."
                    jump ending_3a
                label pilihan2_cc_lanjutan_3a:
                    b "Saya paham risikonya, Pak. Tapi saya ingin tahu lebih banyak. Siapa saja yang terlibat dalam sistem ini? Jika saya mengerti, mungkin kita bisa mencari jalan keluar bersama."
                    h "Saya suka pendekatan Anda. Tapi saya tidak begitu percaya pada niat Anda. Mari kita lihat apakah tindakan Anda sesuai dengan kata-kata Anda." #senyum kecil
                    jump ending_3a
                label ending_3a:
                    n "Pertemuan itu berakhir dengan ketegangan yang belum terselesaikan. Bima meninggalkan kantor Hardi dengan tekad yang semakin kuat, sementara Hardi merencanakan langkah balasan untuk menghentikannya. Perjuangan ini baru dimulai."
                    jump scene_4
    label choices2_common_3a:
        n "Bima menutup teleponnya."

    #Scene 4: Aliansi Kegelapan – Penyatuan Pengusaha Tamak dan Pejabat Korup
    #visual: Sebuah restoran mewah dengan lampu temaram. Meja pribadi di sudut ruangan dihiasi dengan lilin dan segelas anggur merah. Hardi, si pengusaha tamak, duduk santai di kursinya dengan senyum licik. Tidak lama kemudian, Pejabat Korup tiba, mengenakan jas rapi, membawa map dokumen kecil.
    label scene_4:
        h "Pak Herman, akhirnya Anda datang juga. Saya kira Anda terlalu sibuk untuk urusan kecil seperti ini."
        pk "Urusan kecil? Pak Hardi, masalah ini jauh dari kecil. Anak muda itu, Bima, sudah mulai mengguncang fondasi kita. Saya rasa kita berdua tahu dia tidak bisa dibiarkan."
        h "Betul sekali. Saya sudah mendengar tentang presentasinya di parlemen. Dia membawa bukti, bahkan menyebut nama saya secara tidak langsung. Ini tidak bisa dibiarkan berlanjut."
        pk "Dia memang berani, saya beri dia itu. Tapi keberanian tidak akan cukup di dunia ini. Masalahnya, keberanian itu mulai mengganggu kepentingan kita. Jika bukti yang dia punya menyebar, reputasi saya dan bisnis Anda akan hancur." #suara buka map
        h "Dan tidak hanya reputasi. Dia juga bisa menarik perhatian pihak berwenang. Saya tidak mau ada aparat datang ke pabrik saya hanya karena anak baru ini tidak tahu tempatnya."
        pk "Jadi, apa rencana Anda? Anda ingin saya menekan dia di parlemen?"
        h "Itu langkah awal, tapi tidak cukup. Kita perlu menghabisinya secara menyeluruh, baik dari sisi politik maupun publik."
        pk "Itu tidak mudah, Pak Hardi. Anak itu punya integritas. Dia tidak akan takut dengan tekanan biasa. Kita butuh sesuatu yang lebih kuat."
        h "Integritas tidak akan berarti jika dia kehilangan kredibilitas. Kita rusak reputasinya. Saya punya media di bawah kendali saya. Kita bisa menciptakan narasi yang menggambarkan dia sebagai penghasut buruh yang tidak bertanggung jawab."
        pk "Itu langkah yang bagus. Saya juga bisa memastikan dia kehilangan pengaruh di parlemen. Saya akan mengatur agar proposalnya dipermainkan di komite, sehingga dia terlihat tidak kompeten."
        h "Kita juga bisa menargetkan buruh-buruh yang bekerja sama dengannya. Saya akan memberi peringatan kepada mereka melalui tim saya di pabrik. Jika mereka terus bicara, mereka kehilangan pekerjaan mereka."
        pk "Bagus, tapi itu baru permulaan. Kita juga perlu mendorong tekanan pribadi. Jika kita bisa menggali masa lalunya atau kelemahan yang bisa dimanfaatkan, dia tidak akan punya tempat untuk lari."
        h "Saya suka cara Anda berpikir, Pak Herman. Apa Anda punya tim yang bisa melakukan pekerjaan itu?" #senyum
        pk "Saya punya orang-orang yang sangat berbakat untuk hal seperti itu. Tapi ingat, ini harus dilakukan dengan sangat hati-hati. Jika kita terlalu agresif, dia bisa mendapatkan simpati dari publik."
        h "Publik? Publik itu mudah dipengaruhi. Kalau kita kontrol media dengan baik, kita bisa membuatnya terlihat sebagai musuh ekonomi negara. Orang akan percaya apa pun yang kita sajikan."
        pk "Jangan terlalu meremehkan dia. Anak itu pintar. Dia tahu bagaimana memanfaatkan simpati rakyat kecil. Jika kita tidak hati-hati, dia bisa membalikkan semuanya melawan kita."
        h "Saya sudah berurusan dengan orang-orang seperti dia sebelumnya. Mereka semua punya batas. Tekanan yang cukup akan membuatnya menyerah atau kehilangan dukungan." #tertawa kecil
        pk "Baiklah, kita mulai dari sini. Anda kendalikan narasi publik, dan saya akan urus sisi politiknya. Tapi saya butuh jaminan bahwa bisnis Anda tidak akan terlibat skandal lebih besar. Saya tidak ingin nama saya tercemar karena masalah Anda."
        h "Jaminan? Pak Herman, bisnis saya adalah yang menjaga ekonomi daerah Anda tetap hidup. Anda tidak akan punya masalah selama saya tetap bisa menjalankan operasi saya tanpa gangguan."
        pk "Kalau begitu, kita sepakat. Kita pastikan anak itu kehilangan dukungan, kredibilitas, dan kekuatan. Ketika semua ini selesai, dia tidak akan punya apa-apa lagi."
        h "Untuk kerja sama yang sukses. Saya akan pastikan anak itu menyesali keputusannya melawan kita."
        pk "Kita lihat siapa yang bertahan sampai akhir. Saya akan segera memulai langkah pertama saya di parlemen."
        n "Malam itu, aliansi gelap terbentuk. Hardi dan Herman, dua orang dengan kekuasaan besar, menyatukan kekuatan mereka untuk menjatuhkan Bima. Tetapi mereka tidak tahu bahwa Bima telah mempersiapkan langkah balasannya sendiri."

    #Scene 5: KEKALAHAN MC di Ruang Parlemen
    #visual: Ruang parlemen yang megah, dengan deretan politisi berbicara penuh emosi. MC (Bima) duduk di kursinya dengan wajah serius, memegang map dokumen yang berisi bukti pelanggaran. Di sisi lain, Pejabat Korup tersenyum tenang, sementara Hardi (Pengusaha Tamak) duduk sebagai tamu undangan dengan ekspresi percaya diri.
    n "Setelah berhari-hari mengumpulkan bukti dan mengatur strategi, Bima akhirnya memiliki kesempatan untuk mempresentasikan kasusnya di depan parlemen. Namun, di balik layar, musuh-musuhnya telah merencanakan segalanya untuk menjatuhkannya."
       
        #sub-sceneA
        #"Setelah berhari-hari mengumpulkan bukti dan mengatur strategi, Bima akhirnya memiliki kesempatan untuk mempresentasikan kasusnya di depan parlemen. Namun, di balik layar, musuh-musuhnya telah merencanakan segalanya untuk menjatuhkannya."
    b "Rekan-rekan sekalian, hari ini saya akan mempresentasikan bukti yang menunjukkan pelanggaran berat terhadap hak buruh di beberapa pabrik besar, termasuk yang dimiliki oleh Pak Hardi, yang juga hadir di sini."
    #suara riuh
    b "Bukti ini mencakup laporan pemotongan gaji, jam kerja yang melanggar hukum, dan kondisi kerja yang tidak manusiawi. Saya juga memiliki kesaksian dari beberapa buruh yang siap bersaksi jika diperlukan."

        #subscene B
        #Visual: Pejabat Korup berdiri dengan senyum tenang, tangan terlipat di depan dada.
    pk "Terima kasih, Pak Bima, atas presentasi Anda. Tapi izinkan saya bertanya, apakah Anda sudah memastikan keabsahan bukti-bukti ini? Saya melihat ada beberapa kesaksian anonim di sini. Apa ini tidak membuat bukti Anda diragukan?"
    b "Semua bukti ini telah diverifikasi oleh tim saya. Kesaksian anonim diberikan untuk melindungi buruh dari ancaman yang sangat nyata."
    pk "Ancaman? Atau mungkin mereka takut karena mereka tahu informasi ini tidak sepenuhnya benar? Kita harus berhati-hati dengan klaim seperti ini, terutama jika bisa merusak reputasi pengusaha yang telah memberikan banyak kontribusi untuk negara."
    menu:
        "Menjawab dengan tenang dan berfokus pada data.":
            jump pilihan1_5b
        "Langsung menyerang balik dengan mempertanyakan integritas Pejabat Korup.":
            jump pilihan2_5b
    label pilihan1_5b:
        b "Saya memahami kekhawatiran Anda, Pak Herman. Tapi data ini tidak hanya berdasarkan kesaksian. Kami memiliki catatan jam kerja, slip gaji, dan foto-foto kondisi kerja di lapangan yang mendukung temuan kami."
        pk "Itu menarik, tapi kita harus melihat semua ini dengan skeptis. Tidak ada jaminan bahwa data ini tidak dimanipulasi oleh pihak-pihak yang memiliki agenda politik."
        n "Pendekatan tenang Bima tidak cukup untuk menghentikan keraguan yang telah ditanamkan oleh Pejabat Korup. Beberapa anggota parlemen mulai terlihat ragu."
        jump subscene_c
    label pilihan2_5b:
        b "Anda berbicara tentang reputasi, Pak Herman. Tapi izinkan saya bertanya, apakah reputasi Anda juga terlibat di balik pelanggaran ini? Karena saya punya alasan untuk percaya bahwa hubungan Anda dengan Pak Hardi lebih dari sekadar profesional."
        pk "Hati-hati dengan kata-kata Anda, Pak Bima. Tuduhan tanpa bukti hanya akan merusak kredibilitas Anda sendiri."
        n "Serangan Bima berhasil memancing reaksi keras dari Pejabat Korup, tetapi juga membuat suasana semakin panas. Beberapa anggota parlemen mulai merasa tidak nyaman dengan eskalasi ini."
        jump subscene_c
    label subscene_c:
        #visual: Hardi berdiri dari kursi tamunya, berbicara dengan nada tenang namun penuh keyakinan.
        h "Saya menghormati upaya Pak Bima untuk membela buruh, tapi izinkan saya mengatakan bahwa tuduhan ini sangat tidak adil. Sebagai pengusaha, saya selalu memprioritaskan kesejahteraan pekerja saya."
        b "Jika itu benar, bagaimana Anda menjelaskan bukti pemotongan gaji dan pelanggaran jam kerja di pabrik Anda?"
        h "Bukti itu? Saya tidak tahu dari mana Anda mendapatkannya, tapi saya yakin itu adalah laporan yang salah atau dimanipulasi oleh pihak-pihak yang ingin merusak nama baik perusahaan saya."
        menu: 
            "Mencoba menekan Hardi dengan menunjukkan lebih banyak bukti.":
                jump pilihan1_sc_5c
            "Meminta buruh untuk berbicara langsung sebagai saksi.":
                jump pilihan2_sc_5c
        label pilihan1_sc_5c:
            b "Ini bukan hanya laporan. Ini adalah slip gaji yang menunjukkan pemotongan langsung. Ini adalah catatan jam kerja yang melanggar undang-undang ketenagakerjaan."
            h "Semua itu bisa saja dipalsukan, Pak Bima. Dan saya tidak akan tinggal diam melihat nama saya dicemarkan seperti ini!"
            n "Serangan balik Hardi, didukung oleh keraguan yang ditanamkan oleh Pejabat Korup, membuat banyak anggota parlemen mulai meragukan keabsahan data Bima."
            jump subscene_d
        label pilihan2_sc_5c:
            #visual: Salah satu buruh yang hadir berdiri dengan gemetar, mencoba berbicara di depan parlemen.
            b "Saya... saya ingin mengatakan bahwa semua yang dikatakan Pak Bima itu benar. Kami sering dipaksa bekerja melebihi batas, dan gaji kami dipotong tanpa alasan."
            ba "*sambil bergetar.. Apa yang dikatakan buruh ini tidak mewakili mayoritas pekerja saya. Dia hanya satu dari ribuan. Dan bagaimana kita bisa tahu bahwa dia tidak dimanipulasi oleh pihak luar?"
            n "Kehadiran buruh sebagai saksi tidak cukup untuk melawan narasi kuat yang dibangun oleh Hardi dan Pejabat Korup. Dukungan untuk Bima semakin melemah."
            jump subscene_d
        label subscene_d:
            #visual: Ketua sidang memutuskan untuk menunda keputusan tentang kasus ini, menyebut perlunya investigasi lebih lanjut.
            ks "Karena kurangnya kejelasan dan untuk menjaga keadilan, kami akan menunda keputusan ini sampai investigasi resmi dilakukan. Sidang selesai."
            n "Keputusan itu merupakan pukulan berat bagi Bima. Meskipun ia telah memberikan bukti yang kuat, propaganda dan pengaruh antagonis membuatnya terlihat lemah dan tidak efektif."
            jump ending_scene_5
        label ending_scene_5:
            n "Di ruang sidang yang kosong, Bima duduk sendirian, menatap dokumen yang telah ia persiapkan dengan susah payah. Kekalahan ini bukan hanya tentang dirinya, tapi tentang rakyat kecil yang bergantung pada perjuangannya. Namun, di tengah kegelapan, ia bersumpah untuk kembali lebih kuat."
    
    #SCENE 6: Bangkit dari kekalahan
    #visual:Visual: Malam hari di kantor Bima. Lampu ruangan menerangi meja penuh dokumen, laptop, dan peta. Bima duduk di kursi, tangannya mencengkeram sebuah laporan, ekspresi wajahnya mencerminkan perpaduan rasa frustrasi dan tekad yang tak tergoyahkan
    n "Setelah kekalahan di parlemen, Bima merenung. Kekuasaan dan kelicikan musuh-musuhnya telah membuat perjuangannya terlihat sia-sia. Namun, di tengah kegelapan itu, ia menyadari satu hal:"
    n "untuk melawan sistem yang korup, ia membutuhkan bukti yang tak terbantahkan, sesuatu yang tidak bisa disangkal oleh siapa pun." 
    #Visual: Visual: Ruang kecil tempat Bima bertemu dengan beberapa aktivis HAM, wartawan independen, dan buruh yang masih mendukungnya. Mereka duduk melingkar di sekitar meja besar, membahas langkah berikutnya.
    ah "Pak Bima, saya tahu kekalahan ini sulit diterima. Tapi kita masih punya peluang. Jika kita bisa menemukan sesuatu yang lebih besar, sesuatu yang benar-benar mengejutkan, mereka tidak akan bisa menghindar lagi."
    b "Kita butuh bukti yang tidak bisa dibantah. Bukan hanya soal pelanggaran buruh, tapi sesuatu yang mengungkap korupsi dan kejahatan mereka yang sebenarnya."
    wi "Saya dengar ada desas-desus tentang aktivitas ilegal di salah satu pabrik milik Hardi. Beberapa mantan pekerja mengatakan bahwa ada aliran uang gelap dan perdagangan ilegal yang melibatkan perusahaan itu."
    b "Jika itu benar, maka ini adalah kunci kita. Tapi kita harus bertindak hati-hati. Jika mereka tahu kita menyelidiki ini, mereka tidak akan segan-segan menyerang balik."
    ba "Saya punya kenalan yang dulu bekerja di pabrik itu. Dia mungkin tahu sesuatu. Tapi dia sangat takut untuk berbicara."
    b "Kalau begitu, kita temui dia. Kita yakinkan bahwa dia akan aman, dan suara dia bisa membawa perubahan besar."

    #scene 6b
    #visual:Sebuah kawasan industri yang gelap dan suram. Bima bersama seorang aktivis dan buruh mendekati seorang mantan pekerja yang duduk di luar sebuah warung kecil.
    mp "Pak Bima, saya tidak tahu kenapa Anda ingin bertemu saya. Saya sudah lama keluar dari pabrik itu. Saya tidak mau terlibat masalah."
    b "Kami hanya ingin mendengar cerita Anda. Anda tidak perlu takut. Kami akan melindungi Anda."
    mp "Saya tidak tahu banyak, tapi saya pernah mendengar manajer bicara soal 'pengiriman khusus' di malam hari. Mereka sangat merahasiakan itu. Saya curiga ada sesuatu yang tidak beres."
    b "Pengiriman khusus? Apa Anda tahu kapan atau di mana itu terjadi?"
    mp "Biasanya di gudang belakang, setelah jam kerja. Tapi saya tidak pernah melihatnya langsung. Saya hanya mendengar desas-desus dari teman-teman."
    ah "Itu bisa jadi sesuatu. Jika kita bisa mengamati pengiriman itu, kita mungkin bisa menemukan sesuatu yang besar."

    #scene 6c
    #visual: Malam hari di sekitar pabrik. Bima bersama tim kecil mengamati dari kejauhan dengan menggunakan kamera dan catatan.
    n "Dengan informasi baru, Bima dan timnya memutuskan untuk melakukan pengintaian di pabrik Hardi. Mereka harus bertindak cepat, tetapi juga berhati-hati untuk tidak menarik perhatian."
    ah "Lihat itu. Ada truk besar yang keluar dari gudang belakang. Tidak ada tanda pengiriman resmi di kendaraan itu."
    b "Kita harus tahu ke mana mereka membawa barang ini. Kita ikuti, tapi jangan sampai mereka menyadari kita."
    menu:
        "Mengikuti truk dari kejauhan untuk mencari tujuan pengiriman.":
            jump pilihan1_6c
        "Menyusup ke dalam pabrik untuk melihat barang apa yang dikirimkan.":
            jump pilihan2_6c
    label pilihan1_6c:
        #visual: Truk melaju di jalanan malam yang sepi, dengan Bima dan timnya mengikuti dari jarak aman.
        n "Mereka mengikuti truk hingga tiba di sebuah gudang terpencil di pinggir kota. Di sana, mereka melihat aktivitas mencurigakan: beberapa pria memindahkan kotak-kotak besar ke dalam gudang."
        b "Kita harus tahu apa isi kotak-kotak itu. Kalau ini barang ilegal, kita punya bukti yang kita cari."
        jump subscene_6d
    label pilihan2_6c:
        #Visual: Bima dan seorang aktivis menyelinap melalui pagar belakang pabrik, berhati-hati untuk menghindari penjaga keamanan
        n "Menyusup ke dalam pabrik adalah langkah berisiko, tetapi juga memberikan kesempatan untuk melihat langsung apa yang sedang terjadi di sana."
        b "Lihat itu. Kotak-kotak ini tidak memiliki tanda resmi. Apa mungkin ini barang ilegal?"
        ah "Kita harus memotret ini. Kalau kita bisa membawa ini ke media, mereka tidak akan bisa menyangkalnya."
        jump subscene_6d
   
    #scene 6d
    label subscene_6d:
        #visual: Gudang pabrik dengan pencahayaan minim. Bima dan timnya menyusup ke dalam gudang melalui pintu samping yang sedikit terbuka. Kotak-kotak besar berjejer di sudut ruangan, beberapa di antaranya memiliki tanda yang mencurigakan.
        n "Bima dan timnya memasuki gudang dengan hati-hati. Mereka menyadari bahwa apa pun yang disembunyikan di sini, itu bukan sesuatu yang ingin diketahui publik."
        ah "Pak Bima, lihat tanda di kotak itu. Itu bukan logo perusahaan resmi. Apa ini mungkin barang selundupan?"
        b "Hanya ada satu cara untuk tahu pasti. Kita harus membuka salah satu kotak ini."
        menu: 
            "Membuka kotak dengan hati-hati tanpa meninggalkan jejak.":
                jump pilihan1_6d
            "Mengambil risiko dengan memecahkan segel untuk melihat isinya lebih cepat.":
                jump pilihan2_6d
        label pilihan1_6d:
            #visual:Bima menggunakan alat kecil untuk membuka tutup kotak tanpa merusak segel. Dia menarik nafas dalam-dalam sebelum mengintip ke dalam.
            b "Lihat ini. Barang elektronik mahal? Ini tidak tercatat dalam inventaris resmi perusahaan."
            ah "Barang elektronik seperti ini seharusnya diimpor dengan izin tertentu. Jika ini ilegal, maka ini adalah bukti kuat."
            jump lanjutan_scene_6d
        label pilihan2_6d:
            #visual: Dengan sedikit dorongan, segel kotak terbuka. Bima menarik isinya ke luar—tumpukan dokumen dan barang-barang kecil.
            b "Ini lebih dari sekadar selundupan. Lihat dokumen ini. Ada catatan transaksi rahasia, dengan tanda tangan yang menghubungkan Hardi langsung ke jaringan ini." #ekspresi serius
            ah "Itu tanda tangan pejabat! Mereka menggunakan pabrik ini untuk menutupi kegiatan ilegal!" #terkejut
            jump lanjutan_scene_6d
        label lanjutan_scene_6d:
            b "Ini bukan hanya masalah selundupan barang. Ini adalah korupsi besar-besaran. Mereka menggunakan pabrik ini sebagai kedok untuk mengalihkan uang gelap."
            ah "Jika kita bisa membawa dokumen ini ke publik, ini akan menghancurkan mereka. Tapi kita harus berhati-hati. Mereka pasti tidak akan tinggal diam."
            ba "Pak, saya tahu tempat lain di gudang ini. Kadang-kadang ada kotak dengan bahan kimia yang sangat dijaga. Mungkin itu juga terkait."
            b "Kalau begitu, kita harus mencari kotak itu juga. Kalau mereka menyelundupkan bahan kimia tanpa izin, ini akan jadi bukti tambahan."
            #visual: Di sudut gudang yang lebih gelap, Bima dan tim menemukan beberapa drum besar berlabel bahan kimia. Salah satunya bocor, dan bau tajam menguar dari drum tersebut.
            ah "Apa ini? Bahan kimia seperti ini seharusnya tidak ada di pabrik biasa. Ini bisa sangat berbahaya."
            b "Ini lebih buruk dari yang saya kira. Mereka tidak hanya menyelundupkan barang ilegal, tapi juga membahayakan keselamatan pekerja dan lingkungan."
            ba "Pak, kita harus pergi sekarang. Kalau penjaga tahu kita di sini, kita tidak akan bisa keluar."
            menu:
                "Segera keluar dengan bukti yang sudah ditemukan.":
                    jump pilihan1_lanjutan_6d
                "Mengambil risiko untuk mencari lebih banyak bukti.":
                    jump pilihan2_lanjutan_6d
            label pilihan1_lanjutan_6d:
                n "Bima dan tim memutuskan untuk segera keluar sebelum menarik perhatian. Dengan bukti di tangan, mereka tahu ini sudah cukup untuk memulai langkah berikutnya."
                jump ending_scene_6d
            label pilihan2_lanjutan_6d:
                #visual: Bima bergerak lebih dalam ke gudang dan menemukan kotak-kotak yang lebih besar. Salah satu kotak memiliki label 'Tertutup – Hanya untuk Pengiriman Khusus'.
                b "Ini dia. Lihat isi kotak ini. Barang mewah dan obat-obatan? Ini jelas penyelundupan besar."
                ah "Ini cukup untuk menghancurkan mereka. Tapi penjaga akan segera tahu kita di sini. Kita harus pergi sekarang!"
                n "Meskipun berisiko, keputusan Bima untuk mencari lebih banyak bukti memberikan keunggulan strategis. Dengan data yang lebih lengkap, ia kini memiliki kekuatan untuk melawan musuh-musuhnya."
                jump ending_scene_6d
            label ending_scene_6d:
                n "Setelah berhasil keluar dari gudang, Bima dan timnya menyusun kembali semua bukti yang mereka kumpulkan. Barang selundupan, bahan kimia berbahaya, dan dokumen yang menghubungkan pejabat dengan pengusaha."
                n "Semua ini menjadi kunci untuk membongkar jaringan korupsi yang telah lama tersembunyi." 
    # This ends the game.

    return

