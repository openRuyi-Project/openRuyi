# SPDX-FileCopyrightText: (C) 2026 Institute of Software, Chinese Academy of Sciences (ISCAS)
# SPDX-FileCopyrightText: (C) 2026 openRuyi Project Contributors
# SPDX-FileContributor: Kimmy <yucheng.or@isrc.iscas.ac.cn>
# SPDX-FileContributor: Li Guan <guanli.oerv@isrc.iscas.ac.cn>
#
# SPDX-License-Identifier: MulanPSL-2.0

%global srcname fido2

Name:           python-%{srcname}
Version:        2.2.1
Release:        %autorelease
Summary:        FIDO2/WebAuthn library for clients and servers
License:        BSD-2-Clause AND Apache-2.0 AND MPL-2.0
URL:            https://github.com/Yubico/python-fido2
VCS:            git:https://github.com/Yubico/python-fido2.git
#!RemoteAsset:  sha256:85787428a94c3f8eaf72f0ff30afba983b559a1b1b795c93318c81b4ad4062c4
Source0:        https://files.pythonhosted.org/packages/source/f/%{srcname}/%{srcname}-%{version}.tar.gz
BuildArch:      noarch
BuildSystem:    pyproject

BuildOption(install):  %{srcname}
# Skip Windows API modules: cannot import name 'WinDLL' / 'HRESULT' from 'ctypes'.
BuildOption(check):  -e 'fido2.client.win_api'
BuildOption(check):  -e 'fido2.client.windows'
# Skip non-Linux HID backends.
BuildOption(check):  -e 'fido2.hid.macos'
BuildOption(check):  -e 'fido2.hid.windows'

BuildRequires:  pcsc-lite
BuildRequires:  pyproject-rpm-macros
BuildRequires:  pkgconfig(python3)
BuildRequires:  python3dist(cryptography)
BuildRequires:  python3dist(pip)
BuildRequires:  python3dist(poetry-core)
BuildRequires:  python3dist(pyscard)

Provides:       python3-%{srcname} = %{version}-%{release}
%python_provide python3-%{srcname}

%description
python-fido2 provides library functionality for communicating with FIDO2 and
U2F authenticators, and for implementing WebAuthn clients and servers.

%generate_buildrequires
%pyproject_buildrequires

%files -f %{pyproject_files}
%doc README.adoc NEWS
%license COPYING COPYING.APLv2 COPYING.MPLv2

%changelog
%autochangelog
