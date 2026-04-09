# SPDX-FileCopyrightText: (C) 2026 Institute of Software, Chinese Academy of Sciences (ISCAS)
# SPDX-FileCopyrightText: (C) 2026 openRuyi Project Contributors
# SPDX-FileContributor: Julian Zhu <julian.oerv@isrc.iscas.ac.cn>
#
# SPDX-License-Identifier: MulanPSL-2.0

%define _name           go-shlex
%define go_import_path  github.com/anmitsu/go-shlex
%define commit_id 38f4b401e2be5955e3e00b843d96e3c406f5094d

Name:           go-github-anmitsu-go-shlex
Version:        0+git20200514.38f4b40
Release:        %autorelease
Summary:        A library to make a lexical analyzer like Unix shell for golang.
License:        MIT
URL:            https://github.com/anmitsu/go-shlex
#!RemoteAsset
Source0:        https://github.com/anmitsu/go-shlex/archive/%{commit_id}.tar.gz#/%{_name}-%{version}.tar.gz
BuildArch:      noarch
BuildSystem:    golangmodules

BuildRequires:  go
BuildRequires:  go-rpm-macros

Provides:       go(github.com/anmitsu/go-shlex) = %{version}

%description
go-shlex is a library to make a lexical analyzer like Unix shell for Go.

%files
%license LICENSE*
%doc README*
%{go_sys_gopath}/%{go_import_path}

%changelog
%autochangelog
