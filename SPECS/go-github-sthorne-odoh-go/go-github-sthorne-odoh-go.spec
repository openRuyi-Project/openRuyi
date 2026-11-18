# SPDX-FileCopyrightText: (C) 2026 Institute of Software, Chinese Academy of Sciences (ISCAS)
# SPDX-FileCopyrightText: (C) 2026 openRuyi Project Contributors
#
# SPDX-License-Identifier: MulanPSL-2.0

%define _name           odoh-go
%define go_import_path  github.com/sthorne/odoh-go

Name:           go-github-sthorne-odoh-go
Version:        1.0.4
Release:        %autorelease
Summary:        This library implements version 0x0001 of Oblivious DoH
License:        MIT
URL:            https://github.com/sthorne/odoh-go
#!RemoteAsset:  sha256:0ebb9cb770318acf36e9de6377ffd90bb738e15f0c7cfbbc941cfb4fde5f4eaa
Source0:        https://github.com/sthorne/odoh-go/archive/v%{version}.tar.gz#/%{_name}-%{version}.tar.gz
BuildArch:      noarch
BuildSystem:    golangmodules

BuildOption(prep):  -n %{_name}-%{version}
# Disable Go vet printf check on upstream odoh_test.go non-constant format string.
BuildOption(check):  -vet=off

BuildRequires:  go
BuildRequires:  go-rpm-macros
BuildRequires:  go(github.com/cisco/go-hpke)

Provides:       go(github.com/sthorne/odoh-go) = %{version}

Requires:       go(github.com/cisco/go-hpke)

%description
Go implementation of Oblivious DNS over HTTPS (ODoH).

%files
%doc README.md
%license LICENSE.md
%{go_sys_gopath}/%{go_import_path}

%changelog
%autochangelog
