from django.db import models

class User(models.Model): # 사용자
    SEX = (
        ('여성', 'female'),
        ('남성', 'male'),
        ('그외', 'other')
    )
    email = models.EmailField('이메일', primary_key=True)
    password = models.CharField('비밀번호', max_length=12, help_text='최대 12자리입니다.')
    name = models.CharField('이름', max_length=5)
    sex = models.CharField('성별', max_length=2, choices=SEX)
    contact = models.CharField('연락처', max_length=11)
    coin = models.PositiveIntegerField('연료', default=0)

class Sponsor(models.Model): # 주최자
    code = models.CharField('주최사코드', max_length=7, primary_key=True)
    name = models.TextField('주최사명')
    si = models.TextField('시')
    gu_dong = models.TextField('구, 동')
    email = models.EmailField('이메일')
    homepage = models.URLField('홈페이지주소')
    contact = models.CharField('연락처', max_length=11)

class Artist(models.Model): # 가수)
    code = models.TextField('가수코드',primary_key=True)
    name = models.TextField('가수명')
    debut = models.DateField('데뷔년도')

class Concert(models.Model): # 공연 정보
    GENRE = (
        ('락/메탈', '락/메탈'),
        ('발라드/R&B', '발라드/R&B'),
        ('일렉트로니카', '일렉트로니카'),
        ('댄스', '댄스'),
        ('포크', '포크'),
        ('트로트', '트로트'),
        ('힙합/랩', '힙합/랩'),
        ('크로스오버', '크로스오버'),
        ('뉴에이지', '뉴에이지'),
        ('클럽뮤직', '클럽뮤직'),
        ('재즈/블루스', '재즈/블루스'),
        ('J-POP', 'J-POP'),
        ('콘서트', '콘서트'),
        ('탱고', '탱고'),
        ('내한공연', '내한공연'),
        ('개그콘서트', '개그콘서트')
    )
    STATUS = (
        ('진행', '진행'),
        ('예정', '예정'),
        ('종료', '종료')
    )
    code = models.CharField('공연코드', max_length=8, primary_key=True)
    sponsor = models.ForeignKey(Sponsor, on_delete=models.CASCADE)
    name = models.TextField('공연이름')
    genre = models.CharField('공연장르', max_length=7, choices=GENRE)
    rating = models.TextField('관람등급')
    poster = models.ImageField('공연포스터')
    description = models.TextField('공연설명', default="N/A")
    date = models.DateTimeField('관람시간')
    status = models.CharField('상태', max_length=2, choices=STATUS)

class Schedule(models.Model): # 공연 일정
    concert = models.ForeignKey(Concert, primary_key=True, on_delete=models.CASCADE)
    date = models.DateField('공연날짜')

class Time(models.Model): # 공연 회차
    date = models.DateField('공연날짜', primary_key=True)
    time = models.DateTimeField('공연시간')

class Ticket(models.Model): # 티켓
    concert = models.ForeignKey(Concert, on_delete=models.CASCADE)
    section = models.TextField('좌석구역')
    price = models.IntegerField('티켓값', default=0)
    class Meta:
        unique_together = (
            ('concert', 'section')
        )

class Seat(models.Model): # 좌석
    concert = models.ForeignKey(Concert, on_delete=models.CASCADE)
    section = models.TextField('좌석구역')
    number = models.IntegerField('좌석번호', default=0)
    class Meta:
        unique_together = (
            ('concert', 'section')
        )

class FArtist(models.Model): # 관심 가수
    email = models.ForeignKey(User, on_delete=models.CASCADE)
    artist = models.ForeignKey(Artist, on_delete=models.CASCADE)
    class Meta:
        unique_together = (
            ('email', 'artist')
        )

class FConcert(models.Model): # 관심 공연
    email = models.ForeignKey(User, on_delete=models.CASCADE)
    concert = models.ForeignKey(Concert, on_delete=models.CASCADE)
    class Meta:
        unique_together = (
            ('email', 'concert')
        )

class Book(models.Model): # 예매하다
    email = models.ForeignKey(User, on_delete=models.CASCADE)
    artist = models.ForeignKey(Concert, on_delete=models.CASCADE)
    booked_at = models.DateTimeField('예매일시', auto_now_add=True)
    coin = models.IntegerField('사용연료')
    class Meta:
        unique_together = (
            ('email', 'artist')
        )

class Perform(models.Model): # 공연하다
    artist = models.ForeignKey(Artist, on_delete=models.CASCADE)
    concert = models.ForeignKey(Concert, on_delete=models.CASCADE)
    class Meta:
        unique_together = (
            ('artist', 'concert')
        )
