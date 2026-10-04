# PLangRec (ComputationalReflection, University of Oviedo; MIT), pinned: its two trained models (the line model, a
# Keras SavedModel, and the stacking meta-model, .h5), downloaded by fetch_models.py from the URLs in common/model.py
# at 3fb01dd and checked by sha256, baked in at build time (runs are offline); TensorFlow/Keras 2.15.0 as in its
# requirements (tensorflow-cpu-aws is TensorFlow's ARM build), every version pinned in requirements.txt.
# identify.py is its `predict`, batched over all files.
FROM python:3.11-slim
COPY requirements.txt /requirements.txt
RUN pip install --no-cache-dir -r /requirements.txt
COPY fetch_models.py /fetch_models.py
RUN python /fetch_models.py && rm /fetch_models.py
ENV OMP_NUM_THREADS=4
COPY identify.py /identify.py
ENTRYPOINT ["python", "/identify.py"]
