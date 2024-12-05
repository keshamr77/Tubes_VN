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
define pdk = Character("Politisi Pendukung Kebijakan",color="#6666cc"))

#Character expressions
image b default = "characters/MC_Default.png"
image b happy = "characters/MC_Happy.png"
image b angry = "characters/MC_angry.png"
image b worried = "characters/MC_worried.png"
image ibu = "characters/Ibu.png"
image ba silhouette =  "characters/Buruh_Telfon.png"
image bb rame = "characters/Buruh_Ramai.png"

# Background Definitions'
image bg parliament_chamber = im.Scale("backgrounds/parliament_chamber.jpg", 1920, 1080)
image bg parliament_hall = im.Scale("backgrounds/parliament_hall.png", 1920, 1080)
image bg bima_office_sore = im.Scale("backgrounds/bima_office_sore.png", 1920, 1080)
image bg bima_office_pagi = im.Scale("backgrounds/bima_office_pagi.png", 1920, 1080)
image bg bima_office_malam = im.Scale("backgrounds/bima_office_malam.jpg", 1920, 1080)
image bg living_room = im.Scale("backgrounds/living_room.jpg", 1920,1080)
image bg pabrik= im.Scale("backgrounds/pabrik.jpg", 1920,1080)
image bg gudang= im.Scale("backgrounds/gudang.jpg", 1920,1080)

# Transformations 
transform zoomed_for_silhoutte:
    xpos 0.5
    ypos 0.3
    zoom 2.8

# Scene pertama dengan background
label start:
    $ renpy.music.stop()
    
    #START OF ARC 1

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
    b "(Mereka sedang menunggu aku membuat kesalahan. Tapi aku tidak boleh diam. Rakyat membutuhkan suara ini.)"
    
    menu:
        "Berbicara dengan tenang dan penuh perhitungan.":
            b "Terima kasih atas kesempatannya. Saya ingin mengingatkan bahwa kebijakan ini harus melindungi semua pihak, termasuk buruh yang menjadi tulang punggung ekonomi kita. Jika kita hanya memihak pengusaha, kita akan menciptakan ketimpangan yang lebih dalam."
            psa "Pak Bima, Anda berbicara tentang ketimpangan, tetapi apakah Anda memahami kebutuhan investasi? Kita butuh investor untuk menciptakan lapangan kerja."
            b "Saya paham pentingnya investasi. Namun, investasi yang dibangun di atas ketidakadilan hanya akan merusak fondasi bangsa kita. Kita bisa mendukung pengusaha tanpa mengorbankan hak buruh."
            "Pendekatan Bima yang tenang berhasil menarik perhatian beberapa anggota parlemen. Namun, skeptisisme tetap kuat, terutama dari pihak pendukung kebijakan."

        "Langsung menyerang dengan bukti awal yang dimiliki.":
            b "Rancangan kebijakan ini bukan hanya soal ekonomi, tetapi juga soal moralitas. Saya telah melihat sendiri bagaimana pengusaha besar menggunakan kekuasaan mereka untuk menindas buruh, dan bukti ini hanya sebagian kecil dari apa yang saya temukan."
            "Bima menunjukkan dokumen awal yang mengungkap pelanggaran jam kerja dan gaji minimum di pabrik besar. Ruangan sidang menjadi sunyi, namun ketegangan meningkat."
            psb "Apa maksud Anda dengan ini? Tuduhan ini tidak berdasar. Anda hanya mencoba memancing perhatian."
            b "Kalau memang tidak berdasar, kenapa Anda terlihat begitu defensif? Saya hanya menginginkan transparansi. Jika kebijakan ini sah, maka tidak ada yang perlu disembunyikan."
            "Strategi Bima berhasil memancing reaksi keras dari pihak pendukung kebijakan, tetapi juga menarik dukungan dari beberapa anggota parlemen independen."

    # Scene 2: Konflik Internal - Rekan Parlemen Ragu
    scene bg parliament_hall with dissolve
    ka "Bima, apa yang kamu lakukan? Kamu tahu mereka tidak akan tinggal diam. Mereka punya kekuatan untuk menjatuhkanmu."
    b "Kalau aku diam, lalu siapa yang akan bicara untuk rakyat? Aku tidak peduli risiko ini, selama aku tahu aku berada di pihak yang benar."
    kb "Hati-hati, Bima. Kita mendukungmu, tapi jangan membuat mereka merasa terlalu terpojok. Mereka bisa balas menyerang."

    # Scene 3: Konfrontasi dengan Pejabat Korup
    scene bg parliament_chamber with dissolve
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
    

    return