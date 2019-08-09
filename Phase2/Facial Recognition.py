import face_recognition
picture1 = face_recognition.load_image_file("Paul2.jpg")
face_encoding1 = face_recognition.face_encodings(picture1)[0]
picture2 = face_recognition.load_image_file("lennon1.jpg")
face_encoding2 = face_recognition.face_encodings(picture2)[0]
result = face_recognition.compare_faces([face_encoding1], face_encoding2)
if result[0] == True:
    print("Same person!")
else:
    print("Not the same")
