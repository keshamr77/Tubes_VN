﻿# Mendefinisikan karakter
define b = Character("Bima", image="characters/MC_Default.png")
define ibu = Character("Ibunda Bima", color="#ff9999")
define pe = Character("Politisi Senior A", color="#9999ff")
define ps = Character("Politisi Senior B", color="#6666cc")
define asisten = Character("Asisten Parlemen", color="#66cc66")
define lp = Character("Ketua Sidang", color="#ffc0cb")
define mp = Character("Anggota Parlemen Muda", color="#ffcc00")
define tk = Character("Tim Konstituen Bima", color="#e39803")
define ba = Character("Buruh A", color="#cc9966")
define bb = Character("Buruh B", color="#9966cc")
define bc = Character("Buruh C", color="#1ea5f9fc")
define bd = Character("Buruh D", color="#f94ef3")
define be = Character("Buruh E", color="#cc6666")

#Character expressions
image b default = "characters/MC_Default.png"
image b happy = "characters/MC_Happy.png"
image b angry = "characters/MC_angry"
image b worried = "characters/MC_worried"

# Background Definitions'
image bg parliament_chamber = im.Scale("backgrounds/parliament_chamber.jpg", 1920, 1080)
image bg bima_office_sore = im.Scale("backgrounds/bima_office_sore.png", 1920, 1080)
image bg bima_office_pagi = im.Scale("backgrounds/bima_office_pagi.png", 1920, 1080)
image bg living_room = im.Scale("backgrounds/living_room.jpg", 1920,1080)


# Scene pertama dengan background
label start:

    # Scene 1: Rumah Bima - Refleksi Masa Lalu
    scene bg living_room with fade  # Background: ruang tamu
    "Di malam yang tenang, Bima duduk di depan meja. Pikirannya melayang ke masa lalu—sebuah masa penuh luka dan kehilangan yang membentuk dirinya hingga hari ini."
    ibu "Cepat, Bima! Kita harus keluar sebelum mereka datang!"
    b "Tapi Ibu, kenapa kita harus pergi? Ini rumah kita!"
    "Bima muda tidak pernah melupakan malam itu—malam di mana keluarganya kehilangan segalanya karena keputusan segelintir orang di atas."
    
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
    lp "Sebelum kita melanjutkan pembahasan, izinkan saya memperkenalkan anggota baru kita. Bima, dari daerah pemilihan Sumatera Selatan. Anda memiliki waktu untuk memperkenalkan diri dan pandangan Anda. Silakan."
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
            ps "Hmph, langkah kecil tidak akan berarti apa-apa jika Anda tidak memiliki dukungan yang cukup."
            b "(Dukungan? Kalau begitu, aku harus membuktikan diriku terlebih dahulu.)"
        
        "Menegaskan pendapat dengan berani":
            b "Sistem ini mapan, tapi tidak sempurna. Tugas kita bukan untuk menerima kenyataan, melainkan untuk memperbaikinya. Saya yakin, jika kita bekerja sama, kita bisa membawa perubahan."
            "Kata-kata Bima mengundang perhatian yang lebih besar, tetapi juga beberapa tatapan dingin dari anggota parlemen yang merasa terganggu oleh keberaniannya."
            pe "Berani sekali bicara seperti itu di hari pertama Anda. Kita lihat apakah Anda masih bisa bicara besar setelah satu tahun di sini."
            b "(Mungkin aku baru di sini, tapi aku tidak akan membiarkan intimidasi menghentikan langkahku.)"

    # Debat Parlemen: Kebijakan Tenaga Kerja
    lp "Baiklah, mari kita lanjutkan ke agenda hari ini: pembahasan mengenai rancangan undang-undang ketenagakerjaan. Ada pendapat dari pihak pendukung?"
    "Seorang politisi berdiri, berbicara dengan penuh percaya diri."
    pe "Rancangan ini penting untuk meningkatkan daya saing tenaga kerja kita di pasar internasional. Fleksibilitas jam kerja dan efisiensi tenaga kerja akan memberikan keuntungan besar bagi ekonomi kita."
    show b worried at Position(xpos=0.3, ypos=2.0) with dissolve
    b "(Keuntungan ekonomi? Bagaimana dengan nasib para buruh yang jam kerjanya diperpanjang tanpa perlindungan?)"
    
    show b default at Position(xpos=0.3, ypos=2.0) with dissolve
    menu:
        "Memprotes langsung rancangan tersebut dengan argumen yang tajam":
            b "Maaf, tapi saya tidak bisa mendukung rancangan ini. Apakah kita mempertimbangkan bagaimana fleksibilitas ini akan mempengaruhi para buruh? Mereka sudah bekerja terlalu keras untuk upah yang tidak layak. Menambah jam kerja hanya akan memperburuk keadaan mereka."
            ps "Saudara Bima, ini bukan hanya tentang buruh. Ini tentang ekonomi negara kita. Jika buruh tidak kompetitif, siapa yang akan berinvestasi di sini?"
            b "Dan apa gunanya investasi jika masyarakat yang kita wakili hidup dalam penderitaan? Prioritas kita harus selalu rakyat, bukan angka di laporan ekonomi."

        "Mengajukan pertanyaan untuk menggiring diskusi ke isu buruh":
            b "Saya punya pertanyaan. Bagaimana rancangan ini memastikan bahwa hak buruh tetap terlindungi? Apakah ada mekanisme untuk mencegah eksploitasi tenaga kerja?"
            ps "Hmm, tentu saja, ada regulasi tambahan yang akan kita bahas nanti. Tapi fokus kita sekarang adalah pada daya saing."
            b "Kalau begitu, saya berharap pembahasan itu menjadi prioritas. Daya saing tidak ada artinya jika tenaga kerja kita diperlakukan seperti mesin tanpa batas."

    "Pendekatan Bima yang tenang tetapi tajam menarik perhatian lebih banyak anggota parlemen. Beberapa mulai mempertimbangkan ulang pandangan mereka."
    
    # Scene lorong parlemen after scene 3
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
    ba "Pak Bima, terima kasih sudah meluangkan waktu untuk kami. Saya bekerja di pabrik itu hampir 10 tahun. Belakangan ini, kondisi kami semakin buruk. Jam kerja bertambah, tapi gaji tetap kecil. Beberapa teman saya bahkan dipecat setelah mencoba mengajukan protes."
    b "Saya mendengar masalah ini dari laporan. Tapi saya ingin memastikan, apa Anda memiliki bukti, atau ada orang lain yang bisa mendukung cerita ini?"
    ba "Kami punya dokumen slip gaji dan daftar jam kerja yang tidak sesuai dengan kontrak. Tapi kalau kami ketahuan, risikonya terlalu besar. Tolong bantu kami, Pak."
    b "Tenang. Saya akan datang ke tempat Anda dalam beberapa hari. Kita akan bertemu secara aman dan mendiskusikan ini lebih jauh. Saya akan memastikan suara Anda terdengar, tapi Anda juga harus berhati-hati."
    "Bima tahu, ini bukan masalah sederhana. Tapi suara dari buruh itu memberinya alasan lebih kuat untuk bertindak. Dia menyadari bahwa untuk membawa perubahan, dia harus turun langsung ke lapangan."

    # Visual bima meletakkan telepon meraih dokumen dimejanya dan menatap catatan pada papan tulisnya
    b "(Sistem ini cacat, dan aku tidak bisa memperbaikinya hanya dari balik meja. Aku harus melihat langsung, mendengar langsung, dan berjuang bersama mereka.)"
    
    # Scene 5: Pabrik Buruh - Investigasi Awal
    scene bg industrial_area with fade  # Background: kawasan industri
    "Dengan bantuan tim konstituennya, Bima berhasil mengatur pertemuan rahasia dengan beberapa buruh pabrik. Meski pertemuan ini sederhana, bagi para buruh, ini adalah momen penuh harapan."

    # Perjalanan menuju gudang tempat pertemuan
    scene bg warehouse with fade  # Background: gudang
    "Bima berjalan melewati lorong sempit menuju sebuah gudang kosong di belakang pabrik, tempat pertemuan akan diadakan. Sekelompok buruh menunggu di sana, wajah mereka menunjukkan kelelahan dan kecemasan."
    
    show b default at Position(xpos=0.3, ypos=2.0) with dissolve
    # Pertemuan dengan buruh
    b "Terima kasih sudah meluangkan waktu untuk bertemu dengan saya. Saya tahu ini tidak mudah, tapi saya ingin mendengar langsung apa yang kalian alami."
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
    scene bg bima_office_sore with fade
    show b happy at Position(xpos=0.3, ypos=2.0) with dissolve
    b "(Ini baru awal. Masalah ini lebih besar dari yang aku bayangkan. Tapi aku sudah siap untuk melangkah lebih jauh.)"
    
    return