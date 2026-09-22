# SPDX-FileCopyrightText: (C) 2026 Institute of Software, Chinese Academy of Sciences (ISCAS)
# SPDX-FileCopyrightText: (C) 2026 openRuyi Project Contributors
#
# SPDX-License-Identifier: MulanPSL-2.0

%define _name           gettext-go
%define go_import_path  github.com/chai2010/gettext-go
%define commit_id       c6fed771bfd517099caf0f7a961671fa8ed08723

Name:           go-github-chai2010-gettext-go
Version:        0+git20260922.c6fed77
Release:        %autorelease
Summary:        GNU gettext-compatible translation libraries for Go
License:        BSD-3-Clause
URL:            https://github.com/chai2010/gettext-go
#!RemoteAsset:  sha256:3f05a85a4449fe0d418f2da80757bbe93d1fd31d163683277b30e827ae724e5f
Source0:        https://github.com/chai2010/gettext-go/archive/%{commit_id}.tar.gz#/%{_name}-%{version}.tar.gz
BuildArch:      noarch
BuildSystem:    golangmodules

# Normalize modern Go init/closure names used as translation contexts.
# https://github.com/chai2010/gettext-go/commit/6b9f4b1008e1c41455d40558ca5dade14f360ab8
Patch1000:      1000-Normalize-modern-Go-caller-names.patch
# Keep automatic contexts for package-level closures; upstream removed this legacy API.
Patch2000:      2000-Normalize-package-level-closure-contexts.patch

# Caller-name assertions depend on closure symbols before compiler inlining.
BuildOption(check):  -gcflags=all=-l

BuildRequires:  go
BuildRequires:  go-rpm-macros

Provides:       go(github.com/chai2010/gettext-go) = %{version}

%description
This library loads gettext translation catalogs and provides message
lookup, plural handling and PO/MO encoding for Go applications.

%files
%doc README.md
%license LICENSE
%{go_sys_gopath}/%{go_import_path}

%changelog
%autochangelog
