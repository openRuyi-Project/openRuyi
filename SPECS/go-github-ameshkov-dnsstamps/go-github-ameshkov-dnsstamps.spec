# SPDX-FileCopyrightText: (C) 2026 Institute of Software, Chinese Academy of Sciences (ISCAS)
# SPDX-FileCopyrightText: (C) 2026 openRuyi Project Contributors
#
# SPDX-License-Identifier: MulanPSL-2.0

%define _name           dnsstamps
%define go_import_path  github.com/ameshkov/dnsstamps

Name:           go-github-ameshkov-dnsstamps
Version:        1.0.3
Release:        %autorelease
Summary:        Implementation of DNS stamps for Go
License:        Unlicense
URL:            https://github.com/ameshkov/dnsstamps
#!RemoteAsset:  sha256:2cde00423317663aba5c33fdf1cb94d9aa8f92c26b14d8f96f1ed1183834c761
Source0:        https://github.com/ameshkov/dnsstamps/archive/v%{version}.tar.gz#/%{_name}-%{version}.tar.gz
BuildArch:      noarch
BuildSystem:    golangmodules

BuildOption(prep):  -n %{_name}-%{version}

BuildRequires:  go
BuildRequires:  go-rpm-macros

Provides:       go(github.com/ameshkov/dnsstamps) = %{version}

%description
Go implementation of DNS stamps, adding plain DNS and DNS-over-TLS stamp support.

%files
%doc README.md
%license LICENSE
%{go_sys_gopath}/%{go_import_path}

%changelog
%autochangelog
