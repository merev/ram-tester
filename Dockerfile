FROM python:3.9-alpine

WORKDIR /app

# Install psutil for better memory monitoring
RUN pip install psutil

COPY memory_hog_advanced.py .

CMD ["python", "memory_hog_advanced.py"]
