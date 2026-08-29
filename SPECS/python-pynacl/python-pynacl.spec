# SPDX-FileCopyrightText: (C) 2025 Institute of Software, Chinese Academy of Sciences (ISCAS)
# SPDX-FileCopyrightText: (C) 2025 openRuyi Project Contributors
# SPDX-FileContributor: Zheng Junjie <zhengjunjie@iscas.ac.cn>
#
# SPDX-License-Identifier: MulanPSL-2.0

%global srcname pynacl
%global pypi_name PyNaCl

Name:           python-%{srcname}
Version:        1.6.2
Release:        %autorelease
License:        Apache-2.0
URL:            https://github.com/pyca/pynacl/
Summary:        Python bindings to libsodium
#!RemoteAsset:  sha256:018494d6d696ae03c7e656e5e74cdfd8ea1326962cc401bcf018f1ed8436811c
Source0:        https://files.pythonhosted.org/packages/source/P/%{pypi_name}/%{srcname}-%{version}.tar.gz
BuildSystem:    pyproject

BuildOption(install):  -l nacl +auto

BuildRequires:  pkgconfig(libsodium)
BuildRequires:  pyproject-rpm-macros
BuildRequires:  python3dist(pytest)
BuildRequires:  python3dist(hypothesis)
BuildRequires:  pkgconfig(python3)

Provides:       python3-%{srcname} = %{version}-%{release}
Provides:       python3-%{srcname}%{?_isa} = %{version}-%{release}
%python_provide python3-%{srcname}

%description
PyNaCl is a Python binding to libsodium, which is a fork of the
Networking and Cryptography library.  These libraries have a stated goal
of improving usability, security and speed.

%prep -a
rm -rfv src/libsodium/

%generate_buildrequires
%pyproject_buildrequires

%build -p
export SODIUM_INSTALL=system

%check -a
%pytest

%files -f %{pyproject_files}
%doc README.rst

%changelog
%autochangelog
