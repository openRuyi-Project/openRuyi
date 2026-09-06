# SPDX-FileCopyrightText: (C) 2026 Institute of Software, Chinese Academy of Sciences (ISCAS)
# SPDX-FileCopyrightText: (C) 2026 openRuyi Project Contributors
#
# SPDX-License-Identifier: MulanPSL-2.0

%define _name           tinylru
%define go_import_path  github.com/tidwall/tinylru

Name:           go-github-tidwall-tinylru
Version:        1.2.1
Release:        %autorelease
Summary:        Tiny LRU cache for Go
License:        MIT
URL:            https://github.com/tidwall/tinylru
#!RemoteAsset:  sha256:05edd231678979e29870788cc550ab17eeaca5cb0adc647a2617dcc7f03b110f
Source0:        https://github.com/tidwall/tinylru/archive/v%{version}.tar.gz#/%{_name}-%{version}.tar.gz
BuildArch:      noarch
BuildSystem:    golangmodules

BuildRequires:  go
BuildRequires:  go-rpm-macros

Provides:       go(%{go_import_path}) = %{version}

%description
Tinylru provides small fixed-capacity and generic LRU caches for Go.

%files
%doc README.md
%license LICENSE
%{go_sys_gopath}/%{go_import_path}

%changelog
%autochangelog
