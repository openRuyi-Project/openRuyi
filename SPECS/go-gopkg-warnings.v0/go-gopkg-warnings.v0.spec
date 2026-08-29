# SPDX-FileCopyrightText: (C) 2026 Institute of Software, Chinese Academy of Sciences (ISCAS)
# SPDX-FileCopyrightText: (C) 2026 openRuyi Project Contributors
# SPDX-FileContributor: HNO3Miracle <xiangao.or@isrc.iscas.ac.cn>
#
# SPDX-License-Identifier: MulanPSL-2.0

%define _name           warnings.v0
%define go_import_path  gopkg.in/warnings.v0

Name:           go-gopkg-warnings.v0
Version:        0.1.2
Release:        %autorelease
Summary:        Non-fatal warning errors for Go
License:        BSD-2-Clause
URL:            https://github.com/go-warnings/warnings
#!RemoteAsset:  sha256:4712c4ceae321433d8c1d9ebc6afd154d7932c849129ded48b1c4a51c21275e8
Source0:        https://github.com/go-warnings/warnings/archive/refs/tags/v%{version}.tar.gz#/%{_name}-%{version}.tar.gz
BuildArch:      noarch
BuildSystem:    golangmodules

BuildRequires:  go
BuildRequires:  go-rpm-macros

Provides:       go(gopkg.in/warnings.v0) = %{version}

%description
warnings implements error handling helpers for non-fatal errors that should be
reported as warnings.

%files
%doc README
%license LICENSE
%{go_sys_gopath}/%{go_import_path}

%changelog
%autochangelog
