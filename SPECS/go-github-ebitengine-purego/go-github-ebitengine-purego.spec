# SPDX-FileCopyrightText: (C) 2026 Institute of Software, Chinese Academy of Sciences (ISCAS)
# SPDX-FileCopyrightText: (C) 2026 openRuyi Project Contributors
#
# SPDX-License-Identifier: MulanPSL-2.0

%define _name           purego
%define go_import_path  github.com/ebitengine/purego

Name:           go-github-ebitengine-purego
Version:        0.11.1
Release:        %autorelease
Summary:        Call C functions from Go without cgo
License:        Apache-2.0
URL:            https://github.com/ebitengine/purego
#!RemoteAsset:  sha256:1131aa9b11d2d78fbdbfdd28c35e4f80a680f41629b10ddef2827f20e08598d2
Source0:        https://github.com/ebitengine/purego/archive/v%{version}.tar.gz#/%{_name}-%{version}.tar.gz
BuildArch:      noarch
BuildSystem:    golangmodules

BuildRequires:  go
BuildRequires:  go-rpm-macros

Provides:       go(%{go_import_path}) = %{version}

%description
PureGo loads shared libraries and calls C functions from Go without requiring
cgo at build time.

%files
%doc README.md
%license LICENSE
%{go_sys_gopath}/%{go_import_path}

%changelog
%autochangelog
