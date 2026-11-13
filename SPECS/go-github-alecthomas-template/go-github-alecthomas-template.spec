# SPDX-FileCopyrightText: (C) 2026 Institute of Software, Chinese Academy of Sciences (ISCAS)
# SPDX-FileCopyrightText: (C) 2026 openRuyi Project Contributors
#
# SPDX-License-Identifier: MulanPSL-2.0

%define _name           template
%define go_import_path  github.com/alecthomas/template
%define commit_id       fb15b899a75114aa79cc930e33c46b577cc664b1

Name:           go-github-alecthomas-template
Version:        0+git20261029.fb15b89
Release:        %autorelease
Summary:        Go text templates with newline elision
License:        BSD-3-Clause
URL:            https://github.com/alecthomas/template
#!RemoteAsset:  sha256:da731f1da0ec350b18ae61412c92ffdb76e994336043349fa8e008705425cc93
Source0:        https://github.com/alecthomas/template/archive/%{commit_id}.tar.gz#/%{_name}-%{version}.tar.gz
BuildArch:      noarch
BuildSystem:    golangmodules

# Use a permanently unprintable character in the Unicode-sensitive test.
# https://github.com/golang/go/commit/def0be5e34d6657c84407c8afe4ace05d10d1848
Patch1000:      1000-use-stable-noncharacter-in-js-escape-test.patch

BuildOption(prep):  -n %{_name}-%{commit_id}

BuildRequires:  go
BuildRequires:  go-rpm-macros

Provides:       go(%{go_import_path}) = %{version}
Provides:       go(%{go_import_path}/parse) = %{version}

%description
This fork of Go's text/template package supports newline elision after a
template action. It includes the template engine, parser, examples, and
complete upstream tests and test data.

%files
%doc README.md
%license LICENSE
%{go_sys_gopath}/%{go_import_path}

%changelog
%autochangelog
