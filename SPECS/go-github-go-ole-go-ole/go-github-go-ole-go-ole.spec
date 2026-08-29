# SPDX-FileCopyrightText: (C) 2026 Institute of Software, Chinese Academy of Sciences (ISCAS)
# SPDX-FileCopyrightText: (C) 2026 openRuyi Project Contributors
#
# SPDX-License-Identifier: MulanPSL-2.0

%define _name           go-ole
%define go_import_path  github.com/go-ole/go-ole

Name:           go-github-go-ole-go-ole
Version:        1.3.0
Release:        %autorelease
Summary:        Win32 OLE and COM bindings for Go
License:        MIT
URL:            https://github.com/go-ole/go-ole
#!RemoteAsset:  sha256:18fca64d2973bb1fd698caf9496e540a3e9790381b3b28e55dfbe0f1a201f2ad
Source0:        https://github.com/go-ole/go-ole/archive/refs/tags/v%{version}.tar.gz#/%{_name}-%{version}.tar.gz
BuildArch:      noarch
BuildSystem:    golangmodules

BuildRequires:  go
BuildRequires:  go-rpm-macros
BuildRequires:  go(golang.org/x/sys)
BuildRequires:  go(github.com/stretchr/testify)

Provides:       go(github.com/go-ole/go-ole) = %{version}

Requires:       go(golang.org/x/sys)

%description
Go bindings for Microsoft OLE and COM APIs.

%files
%doc README.md
%license LICENSE
%{go_sys_gopath}/%{go_import_path}

%changelog
%autochangelog
