# SPDX-FileCopyrightText: (C) 2026 Institute of Software, Chinese Academy of Sciences (ISCAS)
# SPDX-FileCopyrightText: (C) 2026 openRuyi Project Contributors
#
# SPDX-License-Identifier: MulanPSL-2.0

%define _name           wal
%define go_import_path  github.com/tidwall/wal

Name:           go-github-tidwall-wal
Version:        1.2.1
Release:        %autorelease
Summary:        Fast write-ahead log for Go
License:        MIT
URL:            https://github.com/tidwall/wal
#!RemoteAsset:  sha256:59b57f49f3a049e03884ff6af0a3225674b969ca7410f1ba70ac9de16c6ba9a3
Source0:        https://github.com/tidwall/wal/archive/v%{version}.tar.gz#/%{_name}-%{version}.tar.gz
BuildArch:      noarch
BuildSystem:    golangmodules

BuildRequires:  go
BuildRequires:  go(github.com/tidwall/gjson)
BuildRequires:  go(github.com/tidwall/tinylru)
BuildRequires:  go-rpm-macros

Provides:       go(%{go_import_path}) = %{version}

Requires:       go(github.com/tidwall/gjson)
Requires:       go(github.com/tidwall/tinylru)

%description
Wal provides a fast and durable write-ahead log implementation for Go.

%files
%doc README.md
%license LICENSE
%{go_sys_gopath}/%{go_import_path}

%changelog
%autochangelog
