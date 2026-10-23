# SPDX-FileCopyrightText: (C) 2026 Institute of Software, Chinese Academy of Sciences (ISCAS)
# SPDX-FileCopyrightText: (C) 2026 openRuyi Project Contributors
# SPDX-FileContributor: Li Guan <guanli.oerv@isrc.iscas.ac.cn>
#
# SPDX-License-Identifier: MulanPSL-2.0

%global srcname botocore

Name:           python-%{srcname}
Version:        1.43.115
Release:        %autorelease
Summary:        The low-level, core functionality of boto3 and the AWS CLI
License:        Apache-2.0
URL:            https://github.com/boto/botocore
#!RemoteAsset:  sha256:aa4d9c4e7ef99988b7347e0cd276ba84e1eb1625510557b0e36cd57ecb19bbf2
Source0:        https://files.pythonhosted.org/packages/source/b/%{srcname}/%{srcname}-%{version}.tar.gz
BuildArch:      noarch
BuildSystem:    pyproject

BuildOption(install):  -l %{srcname}
BuildOption(check):  -e botocore.docs.translator

BuildRequires:  pyproject-rpm-macros
BuildRequires:  pkgconfig(python3)
BuildRequires:  python3dist(pip)
BuildRequires:  python3dist(setuptools)
BuildRequires:  python3dist(urllib3)
BuildRequires:  python3dist(jmespath)
BuildRequires:  python3dist(python-dateutil)
BuildRequires:  python3dist(awscrt)
BuildRequires:  python3dist(pytest)
BuildRequires:  python3dist(mock)

Provides:       python3-%{srcname} = %{version}-%{release}
%python_provide python3-%{srcname}

%description
A low-level interface to a growing number of Amazon Web Services.

%generate_buildrequires
%pyproject_buildrequires

%check -a
%pytest tests/unit/test_hooks.py tests/unit/test_regions.py tests/unit/test_session.py tests/unit/test_stub.py

%files -f %{pyproject_files}
%doc README.rst
%license LICENSE.txt

%changelog
%autochangelog
