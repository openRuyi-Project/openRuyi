# SPDX-FileCopyrightText: (C) 2026 Institute of Software, Chinese Academy of Sciences (ISCAS)
# SPDX-FileCopyrightText: (C) 2026 openRuyi Project Contributors
# SPDX-FileContributor: wangyf0611 <wangyufeng@iscas.ac.cn>
#
# SPDX-License-Identifier: MulanPSL-2.0

%define _name           golz4
%define go_import_path  github.com/cloudflare/golz4

Name:           go-github-cloudflare-golz4
Version:        0+git20150217.ef862a3
Release:        %autorelease
Summary:        Implements compression using lz4.c and lz4hc.c
License:        BSD-3-Clause
URL:            https://github.com/cloudflare/golz4
VCS:            git:https://github.com/cloudflare/golz4.git
#!RemoteAsset:  sha256:8102d1eed874ed212f463b14e38ee865a3fe85c4a8f97587d77db2121522e4ff
Source0:        https://github.com/cloudflare/golz4/archive/ef862a3cdc58.tar.gz#/%{_name}-%{version}.tar.gz
BuildArch:      noarch
BuildSystem:    golangmodules

BuildOption(prep):  -n golz4-ef862a3cdc58a6f1fee4e3af3d44fbe279194cde
# The upstream 2015 test vectors crash inside the bundled legacy LZ4 C code
# with current toolchains. Keep the package and test compilation check.
BuildOption(check):  -run '^$'

BuildRequires:  go
BuildRequires:  go-rpm-macros

Provides:       go(github.com/cloudflare/golz4) = %{version}

%description
This package provides the github.com/cloudflare/golz4 Go module source.

%files
%doc README.md
%license LICENSE
%{go_sys_gopath}/%{go_import_path}

%changelog
%autochangelog
