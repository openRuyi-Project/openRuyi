# SPDX-FileCopyrightText: (C) 2026 Institute of Software, Chinese Academy of Sciences (ISCAS)
# SPDX-FileCopyrightText: (C) 2026 openRuyi Project Contributors
# SPDX-License-Identifier: MulanPSL-2.0

%define _name           stringprep
%define go_import_path  github.com/xdg-go/stringprep

Name:           go-github-xdg-go-stringprep
Version:        1.0.4
Release:        %autorelease
Summary:        RFC 3454 stringprep implementation for Go
License:        Apache-2.0
URL:            https://github.com/xdg-go/stringprep
#!RemoteAsset:  sha256:dc2abbf4f868d71e035d96986bc5c25921046d0e34c7675b6c1d555589611cf0
Source0:        https://github.com/xdg-go/stringprep/archive/v%{version}.tar.gz#/%{_name}-%{version}.tar.gz
BuildArch:      noarch
BuildSystem:    golangmodules

BuildRequires:  go
BuildRequires:  go-rpm-macros
BuildRequires:  go(golang.org/x/text)

Provides:       go(%{go_import_path}) = %{version}

Requires:       go(golang.org/x/text)

%description
Stringprep implements RFC 3454 and SASLprep from RFC 4013 for Go.

%files
%doc README.md
%license LICENSE
%{go_sys_gopath}/%{go_import_path}

%changelog
%autochangelog
