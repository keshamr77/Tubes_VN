# Mendefinisikan karakter
define b = Character("Bima", image="characters/MC_Default.png")
define ibu = Character("Ibunda Bima", color="#ff9999")
define psa = Character("Politisi Senior A", color="#9999ff")
define psb = Character("Politisi Senior B", color="#6666cc")
define asisten = Character("Asisten Parlemen", color="#66cc66")
define lp = Character("Ketua Sidang", color="#ffc0cb")
define mp = Character("Anggota Parlemen Muda", color="#ffcc00")
define tk = Character("Tim Konstituen Bima", color="#e39803")
define ba = Character("Buruh A", color="#cc9966")
define bb = Character("Buruh B", color="#9966cc")
define bc = Character("Buruh C", color="#1ea5f9fc")
define bd = Character("Buruh D", color="#f94ef3")
define be = Character("Buruh E", color="#cc6666")
define ka = Character("Kolega A", color="#ffcc00")
define kb = Character("Kolega B", color="#1ea5f9fc")
define pk = Character("Pejabat Korup", color="#cc6666")
define ah = Character("Aktivis HAM", color="#abff4b")
define pdk = Character("Politisi Pendukung Kebijakan",color="#6666cc")
define va = Character("Asisten", color="#9966cc")
define eb = Character("Pengusaha Tamak", color="#cc6666")
define h = Character("Hardi",color="#cc6666")
define wi = Character("Wartawan Independen", color="#f94ef3")
define mp = Character("Mantan Pekerja", color="#ffcc00")

#Character expressions
image b default = "characters/MC_Default.png"
image b happy = "characters/MC_Happy.png"
image b angry = "characters/MC_angry.png"
image b worried = "characters/MC_worried.png"
image ibu = "characters/Ibu.png"
image ba silhouette =  "characters/Buruh_Telfon.png"
image bb rame = "characters/Buruh_Ramai.png"
image h default = "characters/Pengusaha_Default.png"
image h angry = "characters/Pengusaha_angry.png"

# Background Definitions
image bg parliament_chamber = im.Scale("backgrounds/parliament_chamber.jpg", 1920, 1080)
image bg parliament_hall = im.Scale("backgrounds/parliament_hall.png", 1920, 1080)
image bg bima_office_sore = im.Scale("backgrounds/bima_office_sore.png", 1920, 1080)
image bg bima_office_pagi = im.Scale("backgrounds/bima_office_pagi.png", 1920, 1080)
image bg bima_office_malam = im.Scale("backgrounds/bima_office_malam.jpg", 1920, 1080)
image bg living_room = im.Scale("backgrounds/living_room.jpg", 1920,1080)
image bg pabrik= im.Scale("backgrounds/pabrik.jpg", 1920,1080)
image bg gudang= im.Scale("backgrounds/gudang.jpg", 1920,1080)
image bg bussiness_office = im.Scale("backgrounds/kantor_pengusaha.png", 1920, 1080)
image bg restaurant = im.Scale("backgrounds/restoran.png", 1920,1080)

# Music Definitions
define bgm_conflict = "music/conflict_bgm.mp3"
define bgm_flashbacks = "music/flashbacks_bgm.mp3"


# Transformations 
transform zoomed_for_silhoutte:
    xpos 0.5
    ypos 0.3
    zoom 2.8

# Scene pertama dengan background
label start:
    $ renpy.music.stop()
    
    #START OF ARC 1
    play music bgm_flashbacks fadein 1.0 loop

    # Scene 1: Rumah Bima - Refleksi Masa Lalu
    scene bg living_room with fade  # Background: ruang tamu
    "Di malam yang tenang, Bima duduk di depan meja. Pikirannya melayang ke masa lalu—sebuah masa penuh luka dan kehilangan yang membentuk dirinya hingga hari ini."
    show ibu at zoomed_for_silhoutte with dissolve
    ibu "Cepat, Bima! Kita harus keluar sebelum mereka datang!"
    b "Tapi Ibu, kenapa kita harus pergi? Ini rumah kita!"
    "Bima muda tidak pernah melupakan malam itu—malam di mana keluarganya kehilangan segalanya karena keputusan segelintir orang di atas."
    hide ibu
    
    # Kembali ke masa kini
    show bg bima_office_pagi with fade
    "Kembali ke masa kini. Bima menatap foto mendiang ayahnya di meja."
    show b default at Position(xpos=0.3, ypos=2.0) with dissolve
    b "(Ayah, malam itu aku tidak bisa melakukan apa-apa. Tapi sekarang aku punya kesempatan untuk melawan mereka yang mengambil segalanya dari kita.)"

    # Scene 2: Kantor Parlemen - Hari Pertama Bima
    scene bg parliament_hall at truecenter with dissolve # Background: kantor parlemen
    "Hari pertama di parlemen. Bima tahu, ini bukan hanya pekerjaan. Ini adalah perjuangan untuk mereka yang tidak memiliki suara."
    asisten "Pak Bima, selamat datang. Rapat pertama Anda akan dimulai dalam satu jam. Semua anggota sudah tidak sabar mendengar ide-ide segar Anda."
    show b default at Position(xpos=0.3, ypos=2.0) with dissolve
    b "Terima kasih. Saya akan memastikan mereka mendengar apa yang perlu mereka dengar."

    # Scene 3: Sidang Parlemen - Idealisme yang Ditantang
    scene bg parliament_chamber at truecenter with dissolve # Background: ruang sidang
    "Hari pertama Bima sebagai wakil rakyat dimulai dengan sidang pleno. Atmosfer di ruangan itu tegang, penuh pembicaraan tentang rancangan undang-undang yang kontroversial terkait kebijakan tenaga kerja."
    lp "Sebelum kita melanjutkan pembahasan, izinkan saya memperkenalkan anggota baru kita. Bima, dari daerah pemilihan Jawa Timur. Anda memiliki waktu untuk memperkenalkan diri dan pandangan Anda. Silakan."
    "Semua mata tertuju pada Bima. Beberapa politisi tampak menilai, yang lain acuh tak acuh."
    show b default at Position(xpos=0.3, ypos=2.0) with dissolve
    b "Terima kasih atas kesempatan ini. Saya Bima, dan saya merasa terhormat dapat berdiri di sini hari ini. Tapi saya juga tahu, kehormatan ini datang dengan tanggung jawab besar."
    "Beberapa politisi mulai memperhatikan lebih serius."
    b "Sebagai wakil rakyat, tugas utama kita adalah mendengar suara mereka yang memilih kita. Namun, saya tidak bisa mengabaikan kenyataan bahwa ada begitu banyak suara yang tidak terdengar—mereka yang tidak punya kesempatan untuk berbicara di tempat seperti ini."
    pe "Saudara Bima, itu pidato yang indah. Tapi izinkan saya bertanya: apakah Anda tahu betapa sulitnya membawa perubahan dalam sistem yang sudah mapan ini?"
    
    menu:
        "Menjawab dengan sopan namun percaya diri":
            b "Saya mengerti bahwa perubahan itu sulit. Tapi saya percaya, setiap langkah kecil bisa membawa kita ke arah yang lebih baik. Saya di sini untuk memulai langkah itu."
            "Jawaban Bima menunjukkan kedewasaan. Beberapa politisi terlihat sedikit terkesan, meskipun skeptisisme tetap terlihat di wajah mereka."
            psb "Hmph, langkah kecil tidak akan berarti apa-apa jika Anda tidak memiliki dukungan yang cukup."
            b "(Dukungan? Kalau begitu, aku harus membuktikan diriku terlebih dahulu.)"
        
        "Menegaskan pendapat dengan berani":
            b "Sistem ini mapan, tapi tidak sempurna. Tugas kita bukan untuk menerima kenyataan, melainkan untuk memperbaikinya. Saya yakin, jika kita bekerja sama, kita bisa membawa perubahan."
            "Kata-kata Bima mengundang perhatian yang lebih besar, tetapi juga beberapa tatapan dingin dari anggota parlemen yang merasa terganggu oleh keberaniannya."
            psa "Berani sekali bicara seperti itu di hari pertama Anda. Kita lihat apakah Anda masih bisa bicara besar setelah satu tahun di sini."
            b "(Mungkin aku baru di sini, tapi aku tidak akan membiarkan intimidasi menghentikan langkahku.)"

    # Debat Parlemen: Kebijakan Tenaga Kerja
    lp "Baiklah, mari kita lanjutkan ke agenda hari ini: pembahasan mengenai rancangan undang-undang ketenagakerjaan. Ada pendapat dari pihak pendukung?"
    "Seorang politisi berdiri, berbicara dengan penuh percaya diri."
    psa "Rancangan ini penting untuk meningkatkan daya saing tenaga kerja kita di pasar internasional. Fleksibilitas jam kerja dan efisiensi tenaga kerja akan memberikan keuntungan besar bagi ekonomi kita."
    show b worried at Position(xpos=0.3, ypos=2.0) with dissolve
    b "(Keuntungan ekonomi? Bagaimana dengan nasib para buruh yang jam kerjanya diperpanjang tanpa perlindungan?)"
    
    show b default at Position(xpos=0.3, ypos=2.0) with dissolve
    menu:
        "Memprotes langsung rancangan tersebut dengan argumen yang tajam":
            show b angry at Position(xpos=0.3, ypos=2.0) with dissolve
            b "Maaf, tapi saya tidak bisa mendukung rancangan ini. Apakah kita mempertimbangkan bagaimana fleksibilitas ini akan mempengaruhi para buruh? Mereka sudah bekerja terlalu keras untuk upah yang tidak layak. Menambah jam kerja hanya akan memperburuk keadaan mereka."
            psb "Saudara Bima, ini bukan hanya tentang buruh. Ini tentang ekonomi negara kita. Jika buruh tidak kompetitif, siapa yang akan berinvestasi di sini?"
            b "Dan apa gunanya investasi jika masyarakat yang kita wakili hidup dalam penderitaan? Prioritas kita harus selalu rakyat, bukan angka di laporan ekonomi."

        "Mengajukan pertanyaan untuk menggiring diskusi ke isu buruh":
            b "Saya punya pertanyaan. Bagaimana rancangan ini memastikan bahwa hak buruh tetap terlindungi? Apakah ada mekanisme untuk mencegah eksploitasi tenaga kerja?"
            psb "Hmm, tentu saja, ada regulasi tambahan yang akan kita bahas nanti. Tapi fokus kita sekarang adalah pada daya saing."
            b "Kalau begitu, saya berharap pembahasan itu menjadi prioritas. Daya saing tidak ada artinya jika tenaga kerja kita diperlakukan seperti mesin tanpa batas."

            "Pendekatan Bima yang tenang tetapi tajam menarik perhatian lebih banyak anggota parlemen. Beberapa mulai mempertimbangkan ulang pandangan mereka."
    
    # Scene lorong parlemen after scene 3
    scene bg parliament_hall at truecenter with dissolve # Background: kantor parlemen
    mp "Pak Bima, Anda berbicara dengan sangat baik tadi. Tidak banyak orang yang berani mempertanyakan kebijakan seperti itu."
    show b happy at Position(xpos=0.3, ypos=2.0) with dissolve
    b "Terima kasih. Tapi ini baru awal. Masih banyak yang perlu diperjuangkan."
    mp "Saya setuju. Kalau Anda butuh dukungan, saya ada di pihak Anda."
    "Bima mulai mendapatkan sekutu, meskipun perjuangan keadilan masih panjang."

    #Narasi penutup scene 3
    "Hari pertama Bima di parlemen adalah ujian, bukan hanya bagi idealismenya, tetapi juga bagi tekadnya untuk membawa perubahan. Dengan suara rakyat di hatinya, dia melangkah ke dalam sistem yang penuh tantangan, bertekad untuk membuat perbedaan."

    # Scene 4: Ruang Kerja Bima - Penemuan Masalah Awal
    scene bg bima_office_sore with fade  # Background: ruang kerja Bima
    "Hari pertama setelah sidang penuh tantangan, Bima kembali ke ruang kerjanya. Di sini, ia mulai menelaah laporan-laporan yang disampaikan oleh masyarakat. Setiap lembar laporan adalah gambaran tentang ketidakadilan yang masih terjadi di luar sana."
    
    show b angry at Position(xpos=0.3, ypos=2.0) with dissolve
    b "Gaji di bawah standar, jam kerja panjang, dan tidak ada jaminan perlindungan bagi pekerja. Bahkan, laporan ini menyebutkan beberapa pekerja dipecat karena mencoba menyuarakan hak mereka. Ini tidak bisa dibiarkan."
    "Bima menghela napas panjang, lalu meraih telepon di mejanya. Dia menghubungi tim konstituennya di daerah asalnya."

    show b default at Position(xpos=0.3, ypos=2.0) with dissolve
    # Diskusi dengan Tim Konstituen
    tk "Halo, Pak Bima. Apa kabar?"
    b "Halo, semuanya baik. Saya baru menerima laporan tentang pabrik di kawasan industri kita yang mengeksploitasi buruh. Apa ini benar? Bisa Anda ceritakan lebih rinci?"
    tk "Betul, Pak. Sudah ada beberapa laporan masuk dari pekerja di sana. Masalahnya, mereka takut berbicara terbuka karena khawatir dipecat. Salah satu buruh senior kami tahu masalah ini lebih dalam. Saya bisa coba mengatur agar Anda bisa bicara langsung dengannya."
    b "Itu akan sangat membantu. Tolong atur supaya saya bisa berbicara dengannya, tapi pastikan dia merasa aman."

    "Dengan bantuan timnya di daerah, Bima akhirnya berhasil menjalin kontak dengan salah satu buruh yang berani berbicara."
    # Sesi telepon dengan buruh"
    show ba silhouette at Position(xpos=0.7) with dissolve

    ba "Pak Bima, terima kasih sudah meluangkan waktu untuk kami. Saya bekerja di pabrik itu hampir 10 tahun. Belakangan ini, kondisi kami semakin buruk. Jam kerja bertambah, tapi gaji tetap kecil. Beberapa teman saya bahkan dipecat setelah mencoba mengajukan protes."
    b "Saya mendengar masalah ini dari laporan. Tapi saya ingin memastikan, apa Anda memiliki bukti, atau ada orang lain yang bisa mendukung cerita ini?"
    ba "Kami punya dokumen slip gaji dan daftar jam kerja yang tidak sesuai dengan kontrak. Tapi kalau kami ketahuan, risikonya terlalu besar. Tolong bantu kami, Pak."
    b "Tenang. Saya akan datang ke tempat Anda dalam beberapa hari. Kita akan bertemu secara aman dan mendiskusikan ini lebih jauh. Saya akan memastikan suara Anda terdengar, tapi Anda juga harus berhati-hati."
    "Bima tahu, ini bukan masalah sederhana. Tapi suara dari buruh itu memberinya alasan lebih kuat untuk bertindak. Dia menyadari bahwa untuk membawa perubahan, dia harus turun langsung ke lapangan."

    # Visual bima meletakkan telepon meraih dokumen dimejanya dan menatap catatan pada papan tulisnya
    b "(Sistem ini cacat, dan aku tidak bisa memperbaikinya hanya dari balik meja. Aku harus melihat langsung, mendengar langsung, dan berjuang bersama mereka.)"
    
    # Scene 5: Pabrik Buruh - Investigasi Awal
    scene bg pabrik with fade  
    "Dengan bantuan tim konstituennya, Bima berhasil mengatur pertemuan rahasia dengan beberapa buruh pabrik. Meski pertemuan ini sederhana, bagi para buruh, ini adalah momen penuh harapan."

    # Perjalanan menuju gudang tempat pertemuan
    scene bg gudang with fade  
    "Bima berjalan melewati lorong sempit menuju sebuah gudang kosong di belakang pabrik, tempat pertemuan akan diadakan. Sekelompok buruh menunggu di sana, wajah mereka menunjukkan kelelahan dan kecemasan."
    
    show b default at Position(xpos=0.3, ypos=2.0) with dissolve
    # Pertemuan dengan buruh
    b "Terima kasih sudah meluangkan waktu untuk bertemu dengan saya. Saya tahu ini tidak mudah, tapi saya ingin mendengar langsung apa yang kalian alami."
    show bb rame with dissolve
    ba "Pak Bima, terima kasih juga sudah meluangkan waktu untuk bertemu dengan kami. Kami tidak tahu harus bicara ke siapa lagi. Kami sudah mencoba menyampaikan keluhan, tapi tidak ada yang peduli."
    bb "Semakin lama, kondisi kerja kami makin buruk. Jam kerja ditambah tanpa pemberitahuan, tapi gaji tetap kecil. Mereka juga mulai memotong tunjangan kesehatan."
    b "Saya sudah membaca laporan kalian, tapi saya ingin mendengar lebih rinci. Apa ada bukti yang bisa membantu kita memperkuat argumen ini? Dokumen atau catatan yang menunjukkan pelanggaran mereka?"
    bc "Ada, Pak. Beberapa teman kami diam-diam mencatat jam kerja yang tidak sesuai kontrak. Tapi kami takut, Pak. Kalau ketahuan, kami bisa dipecat."
    b "Saya mengerti. Kalian punya alasan untuk khawatir. Tapi kita harus hati-hati. Bukti ini sangat penting untuk membawa kasus kalian ke tingkat yang lebih tinggi."

    # Buruh yang skeptis
    "Di tengah percakapan, salah satu buruh tiba-tiba berdiri. Wajahnya terlihat penuh amarah."
    bd "Apa gunanya semua ini, Pak Bima? Kami sudah mencoba protes sebelumnya, tapi malah diberhentikan! Bos hanya peduli pada keuntungan. Tidak ada yang peduli dengan kami!"
    b "Saya tahu kalian merasa putus asa. Tapi percayalah, jika kita bergerak bersama dengan bukti yang kuat, kita bisa membawa masalah ini ke meja hukum. Saya tidak akan membiarkan mereka lolos begitu saja."

    menu:
        "Mengumpulkan bukti melalui wawancara dan dokumen":
            b "Kita mulai dari langkah kecil. Kumpulkan semua dokumen yang menunjukkan pelanggaran: slip gaji, jam kerja, atau kontrak yang tidak dipatuhi. Saya akan mengatur agar semua ini tetap aman."
            bb "Tapi, bagaimana kalau mereka tahu, Pak? Kami bisa kehilangan pekerjaan."
            b "Saya akan memastikan kalian tidak sendirian. Jika kalian bersatu, suara kalian akan lebih kuat. Percayalah, saya di sini untuk melindungi kalian."
            "Dengan hati-hati, para buruh mulai menyerahkan beberapa dokumen yang mereka kumpulkan. Bima mencatat semua informasi dengan saksama, memastikan mereka merasa aman dan didengar."
        
        "Mengorganisir buruh untuk memulai protes besar":
            b "Jika kita ingin perubahan cepat, kita harus bersatu. Kita bisa mengorganisir protes damai untuk menunjukkan bahwa suara kalian tidak bisa diabaikan."
            ba "Protes? Itu berisiko besar, Pak. Mereka bisa memanggil polisi untuk membubarkan kami."
            b "Risiko itu ada, tapi kita akan melakukannya dengan cara yang aman. Kita libatkan media dan organisasi HAM untuk memastikan bahwa mereka tidak bisa bertindak semena-mena. Ini bukan hanya tentang kalian, tapi tentang ribuan buruh lain yang menghadapi masalah serupa."
            "Setelah diskusi panjang, sebagian buruh setuju untuk mulai mengorganisir protes. Namun, rasa takut tetap ada di antara mereka."
    
    # Tantangan buruh yang skeptis
    be "Pak Bima, saya sudah lama bekerja di sini. Bos kami punya banyak koneksi, bahkan ke pejabat tinggi. Apa Anda yakin bisa melawan mereka?"
    b "Saya tidak bisa menjanjikan kemenangan instan, tapi saya bisa menjanjikan ini: saya akan berdiri di sisi kalian sampai akhir. Sistem ini tidak akan berubah jika kita hanya diam."
    be "(Orang ini berbeda dari politisi lain. Mungkin... dia benar-benar peduli.)"

    #Narasi akhir scene 5
    "Malam itu, Bima meninggalkan kawasan pabrik dengan membawa dokumen dan kesaksian buruh. Di pikirannya, dia tahu ini hanya awal dari perjuangan yang panjang. Tapi dia juga tahu, setiap langkah kecil membawa harapan untuk perubahan."

    # Narasi penutup untuk Arc 1
    scene bg bima_office_malam with fade
    show b happy at Position(xpos=0.3, ypos=2.0) with dissolve
    b "(Ini baru awal. Masalah ini lebih besar dari yang aku bayangkan. Tapi aku sudah siap untuk melangkah lebih jauh.)"

    # START OF ARC 2

    # Scene 1: Sidang Parlemen - Meningkatkan Taruhan
    scene bg parliament_chamber with dissolve # Background: ruang sidang
    "Setelah pernyataan beraninya di sidang sebelumnya, Bima kini menghadapi ujian yang lebih berat. Rancangan kebijakan yang memihak pengusaha telah kembali ke meja parlemen, dan tekanan untuk diam semakin besar."

    lp "Sidang hari ini akan membahas finalisasi rancangan kebijakan tenaga kerja. Kami meminta anggota yang ingin berbicara untuk mengajukan pendapat mereka."
    
    "Semua mata tertuju pada Bima, yang telah menjadi sorotan sejak sidang sebelumnya. Beberapa politisi tersenyum sinis, sementara yang lain mengangguk pelan, mendukungnya secara diam-diam."
    show b worried at Position(xpos=0.3, ypos=2.0) with dissolve
    b "(Mereka sedang menunggu aku membuat kesalahan. Tapi aku tidak boleh diam. Rakyat membutuhkan suara ini.)"
    
    menu:
        "Berbicara dengan tenang dan penuh perhitungan.":
            show b default at Position(xpos=0.3, ypos=2.0) with dissolve
            b "Terima kasih atas kesempatannya. Saya ingin mengingatkan bahwa kebijakan ini harus melindungi semua pihak, termasuk buruh yang menjadi tulang punggung ekonomi kita. Jika kita hanya memihak pengusaha, kita akan menciptakan ketimpangan yang lebih dalam."
            psa "Pak Bima, Anda berbicara tentang ketimpangan, tetapi apakah Anda memahami kebutuhan investasi? Kita butuh investor untuk menciptakan lapangan kerja."
            b "Saya paham pentingnya investasi. Namun, investasi yang dibangun di atas ketidakadilan hanya akan merusak fondasi bangsa kita. Kita bisa mendukung pengusaha tanpa mengorbankan hak buruh."
            "Pendekatan Bima yang tenang berhasil menarik perhatian beberapa anggota parlemen. Namun, skeptisisme tetap kuat, terutama dari pihak pendukung kebijakan."

        "Langsung menyerang dengan bukti awal yang dimiliki.":
            show b angry at Position(xpos=0.3, ypos=2.0) with dissolve
            b "Rancangan kebijakan ini bukan hanya soal ekonomi, tetapi juga soal moralitas. Saya telah melihat sendiri bagaimana pengusaha besar menggunakan kekuasaan mereka untuk menindas buruh, dan bukti ini hanya sebagian kecil dari apa yang saya temukan."
            "Bima menunjukkan dokumen awal yang mengungkap pelanggaran jam kerja dan gaji minimum di pabrik besar. Ruangan sidang menjadi sunyi, namun ketegangan meningkat."
            psb "Apa maksud Anda dengan ini? Tuduhan ini tidak berdasar. Anda hanya mencoba memancing perhatian."
            b "Kalau memang tidak berdasar, kenapa Anda terlihat begitu defensif? Saya hanya menginginkan transparansi. Jika kebijakan ini sah, maka tidak ada yang perlu disembunyikan."
            "Strategi Bima berhasil memancing reaksi keras dari pihak pendukung kebijakan, tetapi juga menarik dukungan dari beberapa anggota parlemen independen."

    # Scene 2: Konflik Internal - Rekan Parlemen Ragu
    ka "Bima, apa yang kamu lakukan? Kamu tahu mereka tidak akan tinggal diam. Mereka punya kekuatan untuk menjatuhkanmu."
    show b angry at Position(xpos=0.3, ypos=2.0) with dissolve
    b "Kalau aku diam, lalu siapa yang akan bicara untuk rakyat? Aku tidak peduli risiko ini, selama aku tahu aku berada di pihak yang benar."
    kb "Hati-hati, Bima. Kita mendukungmu, tapi jangan membuat mereka merasa terlalu terpojok. Mereka bisa balas menyerang."

    # Scene 3: Konfrontasi dengan Pejabat Korup
    pk "Pak Bima, saya memahami semangat Anda sebagai anggota baru di parlemen. Namun, izinkan saya memberi sedikit masukan. Dunia politik tidak sesederhana yang Anda bayangkan. Terkadang, kompromi adalah jalan terbaik untuk mencapai tujuan besar."
    b "Kompromi? Apa yang Anda maksud dengan kompromi, Pak? Membiarkan rakyat terus menderita demi menjaga keuntungan segelintir pihak?"
    
    pk "Anda salah paham. Tidak ada yang ingin rakyat menderita. Namun, kita juga harus berpikir realistis. Dunia tidak bekerja dengan idealisme, Pak Bima. Anda perlu memahami bahwa roda ekonomi harus terus berputar, dan itu membutuhkan keseimbangan, meskipun terkadang ada yang harus berkorban."
    
    b "(Dia berbicara tentang keseimbangan, tetapi jelas ini hanyalah pembenaran untuk membiarkan ketidakadilan terus terjadi. Aku harus memilih kata-kataku dengan hati-hati.)"
    
    menu:
        "Menanggapi dengan sopan dan logis.":
            b "Saya menghargai masukan Anda, Pak. Memang benar bahwa dunia tidak sempurna, dan terkadang kita harus membuat keputusan sulit. Namun, saya percaya bahwa keputusan sulit tidak boleh mengorbankan prinsip dasar keadilan."
            pk "Prinsip dasar keadilan? Prinsip itu bagus di atas kertas, tapi kita bekerja di dunia nyata, Pak Bima. Kalau kita terlalu berpihak pada satu sisi, sisi lainnya akan runtuh."
            b "Tugas kita di sini adalah menjaga agar tidak ada yang runtuh, Pak. Jika kita memihak buruh, bukan berarti kita menolak pengusaha. Kita hanya meminta mereka untuk memenuhi kewajiban mereka, yang seharusnya tidak menjadi beban besar bagi mereka."
            pk "Menarik sekali, Pak Bima. Anda berbicara seperti orang yang tidak pernah bekerja dengan anggaran besar atau tekanan investor. Apa Anda yakin bisa memahami kompleksitas masalah ini?"
            b "Saya mungkin belum pernah bekerja dengan investor besar, tapi saya bekerja dengan rakyat kecil setiap hari. Saya mendengar keluhan mereka, dan itu cukup untuk memahami bahwa sistem ini perlu diperbaiki, bukan dipertahankan."
            "Pendekatan diplomatis Bima menarik perhatian beberapa anggota parlemen. Beberapa terlihat mengangguk setuju, meskipun ketegangan dengan pejabat korup itu tidak berkurang."

        "Menyerang balik dengan mempertanyakan integritasnya.":
            b "Pak, maaf kalau saya salah paham, tapi dari cara Anda berbicara, sepertinya yang Anda maksud dengan keseimbangan adalah membiarkan ketidakadilan terus terjadi demi keuntungan segelintir pihak."
            pk "Anda menuduh tanpa bukti, Pak Bima. Hati-hati dengan kata-kata Anda. Tuduhan seperti ini bisa berbalik kepada Anda."
            b "Saya tidak menuduh, Pak. Saya hanya bertanya. Jika kebijakan ini benar-benar adil, mengapa buruh di lapangan mengatakan bahwa mereka tidak pernah dilibatkan dalam diskusi? Mengapa ada begitu banyak pelanggaran terhadap hak dasar mereka yang dibiarkan begitu saja?"
            pk "Pak Bima, dunia ini tidak hanya hitam dan putih. Kalau Anda terus mendesak seperti ini, Anda akan menemukan banyak musuh. Apa Anda siap menghadapi itu?"
            b "Jika membela rakyat kecil membuat saya punya banyak musuh, maka biarlah begitu. Saya lebih baik kalah dengan prinsip daripada menang dengan cara mengkhianati mereka yang mempercayakan suara mereka kepada saya."
            "Pernyataan Bima membuat ruangan menjadi sunyi. Beberapa anggota parlemen mulai memandangnya dengan kagum, sementara pejabat korup itu tersenyum tipis, menyembunyikan rasa tidak senangnya."
            pk "(Anak muda ini terlalu berani. Kita lihat sampai kapan dia bisa bertahan.)"

    # Narasi Penutup Scene
    scene bg parliament_hall with dissolve
    "Pertukaran kata-kata antara Bima dan pejabat korup itu menjadi momen penting di sidang hari itu. Bima tahu bahwa dia telah membuat lawannya merasa terancam, tetapi dia juga menyadari bahwa serangan balik dari pihak mereka tidak akan lama lagi."

    # Scene 2 : Investigasi Lapangan - Menyusun Bukti
    scene bg pabrik with fade  
    ba "Pak Bima, ini semua dokumen yang kami punya. Slip gaji, laporan jam kerja, dan foto kondisi tempat kerja kami. Tapi hati-hati, dokumen ini bisa membuat mereka marah jika mereka tahu kami yang menyerahkannya."
    b "Kalian sudah melakukan hal yang luar biasa. Saya akan memastikan bukti ini digunakan dengan hati-hati. Tidak ada yang akan tahu siapa yang memberikan ini."
    ah "Pak Bima, kita punya cukup bukti untuk menekan parlemen. Tapi saya tahu para pejabat yang terkait pasti akan menyerang balik. Kita harus bersiap."
    b "Saya tidak akan mundur. Saya akan membawa ini ke meja parlemen, apa pun risikonya."
    "Dengan bukti di tangan, Bima tahu langkah berikutnya adalah mempresentasikan kasus ini di parlemen. Namun, ia juga sadar bahwa musuhnya, terutama pejabat korup dan pengusaha besar, tidak akan tinggal diam."

    scene bg bima_office_malam with fade
    b "(Bukti ini kuat, tapi akan sulit untuk membuat semua pihak mendengar. Aku harus melangkah hati-hati, karena musuhku ada di sini, di ruang parlemen ini sendiri.)"

    scene bg parliament_chamber with fade
    lp "Anggota Bima, Anda meminta waktu untuk menyampaikan pendapat Anda tentang rancangan kebijakan ini. Silakan."
    "Bima berdiri, membawa dokumen dari investigasi lapangannya. Ia mengambil napas dalam-dalam sebelum mulai berbicara."
    b "Terima kasih, Ketua Sidang. Hari ini, saya ingin membahas apa yang sering kali terabaikan dalam rancangan kebijakan ini: nasib buruh. Selama beberapa minggu terakhir, saya telah turun langsung ke lapangan untuk mendengar suara mereka."
    b "Yang saya temukan sungguh mengkhawatirkan. Jam kerja yang melebihi batas hukum, gaji yang jauh di bawah standar, dan tempat kerja yang tidak aman. Semua ini adalah pelanggaran yang nyata terhadap hak asasi manusia."
    "Bima menunjukkan dokumen-dokumen yang dibawanya kepada anggota parlemen lain."
    pdk "Apa yang Anda bawa ini hanya laporan sepihak. Kita tidak bisa menyusun kebijakan berdasarkan cerita yang tidak terverifikasi, Pak Bima."
    b "Laporan ini bukan sekadar cerita. Ini bukti. Dokumen ini menunjukkan pemotongan gaji ilegal, laporan medis buruh yang terluka akibat kondisi kerja, dan catatan jam kerja yang melebihi batas hukum. Apa ini masih Anda anggap cerita sepihak?"
    "Pejabat Korup, yang sejak tadi diam, akhirnya bangkit berdiri. Ia tersenyum kecil, mencoba mencairkan suasana."
    pk "Anda berbicara dengan semangat yang luar biasa. Tapi izinkan saya bertanya: apakah Anda paham betapa sulitnya mengatur keseimbangan antara kebutuhan pengusaha dan hak buruh? Dunia ini tidak hanya hitam dan putih, Pak Bima."

    menu :
        "Menanggapi dengan sopan dan logis." :
            b "Saya paham bahwa ini tidak mudah, Pak. Tapi tugas kita di sini adalah membuat keputusan yang adil untuk semua pihak, bukan hanya untuk mereka yang memiliki kuasa. Jika keseimbangan yang Anda maksud adalah terus membiarkan pelanggaran ini, maka saya rasa itu bukan keseimbangan, melainkan ketidakadilan."
            pk "Tuduhan Anda terlalu berat untuk sesuatu yang Anda anggap 'ketidakadilan'. Hati-hati, Pak Bima. Anda bisa melangkah terlalu jauh."
        "Menyerang balik dengan mempertanyakan integritasnya." :
            b "Keseimbangan? Apa yang Anda maksud dengan keseimbangan adalah memberikan kekuasaan mutlak kepada pengusaha dan membiarkan buruh menjadi korban? Kalau begitu, saya tidak ingin menjadi bagian dari keseimbangan itu."
            pk "Kata-kata Anda keras, Pak Bima. Tapi keras kepala saja tidak cukup untuk membuat perubahan. Apa Anda yakin bisa menghadapi konsekuensi dari ucapan Anda?"
            b "Kalau memperjuangkan keadilan membawa konsekuensi, maka saya akan menerimanya. Yang tidak bisa saya terima adalah diam melihat rakyat terus menderita."
    
    "Dialog itu menjadi momen puncak dalam sidang hari itu. Bima telah membuat musuhnya merasa terpojok, tetapi ia juga tahu bahwa serangan balik dari mereka tidak akan lama lagi. Pejabat korup itu duduk kembali dengan senyum tipis, merencanakan langkah selanjutnya."
    "Dengan bukti yang kuat dan dukungan yang mulai tumbuh, Bima harus bersiap menghadapi langkah selanjutnya. Lawannya, pejabat korup dan pengusaha besar, pasti akan mencoba membalas serangan ini. Namun, Bima tahu, perjuangannya baru dimulai."

    # Scene 3 : Munculnya Pengusaha Tamak
    scene bg bussiness_office with fade
    va "Pak, Anda mungkin ingin melihat ini. Anggota parlemen baru, Bima, baru saja mempresentasikan bukti tentang pelanggaran di pabrik Anda dalam sidang tadi."
    eb "Bima, ya? Anak baru yang penuh idealisme itu? Aku sudah mendengar tentangnya. Dia terlalu bersemangat untuk kebaikannya sendiri."
    va "Bukti yang dia tunjukkan cukup kuat, Pak. Jika ini terus berlanjut, reputasi Anda bisa terancam, dan kebijakan kita mungkin akan diblokir."
    eb "Hmph, aku tidak sampai di sini dengan membiarkan bocah seperti dia menghancurkan semuanya. Kita lihat apakah dia tetap idealis setelah diajak bicara. Hubungi orang-orang kita di parlemen dan atur pertemuan dengannya."
    "Pengusaha itu tahu bahwa mengabaikan ancaman seperti Bima bisa berbahaya. Dia memutuskan untuk mengambil langkah langsung untuk mengontrol situasi."

    scene bg bima_office_malam with fade
    b "Halo, ini Bima."
    va "Pak Bima, nama saya Indra. Saya asisten dari Pak Hardi, salah satu pemilik pabrik di kawasan industri yang Anda investigasi. Bos saya ingin bertemu dengan Anda untuk mendiskusikan laporan Anda."
    b "Pak Hardi? Saya tidak menyangka dia akan merespons secepat ini."
    va "Pak Hardi merasa bahwa ada kesalahpahaman yang perlu diluruskan. Dia ingin bertemu di kantornya besok malam. Ini akan menjadi pertemuan pribadi dan informal."
    
    menu :
        "Menerima undangan untuk bertemu langsung." :
            b "Baik, saya akan datang. Tapi saya harap ini adalah diskusi terbuka dan jujur. Jika ada sesuatu yang perlu dijelaskan, saya ingin mendengarnya langsung."
            va "Tentu saja, Pak. Bos saya sangat menghormati posisi Anda."

        "Menolak bertemu dan meminta semua komunikasi dilakukan secara resmi." :
            b "Terima kasih atas undangannya, tapi saya rasa semua diskusi tentang isu ini harus dilakukan secara resmi. Saya tidak ingin ada yang disalahartikan."
            va "Saya mengerti, Pak. Tapi ini adalah kesempatan baik untuk menyelesaikan kesalahpahaman sebelum masalah ini menjadi lebih besar."
            b "Saya akan tetap pada pendirian saya. Jika Pak Hardi ingin berbicara, dia bisa menghadapi saya di parlemen atau melalui jalur resmi lainnya."

    scene bg bussiness_office with fade
    show h default at Position(xpos=0.8, ypos=2.0) with dissolve
    h "Pak Bima, pertama-tama, saya ingin mengucapkan terima kasih atas waktu Anda. Tidak banyak anggota parlemen yang mau repot-repot mendengar langsung dari pelaku usaha seperti saya."
    show b happy at Position(xpos=0.3, ypos=2.0) with dissolve
    b "Terima kasih atas undangannya, Pak. Saya di sini untuk memastikan bahwa kebenaran muncul dan keadilan ditegakkan. Saya harap diskusi ini bisa bermanfaat."
    h "Ah, keadilan, kata yang indah. Tapi, Anda harus tahu bahwa keadilan sering kali bersifat relatif, tergantung dari mana Anda melihatnya. Dunia ini penuh nuansa, Pak Bima, bukan hitam putih seperti yang sering digambarkan."

    menu :
        "Tetap sopan dan mendengarkan argumen Hardi." :
            b "Saya setuju bahwa dunia tidak selalu hitam dan putih, Pak. Namun, jika kita membiarkan prinsip keadilan menjadi terlalu fleksibel, kita berisiko mengabaikan mereka yang paling rentan."
            h "Pernyataan yang bagus. Tapi izinkan saya bertanya: apa Anda tahu bagaimana sulitnya menjalankan bisnis di negeri ini? Pajak yang tinggi, regulasi yang tumpang tindih, tekanan dari investor. Semua itu memaksa pengusaha seperti saya untuk membuat keputusan yang, terkadang, tidak ideal."
            b "Keputusan tidak ideal yang Anda maksud, apakah itu termasuk pemotongan gaji buruh dan pelanggaran jam kerja?"
            h "Ah, saya lihat Anda datang dengan membawa tuduhan berat. Tapi percayalah, masalah ini sering kali disebabkan oleh manajemen di lapangan, bukan kebijakan saya. Saya tidak pernah berniat merugikan pekerja saya."
            b "Kalau begitu, saya harap Anda siap bekerja sama untuk memperbaiki masalah ini. Para buruh Anda berhak mendapatkan keadilan."
        
        "Langsung mempertanyakan integritas Hardi." :
            b "Relatif atau tidak, keadilan tetaplah keadilan, Pak. Apa yang terjadi di pabrik Anda adalah pelanggaran nyata terhadap hukum dan hak asasi manusia. Jika Anda tahu tentang ini, Anda seharusnya bertindak lebih cepat."
            h "Hati-hati dengan tuduhan Anda, Pak Bima. Saya menghormati posisi Anda, tetapi saya tidak akan menerima fitnah tanpa dasar."
            b "Ini bukan fitnah. Saya punya bukti yang menunjukkan pemotongan gaji ilegal, pelanggaran jam kerja, dan kondisi kerja yang tidak aman. Semua ini terjadi di pabrik Anda."
            h "Kalau begitu, mari kita selidiki bersama. Saya akan membentuk tim internal untuk menyelesaikan ini. Tapi, Anda juga harus memahami bahwa kesalahan seperti ini sering kali berasal dari manajemen tingkat bawah."
            b "Saya akan menunggu hasil investigasi Anda, tapi saya tidak akan tinggal diam jika masalah ini tidak segera ditangani."
    
    h "Pak Bima, izinkan saya berbicara jujur. Anda adalah orang baru di dunia politik, penuh dengan semangat dan idealisme. Itu bagus. Tapi Anda juga harus belajar bahwa dunia ini tidak berjalan hanya dengan moral. Kadang kita harus berkompromi."

    menu :
        "Menyatakan bahwa prinsip lebih penting daripada kompromi." :
            b "Mungkin Anda benar bahwa kompromi penting dalam beberapa hal. Tapi untuk pelanggaran hak asasi manusia, saya tidak akan pernah berkompromi. Keadilan adalah hal yang tidak bisa ditawar."
            h "Pendekatan seperti itu mungkin ideal, tapi tidak realistis. Jika Anda terus bertahan dengan pandangan itu, Anda akan menghadapi lebih banyak musuh daripada teman di dunia ini."
            b "Kalau mempertahankan prinsip membuat saya punya lebih banyak musuh, maka itu risiko yang saya terima. Lebih baik saya kalah dengan integritas daripada menang dengan mengkhianati rakyat."
        
        "Mengakui bahwa kompromi kadang diperlukan, tetapi tidak untuk melanggar hak asasi." :
            b "Saya paham bahwa kompromi kadang diperlukan, Pak. Tapi saya tidak percaya bahwa kompromi bisa menjadi alasan untuk melanggar hak asasi manusia. Ada batasan yang tidak boleh dilanggar."
            h "Batasan, ya? Kalau begitu, izinkan saya menanyakan ini: apa batasan Anda? Apa Anda siap kehilangan dukungan politik hanya karena Anda tidak mau sedikit melonggarkan prinsip Anda?"
            b "Kalau prinsip saya harus dilonggarkan untuk mendukung ketidakadilan, maka saya lebih baik kehilangan dukungan itu."
    
    h "Pak Bima, izinkan saya memberi saran. Jika Anda terus maju seperti ini, Anda tidak hanya melawan saya. Anda melawan sistem. Apakah Anda yakin siap untuk itu?"

    menu :
        "Menghadapi ancaman Hardi dengan tegas." :
            b "Kalau memperjuangkan rakyat berarti melawan sistem, maka itu yang akan saya lakukan. Saya tidak takut pada ancaman Anda, Pak Hardi."
            h "Baiklah, kita lihat sampai kapan idealisme Anda bisa bertahan. Tapi jangan bilang saya tidak memperingatkan Anda."

        "Memanfaatkan situasi untuk mendapatkan lebih banyak informasi." :
            b "Saya paham risikonya, Pak. Tapi saya ingin tahu lebih banyak. Siapa saja yang terlibat dalam sistem ini? Jika saya mengerti, mungkin kita bisa mencari jalan keluar bersama."
            h "Saya suka pendekatan Anda. Tapi saya tidak begitu percaya pada niat Anda. Mari kita lihat apakah tindakan Anda sesuai dengan kata-kata Anda."
    
    "Pertemuan itu berakhir dengan ketegangan yang belum terselesaikan. Bima meninggalkan kantor Hardi dengan tekad yang semakin kuat, sementara Hardi merencanakan langkah balasan untuk menghentikannya. Perjuangan ini baru dimulai."

    # Scene 4 : Aliansi Kegelapan - Penyatuan Pengusaha Tamak dan Pejabat Korup
    scene bg restaurant with fade
    h "Pak Herman, akhirnya Anda datang juga. Saya kira Anda terlalu sibuk untuk urusan kecil seperti ini."
    pk "Urusan kecil? Pak Hardi, masalah ini jauh dari kecil. Anak muda itu, Bima, sudah mulai mengguncang fondasi kita. Saya rasa kita berdua tahu dia tidak bisa dibiarkan."
    h "Betul sekali. Saya sudah mendengar tentang presentasinya di parlemen. Dia membawa bukti, bahkan menyebut nama saya secara tidak langsung. Ini tidak bisa dibiarkan berlanjut."
    # Menyusun permasalahan bersama
    pk "Dia memang berani, saya beri dia itu. Tapi keberanian tidak akan cukup di dunia ini. Masalahnya, keberanian itu mulai mengganggu kepentingan kita. Jika bukti yang dia punya menyebar, reputasi saya dan bisnis Anda akan hancur."
    h "Dan tidak hanya reputasi. Dia juga bisa menarik perhatian pihak berwenang. Saya tidak mau ada aparat datang ke pabrik saya hanya karena anak baru ini tidak tahu tempatnya."
    pk "Jadi, apa rencana Anda? Anda ingin saya menekan dia di parlemen?"
    h "Itu langkah awal, tapi tidak cukup. Kita perlu menghabisinya secara menyeluruh, baik dari sisi politik maupun publik."
    pk "Itu tidak mudah, Pak Hardi. Anak itu punya integritas. Dia tidak akan takut dengan tekanan biasa. Kita butuh sesuatu yang lebih kuat."
    # Rencana mengerikan : menyatukan kekuatan
    h "Integritas tidak akan berarti jika dia kehilangan kredibilitas. Kita rusak reputasinya. Saya punya media di bawah kendali saya. Kita bisa menciptakan narasi yang menggambarkan dia sebagai penghasut buruh yang tidak bertanggung jawab."
    pk "Itu langkah yang bagus. Saya juga bisa memastikan dia kehilangan pengaruh di parlemen. Saya akan mengatur agar proposalnya dipermainkan di komite, sehingga dia terlihat tidak kompeten."
    h "Kita juga bisa menargetkan buruh-buruh yang bekerja sama dengannya. Saya akan memberi peringatan kepada mereka melalui tim saya di pabrik. Jika mereka terus bicara, mereka kehilangan pekerjaan mereka."
    pk "Bagus, tapi itu baru permulaan. Kita juga perlu mendorong tekanan pribadi. Jika kita bisa menggali masa lalunya atau kelemahan yang bisa dimanfaatkan, dia tidak akan punya tempat untuk lari."
    h "Saya suka cara Anda berpikir, Pak Herman. Apa Anda punya tim yang bisa melakukan pekerjaan itu?"
    pk "Saya punya orang-orang yang sangat berbakat untuk hal seperti itu. Tapi ingat, ini harus dilakukan dengan sangat hati-hati. Jika kita terlalu agresif, dia bisa mendapatkan simpati dari publik."
    #Dialog yang Menunjukkan Ketegangan Antagonis
    h "Publik? Publik itu mudah dipengaruhi. Kalau kita kontrol media dengan baik, kita bisa membuatnya terlihat sebagai musuh ekonomi negara. Orang akan percaya apa pun yang kita sajikan."
    pk "Jangan terlalu meremehkan dia. Anak itu pintar. Dia tahu bagaimana memanfaatkan simpati rakyat kecil. Jika kita tidak hati-hati, dia bisa membalikkan semuanya melawan kita."
    h "Saya sudah berurusan dengan orang-orang seperti dia sebelumnya. Mereka semua punya batas. Tekanan yang cukup akan membuatnya menyerah atau kehilangan dukungan."
    pk "Baiklah, kita mulai dari sini. Anda kendalikan narasi publik, dan saya akan urus sisi politiknya. Tapi saya butuh jaminan bahwa bisnis Anda tidak akan terlibat skandal lebih besar. Saya tidak ingin nama saya tercemar karena masalah Anda."
    h "Jaminan? Pak Herman, bisnis saya adalah yang menjaga ekonomi daerah Anda tetap hidup. Anda tidak akan punya masalah selama saya tetap bisa menjalankan operasi saya tanpa gangguan."
    # Rencana Final
    pk "Kalau begitu, kita sepakat. Kita pastikan anak itu kehilangan dukungan, kredibilitas, dan kekuatan. Ketika semua ini selesai, dia tidak akan punya apa-apa lagi."
    h "Untuk kerja sama yang sukses. Saya akan pastikan anak itu menyesali keputusannya melawan kita."
    pk "Kita lihat siapa yang bertahan sampai akhir. Saya akan segera memulai langkah pertama saya di parlemen."

    "Malam itu, aliansi gelap terbentuk. Hardi dan Herman, dua orang dengan kekuasaan besar, menyatukan kekuatan mereka untuk menjatuhkan Bima. Tetapi mereka tidak tahu bahwa Bima telah mempersiapkan langkah balasannya sendiri."

    # Scene 5 : Kekalahan Bima di Ruang Parlemen
    scene bg parliament_chamber with dissolve
    "Setelah berhari-hari mengumpulkan bukti dan mengatur strategi, Bima akhirnya memiliki kesempatan untuk mempresentasikan kasusnya di depan parlemen. Namun, di balik layar, musuh-musuhnya telah merencanakan segalanya untuk menjatuhkannya."

    # Bima Memulai Presentasi
    b "Rekan-rekan sekalian, hari ini saya akan mempresentasikan bukti yang menunjukkan pelanggaran berat terhadap hak buruh di beberapa pabrik besar, termasuk yang dimiliki oleh Pak Hardi, yang juga hadir di sini."
    "Suasana ruangan mulai riuh. Beberapa anggota parlemen tampak terkejut, sementara lainnya berbicara dalam bisikan."
    b "Bukti ini mencakup laporan pemotongan gaji, jam kerja yang melanggar hukum, dan kondisi kerja yang tidak manusiawi. Saya juga memiliki kesaksian dari beberapa buruh yang siap bersaksi jika diperlukan."
    "Bima menyerahkan salinan dokumen kepada Ketua Sidang, yang mulai membacanya dengan raut serius."

    # Pejabat Korup Menyerang dengan Strategi Politik
    pk "Terima kasih, Pak Bima, atas presentasi Anda. Tapi izinkan saya bertanya, apakah Anda sudah memastikan keabsahan bukti-bukti ini? Saya melihat ada beberapa kesaksian anonim di sini. Apa ini tidak membuat bukti Anda diragukan?"
    b "Semua bukti ini telah diverifikasi oleh tim saya. Kesaksian anonim diberikan untuk melindungi buruh dari ancaman yang sangat nyata."
    pk "Ancaman? Atau mungkin mereka takut karena mereka tahu informasi ini tidak sepenuhnya benar? Kita harus berhati-hati dengan klaim seperti ini, terutama jika bisa merusak reputasi pengusaha yang telah memberikan banyak kontribusi untuk negara."

    menu :
        "Menjawab dengan tenang dan berfokus pada data." :
            b "Saya memahami kekhawatiran Anda, Pak Herman. Tapi data ini tidak hanya berdasarkan kesaksian. Kami memiliki catatan jam kerja, slip gaji, dan foto-foto kondisi kerja di lapangan yang mendukung temuan kami."
            pk "Itu menarik, tapi kita harus melihat semua ini dengan skeptis. Tidak ada jaminan bahwa data ini tidak dimanipulasi oleh pihak-pihak yang memiliki agenda politik."
            "Pendekatan tenang Bima tidak cukup untuk menghentikan keraguan yang telah ditanamkan oleh Pejabat Korup. Beberapa anggota parlemen mulai terlihat ragu."
        
        "Langsung menyerang balik dengan mempertanyakan integritas Pejabat Korup." :
            b "Anda berbicara tentang reputasi, Pak Herman. Tapi izinkan saya bertanya, apakah reputasi Anda juga terlibat di balik pelanggaran ini? Karena saya punya alasan untuk percaya bahwa hubungan Anda dengan Pak Hardi lebih dari sekadar profesional."
            pk "Hati-hati dengan kata-kata Anda, Pak Bima. Tuduhan tanpa bukti hanya akan merusak kredibilitas Anda sendiri."
            "Serangan Bima berhasil memancing reaksi keras dari Pejabat Korup, tetapi juga membuat suasana semakin panas. Beberapa anggota parlemen mulai merasa tidak nyaman dengan eskalasi ini."

    # Pengusaha Tamak Memutar Balikkan Narasi
    h "Saya menghormati upaya Pak Bima untuk membela buruh, tapi izinkan saya mengatakan bahwa tuduhan ini sangat tidak adil. Sebagai pengusaha, saya selalu memprioritaskan kesejahteraan pekerja saya."
    b "Jika itu benar, bagaimana Anda menjelaskan bukti pemotongan gaji dan pelanggaran jam kerja di pabrik Anda?"
    h "Bukti itu? Saya tidak tahu dari mana Anda mendapatkannya, tapi saya yakin itu adalah laporan yang salah atau dimanipulasi oleh pihak-pihak yang ingin merusak nama baik perusahaan saya."

    menu :
        "Mencoba menekan Hardi dengan menunjukkan lebih banyak bukti." :
            b "Ini bukan hanya laporan. Ini adalah slip gaji yang menunjukkan pemotongan langsung. Ini adalah catatan jam kerja yang melanggar undang-undang ketenagakerjaan."
            h "Semua itu bisa saja dipalsukan, Pak Bima. Dan saya tidak akan tinggal diam melihat nama saya dicemarkan seperti ini!"
            "Serangan balik Hardi, didukung oleh keraguan yang ditanamkan oleh Pejabat Korup, membuat banyak anggota parlemen mulai meragukan keabsahan data Bima."

        "Meminta buruh untuk berbicara langsung sebagai saksi." :
            b "Saya... saya ingin mengatakan bahwa semua yang dikatakan Pak Bima itu benar. Kami sering dipaksa bekerja melebihi batas, dan gaji kami dipotong tanpa alasan."
            h "Apa yang dikatakan buruh ini tidak mewakili mayoritas pekerja saya. Dia hanya satu dari ribuan. Dan bagaimana kita bisa tahu bahwa dia tidak dimanipulasi oleh pihak luar?"
            "Kehadiran buruh sebagai saksi tidak cukup untuk melawan narasi kuat yang dibangun oleh Hardi dan Pejabat Korup. Dukungan untuk Bima semakin melemah."
    
    # Kekalahan Bima
    lp "Karena kurangnya kejelasan dan untuk menjaga keadilan, kami akan menunda keputusan ini sampai investigasi resmi dilakukan. Sidang selesai."
    "Keputusan itu merupakan pukulan berat bagi Bima. Meskipun ia telah memberikan bukti yang kuat, propaganda dan pengaruh antagonis membuatnya terlihat lemah dan tidak efektif."

    "Di ruang sidang yang kosong, Bima duduk sendirian, menatap dokumen yang telah ia persiapkan dengan susah payah. Kekalahan ini bukan hanya tentang dirinya, tapi tentang rakyat kecil yang bergantung pada perjuangannya. Namun, di tengah kegelapan, ia bersumpah untuk kembali lebih kuat."

    # SCENE 6 : Bangkit dari Kekalahan - Pencarian Bukti Kegiatan Ilegal
    scene bg bima_office_malam with dissolve
    "Setelah kekalahan di parlemen, Bima merenung. Kekuasaan dan kelicikan musuh-musuhnya telah membuat perjuangannya terlihat sia-sia. Namun, di tengah kegelapan itu, ia menyadari satu hal: untuk melawan sistem yang korup, ia membutuhkan bukti yang tak terbantahkan, sesuatu yang tidak bisa disangkal oleh siapa pun."

    # Diskusi dengan Tim Pendukung
    ah "Pak Bima, saya tahu kekalahan ini sulit diterima. Tapi kita masih punya peluang. Jika kita bisa menemukan sesuatu yang lebih besar, sesuatu yang benar-benar mengejutkan, mereka tidak akan bisa menghindar lagi."
    b "Kita butuh bukti yang tidak bisa dibantah. Bukan hanya soal pelanggaran buruh, tapi sesuatu yang mengungkap korupsi dan kejahatan mereka yang sebenarnya."
    wi "Saya dengar ada desas-desus tentang aktivitas ilegal di salah satu pabrik milik Hardi. Beberapa mantan pekerja mengatakan bahwa ada aliran uang gelap dan perdagangan ilegal yang melibatkan perusahaan itu."
    b "Jika itu benar, maka ini adalah kunci kita. Tapi kita harus bertindak hati-hati. Jika mereka tahu kita menyelidiki ini, mereka tidak akan segan-segan menyerang balik."
    ba "Saya punya kenalan yang dulu bekerja di pabrik itu. Dia mungkin tahu sesuatu. Tapi dia sangat takut untuk berbicara."
    b "Kalau begitu, kita temui dia. Kita yakinkan bahwa dia akan aman, dan suara dia bisa membawa perubahan besar."

    # Investigasi Awal
    scene bg pabrik_malam with dissolve
    mp "Pak Bima, saya tidak tahu kenapa Anda ingin bertemu saya. Saya sudah lama keluar dari pabrik itu. Saya tidak mau terlibat masalah."
    b "Kami hanya ingin mendengar cerita Anda. Anda tidak perlu takut. Kami akan melindungi Anda."
    mp "Saya tidak tahu banyak, tapi saya pernah mendengar manajer bicara soal 'pengiriman khusus' di malam hari. Mereka sangat merahasiakan itu. Saya curiga ada sesuatu yang tidak beres."
    b "Pengiriman khusus? Apa Anda tahu kapan atau di mana itu terjadi?"
    mp "Biasanya di gudang belakang, setelah jam kerja. Tapi saya tidak pernah melihatnya langsung. Saya hanya mendengar desas-desus dari teman-teman."
    ah "Itu bisa jadi sesuatu. Jika kita bisa mengamati pengiriman itu, kita mungkin bisa menemukan sesuatu yang besar."

    # Operasi Pengintaian
    "Dengan informasi baru, Bima dan timnya memutuskan untuk melakukan pengintaian di pabrik Hardi. Mereka harus bertindak cepat, tetapi juga berhati-hati untuk tidak menarik perhatian."
    ah "Lihat itu. Ada truk besar yang keluar dari gudang belakang. Tidak ada tanda pengiriman resmi di kendaraan itu."
    b "Kita harus tahu ke mana mereka membawa barang ini. Kita ikuti, tapi jangan sampai mereka menyadari kita."

    menu :
        "Mengikuti truk dari kejauhan untuk mencari tujuan pengiriman." :
            "Mereka mengikuti truk hingga tiba di sebuah gudang terpencil di pinggir kota. Di sana, mereka melihat aktivitas mencurigakan: beberapa pria memindahkan kotak-kotak besar ke dalam gudang."
            b "Kita harus tahu apa isi kotak-kotak itu. Kalau ini barang ilegal, kita punya bukti yang kita cari."
        
        "Menyusup ke dalam pabrik untuk melihat barang apa yang dikirimkan." :
            "Menyusup ke dalam pabrik adalah langkah berisiko, tetapi juga memberikan kesempatan untuk melihat langsung apa yang sedang terjadi di sana."
            b "Lihat itu. Kotak-kotak ini tidak memiliki tanda resmi. Apa mungkin ini barang ilegal?"
            ah "Kita harus memotret ini. Kalau kita bisa membawa ini ke media, mereka tidak akan bisa menyangkalnya."
    
    # Penemuan Barang Ilegal
    scene bg gudang_pabrik with dissolve
    "Bima dan timnya memasuki gudang dengan hati-hati. Mereka menyadari bahwa apa pun yang disembunyikan di sini, itu bukan sesuatu yang ingin diketahui publik."
    ah "Pak Bima, lihat tanda di kotak itu. Itu bukan logo perusahaan resmi. Apa ini mungkin barang selundupan?"
    b "Hanya ada satu cara untuk tahu pasti. Kita harus membuka salah satu kotak ini."

    menu :
        "Membuka kotak dengan hati-hati tanpa meninggalkan jejak." :
            b "Lihat ini. Barang elektronik mahal? Ini tidak tercatat dalam inventaris resmi perusahaan."
            ah "Barang elektronik seperti ini seharusnya diimpor dengan izin tertentu. Jika ini ilegal, maka ini adalah bukti kuat."
        
        "Mengambil risiko dengan memecahkan segel untuk melihat isinya lebih cepat." :
            b "Ini lebih dari sekadar selundupan. Lihat dokumen ini. Ada catatan transaksi rahasia, dengan tanda tangan yang menghubungkan Hardi langsung ke jaringan ini."
            ah "Itu tanda tangan pejabat! Mereka menggunakan pabrik ini untuk menutupi kegiatan ilegal!"
    
    # Penemuan yang Mengejutkan
    b "Ini bukan hanya masalah selundupan barang. Ini adalah korupsi besar-besaran. Mereka menggunakan pabrik ini sebagai kedok untuk mengalihkan uang gelap."
    ah "Jika kita bisa membawa dokumen ini ke publik, ini akan menghancurkan mereka. Tapi kita harus berhati-hati. Mereka pasti tidak akan tinggal diam."
    ba "Pak, saya tahu tempat lain di gudang ini. Kadang-kadang ada kotak dengan bahan kimia yang sangat dijaga. Mungkin itu juga terkait."
    b "Kalau begitu, kita harus mencari kotak itu juga. Kalau mereka menyelundupkan bahan kimia tanpa izin, ini akan jadi bukti tambahan."

    # Penemuan Barang Berbahaya
    scene bg gudang_chemical with dissolve
    ah "Apa ini? Bahan kimia seperti ini seharusnya tidak ada di pabrik biasa. Ini bisa sangat berbahaya."
    b "Ini lebih buruk dari yang saya kira. Mereka tidak hanya menyelundupkan barang ilegal, tapi juga membahayakan keselamatan pekerja dan lingkungan."
    ba "Pak, kita harus pergi sekarang. Kalau penjaga tahu kita di sini, kita tidak akan bisa keluar."

    menu :
        "Segera keluar dengan bukti yang sudah ditemukan." :
            "Bima dan tim memutuskan untuk segera keluar sebelum menarik perhatian. Dengan bukti di tangan, mereka tahu ini sudah cukup untuk memulai langkah berikutnya."
        
        "Mengambil risiko untuk mencari lebih banyak bukti." :
            b "Ini dia. Lihat isi kotak ini. Barang mewah dan obat-obatan? Ini jelas penyelundupan besar."
            ah "Ini cukup untuk menghancurkan mereka. Tapi penjaga akan segera tahu kita di sini. Kita harus pergi sekarang!"
            "Meskipun berisiko, keputusan Bima untuk mencari lebih banyak bukti memberikan keunggulan strategis. Dengan data yang lebih lengkap, ia kini memiliki kekuatan untuk melawan musuh-musuhnya."
    
    scene bg bima_office_malam with dissolve
    "Setelah berhasil keluar dari gudang, Bima dan timnya menyusun kembali semua bukti yang mereka kumpulkan. Barang selundupan, bahan kimia berbahaya, dan dokumen yang menghubungkan pejabat dengan pengusaha. Semua ini menjadi kunci untuk membongkar jaringan korupsi yang telah lama tersembunyi."


    return