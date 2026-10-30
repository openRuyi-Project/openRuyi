# SPDX-FileCopyrightText: (C) 2026 Institute of Software, Chinese Academy of Sciences (ISCAS)
# SPDX-FileCopyrightText: (C) 2026 openRuyi Project Contributors
#
# SPDX-License-Identifier: MulanPSL-2.0

%define _name           qr
%define go_import_path  rsc.io/qr
%define go_test_exclude %{go_import_path}/coding

Name:           go-rsc-qr
Version:        0.2.0
Release:        %autorelease
Summary:        Basic QR encoder
License:        BSD-3-Clause
URL:            https://github.com/rsc/qr
#!RemoteAsset:  sha256:a39800570e994df470ff3917b2131d80829ae447d3aac794034ef87cb93d1a66
Source0:        https://github.com/rsc/qr/archive/v%{version}.tar.gz#/%{_name}-%{version}.tar.gz
BuildArch:      noarch
BuildSystem:    golangmodules

BuildRequires:  go
BuildRequires:  go-rpm-macros
BuildRequires:  gcc
BuildRequires:  pkgconfig(libqrencode)

Provides:       go(rsc.io/qr) = %{version}

%description
Basic QR encoder.

%files
%doc README.md
%license LICENSE
%{go_sys_gopath}/%{go_import_path}

%changelog
%autochangelog
