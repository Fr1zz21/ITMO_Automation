-- Создание таблицы 
CREATE Table Doctors (doctor_id integer primary key, first_name varchar(30),
                      last_name varchar(30), specialty varchar(25));
-- Добавление значений 
INSERT INTO Doctors (doctor_id, first_name, last_name, specialty)
VALUES (1, 'Igor', 'Mironov', 'QA'),
(2, 'Chupa','Chups', 'AQA');
-- Выборка
SELECT * 
FROM doctors;
CREATE TABLE Admissions (patient_id integer, admission_date date, 
                         discharge_date date, diagnosis varchar(50), 
                         attending_doctor_id integer, 
                         FOREIGN key (attending_doctor_id) REFERENCES doctors(doctor_id));
INSERt into Admissions (patient_id, admission_date, discharge_date, diagnosis, attending_doctor_id)
VALUES (13, '2025-09-12', '2009-09-13', 'Tooth_Brush', 1),
(34, '2025-10-23', '2025-10-25', 'Break_Leg', 2);
INSERt into Admissions (patient_id, admission_date, discharge_date, diagnosis, attending_doctor_id)
VALUES (234, '2025-09-22', '2009-10-13', 'Tooth_Brush', 1);
SELECT Doctors.first_name, Doctors.last_name, COUNT (attending_doctor_id)
FROM Doctors JOIN Admissions
ON Doctors.doctor_id = Admissions.attending_doctor_id
WHERE attending_doctor_id = 1
-- Удаление информации из таблицы
DELETE 
FROM Admissions WHERE Admissions.patient_id = 23