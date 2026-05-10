# SPDX-FileCopyrightText: (C) 2025 Institute of Software, Chinese Academy of Sciences (ISCAS)
# SPDX-FileCopyrightText: (C) 2025 openRuyi Project Contributors
# SPDX-FileContributor: misaka00251 <liuxin@iscas.ac.cn>
#
# SPDX-License-Identifier: MulanPSL-2.0

%global srcname pyopenssl

Name:           python-%{srcname}
Version:        26.2.0
Release:        %autorelease
Summary:        pyopenssl is a wrapper around the OpenSSL library
License:        Apache-2.0
URL:            https://github.com/pyca/pyopenssl
#!RemoteAsset:  sha256:8c6fcecd1183a7fc897548dfe388b0cdb7f37e018200d8409cf33959dbe35387
Source0:        https://files.pythonhosted.org/packages/source/p/%{srcname}/%{srcname}-%{version}.tar.gz
BuildArch:      noarch
BuildSystem:    pyproject

BuildOption(install):  OpenSSL

BuildRequires:  pyproject-rpm-macros
BuildRequires:  pkgconfig(python3)
BuildRequires:  openssl

Provides:       python3-%{srcname} = %{version}-%{release}
%python_provide python3-%{srcname}

%description
High-level wrapper around a subset of the OpenSSL library, includes among others
 * SSL.Connection objects, wrapping the methods of Python's portable
   sockets
 * Callbacks written in Python
 * Extensive error-handling mechanism, mirroring OpenSSL's error codes

%generate_buildrequires
%pyproject_buildrequires

%files -f %{pyproject_files}
%doc README.rst
%license LICENSE

%changelog
%autochangelog
