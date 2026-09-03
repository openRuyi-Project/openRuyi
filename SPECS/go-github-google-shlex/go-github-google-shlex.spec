# SPDX-FileCopyrightText: (C) 2026 Institute of Software, Chinese Academy of Sciences (ISCAS)
# SPDX-FileCopyrightText: (C) 2026 openRuyi Project Contributors
#
# SPDX-License-Identifier: MulanPSL-2.0

%define _name           shlex
%define go_import_path  github.com/google/shlex
%define commit_id       e7afc7fbc51079733e9468cdfd1efcd7d196cd1d

Name:           go-github-google-shlex
Version:        0+git20260723.e7afc7f
Release:        %autorelease
Summary:        Shell-style lexical analysis for Go
License:        Apache-2.0
URL:            https://github.com/google/shlex
#!RemoteAsset:  sha256:76630734d2b77222b4c5d89b0fa36ee8ce4a1fa2acae3af6ede75c704104357a
Source0:        https://github.com/google/shlex/archive/%{commit_id}.tar.gz#/%{_name}-%{version}.tar.gz
BuildArch:      noarch
BuildSystem:    golangmodules

BuildRequires:  go
BuildRequires:  go-rpm-macros

Provides:       go(github.com/google/shlex) = %{version}

%description
shlex provides a simple lexer for splitting shell-style command strings into
words while respecting quoting and escaping rules.

%files
%doc README*
%license COPYING
%{go_sys_gopath}/%{go_import_path}

%changelog
%autochangelog
