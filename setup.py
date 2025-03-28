from setuptools import setup, find_packages

setup(
    name="wwlei-common-utils",  # 包的名称
    version="0.1.0",  # 版本号
    author="Lei Wang",
    author_email="greatbestlei@gmail.com",
    description="common utils",
    long_description=open("README.md").read(),
    long_description_content_type="text/markdown",
    url="https://github.com/wang14597/wwlei-common-utils.git",  # GitHub 仓库地址
    packages=find_packages(),  # 自动发现包
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires=">=3.9",  # Python 版本要求
    install_requires=[
        "annotated-types==0.7.0",
        "anyio==4.9.0",
        "cachetools==5.5.2",
        "certifi==2025.1.31",
        "charset-normalizer==3.4.1",
        "docstring_parser==0.16",
        "ffmpeg-python==0.2.0",
        "future==1.0.0",
        "google-api-core==2.24.2",
        "google-auth==2.38.0",
        "google-cloud-aiplatform==1.71.1",
        "google-cloud-bigquery==3.30.0",
        "google-cloud-core==2.4.3",
        "google-cloud-resource-manager==1.14.2",
        "google-cloud-storage==2.19.0",
        "google-crc32c==1.7.0",
        "google-genai==1.5.0",
        "google-resumable-media==2.7.2",
        "googleapis-common-protos==1.69.2",
        "grpc-google-iam-v1==0.14.2",
        "grpcio==1.71.0",
        "grpcio-status==1.71.0",
        "h11==0.14.0",
        "httpcore==1.0.7",
        "httpx==0.28.1",
        "idna==3.10",
        "numpy==2.2.4",
        "packaging==24.2",
        "proto-plus==1.26.1",
        "protobuf==5.29.3",
        "pyasn1==0.6.1",
        "pyasn1_modules==0.4.1",
        "pydantic==2.10.6",
        "pydantic_core==2.27.2",
        "python-dateutil==2.9.0.post0",
        "requests==2.32.3",
        "rsa==4.9",
        "shapely==2.0.7",
        "six==1.17.0",
        "sniffio==1.3.1",
        "typing_extensions==4.12.2",
        "urllib3==2.3.0",
        "vertexai==1.71.1",
        "websockets==14.2",
        "SQLAlchemy==2.0.39",
        "greenlet==3.1.1",
        "google-cloud-texttospeech==2.25.1"
    ],
)
