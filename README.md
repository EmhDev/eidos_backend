# EIDOS Backend

Este proyecto implementa el núcleo ético y defensivo de EIDOS usando FastAPI y arquitectura hexagonal.

# Para arrancar 

   uvicorn app.main:app --reload

# run Docker

   docker build -t eidos-backend .
   docker run -p 8000:8000 eidos-backend
