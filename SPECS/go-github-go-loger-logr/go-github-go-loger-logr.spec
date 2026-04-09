# SPDX-FileCopyrightText: (C) 2026 Institute of Software, Chinese Academy of Sciences (ISCAS)
# SPDX-FileCopyrightText: (C) 2026 openRuyi Project Contributors
# SPDX-FileContributor: Julian Zhu <julian.oerv@isrc.iscas.ac.cn>
#
# SPDX-License-Identifier: MulanPSL-2.0

%define _name           logr
%define go_import_path  github.com/go-logr/logr

Name:           go-github-go-loger-logr
Version:        1.4.3
Release:        %autorelease
Summary:        A simple logging interface for Go
License:        Apache-2.0
URL:            https://github.com/go-logr/logr
#!RemoteAsset
Source0:        https://github.com/go-logr/logr/archive/v%{version}.tar.gz#/%{_name}-%{version}.tar.gz
BuildArch:      noarch
BuildSystem:    golangmodules

BuildRequires:  go
BuildRequires:  go-rpm-macros

Provides:       go(github.com/go-logr/logr) = %{version}

%description
logr offers an(other) opinion on how Go programs and libraries can do
logging without becoming coupled to a particular logging implementation.
This is not an implementation of logging - it is an API.  In fact it is
two APIs with two different sets of users.

The Logger type is intended for application and library authors.  It
provides a relatively small API which can be used everywhere you want to
emit logs.  It defers the actual act of writing logs (to files, to
stdout, or whatever) to the LogSink interface.

The LogSink interface is intended for logging library implementers.  It
is a pure interface which can be implemented by logging frameworks to
provide the actual logging functionality.

%files
%license LICENSE*
%doc README*
%{go_sys_gopath}/%{go_import_path}

%changelog
%autochangelog
