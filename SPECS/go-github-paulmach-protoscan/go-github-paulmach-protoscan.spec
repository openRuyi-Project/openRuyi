# SPDX-FileCopyrightText: (C) 2026 Institute of Software, Chinese Academy of Sciences (ISCAS)
# SPDX-FileCopyrightText: (C) 2026 openRuyi Project Contributors
#
# SPDX-License-Identifier: MulanPSL-2.0

%define _name           protoscan
%define go_import_path  github.com/paulmach/protoscan

Name:           go-github-paulmach-protoscan
Version:        0.2.1
Release:        %autorelease
Summary:        Low-level Protocol Buffers scanner for Go
License:        MIT
URL:            https://github.com/paulmach/protoscan
#!RemoteAsset:  sha256:714e9d717c8e6539fc0ff90a0c9a604f8ba770e30dfe079c6449deab4538fab9
Source0:        https://github.com/paulmach/protoscan/archive/v%{version}.tar.gz#/%{_name}-%{version}.tar.gz
BuildArch:      noarch
BuildSystem:    golangmodules

BuildRequires:  go
BuildRequires:  go-rpm-macros
BuildRequires:  go(google.golang.org/protobuf)

Provides:       go(%{go_import_path}) = %{version}

Requires:       go(google.golang.org/protobuf)

%description
Protoscan scans Protocol Buffers wire data and exposes field values without
requiring generated message types.

%files
%doc README.md
%license LICENSE.md
%{go_sys_gopath}/%{go_import_path}

%changelog
%autochangelog
