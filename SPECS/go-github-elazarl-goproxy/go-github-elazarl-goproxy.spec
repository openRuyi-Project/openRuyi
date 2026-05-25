# SPDX-FileCopyrightText: (C) 2026 Institute of Software, Chinese Academy of Sciences (ISCAS)
# SPDX-FileCopyrightText: (C) 2026 openRuyi Project Contributors
# SPDX-FileContributor: HNO3Miracle <xiangao.or@isrc.iscas.ac.cn>
#
# SPDX-License-Identifier: MulanPSL-2.0

%define _name           goproxy
%define go_import_path  github.com/elazarl/goproxy
# Nested Go modules have their own module path/dependencies. The main package
# tests are also not hermetic in OBS: TestHttpProxyAddrsFromEnv uses
# process-wide proxy environment caching, and TestSimpleHttpRequest binds fixed
# localhost:5000. - HNO3Miracle
%define go_test_exclude_glob %{shrink:
    %{go_import_path}
    %{go_import_path}/examples*
    %{go_import_path}/ext*
}

Name:           go-github-elazarl-goproxy
Version:        1.8.3
Release:        %autorelease
Summary:        Customizable HTTP/HTTPS proxy library for Go
License:        BSD-3-Clause
URL:            https://github.com/elazarl/goproxy
#!RemoteAsset:  sha256:265928cc5d79b863f7c050f1807528e82e37a10f161dae866a5e1a6b40c63d2e
Source0:        https://github.com/elazarl/goproxy/archive/refs/tags/v%{version}.tar.gz#/%{_name}-%{version}.tar.gz
BuildArch:      noarch
BuildSystem:    golangmodules

BuildRequires:  go
BuildRequires:  go-rpm-macros
BuildRequires:  go(github.com/coder/websocket)
BuildRequires:  go(github.com/davecgh/go-spew)
BuildRequires:  go(github.com/pmezard/go-difflib)
BuildRequires:  go(github.com/stretchr/testify)
BuildRequires:  go(golang.org/x/net)
BuildRequires:  go(golang.org/x/text)
BuildRequires:  go(gopkg.in/yaml.v3)

Provides:       go(github.com/elazarl/goproxy) = %{version}

Requires:       go(golang.org/x/net)
Requires:       go(golang.org/x/text)

%description
goproxy is a Go library for building customizable HTTP and HTTPS proxy
servers. It provides hooks for request and response manipulation, CONNECT
handling, MITM proxying, and custom transports.

%files
%doc README.md
%license LICENSE
%{go_sys_gopath}/%{go_import_path}
# Nested Go modules are packaged separately; do not let this module own
# their source directories, otherwise RPM can hit file conflicts.
%exclude %{go_sys_gopath}/%{go_import_path}/examples
%exclude %{go_sys_gopath}/%{go_import_path}/ext

%changelog
%autochangelog
