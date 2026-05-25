# SPDX-FileCopyrightText: (C) 2026 Institute of Software, Chinese Academy of Sciences (ISCAS)
# SPDX-FileCopyrightText: (C) 2026 openRuyi Project Contributors
# SPDX-FileContributor: HNO3Miracle <xiangao.or@isrc.iscas.ac.cn>
#
# SPDX-License-Identifier: MulanPSL-2.0

%define _name           aec
%define go_import_path  github.com/morikuni/aec

Name:           go-github-morikuni-aec
Version:        1.1.0
Release:        %autorelease
Summary:        Go wrapper for ANSI escape code
License:        MIT
URL:            https://github.com/morikuni/aec
#!RemoteAsset:  sha256:87f4fe8f7bdcf86ea94d89d993640adaff83302b71fbdfe88a252ec67794111b
Source0:        https://github.com/morikuni/aec/archive/refs/tags/v1.1.0.tar.gz#/%{_name}-%{version}.tar.gz
BuildArch:      noarch
BuildSystem:    golangmodules

BuildOption(prep):  -n aec-1.1.0

BuildRequires:  go
BuildRequires:  go-rpm-macros

Provides:       go(github.com/morikuni/aec) = %{version}


%description
aec

[Image: GoDoc] (https://godoc.org/github.com/morikuni/aec?status.svg)
(https://godoc.org/github.com/morikuni/aec)

Go wrapper for ANSI escape code.

Install

  go get github.com/morikuni/aec


%files
%doc README.md
%license LICENSE
%{go_sys_gopath}/%{go_import_path}

%changelog
%autochangelog
