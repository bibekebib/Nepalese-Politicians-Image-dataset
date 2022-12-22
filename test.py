Names = ["prachanda" ,"bhamdev gautam","komal oli", "Kp Oli", "Baburam Bhattarai", "Lokendra Bahadur Chand",
"Onsari Gharti Magar",
"Astalaxmi Shakya",
"Sujata Koirala","Janardan Sharma",
"Hisila Yami","Matrika Prasad Yadav","Matrika Prasad Koirala","Shashanka Koirala",
"Shekhar Koirala","Arjun Narasingha K.C.",
"Arzu Rana Deuba","Deepak Manange","Ram Chandra Poudel",
"Renu Dahal","C. P. Mainali","Subaschandra Nemwang","Ram Baran Yadav","Deepak Bohara",
"Sunita Dangol","Raghubir Mahaseth","Surendra Pandey","Lal Babu Pandit",
"Bishnu Prasad Paudel","Shankar Pokharel","Giriraj Mani Pokharel","Kamal Thapa","Rekha Thapa",
"Barsaman Pun","Agni Prasad Sapkota","Bhuwan K.C.","Swarnim Wagle",'Mahindra Ray Yadav',"Manushi Yami Bhattarai",
"Nanda Kishor Pun","Rajendra Mahato","Chiri Babu Maharjan","Bijay Kumar Gachhadar",
"Upendra Mahato","Gokarna Bista","Minendra Rijal","Bimalendra Nidhi","Mahantha Thakur","Bikram Pandey",
"Ishwar Pokhrel","Dormani Poudel","Prabhu Sah","Ram Kumari Jhakri","Chitra Bahadur K.C.","Abdus Miya","shree gurung",
"Ranju Darshana","Birodh Khatiwada","Ghanashyam Bhusal","Mohammad Aftab Alam",
"Bidya Devi Bhandari","Padma Kumari Aryal","Pampha Bhusal","Dhana Raj Acharya","Abdul Rahim Ansari","Sagar Dhakal",
"Janat Ansari","Narayan Man Bijukchhe","Prem Ale","Gagan Thapa","Tulsi Giri",
"CK Raut","Balen Shah","Ravi lamichane","Sobita Gautam","Toshima Karki","Rabindra Mishra","Pukar Bam","Milan Pandey","rabindra adhikari",
"Prithvi Man Gurung","Gokul Prasad Baskota","Prithvi Subba Gurung","Pradeep Gyawali",
"Mahesh Basnet","Yogesh Bhattarai","Binod Chaudhary","Prakash Man Singh","Rajendra Prasad Lingden",
"Kalpana Bista","Upendra Mahato","Surendra Raj Pandey","Pradip Paudel","Biraj Bhakta Shrestha","Shishir Khanal",
"Rupchandra Bista","Madhav Kumar Nepal","Subarna Shamsher Rana","Ganesh Man Singh","Ujwal Thapa", "BP Koirala","Man Mohan Adhikari",
 "Jhala Nath Khanal","Girija Prasad Koirala"]


from bing_image_downloader import downloader
for i in range(len(Names)):
    # print (Names[i])
    # print(i)
    downloader.download(Names[i], limit=50,  output_dir='final', adult_filter_off=True, force_replace=False, timeout=60, verbose=True)
