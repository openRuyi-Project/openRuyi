# SPDX-FileCopyrightText: (C) 2026 Institute of Software, Chinese Academy of Sciences (ISCAS)
# SPDX-FileCopyrightText: (C) 2026 openRuyi Project Contributors
# SPDX-FileContributor: Li Guan <guanli.oerv@isrc.iscas.ac.cn>
#
# SPDX-License-Identifier: MulanPSL-2.0

%global srcname sagemaker

Name:           python-%{srcname}
Version:        3.8.0
Release:        %autorelease
Summary:        A library for training and deploying machine learning models on Amazon SageMaker
License:        Apache-2.0
URL:            https://sagemaker.readthedocs.io/en/stable/
VCS:            git:https://github.com/aws/sagemaker-python-sdk.git
#!RemoteAsset:  sha256:7b6663186b066cac9916701c8734e3182874a70cfddec7389a1e0edb07fe03c1
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
