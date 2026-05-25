# SPDX-FileCopyrightText: (C) 2026 Institute of Software, Chinese Academy of Sciences (ISCAS)
# SPDX-FileCopyrightText: (C) 2026 openRuyi Project Contributors
# SPDX-FileContributor: HNO3Miracle <xiangao.or@isrc.iscas.ac.cn>
#
# SPDX-License-Identifier: MulanPSL-2.0

%define _name           errs
%define go_import_path  github.com/zeebo/errs

Name:           go-github-zeebo-errs
Version:        1.4.0
Release:        %autorelease
Summary:        Error handling helpers for Go
License:        MIT
URL:            https://github.com/zeebo/errs
#!RemoteAsset:  sha256:35bb3b9af344c8c164f7b6c21f7b948971623f5d704c9a15534db3e3cb55df20
Source0:        https://github.com/zeebo/errs/archive/refs/tags/v%{version}.tar.gz#/%{_name}-%{version}.tar.gz
BuildArch:      noarch
BuildSystem:    golangmodules

# Current Go vet treats the local assert helper as printf-like, so assertion
# messages must not contain stray printf directives. - HNO3Miracle
Patch2000:      2000-avoid-printf-directives-in-assert-messages.patch

BuildRequires:  go
BuildRequires:  go-rpm-macros

Provides:       go(github.com/zeebo/errs) = %{version}

%description
This package provides error handling helpers for Go.

%files
%doc README.md
%license LICENSE
%{go_sys_gopath}/%{go_import_path}

%changelog
%autochangelog
