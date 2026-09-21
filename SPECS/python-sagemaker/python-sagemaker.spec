# SPDX-FileCopyrightText: (C) 2026 Institute of Software, Chinese Academy of Sciences (ISCAS)
# SPDX-FileCopyrightText: (C) 2026 openRuyi Project Contributors
# SPDX-FileContributor: Li Guan <guanli.oerv@isrc.iscas.ac.cn>
#
# SPDX-License-Identifier: MulanPSL-2.0

%global srcname sagemaker

Name:           python-%{srcname}
Version:        3.11.0
Release:        %autorelease
Summary:        A library for training and deploying machine learning models on Amazon SageMaker
License:        Apache-2.0
URL:            https://sagemaker.readthedocs.io/en/stable/
VCS:            git:https://github.com/aws/sagemaker-python-sdk.git
#!RemoteAsset:  sha256:93f20ba7751063e179f25cd1a38b8f88bff086f0cd273fff5b72a3a78d4610c5
Source0:        https://files.pythonhosted.org/packages/source/s/%{srcname}/%{srcname}-%{version}.tar.gz
BuildArch:      noarch
BuildSystem:    pyproject

# This package contains no actual code.
BuildOption(install):  -l '*'

BuildRequires:  pyproject-rpm-macros
BuildRequires:  pkgconfig(python3)

Provides:       python3-%{srcname} = %{version}-%{release}
%python_provide python3-%{srcname}

%description
SageMaker Python SDK is an open source library for training
and deploying machine learning models on Amazon SageMaker.

%generate_buildrequires
%pyproject_buildrequires

# This package contains no actual code, No tests.
%check

%files -f %{pyproject_files}
%doc README.rst
%license LICENSE

%changelog
%autochangelog
