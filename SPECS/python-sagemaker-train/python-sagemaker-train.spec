# SPDX-FileCopyrightText: (C) 2026 Institute of Software, Chinese Academy of Sciences (ISCAS)
# SPDX-FileCopyrightText: (C) 2026 openRuyi Project Contributors
# SPDX-FileContributor: Li Guan <guanli.oerv@isrc.iscas.ac.cn>
#
# SPDX-License-Identifier: MulanPSL-2.0

%global srcname sagemaker-train
%global pypi_name sagemaker_train

Name:           python-%{srcname}
Version:        1.26.0
Release:        %autorelease
Summary:        Amazon SageMaker Python SDK for SageMaker Training
License:        Apache-2.0 AND MIT
URL:            https://sagemaker.readthedocs.io/en/stable/
VCS:            git:https://github.com/aws/sagemaker-python-sdk.git
#!RemoteAsset:  sha256:6bfeebd035bff521750c43e5a33ebf89d11ba0864c207543575b74289dd90aa8
Source0:        https://files.pythonhosted.org/packages/source/s/%{srcname}/%{pypi_name}-%{version}.tar.gz
BuildArch:      noarch
BuildSystem:    pyproject

# Graphene is only used for string conversion; GraphQL 3.3 is incompatible.
Patch2000:      2000-use-string-converters-without-graphql.patch

BuildOption(install):  -l sagemaker

BuildRequires:  pyproject-rpm-macros
BuildRequires:  pkgconfig(python3)
BuildRequires:  python3dist(pytest)

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

# SDK initialization needs a region; instance metadata is unavailable during builds.
%check -p
export AWS_DEFAULT_REGION=us-east-1
export AWS_EC2_METADATA_DISABLED=true

%check -a
%pytest tests/test_str_converters.py

%files -f %{pyproject_files}
%doc README.rst
%license LICENSE LICENSE.graphene

%changelog
%autochangelog
