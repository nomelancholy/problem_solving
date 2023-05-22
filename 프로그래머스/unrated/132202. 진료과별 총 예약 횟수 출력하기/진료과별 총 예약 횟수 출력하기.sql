SELECT MCDP_CD as 진료과코드, COUNT(*) as 5월예약건수
FROM APPOINTMENT
WHERE date_format(APNT_YMD, '%y-%m') like '22-05'
GROUP BY MCDP_CD
ORDER BY 5월예약건수 ASC, 진료과코드 ASC