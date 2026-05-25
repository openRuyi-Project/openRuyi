# SPDX-FileCopyrightText: (C) 2026 Institute of Software, Chinese Academy of Sciences (ISCAS)
# SPDX-FileCopyrightText: (C) 2026 openRuyi Project Contributors
# SPDX-FileContributor: HNO3Miracle <xiangao.or@isrc.iscas.ac.cn>
#
# SPDX-License-Identifier: MulanPSL-2.0

%define _name           go-diff
%define go_import_path  github.com/gkampitakis/go-diff

Name:           go-github-gkampitakis-go-diff
Version:        1.3.2
Release:        %autorelease
Summary:        Diff library for Go
License:        MIT
URL:            https://github.com/gkampitakis/go-diff
#!RemoteAsset:  sha256:30f053b4ebfcaaaddc0b6cb3c56473eaa39f5b1c0aa4894e2d15f963e476acfa
Source0:        https://github.com/gkampitakis/go-diff/archive/refs/tags/v%{version}.tar.gz#/%{_name}-%{version}.tar.gz
BuildArch:      noarch
BuildSystem:    golangmodules

BuildRequires:  go
BuildRequires:  go-rpm-macros

Provides:       go(github.com/gkampitakis/go-diff) = %{version}

%description
go-diff provides text diff helpers for Go projects.

%files
%doc README.md
%license LICENSE
%{go_sys_gopath}/%{go_import_path}

%changelog
%autochangelog
