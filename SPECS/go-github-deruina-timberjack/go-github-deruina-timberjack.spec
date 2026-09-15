# SPDX-FileCopyrightText: (C) 2026 Institute of Software, Chinese Academy of Sciences (ISCAS)
# SPDX-FileCopyrightText: (C) 2026 openRuyi Project Contributors
#
# SPDX-License-Identifier: MulanPSL-2.0

%define _name           timberjack
%define go_import_path  github.com/DeRuina/timberjack

Name:           go-github-deruina-timberjack
Version:        1.4.6
Release:        %autorelease
Summary:        Size- and time-based rolling logger for Go
License:        MIT
URL:            https://github.com/DeRuina/timberjack
#!RemoteAsset:  sha256:390a6801573946fb63d30a02092f98b5b465b00bef327e466e05df61820d7661
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
