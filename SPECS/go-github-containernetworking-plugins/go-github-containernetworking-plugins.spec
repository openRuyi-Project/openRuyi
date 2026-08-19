# SPDX-FileCopyrightText: (C) 2026 Institute of Software, Chinese Academy of Sciences (ISCAS)
# SPDX-FileCopyrightText: (C) 2026 openRuyi Project Contributors
#
# SPDX-License-Identifier: MulanPSL-2.0

%define _name           plugins
%define go_import_path  github.com/containernetworking/plugins
# Package, plugin, and integration tests require privileges or tools
# unavailable in OBS (including network namespaces, netfilter, and cnitool).
# - Jvle
%define go_test_exclude_glob %{shrink:
    %{go_import_path}/pkg/*
    %{go_import_path}/plugins/*
    %{go_import_path}/integration
}

Name:           go-github-containernetworking-plugins
Version:        1.9.1
Release:        %autorelease
Summary:        Standard networking plugins for the Container Network Interface
License:        Apache-2.0
URL:            https://github.com/containernetworking/plugins
#!RemoteAsset:  sha256:34bd82d47e981940751619c9cc44c095bb90bfcaf8d71865cbb822c37690a764
Source0:        https://github.com/containernetworking/plugins/archive/refs/tags/v%{version}.tar.gz#/%{_name}-%{version}.tar.gz
BuildArch:      noarch
BuildSystem:    golangmodules

BuildRequires:  go
BuildRequires:  go-rpm-macros
BuildRequires:  go(golang.org/x/sys)

Provides:       go(github.com/containernetworking/plugins) = %{version}
Provides:       go(github.com/containernetworking/plugins/pkg/ns) = %{version}

Requires:       go(golang.org/x/sys)

%description
This package provides the Go libraries for Container Network Interface
plugins, including the network namespace helper package.

%files
%doc README.md
%license LICENSE
%{go_sys_gopath}/%{go_import_path}

%changelog
%autochangelog
