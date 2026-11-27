# SPDX-FileCopyrightText: (C) 2026 Institute of Software, Chinese Academy of Sciences (ISCAS)
# SPDX-FileCopyrightText: (C) 2026 openRuyi Project Contributors
# SPDX-FileContributor: Jingwiw <wangjingwei@iscas.ac.cn>
#
# SPDX-License-Identifier: MulanPSL-2.0

%global srcname crypt-r
%global pypi_name crypt_r

Name:           python-%{srcname}
Version:        3.13.1
Release:        %autorelease
Summary:        Python interface to the system crypt_r function
License:        Python-2.0
URL:            https://github.com/fedora-python/crypt_r
VCS:            git:https://github.com/fedora-python/crypt_r
#!RemoteAsset:  sha256:5bd46ad51f5b7fe5f0ecf49d8ba2cafd6fbd43aa3bb5efbcaa6b44df6340c1a6
Source0:        https://files.pythonhosted.org/packages/source/c/%{pypi_name}/%{pypi_name}-%{version}.tar.gz
BuildSystem:    pyproject

BuildOption(install):  -l crypt crypt_r _crypt_r

BuildRequires:  pyproject-rpm-macros
BuildRequires:  pkgconfig(python3)
BuildRequires:  pkgconfig(libxcrypt)
BuildRequires:  python3dist(pip) >= 19
BuildRequires:  python3dist(setuptools) >= 61
BuildRequires:  gcc

Provides:       python3-%{srcname} = %{version}-%{release}
Provides:       python3-%{srcname}%{?_isa} = %{version}-%{release}

%description
crypt-r provides the crypt module removed from Python 3.13. It uses the
system crypt_r function to verify existing Unix password hashes.

%check -a
PYTHONPATH=%{buildroot}%{python3_sitearch} %{__python3} tests/test_crypt_r.py

%files -f %{pyproject_files}
%doc README.rst

%changelog
%autochangelog
