# SPDX-FileCopyrightText: (C) 2026 Institute of Software, Chinese Academy of Sciences (ISCAS)
# SPDX-FileCopyrightText: (C) 2026 openRuyi Project Contributors
# SPDX-FileContributor: HNO3Miracle <xiangao.or@isrc.iscas.ac.cn>
#
# SPDX-License-Identifier: MulanPSL-2.0

%define _name           resize
%define go_import_path  github.com/nfnt/resize
%define commit_id 83c6a9932646f83e3267f353373d47347b6036b2

Name:           go-github-nfnt-resize
Version:        0+git20260611.83c6a99
Release:        %autorelease
Summary:        Pure golang image resizing
License:        ISC
URL:            https://github.com/nfnt/resize
#!RemoteAsset:  sha256:8e10018e7e272917a57525dc42d443075a5c040c9f2ee73907562a8d84a45f4b
Source0:        https://github.com/nfnt/resize/archive/%{commit_id}.tar.gz#/%{_name}-%{version}.tar.gz
BuildArch:      noarch
BuildSystem:    golangmodules

BuildRequires:  go
BuildRequires:  go-rpm-macros

Provides:       go(github.com/nfnt/resize) = %{version}

%description
Image resizing for the Go programming language with
common interpolation methods.

%files
%doc README.md
%license LICENSE
%{go_sys_gopath}/%{go_import_path}

%changelog
%autochangelog
