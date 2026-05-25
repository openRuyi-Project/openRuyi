# SPDX-FileCopyrightText: (C) 2026 Institute of Software, Chinese Academy of Sciences (ISCAS)
# SPDX-FileCopyrightText: (C) 2026 openRuyi Project Contributors
# SPDX-FileContributor: HNO3Miracle <xiangao.or@isrc.iscas.ac.cn>
#
# SPDX-License-Identifier: MulanPSL-2.0

%define _name           gnuflag
%define go_import_path  github.com/juju/gnuflag

Name:           go-github-juju-gnuflag
Version:        1.0.0
Release:        %autorelease
Summary:        GNU-compatible flag handling with a stdlib-like API for Go
License:        BSD-3-Clause
URL:            https://github.com/juju/gnuflag
#!RemoteAsset:  sha256:97f7598bd77f1fbb21f86350907ce359b3964c150dc6ffc237eb87c606bedad2
Source0:        https://github.com/juju/gnuflag/archive/refs/tags/v%{version}.tar.gz#/%{_name}-%{version}.tar.gz
BuildArch:      noarch
BuildSystem:    golangmodules

BuildRequires:  go
BuildRequires:  go-rpm-macros

Provides:       go(github.com/juju/gnuflag) = %{version}

%description
The gnuflag package is a fork of the Go standard library flag package that
supports GNU-compatible flag syntax.

%files
%doc README.md
%license LICENSE
%{go_sys_gopath}/%{go_import_path}

%changelog
%autochangelog
