from fastapi import FastAPI, HTTPException
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel
from typing import List
from sqlalchemy import (
    create_engine, Column, Integer, String, Numeric, CheckConstraint
)
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

# Veritabanı bağlantı ayarları
DATABASE_URL = "postgresql://postgres:5493@localhost:5432/gelir_gider" 

engine = create_engine(DATABASE_URL)
SessionLocal = sessionmaker(bind=engine)
Base = declarative_base()

app = FastAPI()

# CORS ayarları
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Ana sayfa
@app.get("/")
def root():
    return {"message": "FastAPI çalışıyor!"}

# =========================
# SQLAlchemy MODELLER
# =========================

class Musteri(Base):
    __tablename__ = "musteri"
    id = Column(Integer, primary_key=True, index=True)
    ad = Column(String)
    soyad = Column(String)
    yas = Column(Integer)
    calisma_durumu = Column(String)
    kredi_puani = Column(Integer)

class GelirGider(Base):
    __tablename__ = "gelir_gider"
    id = Column(Integer, primary_key=True, index=True)
    islem_turu = Column(String(10), nullable=False)
    tutar = Column(Numeric(12, 2), nullable=False)
    kategori = Column(String, nullable=False)
    aciklama = Column(String)

    __table_args__ = (
        CheckConstraint("islem_turu IN ('Gelir', 'Gider')", name="check_islem_turu"),
        CheckConstraint("tutar > 0", name="check_tutar_positive"),
    )

# Tabloları oluştur
Base.metadata.create_all(bind=engine)

# =========================
# Pydantic MODELLER
# =========================

class MusteriCreate(BaseModel):
    ad: str
    soyad: str
    yas: int
    calisma_durumu: str
    kredi_puani: int

class MusteriOut(MusteriCreate):
    id: int

class GelirGiderCreate(BaseModel):
    islem_turu: str
    tutar: float
    kategori: str
    aciklama: str | None = None

class GelirGiderOut(GelirGiderCreate):
    id: int

# =========================
# MÜŞTERİ CRUD
# =========================

@app.post("/musteri/", response_model=MusteriOut)
def musteri_ekle(musteri: MusteriCreate):
    db = SessionLocal()
    db_musteri = Musteri(**musteri.dict())
    db.add(db_musteri)
    db.commit()
    db.refresh(db_musteri)
    db.close()
    return db_musteri

@app.get("/musteri/", response_model=List[MusteriOut])
def musteri_listele():
    db = SessionLocal()
    musteriler = db.query(Musteri).all()
    db.close()
    return musteriler

@app.put("/musteri/{musteri_id}", response_model=MusteriOut)
def musteri_guncelle(musteri_id: int, guncel_musteri: MusteriCreate):
    db = SessionLocal()
    musteri = db.query(Musteri).filter(Musteri.id == musteri_id).first()
    if not musteri:
        raise HTTPException(status_code=404, detail="Müşteri bulunamadı")
    for key, value in guncel_musteri.dict().items():
        setattr(musteri, key, value)
    db.commit()
    db.refresh(musteri)
    db.close()
    return musteri

@app.delete("/gelir-gider/{kayit_id}")
def gelir_gider_sil(kayit_id: int):
    db = SessionLocal()
    kayit = db.query(GelirGider).filter(GelirGider.id == kayit_id).first()
    if not kayit:
        db.close()
        raise HTTPException(status_code=404, detail="Kayıt bulunamadı")
    db.delete(kayit)
    db.commit()
    db.close()
    return {"message": "Kayıt silindi"}

# =========================
# GELİR-GİDER CRUD
# =========================

@app.post("/gelir-gider/", response_model=GelirGiderOut)
def gelir_gider_ekle(kayit: GelirGiderCreate):
    db = SessionLocal()
    yeni_kayit = GelirGider(**kayit.dict())
    db.add(yeni_kayit)
    db.commit()
    db.refresh(yeni_kayit)
    db.close()
    return yeni_kayit

@app.get("/gelir-gider/", response_model=List[GelirGiderOut])
def gelir_gider_listele():
    db = SessionLocal()
    kayitlar = db.query(GelirGider).all()
    db.close()
    return kayitlar

@app.put("/gelir-gider/{kayit_id}", response_model=GelirGiderOut)
def gelir_gider_guncelle(kayit_id: int, guncel_kayit: GelirGiderCreate):
    db = SessionLocal()
    kayit = db.query(GelirGider).filter(GelirGider.id == kayit_id).first()
    if not kayit:
        raise HTTPException(status_code=404, detail="Kayıt bulunamadı")
    for key, value in guncel_kayit.dict().items():
        setattr(kayit, key, value)
    db.commit()
    db.refresh(kayit)
    db.close()
    return kayit

@app.get("/gelir-gider/{kayit_id}", response_model=GelirGiderOut)
def gelir_gider_getir(kayit_id: int):
    db = SessionLocal()
    kayit = db.query(GelirGider).filter(GelirGider.id == kayit_id).first()
    db.close()
    if not kayit:
        raise HTTPException(status_code=404, detail="Kayıt bulunamadı")
    return kayit
