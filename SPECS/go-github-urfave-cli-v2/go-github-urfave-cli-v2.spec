# SPDX-FileCopyrightText: (C) 2026 Institute of Software, Chinese Academy of Sciences (ISCAS)
# SPDX-FileCopyrightText: (C) 2026 openRuyi Project Contributors
#
# SPDX-License-Identifier: MulanPSL-2.0

%define _name           cli
%define go_import_path  github.com/urfave/cli/v2

Name:           go-github-urfave-cli-v2
Version:        2.27.7
Release:        %autorelease
Summary:        Provides a minimal framework for creating and organizing command line Go applications
License:        MIT
URL:            https://github.com/urfave/cli
#!RemoteAsset:  sha256:328901eeafba69fd9c3c9f6bbee5813a5a0faacc206256222586684b43d89f4e
Source0:        https://github.com/urfave/cli/archive/v%{version}.tar.gz#/%{_name}-%{version}.tar.gz
BuildArch:      noarch
BuildSystem:    golangmodules

BuildRequires:  go
BuildRequires:  go-rpm-macros
BuildRequires:  go(github.com/BurntSushi/toml)
BuildRequires:  go(github.com/cpuguy83/go-md2man/v2)
BuildRequires:  go(github.com/xrash/smetrics)
BuildRequires:  go(golang.org/x/text)
BuildRequires:  go(gopkg.in/yaml.v3)

Provides:       go(github.com/urfave/cli/v2) = %{version}

Requires:       go(github.com/BurntSushi/toml)
Requires:       go(github.com/cpuguy83/go-md2man/v2)
Requires:       go(github.com/xrash/smetrics)
Requires:       go(golang.org/x/text)
Requires:       go(gopkg.in/yaml.v3)

%description
cli is a simple, fast, and fun package for building command line apps in
Go. The goal is to enable developers to write fast and distributable
command line applications in an expressive way.

%files
%doc README.md
%license LICENSE
%{go_sys_gopath}/%{go_import_path}

%changelog
%autochangelog
