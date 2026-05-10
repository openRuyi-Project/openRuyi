# SPDX-FileCopyrightText: (C) 2026 Institute of Software, Chinese Academy of Sciences (ISCAS)
# SPDX-FileCopyrightText: (C) 2026 openRuyi Project Contributors
# SPDX-FileContributor: Li Guan <guanli.oerv@isrc.iscas.ac.cn>
#
# SPDX-License-Identifier: MulanPSL-2.0

%global srcname botocore

Name:           python-%{srcname}
Version:        1.43.6
Release:        %autorelease
Summary:        The low-level, core functionality of boto3 and the AWS CLI
License:        Apache-2.0
URL:            https://github.com/boto/botocore
#!RemoteAsset:  sha256:b1e395b347356860398da42e61c808cf1e34b6fa7180cf2b9d87d986e1a06ba0
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

Provides:       python3-%{srcname} = %{version}-%{release}
%python_provide python3-%{srcname}

%description
A low-level interface to a growing number of Amazon Web Services.

%generate_buildrequires
%pyproject_buildrequires

%files -f %{pyproject_files}
%license LICENSE.txt
%doc README.rst

%changelog
%autochangelog
