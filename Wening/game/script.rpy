﻿# Mendefinisikan karakter
define b = Character("Bima", image="characters/MC_Default.png")
define ibu = Character("Ibunda Bima", color="#ff9999")
define pe = Character("Politisi Senior A", color="#9999ff")
define ps = Character("Politisi Senior B", color="#6666cc")
define asisten = Character("Asisten Parlemen", color="#66cc66")
define mp = Character("Anggota Parlemen Muda", color="#ffcc00")
define bp = Character("Buruh", color="#cc9966")
define bu = Character("Buruh Senior", color="#9966cc")
define be = Character("Buruh E", color="#cc6666")
define wartawan_a = Character("Wartawan A")
define hardi = Character("Hardi")
define korup = Character("Pejabat Korup")
define pendukung = Character("Tim Pendukung")
define wartawan_ind = Character("Wartawan Independen")
define ketusidang = Character("Ketua Sidang")

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


label startarc3:

    "Setelah berhari-hari mengumpulkan bukti yang kuat, Bima memutuskan untuk melangkah lebih jauh dengan membawa bukti ini ke publik."
    "Baginya, ini adalah langkah penting untuk melawan propaganda dan konspirasi yang melindungi pelaku kejahatan."

label scene1:
    
    show b default at Position(xpos=0.3, ypos=2.0) with dissolve
    b "Hari ini, saya berdiri di sini bukan hanya sebagai seorang anggota parlemen, tetapi sebagai suara rakyat yang selama ini diabaikan."
    b "Bukti ini menunjukkan kejahatan yang telah dilakukan oleh pengusaha besar dan pejabat yang seharusnya melindungi rakyat."
    b "Saya tidak akan diam sampai keadilan ditegakkan."

label pilihanscene1:

    menu:
        "Mengungkap bukti secara rinci di depan wartawan.":
            jump choices1_a
        "Menyampaikan ancaman halus kepada pihak yang terlibat agar mereka bertanggung jawab.":
            jump choices1_b

label choices1_a:
    
    b "Bukti-bukti ini menunjukkan adanya penyelundupan barang ilegal dan pelanggaran hak buruh di pabrik tertentu."
    b "Selain itu, terdapat dokumen yang menghubungkan aliran dana ilegal kepada pejabat tertentu."
    b "Semua ini diverifikasi oleh tim saya."

    "Wartawan segera mengambil gambar dan mencatat pernyataan Bima. Beberapa dari mereka mulai mengajukan pertanyaan tajam, mencoba menggali lebih jauh."

    wartawan_a "Pak Bima, apakah ini berarti Anda menuduh pejabat tinggi yang disebutkan dalam dokumen ini sebagai pelaku korupsi?"

    b "Saya tidak menuduh, saya hanya menyampaikan fakta. Fakta yang telah diverifikasi dan akan saya bawa ke pengadilan."
    jump scene2

label choices1_b:
    b "Bagi mereka yang terlibat, saya ingin mengingatkan..."
    b "Waktu Anda untuk bertanggung jawab semakin menipis!"
    b "Jika Anda tidak mengambil langkah untuk memperbaiki kesalahan ini, maka saya akan memastikan hukum berjalan,"
    b "Apa pun risikonya."
    b "..."

    "Pernyataan tegas Bima menjadi sorotan utama di berita malam itu. Beberapa pejabat yang terlibat mulai merasa terpojok, sementara pendukung rakyat kecil memberikan dukungan penuh."
    jump scene2

label scene2:

    "Pengungkapan Bima membawa tekanan besar bagi para pelaku. Namun, mereka tidak akan tinggal diam. Dengan kekuasaan dan pengaruh yang besar, mereka merencanakan serangan balik."

    hardi "Dia pikir dia bisa menang hanya dengan bukti itu? Media mudah dipengaruhi. Kita buat cerita yang menunjukkan dia sebagai penghasut dan manipulatif."

    korup "Dan saya akan memastikan dukungannya di parlemen menghilang. Kita hanya perlu membuatnya terlihat tidak kompeten."

label pilihanscene2:

    menu:
        "Membalas dengan langkah hukum cepat untuk melindungi kredibilitas.":
            jump choices2_a
        "Membangun aliansi dengan media independen untuk melawan propaganda.":
            jump choices2_b
        
label choices2_a:

    b "Saya tahu mereka akan mencoba membalas. Kita harus segera membawa bukti ini ke pihak berwenang sebelum opini publik diputarbalikkan. Hukum harus mendahului propaganda mereka."

    pendukung "Pak Bima, kami akan bekerja untuk memastikan tidak ada celah yang bisa dimanfaatkan."

    "Bima membawa bukti-bukti itu langsung ke KPK dan media nasional untuk memastikan langkah hukumnya tidak dapat diganggu."
    jump scene3

label choices2_b:
    b "Mereka mungkin punya media besar, tapi kita punya kebenaran di pihak kita. Kita bekerja dengan media independen untuk memastikan rakyat tahu apa yang sebenarnya terjadi."

    wartawan_ind "Kami akan membantu Anda, Pak Bima. Tapi ini akan menjadi perang panjang, dan kami juga akan menjadi target."

    "Media independen mulai mempublikasikan bukti Bima secara luas. Meski mendapat tekanan besar,"
    "Kebenaran perlahan mulai mencuat."
    jump scene3

label scene3:
    ketusidang "Anggota Bima, Anda telah meminta sidang ini untuk mempresentasikan kasus Anda. Kami ingin mendengar pernyataan Anda."

    b "Bukti-bukti yang saya bawa tidak hanya tentang pelanggaran buruh, tetapi juga penyelundupan dan korupsi yang melibatkan pejabat tinggi dan pengusaha besar."
    b "Jika parlemen tidak bertindak sekarang, maka kita semua bertanggung jawab atas penderitaan rakyat."

label pilihanscene3:
    menu:
        "Fokus pada bukti dan data yang tidak dapat dibantah.":
            jump choices3_a
        "Menyerang langsung integritas para pelaku di depan sidang.":
            jump choices3_b
        
label choices3_a:
    b "Berikut adalah catatan transaksi yang menghubungkan pengusaha dan pejabat tertentu, serta foto-foto barang selundupan dari pabrik."
    b "Semua ini telah diverifikasi oleh pihak ketiga."

    "Pendekatan profesional Bima membuat sebagian anggota parlemen mulai mempertimbangkan untuk mendukungnya."
    "Namun, beberapa masih skeptis..."
    jump scene4

label choices3_b:
    b "Pejabat seperti Anda, Pak Herman, tidak bisa lagi berlindung di balik kekuasaan."
    b "Bukti ini menunjukkan jelas keterlibatan Anda dalam jaringan korupsi."
    b "Saya menantang Anda untuk membuktikan sebaliknya."

    "Pendekatan agresif Bima membuat suasana sidang memanas. Beberapa anggota parlemen mendukung, tetapi ada yang merasa cara ini terlalu berisiko."
    jump scene4

label goodending:

    "Hakim mengetuk palu, memutuskan Hardi dan Pejabat Korup bersalah."
    "Dan undang-undang yang baru kemudian disahkan."

label badending:
    "Sayangnya, serangan balik musuh berhasil."
    "Bima kehilangan dukungan politik dan reputasinya hancur."
    
label scene4:

    "Perjuangan melawan ketidakadilan bukanlah jalan yang mudah. Namun, setiap langkah kecil selalu berarti bagi masa depan yang lebih baik."

    return
