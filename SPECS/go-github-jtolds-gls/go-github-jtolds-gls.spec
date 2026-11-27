# SPDX-FileCopyrightText: (C) 2026 Institute of Software, Chinese Academy of Sciences (ISCAS)
# SPDX-FileCopyrightText: (C) 2026 openRuyi Project Contributors
#
# SPDX-License-Identifier: MulanPSL-2.0

%define _name           gls
%define go_import_path  github.com/jtolds/gls

Name:           go-github-jtolds-gls
Version:        4.20
Release:        %autorelease
Summary:        Goroutine-local storage for Go
License:        MIT
URL:            https://github.com/jtolds/gls
#!RemoteAsset:  sha256:6949a08ca9c4afde7fa020857bbad565af69c5ad86e714dc3f8e1701d3c0ea6d
Source0:        https://github.com/jtolds/gls/archive/v%{version}.tar.gz#/%{_name}-%{version}.tar.gz
BuildArch:      noarch
BuildSystem:    golangmodules

BuildRequires:  go
BuildRequires:  go-rpm-macros

Provides:       go(%{go_import_path}) = %{version}

%description
GLS provides goroutine-local storage primitives for Go.

%files
%doc README.md
%license LICENSE
%{go_sys_gopath}/%{go_import_path}

%changelog
%autochangelog
