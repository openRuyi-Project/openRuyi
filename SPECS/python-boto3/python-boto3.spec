# SPDX-FileCopyrightText: (C) 2026 Institute of Software, Chinese Academy of Sciences (ISCAS)
# SPDX-FileCopyrightText: (C) 2026 openRuyi Project Contributors
# SPDX-FileContributor: Li Guan <guanli.oerv@isrc.iscas.ac.cn>
#
# SPDX-License-Identifier: MulanPSL-2.0

%global srcname boto3

Name:           python-%{srcname}
Version:        1.42.89
Release:        %autorelease
Summary:        Boto3, an AWS SDK for Python
License:        Apache-2.0
URL:            https://github.com/boto/boto3
#!RemoteAsset:  sha256:3e43aacc0801bba9bcd23a8c271c089af297a69565f783fcdd357ae0e330bf1e
Source0:        https://files.pythonhosted.org/packages/source/b/%{srcname}/%{srcname}-%{version}.tar.gz
BuildArch:      noarch
BuildSystem:    pyproject

BuildOption(install):  -l %{srcname}

BuildRequires:  pyproject-rpm-macros
BuildRequires:  pkgconfig(python3)
BuildRequires:  python3dist(pip)
BuildRequires:  python3dist(setuptools)
BuildRequires:  python3dist(botocore)
BuildRequires:  python3dist(jmespath)
BuildRequires:  python3dist(s3transfer)
BuildRequires:  python3dist(awscrt)

Provides:       python3-%{srcname}
%python_provide python3-%{srcname}

%description
Boto3 is the Amazon Web Services (AWS) Software Development Kit (SDK) for Python.

%generate_buildrequires
%pyproject_buildrequires

%files -f %{pyproject_files}
%license LICENSE
%doc README.rst

%changelog
%autochangelog
