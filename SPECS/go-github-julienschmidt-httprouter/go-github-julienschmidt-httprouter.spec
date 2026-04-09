# SPDX-FileCopyrightText: (C) 2026 Institute of Software, Chinese Academy of Sciences (ISCAS)
# SPDX-FileCopyrightText: (C) 2026 openRuyi Project Contributors
# SPDX-FileContributor: misaka00251 <liuxin@iscas.ac.cn>
#
# SPDX-License-Identifier: MulanPSL-2.0

%define _name           httprouter
%define go_import_path  github.com/julienschmidt/httprouter

Name:           go-github-julienschmidt-httprouter
Version:        1.3.0
Release:        %autorelease
Summary:        A high performance HTTP request router that scales well
License:        BSD-3-Clause
URL:            https://github.com/julienschmidt/httprouter
#!RemoteAsset
Source0:        https://github.com/julienschmidt/httprouter/archive/v%{version}.tar.gz#/%{_name}-%{version}.tar.gz
BuildArch:      noarch
BuildSystem:    golangmodules

BuildOption(prep):  -n %{_name}-%{version}

BuildRequires:  go
BuildRequires:  go-rpm-macros

Provides:       go(github.com/julienschmidt/httprouter) = %{version}

%description
HttpRouter is a lightweight high performance HTTP request router (also
called *multiplexer* or just *mux* for short) for Go
(https://golang.org/).

In contrast to the default mux
(https://golang.org/pkg/net/http/#ServeMux) of Go's net/http package,
this router supports variables in the routing pattern and matches
against the request method. It also scales better.

The router is optimized for high performance and a small memory
footprint. It scales well even with very long paths and a large number
of routes. A compressing dynamic trie (radix tree) structure is used for
efficient matching.

%files
%license LICENSE*
%doc README*
%{go_sys_gopath}/%{go_import_path}

%changelog
%autochangelog
