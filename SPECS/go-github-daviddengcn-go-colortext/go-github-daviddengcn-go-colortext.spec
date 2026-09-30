# SPDX-FileCopyrightText: (C) 2026 Institute of Software, Chinese Academy of Sciences (ISCAS)
# SPDX-FileCopyrightText: (C) 2026 openRuyi Project Contributors
#
# SPDX-License-Identifier: MulanPSL-2.0

%define _name           go-colortext
%define go_import_path  github.com/daviddengcn/go-colortext
%define commit_id       511bcaf42ccd42c38aba7427b6673277bf19e2a1

Name:           go-github-daviddengcn-go-colortext
Version:        0+git20260922.511bcaf
Release:        %autorelease
Summary:        Set console foreground and background colors in Go
License:        BSD-3-Clause OR MIT
URL:            https://github.com/daviddengcn/go-colortext
#!RemoteAsset:  sha256:d4ab75bfeb39da14adc69696f26dd00284e79e9938c213a9bfcfb3bd7f314783
Source0:        https://github.com/daviddengcn/go-colortext/archive/%{commit_id}.tar.gz#/%{_name}-%{version}.tar.gz
BuildArch:      noarch
BuildSystem:    golangmodules

BuildRequires:  go
BuildRequires:  go-rpm-macros
BuildRequires:  go(github.com/golangplus/testing)

Provides:       go(github.com/daviddengcn/go-colortext) = %{version}

%description
This library controls console text colors using ANSI escape sequences
on Unix and the console API on Windows.

%files
%doc README.md
%license LICENSE
%{go_sys_gopath}/%{go_import_path}

%changelog
%autochangelog
