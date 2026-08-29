# SPDX-FileCopyrightText: (C) 2026 Institute of Software, Chinese Academy of Sciences (ISCAS)
# SPDX-FileCopyrightText: (C) 2026 openRuyi Project Contributors
# SPDX-FileContributor: Kimmy <yucheng.or@isrc.iscas.ac.cn>
#
# SPDX-License-Identifier: MulanPSL-2.0

%global srcname fido2

Name:           python-%{srcname}
Version:        1.1.2
Release:        %autorelease
Summary:        FIDO2/WebAuthn library for clients and servers
License:        BSD-2-Clause AND Apache-2.0 AND MPL-2.0
URL:            https://github.com/Yubico/python-fido2
VCS:            git:https://github.com/Yubico/python-fido2.git
#!RemoteAsset:  sha256:6110d913106f76199201b32d262b2857562cc46ba1d0b9c51fbce30dc936c573
Source0:        https://files.pythonhosted.org/packages/source/f/%{srcname}/%{srcname}-%{version}.tar.gz
BuildArch:      noarch
BuildSystem:    pyproject

BuildOption(install):  %{srcname}
# Skip Windows API module: cannot import name 'WinDLL' from 'ctypes'.
BuildOption(check):  -e 'fido2.win_api'
# Skip non-Linux HID backends.
BuildOption(check):  -e 'fido2.hid.macos'
BuildOption(check):  -e 'fido2.hid.windows'

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

%prep -a
# Relax cryptography upper bound for the version packaged in openRuyi.
sed -i 's/cryptography = ">=2.6, !=35, <44"/cryptography = ">=2.6, !=35"/' pyproject.toml

%generate_buildrequires
%pyproject_buildrequires

%files -f %{pyproject_files}
%doc README.adoc NEWS
%license COPYING COPYING.APLv2 COPYING.MPLv2

%changelog
%autochangelog
