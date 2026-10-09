# SPDX-FileCopyrightText: (C) 2026 Institute of Software, Chinese Academy of Sciences (ISCAS)
# SPDX-FileCopyrightText: (C) 2026 openRuyi Project Contributors
#
# SPDX-License-Identifier: MulanPSL-2.0

%define _name           timberjack
%define go_import_path  github.com/DeRuina/timberjack

Name:           go-github-deruina-timberjack
Version:        1.4.8
Release:        %autorelease
Summary:        Size- and time-based rolling logger for Go
License:        MIT
URL:            https://github.com/DeRuina/timberjack
#!RemoteAsset:  sha256:8764647fdf9309d7f2b6c42b694a5bba96f272205f14f9ca840f50b77a57289b
Source0:        https://github.com/DeRuina/timberjack/archive/v%{version}.tar.gz#/%{_name}-%{version}.tar.gz
BuildArch:      noarch
BuildSystem:    golangmodules

BuildRequires:  go
BuildRequires:  go-rpm-macros
BuildRequires:  go(github.com/fortytw2/leaktest)
BuildRequires:  go(github.com/klauspost/compress)

Provides:       go(%{go_import_path}) = %{version}

Requires:       go(github.com/klauspost/compress)

%description
Timberjack provides rolling log files with size-based and time-based rotation,
compression, retention, and cleanup.

%files
%doc README.md
%license LICENSE
%{go_sys_gopath}/%{go_import_path}

%changelog
%autochangelog
