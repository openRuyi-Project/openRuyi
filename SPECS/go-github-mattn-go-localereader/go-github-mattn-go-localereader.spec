# SPDX-FileCopyrightText: (C) 2026 Institute of Software, Chinese Academy of Sciences (ISCAS)
# SPDX-FileCopyrightText: (C) 2026 openRuyi Project Contributors
#
# SPDX-License-Identifier: MulanPSL-2.0

%define _name           go-localereader
%define go_import_path  github.com/mattn/go-localereader

Name:           go-github-mattn-go-localereader
Version:        0.0.1
Release:        %autorelease
Summary:        Code-page decoder reader for Windows
License:        MIT
URL:            https://github.com/mattn/go-localereader
#!RemoteAsset:  sha256:03bd5a512b593c793cccd3a1f507e3a5ba6f92681b1fa4f812a53eddbc3751dc
Source0:        https://github.com/mattn/go-localereader/archive/v%{version}.tar.gz#/%{_name}-%{version}.tar.gz
BuildArch:      noarch
BuildSystem:    golangmodules

BuildRequires:  go
BuildRequires:  go-rpm-macros

Provides:       go(github.com/mattn/go-localereader) = %{version}

%description
go-localereader decodes Windows ACP/code-page input into UTF-8.
cmd/acptee is a sample program, not the library.

%prep -a
# cmd/acptee is a sample stdin decoder, not a distributed program.
rm -rf cmd
# Tests call Windows-only NewCodePageDecoder and do not compile on Linux.
rm -f *_test.go

%files
%doc README.md
%{go_sys_gopath}/%{go_import_path}

%changelog
%autochangelog
