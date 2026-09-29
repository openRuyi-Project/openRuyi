# SPDX-FileCopyrightText: (C) 2026 Institute of Software, Chinese Academy of Sciences (ISCAS)
# SPDX-FileCopyrightText: (C) 2026 openRuyi Project Contributors
# SPDX-FileContributor: Li Guan <guanli.oerv@isrc.iscas.ac.cn>
#
# SPDX-License-Identifier: MulanPSL-2.0

%global srcname pyspnego

Name:           python-%{srcname}
Version:        0.12.2
Release:        %autorelease
Summary:        SPNEGO authentication library for Python
License:        MIT
URL:            https://github.com/jborean93/pyspnego
#!RemoteAsset:  sha256:448a491a9bf0e5fb957567fe46e6809fa836aa40dfcccebcc740bb64acb1be1c
Source0:        https://files.pythonhosted.org/packages/source/p/%{srcname}/%{srcname}-%{version}.tar.gz
BuildArch:      noarch
BuildSystem:    pyproject

BuildOption(install):  -l spnego +auto

BuildRequires:  pyproject-rpm-macros
BuildRequires:  pkgconfig(python3)
BuildRequires:  python3dist(cryptography)
BuildRequires:  python3dist(setuptools) >= 77.0.3

Provides:       python3-%{srcname} = %{version}-%{release}
%python_provide python3-%{srcname}

%description
PySPNEGO implements SPNEGO authentication with NTLM, Kerberos, and Negotiate
protocol support for Python applications.

%generate_buildrequires
%pyproject_buildrequires

%files -f %{pyproject_files}
%doc README.md CHANGELOG.md
%license LICENSE
%{_bindir}/pyspnego-parse

%changelog
%autochangelog
