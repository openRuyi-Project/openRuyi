# SPDX-FileCopyrightText: (C) 2026 Institute of Software, Chinese Academy of Sciences (ISCAS)
# SPDX-FileCopyrightText: (C) 2026 openRuyi Project Contributors
#
# SPDX-License-Identifier: MulanPSL-2.0

%define _name           is
%define go_import_path  github.com/matryer/is

Name:           go-github-matryer-is
Version:        1.4.0
Release:        %autorelease
Summary:        Lightweight testing assertions for Go
License:        MIT
URL:            https://github.com/matryer/is
#!RemoteAsset:  sha256:9fdffa00496e767c2585c2fd7dbb018bee65b6f65f95aaeb96966719fbdd3ddc
Source0:        https://github.com/matryer/is/archive/v%{version}.tar.gz#/%{_name}-%{version}.tar.gz
BuildArch:      noarch
BuildSystem:    golangmodules

BuildOption(check):  -vet=off

BuildRequires:  go
BuildRequires:  go-rpm-macros

Provides:       go(github.com/matryer/is) = %{version}

%description
is is a compact testing helper library that provides readable assertions and
failure messages for Go tests.

%files
%doc README*
%license LICENSE*
%{go_sys_gopath}/%{go_import_path}

%changelog
%autochangelog
