# SPDX-FileCopyrightText: (C) 2026 Institute of Software, Chinese Academy of Sciences (ISCAS)
# SPDX-FileCopyrightText: (C) 2026 openRuyi Project Contributors
# SPDX-FileContributor: Li Guan <guanli.oerv@isrc.iscas.ac.cn>
#
# SPDX-License-Identifier: MulanPSL-2.0

%global srcname boto3

Name:           python-%{srcname}
Version:        1.43.6
Release:        %autorelease
Summary:        Boto3, an AWS SDK for Python
License:        Apache-2.0
URL:            https://github.com/boto/boto3
#!RemoteAsset:  sha256:e6315effaf12b890b99956e6f8e2c3000a3f64e4ee91943cec3895ce9a836afb
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

Provides:       python3-%{srcname} = %{version}-%{release}
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
