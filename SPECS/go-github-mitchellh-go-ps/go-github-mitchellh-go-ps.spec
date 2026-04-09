# SPDX-FileCopyrightText: (C) 2026 Institute of Software, Chinese Academy of Sciences (ISCAS)
# SPDX-FileCopyrightText: (C) 2026 openRuyi Project Contributors
# SPDX-FileContributor: Julian Zhu <julian.oerv@isrc.iscas.ac.cn>
#
# SPDX-License-Identifier: MulanPSL-2.0

%define _name           go-ps
%define go_import_path  github.com/mitchellh/go-ps

Name:           go-github-mitchellh-go-ps
Version:        1.0.0
Release:        %autorelease
Summary:        Find, list, and inspect processes from Go (golang).
License:        MIT
URL:            https://github.com/mitchellh/go-ps
#!RemoteAsset
Source0:        https://github.com/mitchellh/go-ps/archive/v%{version}.tar.gz#/%{_name}-%{version}.tar.gz
BuildArch:      noarch
BuildSystem:    golangmodules

BuildRequires:  go
BuildRequires:  go-rpm-macros

Provides:       go(github.com/mitchellh/go-ps) = %{version}

%description
go-ps is a library for Go that implements OS-specific APIs to list and
manipulate processes in a platform-safe way. The library can find and
list processes on Linux, Mac OS X, Solaris, and Windows.

If you're new to Go, this library has a good amount of advanced Go
educational value as well. It uses some advanced features of Go: build
tags, accessing DLL methods for Windows, cgo for Darwin, etc.

%files
%license LICENSE*
%doc README*
%{go_sys_gopath}/%{go_import_path}

%changelog
%autochangelog
