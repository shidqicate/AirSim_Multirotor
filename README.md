# AirSim Drone Object Detection Simulation in Unreal Engine 4.27
## _The Last Markdown Editor, Ever_

[![N|Solid](https://cldup.com/dTxpPi9lDf.thumb.png)](https://nodesource.com/products/nsolid)

[![Build Status](https://travis-ci.org/joemccann/dillinger.svg?branch=master)](https://github.com/shidqicate)

Simulasi ini merupakan implementasi **drone autonomous** menggunakan [AirSim](https://github.com/microsoft/AirSim) di lingkungan **Unreal Engine**, yang mampu mendeteksi objek-objek seperti **mobil, manusia, pohon**, dan lainnya. Proyek ini cocok untuk kebutuhan riset di bidang **computer vision**, **machine learning**, serta pengembangan sistem navigasi drone secara otomatis.
## 🎯 Fitur Utama
---
- 🚁 Simulasi drone menggunakan AirSim dengan Unreal Engine
- 🔍 Deteksi objek secara real-time (mobil, manusia, pohon, dll)
- 🎥 Streaming kamera drone (FPV)
- 🧠 Bisa dikembangkan untuk integrasi AI/Deep Learning (YOLO, SSD, dll)
- 💾 Logging data penerbangan dan visualisasi hasil deteksi

## 🛠️ Prasyarat
---
Sebelum menjalankan proyek ini, pastikan sistem Anda sudah memiliki:

- [Unreal Engine 4.27+](https://www.unrealengine.com/)
- [AirSim](https://github.com/microsoft/AirSim)
- Python 3.7+
- OpenCV for Python
- Microsoft visual studio 22
- Desktop development with C++ 
- NET Framework SDK
- YOLOv5, atau menggunakan model lain.


## Installation
---
Cara installasi:

- Download & Install [Epic Games Launcher](https://store.epicgames.com/it/download), [Unreal Engine 4.27](https://docs.unrealengine.com/4.27/en-US/Basics/InstallingUnrealEngine/), [AirSim Package](https://microsoft.github.io/AirSim/)
- Untuk integrasi dan compile program dapat dilihat dari [guidebook AirSim](https://microsoft.github.io/AirSim/build_windows)
- Simpan file ```setting.json``` ke folder **C:\Users\user\Documents\AirSim**
- Download file ```AirSimTest01.zip``` lalu simpan juga di folder sehingga terlihat seperti ini **C:\Users\user\Documents\Unreal Project\AirSimTest01**
- Klik kanan pada AirSimTest01.uprojectfile di folder AirSimTest01 dan pilih Generate Visual Studio project files untuk melakukan compile akhir proyek dengan file yang baru ditambahkan.
- Jika sudah klik ```AirSimTest01.sln``` dan pastikan debugger menggunakan "Debug Game Editor" dan menggunakan platform "Win64" lalu start project.
- Penjelasan tambahan: 
-- file ```setting.json``` adalah tempat properti seperti jenis kendaraan, kamera, sensor, dan lainnya.
-- terdapat file yang berekstensi .umap - itu adalah file yang berisikan map, dan dapat diganti sesuai map yang dibutuhkan.
- untuk mengendalikan drone, saya menggunakan [PX4-autopilot](https://github.com/PX4/PX4-Autopilot)
- deteksi objek disini menggunakan model YOLOv5 dari ultralytics yang mengambil model pretrained dan target objeknya yaitu `car` dan `person`. Saat environtment simulator sudah di setup, langkah selanjutnya yaitu menjalankan script `detect.py`. Pop up window akan menampilkan visual kamera drone dengan nama "FrontCenterRGB".

## PX4-Autopilot Command List

Terdapat basic command yang dapat digunakan dalam simulasi drone di unreal menggunakan [PX4-autopilot](https://github.com/PX4/PX4-Autopilot). Untuk command lengkapnya dapat dilihat dari [dokumentasi PX4](https://docs.px4.io/main/en/).

| Command | Fungsi |
| ------ | ------ |
| commander arm | Mengaktifkan Motor |
| commander disarm | Menonaktifkan Motor |
| commander takeoff | Lepas landas (terbang) |
| commander land | mendarat otomatis |
| commander mode offboard | Mode offboard (kontrol dari AirSim/script MAVSDK) |
| commander mode position | Mode position control |

## Screenshoot and Video
![img](https://raw.githubusercontent.com/shidqicate/AirSim_Multirotor/refs/heads/main/drone1.png)
![video](Assets/AirSim.gif)


[//]: # (These are reference links used in the body of this note and get stripped out when the markdown processor does its job. There is no need to format nicely because it shouldn't be seen. Thanks SO - http://stackoverflow.com/questions/4823468/store-comments-in-markdown-syntax)

   [dill]: <https://github.com/joemccann/dillinger>
   [git-repo-url]: <https://github.com/joemccann/dillinger.git>
   [john gruber]: <http://daringfireball.net>
   [df1]: <http://daringfireball.net/projects/markdown/>
   [markdown-it]: <https://github.com/markdown-it/markdown-it>
   [Ace Editor]: <http://ace.ajax.org>
   [node.js]: <http://nodejs.org>
   [Twitter Bootstrap]: <http://twitter.github.com/bootstrap/>
   [jQuery]: <http://jquery.com>
   [@tjholowaychuk]: <http://twitter.com/tjholowaychuk>
   [express]: <http://expressjs.com>
   [AngularJS]: <http://angularjs.org>
   [Gulp]: <http://gulpjs.com>

   [PlDb]: <https://github.com/joemccann/dillinger/tree/master/plugins/dropbox/README.md>
   [PlGh]: <https://github.com/joemccann/dillinger/tree/master/plugins/github/README.md>
   [PlGd]: <https://github.com/joemccann/dillinger/tree/master/plugins/googledrive/README.md>
   [PlOd]: <https://github.com/joemccann/dillinger/tree/master/plugins/onedrive/README.md>
   [PlMe]: <https://github.com/joemccann/dillinger/tree/master/plugins/medium/README.md>
   [PlGa]: <https://github.com/RahulHP/dillinger/blob/master/plugins/googleanalytics/README.md>
