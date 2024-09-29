import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import streamlit as st

# Membaca data dari CSV
merged_df = pd.read_csv("all.csv")


# Menghitung total penyewa berdasarkan kondisi cuaca
st.subheader("Tren Penggunaan Sepeda per Bulan")
st.markdown("""
Data yang kita analisis menunjukkan adanya korelasi yang sangat kuat antara kondisi cuaca dan minat masyarakat untuk menyewa sepeda. Terlihat jelas bahwa cuaca cerah menjadi faktor utama yang mendorong masyarakat untuk memilih sepeda sebagai moda transportasi atau rekreasi. Sebaliknya, kondisi cuaca buruk seperti hujan atau salju secara signifikan mengurangi jumlah penyewa sepeda. Hal ini mengindikasikan bahwa cuaca memiliki pengaruh yang sangat dominan dalam menentukan permintaan terhadap layanan penyewaan sepeda.

Implikasi dari temuan ini sangat luas. Bagi perusahaan penyewaan sepeda, informasi ini dapat menjadi dasar untuk menyusun strategi pemasaran yang lebih efektif, seperti menawarkan promo khusus pada saat cuaca cerah atau menyediakan fasilitas tambahan untuk pengguna sepeda saat cuaca buruk. Pemerintah juga dapat memanfaatkan data ini untuk merancang kebijakan yang mendukung penggunaan sepeda, misalnya dengan membangun infrastruktur yang lebih baik untuk pesepeda atau mengadakan kampanye promosi bersepeda.

Secara keseluruhan, data ini menegaskan pentingnya mempertimbangkan faktor cuaca dalam perencanaan dan pengembangan layanan penyewaan sepeda. Dengan memahami hubungan antara cuaca dan permintaan, kita dapat mengambil langkah-langkah yang lebih tepat untuk mendorong penggunaan sepeda sebagai moda transportasi yang ramah lingkungan dan sehat.

Apakah Anda ingin saya menambahkan informasi lain atau mengubah fokus kesimpulan ini? Misalnya, kita bisa membahas potensi dampak perubahan iklim terhadap penggunaan sepeda atau membandingkan pola penggunaan sepeda di berbagai wilayah dengan kondisi iklim yang berbeda.
""")
weather_agg = merged_df.groupby('weathersit_x')['cnt'].sum().reset_index()
weather_agg.columns = ['Kondisi Cuaca', 'Total Penyewa']
weather_agg_sorted = weather_agg.sort_values(by='Total Penyewa', ascending=True)

st.write(weather_agg_sorted)
plt.figure(figsize=(8, 6))
weather_agg_sorted.plot(kind='bar', x='Kondisi Cuaca', y='Total Penyewa', color='skyblue')
plt.title('Total Penyewa Sepeda berdasarkan Kondisi Cuaca')
plt.xlabel('Kondisi Cuaca')
plt.ylabel('Total Penyewa')
plt.xticks(rotation=0)
plt.grid(axis='y')
for i, val in enumerate(weather_agg_sorted['Total Penyewa']):
    plt.text(i, val + 20, str(val), ha='center', va='bottom')
plt.tight_layout()
st.pyplot(plt)

# Grafik Total Penyewa berdasarkan Hari dalam Seminggu
# Mengelompokkan data berdasarkan hari dalam seminggu dan menghitung total penyewa
st.subheader("Penyewa berdasarkan Hari dalam Seminggu")
st.markdown("""
Data penggunaan sepeda menunjukkan pola yang menarik sepanjang satu minggu. Pada hari kerja, jumlah orang yang mulai menggunakan layanan penyewaan sepeda cenderung lebih tinggi dibandingkan akhir pekan. Ini menunjukkan bahwa banyak orang memanfaatkan sepeda sebagai alternatif transportasi untuk beraktivitas sehari-hari seperti bekerja atau bersekolah. Di sisi lain, pada akhir pekan, jumlah pengguna yang sudah terdaftar sebagai anggota cenderung meningkat, mengindikasikan bahwa mereka lebih sering menggunakan sepeda untuk rekreasi atau olahraga.

Pola penggunaan ini memberikan beberapa wawasan penting. Pertama, layanan penyewaan sepeda memiliki potensi besar sebagai solusi transportasi alternatif yang ramah lingkungan. Kedua, kebutuhan pengguna sepeda berbeda antara hari kerja dan akhir pekan, sehingga perusahaan penyewaan sepeda perlu menyesuaikan strategi mereka untuk memenuhi kebutuhan pelanggan yang beragam.

Dengan memahami pola penggunaan ini, perusahaan penyewaan sepeda dapat mengambil langkah-langkah yang lebih efektif. Misalnya, dengan menawarkan promo khusus pada hari kerja untuk menarik lebih banyak pengguna baru, atau menyediakan fasilitas tambahan seperti tempat parkir sepeda yang aman pada akhir pekan untuk memenuhi kebutuhan pengguna yang berbeda. Selain itu, data ini juga dapat menjadi acuan bagi pemerintah dan pemangku kepentingan terkait untuk mengembangkan infrastruktur yang mendukung aktivitas bersepeda, seperti jalur sepeda yang lebih aman dan nyaman.

Kesimpulannya, data yang kita miliki menunjukkan bahwa penggunaan sepeda sebagai moda transportasi dan rekreasi semakin populer. Dengan memahami pola penggunaan ini, kita dapat mengembangkan strategi yang lebih efektif untuk mendorong pertumbuhan industri sepeda dan menciptakan lingkungan yang lebih ramah lingkungan.
""")
segmentation = merged_df.groupby('weekday')[['casual', 'registered']].sum().reset_index()
segmentation['Total Penyewa'] = segmentation['casual'] + segmentation['registered']
segmentation.columns = ['Hari', 'Penyewa Baru', 'Penyewa Terdaftar', 'Total Penyewa']

hari_nama = {0: 'Senin', 1: 'Selasa', 2: 'Rabu', 3: 'Kamis', 4: 'Jumat', 5: 'Sabtu', 6: 'Minggu'}
segmentation['Hari'] = segmentation['Hari'].map(hari_nama)

hari_urut = ['Senin', 'Selasa', 'Rabu', 'Kamis', 'Jumat', 'Sabtu', 'Minggu']
segmentation['Hari'] = pd.Categorical(segmentation['Hari'], categories=hari_urut, ordered=True)
segmentation = segmentation.sort_values('Hari')
weekly_pattern = merged_df.groupby('weekday')['cnt'].sum().reset_index()
weekly_pattern.columns = ['Hari', 'Total Penyewa']
weekly_pattern['Hari'] = weekly_pattern['Hari'].map(hari_nama)

weekly_pattern['Hari'] = pd.Categorical(weekly_pattern['Hari'], categories=hari_urut, ordered=True)
weekly_pattern = weekly_pattern.sort_values('Hari')

plt.figure(figsize=(10, 6))
sns.lineplot(data=weekly_pattern, x='Hari', y='Total Penyewa', marker='o', color='skyblue')

plt.title('Total Penyewa Sepeda berdasarkan Hari dalam Seminggu', fontsize=16)
plt.xlabel('Hari', fontsize=14)
plt.ylabel('Total Penyewa', fontsize=14)
plt.xticks(rotation=0)
plt.grid(axis='y', linestyle='--', alpha=0.7)

for i, val in enumerate(weekly_pattern['Total Penyewa']):
    plt.text(i, val + 20, str(val), ha='center', va='bottom')

plt.tight_layout()

st.pyplot(plt)

plt.clf()
# Grafik Perbandingan Penyewa Baru dan Terdaftar
# Mengelompokkan data berdasarkan hari dalam seminggu
st.subheader("Perbandingan Penyewa Baru dan Terdaftar")

st.markdown("""
Analisis data penggunaan sepeda menunjukkan pola yang menarik sepanjang satu minggu. Terdapat perbedaan yang cukup signifikan antara jumlah pengguna baru dan pengguna terdaftar pada hari kerja dan akhir pekan. Pada hari kerja, jumlah pengguna baru cenderung lebih tinggi, mengindikasikan banyak orang menggunakan layanan ini untuk mobilitas sehari-hari seperti bekerja atau bersekolah. Sebaliknya, pada akhir pekan, jumlah pengguna terdaftar cenderung lebih tinggi, menunjukkan bahwa pengguna setia lebih sering memanfaatkan layanan ini untuk rekreasi atau olahraga.

Pola ini memberikan beberapa wawasan penting. Pertama, layanan penyewaan sepeda telah menjadi bagian dari rutinitas mobilitas banyak orang, terutama pada hari kerja. Kedua, akhir pekan menjadi waktu yang populer bagi pengguna setia untuk kembali menggunakan layanan ini. Memahami perbedaan ini sangat krusial bagi perusahaan penyewaan sepeda dalam merancang strategi bisnis yang efektif.

Dengan memahami pola ini, perusahaan dapat menyesuaikan layanan mereka. Misalnya, pada hari kerja, fokus promosi dapat diarahkan untuk menarik lebih banyak pengguna baru. Sementara itu, pada akhir pekan, perusahaan dapat menawarkan program atau fasilitas tambahan untuk meningkatkan pengalaman pengguna setia. Secara keseluruhan, data ini menunjukkan potensi besar layanan penyewaan sepeda sebagai bagian dari solusi mobilitas perkotaan yang berkelanjutan.

Kesimpulannya, data penggunaan sepeda menunjukkan adanya pola yang jelas terkait hari dalam seminggu. Dengan memahami pola ini, perusahaan dapat menyusun strategi yang lebih efektif untuk meningkatkan jumlah pengguna dan mempertahankan pelanggan setia.
""")
plt.figure(figsize=(10, 6))
bar_width = 0.35
x = range(len(segmentation['Hari']))

bars1 = plt.bar(x, segmentation['Penyewa Baru'], width=bar_width, label='Penyewa Baru', color='skyblue')

bars2 = plt.bar([p + bar_width for p in x], segmentation['Penyewa Terdaftar'], width=bar_width, label='Penyewa Terdaftar', color='orange')

plt.xlabel('Hari dalam Seminggu')
plt.ylabel('Total Penyewa')
plt.title('Perbandingan Penyewa Baru dan Terdaftar berdasarkan Hari')
plt.xticks([p + bar_width / 2 for p in x], segmentation['Hari'])
plt.legend()
plt.grid(axis='y')

for bar in bars1:
    yval = bar.get_height()
    plt.text(bar.get_x() + bar.get_width()/2, yval, int(yval), ha='center', va='bottom')

for bar in bars2:
    yval = bar.get_height()
    plt.text(bar.get_x() + bar.get_width()/2, yval, int(yval), ha='center', va='bottom')

st.pyplot(plt)

plt.clf()
