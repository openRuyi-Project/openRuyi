# SPDX-FileCopyrightText: (C) 2026 Institute of Software, Chinese Academy of Sciences (ISCAS)
# SPDX-FileCopyrightText: (C) 2026 openRuyi Project Contributors
# SPDX-FileContributor: Li Guan <guanli.oerv@isrc.iscas.ac.cn>
#
# SPDX-License-Identifier: MulanPSL-2.0

%global srcname sagemaker-train
%global pypi_name sagemaker_train

Name:           python-%{srcname}
Version:        1.8.0
Release:        %autorelease
Summary:        Amazon SageMaker Python SDK for SageMaker Training
License:        Apache-2.0
URL:            https://sagemaker.readthedocs.io/en/stable/
VCS:            git:https://github.com/aws/sagemaker-python-sdk.git
#!RemoteAsset:  sha256:e241e99c6c3dec0d0464f33e6da87bc45db97867b7ed1f02ff2e264553fac54b
Source0:        https://files.pythonhosted.org/packages/source/s/%{srcname}/%{pypi_name}-%{version}.tar.gz
BuildArch:      noarch
BuildSystem:    pyproject

BuildOption(install):  -l sagemaker

BuildRequires:  pyproject-rpm-macros
BuildRequires:  pkgconfig(python3)

Provides:       python3-%{srcname} = %{version}-%{release}
%python_provide python3-%{srcname}

%description
SageMaker Python SDK is an open source library for
training and deploying machine learning models on Amazon SageMaker.

%prep -a
sed -i '/mlflow/d' pyproject.toml

%generate_buildrequires
%pyproject_buildrequires

%install -a
rm -f %{buildroot}%{python3_sitelib}/sagemaker/__init__.py
rm -f %{buildroot}%{python3_sitelib}/sagemaker/__pycache__/__init__.*
sed -i '\|/sagemaker/__init__.py|d' %{pyproject_files}
sed -i '\|/sagemaker/__pycache__/__init__|d' %{pyproject_files}

%files -f %{pyproject_files}
%doc README.rst
%license LICENSE

%changelog
%autochangelog
