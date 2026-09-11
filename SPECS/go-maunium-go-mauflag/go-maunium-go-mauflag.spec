# SPDX-FileCopyrightText: (C) 2026 Institute of Software, Chinese Academy of Sciences (ISCAS)
# SPDX-FileCopyrightText: (C) 2026 openRuyi Project Contributors
#
# SPDX-License-Identifier: MulanPSL-2.0

%define _name           mauflag
%define go_import_path  maunium.net/go/mauflag

Name:           go-maunium-go-mauflag
Version:        1.0.0
Release:        %autorelease
Summary:        Extensible command-line argument parser for Go
License:        GPL-3.0-or-later
URL:            https://github.com/tulir/mauflag
#!RemoteAsset:  sha256:533084852643732519b0e39afa6388a8481c1c44519e71244e72d4b7e333e46b
Source0:        https://github.com/tulir/mauflag/archive/v%{version}.tar.gz#/%{_name}-%{version}.tar.gz
BuildArch:      noarch
BuildSystem:    golangmodules

BuildRequires:  go
BuildRequires:  go-rpm-macros

Provides:       go(maunium.net/go/mauflag) = %{version}

%description
Command-line argument parser for Go supporting short and long flags,
default values, chained flags and custom value types.

%files
%doc README.md
%license LICENSE
%{go_sys_gopath}/%{go_import_path}

%changelog
%autochangelog
