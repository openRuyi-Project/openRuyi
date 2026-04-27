# SPDX-FileCopyrightText: (C) 2026 Institute of Software, Chinese Academy of Sciences (ISCAS)
# SPDX-FileCopyrightText: (C) 2026 openRuyi Project Contributors
# SPDX-FileContributor: purofle <yuguo.or@isrc.iscas.ac.cn>
#
# SPDX-License-Identifier: MulanPSL-2.0

%global srcname pycares

Name:           python-%{srcname}
Version:        5.0.1
Release:        %autorelease
Summary:        Python interface for c-ares
License:        MIT
URL:            https://github.com/saghul/pycares
#!RemoteAsset:  sha256:5a3c249c830432631439815f9a818463416f2a8cbdb1e988e78757de9ae75081
Source0:        https://files.pythonhosted.org/packages/source/p/%{srcname}/%{srcname}-%{version}.tar.gz
BuildSystem:    pyproject

BuildOption(install):  -l %{srcname}

BuildRequires:  pyproject-rpm-macros
BuildRequires:  pkgconfig(python3)
BuildRequires:  python3dist(setuptools)
BuildRequires:  python3dist(pip)
BuildRequires:  python3dist(wheel)
BuildRequires:  python3dist(pytest)
BuildRequires:  python3dist(idna)
BuildRequires:  python3dist(cffi)
BuildRequires:  pkgconfig(libcares)

Provides:       python3-%{srcname} = %{version}-%{release}
Provides:       python3-%{srcname}%{?_isa} = %{version}-%{release}
%python_provide python3-%{srcname}

%description
pycares is a Python module which provides an interface to c-ares.
c-ares is a C library that performs DNS requests and name resolutions asynchronously.

%prep -a
rm -r deps/c-ares

%build -p
export PYCARES_USE_SYSTEM_LIB=1

%generate_buildrequires
%pyproject_buildrequires

%files -f %{pyproject_files}
%doc README.rst
%license LICENSE

%changelog
%autochangelog
