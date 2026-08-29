# SPDX-FileCopyrightText: (C) 2026 Institute of Software, Chinese Academy of Sciences (ISCAS)
# SPDX-FileCopyrightText: (C) 2026 openRuyi Project Contributors
#
# SPDX-License-Identifier: MulanPSL-2.0

%define _name           httpretty
%define go_import_path  github.com/henvic/httpretty

Name:           go-github-henvic-httpretty
Version:        0.1.4
Release:        %autorelease
Summary:        Prints your HTTP requests pretty on your terminal screen
License:        MIT
URL:            https://github.com/henvic/httpretty
#!RemoteAsset:  sha256:ed8ea43508c568d24317d67a31adb625be452eec49f35a95f8fd95f313484c99
Source0:        https://github.com/henvic/httpretty/archive/v%{version}.tar.gz#/%{_name}-%{version}.tar.gz
BuildArch:      noarch
BuildSystem:    golangmodules

BuildRequires:  go
BuildRequires:  go-rpm-macros
BuildRequires:  go(golang.org/x/tools)

Provides:       go(github.com/henvic/httpretty) = %{version}

%description
Package httpretty prints the HTTP requests of your Go programs pretty on
your terminal screen. It is mostly inspired in curl
(https://curl.haxx.se)'s --verbose mode, and also on the
httputil.DumpRequest (https://golang.org/pkg/net/http/httputil/) and
similar functions.

%files
%doc README.md
%license LICENSE.md
%{go_sys_gopath}/%{go_import_path}

%changelog
%autochangelog
