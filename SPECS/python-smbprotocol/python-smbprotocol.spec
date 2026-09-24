# SPDX-FileCopyrightText: (C) 2026 Institute of Software, Chinese Academy of Sciences (ISCAS)
# SPDX-FileCopyrightText: (C) 2026 openRuyi Project Contributors
# SPDX-FileContributor: Li Guan <guanli.oerv@isrc.iscas.ac.cn>
#
# SPDX-License-Identifier: MulanPSL-2.0

%global srcname smbprotocol

Name:           python-%{srcname}
Version:        1.17.0
Release:        %autorelease
Summary:        SMBv2 and SMBv3 client implementation for Python
License:        MIT
URL:            https://github.com/jborean93/smbprotocol
#!RemoteAsset:  sha256:bcc27edfff7d727a7eb30424138766e1ee216ae2ffc1af03dab0448f29c4731c
Source0:        https://files.pythonhosted.org/packages/source/s/%{srcname}/%{srcname}-%{version}.tar.gz
BuildArch:      noarch
BuildSystem:    pyproject

BuildOption(install):  -l %{srcname} smbclient +auto

BuildRequires:  pyproject-rpm-macros
BuildRequires:  pkgconfig(python3)
BuildRequires:  python3dist(cryptography)
BuildRequires:  python3dist(pyspnego)
BuildRequires:  python3dist(setuptools) >= 77

Provides:       python3-%{srcname} = %{version}-%{release}
%python_provide python3-%{srcname}

%description
Smbprotocol implements the SMBv2 and SMBv3 protocols in Python and provides
high-level file access helpers.

%generate_buildrequires
%pyproject_buildrequires

%files -f %{pyproject_files}
%doc README.md CHANGELOG.md
%license LICENSE

%changelog
%autochangelog
