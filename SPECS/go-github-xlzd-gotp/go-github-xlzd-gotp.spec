# SPDX-FileCopyrightText: (C) 2026 Institute of Software, Chinese Academy of Sciences (ISCAS)
# SPDX-FileCopyrightText: (C) 2026 openRuyi Project Contributors
#
# SPDX-License-Identifier: MulanPSL-2.0

%define _name           gotp
%define go_import_path  github.com/xlzd/gotp

Name:           go-github-xlzd-gotp
Version:        0.1.0
Release:        %autorelease
Summary:        One-time password library for Go
License:        MIT
URL:            https://github.com/xlzd/gotp
#!RemoteAsset:  sha256:f40b63ae731d140158baad46df1a4c35f2aacff033633278a0dba7e61d23eb72
Source0:        https://github.com/xlzd/gotp/archive/refs/tags/v%{version}.tar.gz#/%{_name}-%{version}.tar.gz
BuildArch:      noarch
BuildSystem:    golangmodules

BuildRequires:  go
BuildRequires:  go-rpm-macros

Provides:       go(%{go_import_path}) = %{version}

%description
Gotp implements time-based and counter-based one-time passwords in Go.

%files
%doc README.md
%license LICENSE
%{go_sys_gopath}/%{go_import_path}

%changelog
%autochangelog
