# SPDX-FileCopyrightText: (C) 2026 Institute of Software, Chinese Academy of Sciences (ISCAS)
# SPDX-FileCopyrightText: (C) 2026 openRuyi Project Contributors
# SPDX-FileContributor: misaka00251 <liuxin@iscas.ac.cn>
#
# SPDX-License-Identifier: MulanPSL-2.0

%define _name           thrift
%define go_import_path  github.com/apache/thrift
# Not gonna include tests & tutorials - 251
%define go_test_exclude_glob %{shrink:
    github.com/apache/thrift/tutorial*
    github.com/apache/thrift/test*
}

Name:           go-github-apache-thrift
Version:        0.22.0
Release:        %autorelease
Summary:        Apache Thrift
License:        Apache-2.0
URL:            https://github.com/apache/thrift
#!RemoteAsset
Source0:        https://github.com/apache/thrift/archive/v%{version}.tar.gz#/%{_name}-%{version}.tar.gz
BuildArch:      noarch
BuildSystem:    golangmodules

BuildOption(prep):  -n %{_name}-%{version}
BuildOption(check):  -skip TestSocketIsntListeningAfterInterrupt

BuildRequires:  go
BuildRequires:  go-rpm-macros

Provides:       go(github.com/apache/thrift) = %{version}

%description
Thrift is a lightweight, language-independent software stack for point-
to-point RPC implementation. Thrift provides clean abstractions and
implementations for data transport, data serialization, and application
level processing. The code generation system takes a simple definition
language as input and generates code across programming languages that
uses the abstracted stack to build interoperable RPC clients and
servers.

%prep -a
# Remove files unrelated to the Go Library
find ./* -maxdepth 0 -type d -not -name "lib" -and -not -name "_build" -exec rm -rf "{}" \;
find ./lib -mindepth 1 -maxdepth 1 -type d -not -name "go" -exec rm -rf "{}" \;
rm -rf lib/go/test

%files
%license LICENSE*
%doc README*
%{go_sys_gopath}/%{go_import_path}

%changelog
%autochangelog
