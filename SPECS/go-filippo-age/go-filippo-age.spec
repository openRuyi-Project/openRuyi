# SPDX-FileCopyrightText: (C) 2026 Institute of Software, Chinese Academy of Sciences (ISCAS)
# SPDX-FileCopyrightText: (C) 2026 openRuyi Project Contributors
#
# SPDX-License-Identifier: MulanPSL-2.0

%define _name           age
%define go_import_path  filippo.io/age

Name:           go-filippo-age
Version:        1.3.2
Release:        %autorelease
Summary:        Simple, modern, and secure file encryption library for Go
License:        BSD-3-Clause
URL:            https://github.com/FiloSottile/age
#!RemoteAsset:  sha256:b07c28c6c4bdafa272073a310b75bc22c49da8904585a89c30e5ca4233e63843
Source0:        https://github.com/FiloSottile/age/archive/v%{version}.tar.gz#/%{_name}-%{version}.tar.gz
BuildArch:      noarch
BuildSystem:    golangmodules

BuildRequires:  go
BuildRequires:  go(c2sp.org/CCTV/age)
BuildRequires:  go(filippo.io/edwards25519)
BuildRequires:  go(filippo.io/hpke)
BuildRequires:  go(filippo.io/nistec)
BuildRequires:  go(github.com/rogpeppe/go-internal)
BuildRequires:  go(golang.org/x/crypto)
BuildRequires:  go(golang.org/x/sys)
BuildRequires:  go(golang.org/x/term)
BuildRequires:  go(golang.org/x/tools)
BuildRequires:  go-rpm-macros

Provides:       go(%{go_import_path}) = %{version}

Requires:       go(c2sp.org/CCTV/age)
Requires:       go(filippo.io/edwards25519)
Requires:       go(filippo.io/hpke)
Requires:       go(filippo.io/nistec)
Requires:       go(github.com/rogpeppe/go-internal)
Requires:       go(golang.org/x/crypto)
Requires:       go(golang.org/x/sys)
Requires:       go(golang.org/x/term)
Requires:       go(golang.org/x/tools)

%description
Age implements the age file encryption format and installs the complete Go
module, including armor, SSH recipient, plugin, and post-quantum support.

%files
%doc README.md
%license LICENSE
%{go_sys_gopath}/%{go_import_path}

%changelog
%autochangelog
