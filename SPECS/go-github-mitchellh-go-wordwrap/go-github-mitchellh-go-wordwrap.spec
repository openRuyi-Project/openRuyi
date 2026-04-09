# SPDX-FileCopyrightText: (C) 2026 Institute of Software, Chinese Academy of Sciences (ISCAS)
# SPDX-FileCopyrightText: (C) 2026 openRuyi Project Contributors
# SPDX-FileContributor: Julian Zhu <julian.oerv@isrc.iscas.ac.cn>
#
# SPDX-License-Identifier: MulanPSL-2.0

%define _name           go-wordwrap
%define go_import_path  github.com/mitchellh/go-wordwrap

Name:           go-github-mitchellh-go-wordwrap
Version:        1.0.1
Release:        %autorelease
Summary:        A Go (golang) library for wrapping words in a string.
License:        MIT
URL:            https://github.com/mitchellh/go-wordwrap
#!RemoteAsset
Source0:        https://github.com/mitchellh/go-wordwrap/archive/v%{version}.tar.gz#/%{_name}-%{version}.tar.gz
BuildArch:      noarch
BuildSystem:    golangmodules

BuildRequires:  go
BuildRequires:  go-rpm-macros

Provides:       go(github.com/mitchellh/go-wordwrap) = %{version}

%description
go-wordwrap (Golang package: wordwrap) is a package for Go that
automatically wraps words into multiple lines. The primary use case for
this is in formatting CLI output, but of course word wrapping is a
generally useful thing to do.

%files
%license LICENSE*
%doc README*
%{go_sys_gopath}/%{go_import_path}

%changelog
%autochangelog
