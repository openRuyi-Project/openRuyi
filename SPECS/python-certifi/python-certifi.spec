# SPDX-FileCopyrightText: (C) 2025 Institute of Software, Chinese Academy of Sciences (ISCAS)
# SPDX-FileCopyrightText: (C) 2025 openRuyi Project Contributors
# SPDX-FileContributor: Zheng Junjie <zhengjunjie@iscas.ac.cn>
#
# SPDX-License-Identifier: MulanPSL-2.0

%global srcname certifi

Name:           python-%{srcname}
Version:        2025.11.12
Release:        %autorelease
Summary:        Python CA certificate bundle
License:        MIT
URL:            https://certifi.io
#!RemoteAsset:  sha256:d8ab5478f2ecd78af242878415affce761ca6bc54a22a27e026d7c25357c3316
Source0:        https://files.pythonhosted.org/packages/source/c/%{srcname}/%{srcname}-%{version}.tar.gz
BuildArch:      noarch
BuildSystem:    pyproject

BuildOption(install):  -l %{srcname}

BuildRequires:  pyproject-rpm-macros
BuildRequires:  pkgconfig(python3)
BuildRequires:  python3dist(pip)
BuildRequires:  python3dist(setuptools)

Provides:       python3-%{srcname} = %{version}-%{release}
%python_provide python3-%{srcname}

%description
Certifi is a Python library that contains a CA certificate bundle, which
is used by the Requests library to verify HTTPS requests.

%generate_buildrequires
%pyproject_buildrequires

%files -f %{pyproject_files}
%license LICENSE
%doc README*

%changelog
%autochangelog
