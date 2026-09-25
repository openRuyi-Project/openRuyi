# SPDX-FileCopyrightText: (C) 2026 Institute of Software, Chinese Academy of Sciences (ISCAS)
# SPDX-FileCopyrightText: (C) 2026 openRuyi Project Contributors
#
# SPDX-License-Identifier: MulanPSL-2.0

%define _name           errors
%define go_import_path  github.com/golang-plus/errors

Name:           go-github-golang-plus-errors
Version:        1.0.0
Release:        %autorelease
Summary:        Error wrapping and stack trace utilities for Go
License:        Apache-2.0
URL:            https://github.com/golang-plus/errors
#!RemoteAsset:  sha256:5452d8c1efc5105c0158e76c4b1656bc9c1e2778dbdc929405f29a62006874f4
Source0:        https://github.com/golang-plus/errors/archive/v%{version}.tar.gz#/%{_name}-%{version}.tar.gz
# Upstream added the license after v1.0.0.
# https://github.com/golang-plus/errors/blob/ba223c001a0652d97128ab4f47efee9d7529560b/LICENSE
Source1:        LICENSE
BuildArch:      noarch
BuildSystem:    golangmodules

BuildRequires:  go
BuildRequires:  go-rpm-macros

Provides:       go(github.com/golang-plus/errors) = %{version}

%description
Error wrapping and stack trace utilities for Go.

%prep -a
cp %{SOURCE1} LICENSE

%files
%license LICENSE
%{go_sys_gopath}/%{go_import_path}

%changelog
%autochangelog
