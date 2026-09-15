# SPDX-FileCopyrightText: (C) 2026 Institute of Software, Chinese Academy of Sciences (ISCAS)
# SPDX-FileCopyrightText: (C) 2026 openRuyi Project Contributors
# SPDX-FileContributor: HNO3Miracle <xiangao.or@isrc.iscas.ac.cn>
#
# SPDX-License-Identifier: MulanPSL-2.0

%define _name           histogram
%define go_import_path  github.com/valyala/histogram

Name:           go-github-valyala-histogram
Version:        1.2.0
Release:        %autorelease
Summary:        Fast histogram implementations for Go
License:        MIT
URL:            https://github.com/valyala/histogram
#!RemoteAsset:  sha256:cd0d9a0e35d1f996ddd5d3e570d5c60c1de5723416d8cfaefcfaf6f08c10ebb9
Source0:        https://github.com/valyala/histogram/archive/v%{version}.tar.gz#/%{_name}-%{version}.tar.gz
BuildArch:      noarch
BuildSystem:    golangmodules

BuildRequires:  go
BuildRequires:  go-rpm-macros
BuildRequires:  go(github.com/valyala/fastrand)

Provides:       go(github.com/valyala/histogram) = %{version}

Requires:       go(github.com/valyala/fastrand)

%description
Histogram provides fast fixed-bucket and quantile histogram implementations
for Go applications.

%files
%doc README.md
%license LICENSE
%{go_sys_gopath}/%{go_import_path}

%changelog
%autochangelog
