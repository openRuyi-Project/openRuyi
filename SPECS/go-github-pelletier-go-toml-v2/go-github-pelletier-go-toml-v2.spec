# SPDX-FileCopyrightText: (C) 2026 Institute of Software, Chinese Academy of Sciences (ISCAS)
# SPDX-FileCopyrightText: (C) 2026 openRuyi Project Contributors
# SPDX-FileContributor: misaka00251 <liuxin@iscas.ac.cn>
# SPDX-FileContributor: Julian Zhu <julian.oerv@isrc.iscas.ac.cn>
#
# SPDX-License-Identifier: MulanPSL-2.0

%define _name           go-toml
%define go_import_path  github.com/pelletier/go-toml/v2

Name:           go-github-pelletier-go-toml-v2
Version:        2.4.3
Release:        %autorelease
Summary:        Go library for the TOML file format
License:        MIT
URL:            https://github.com/pelletier/go-toml
#!RemoteAsset:  sha256:0778701c7c7d3261510da7f622c20bfc17c204c80134c1e032aacc99e14c8b35
Source0:        https://github.com/pelletier/go-toml/archive/v%{version}.tar.gz#/%{_name}-%{version}.tar.gz
BuildArch:      noarch
BuildSystem:    golangmodules

BuildOption(prep):  -n %{_name}-%{version}
BuildOption(check):  -vet=off -short

BuildRequires:  go
BuildRequires:  go-rpm-macros

Provides:       go(github.com/pelletier/go-toml/v2) = %{version}

%description
Go library for the TOML (https://toml.io/en/) format.

This library supports TOML v1.0.0 (https://toml.io/en/v1.0.0).

%files
%license LICENSE*
%doc README*
%{go_sys_gopath}/%{go_import_path}

%changelog
%autochangelog
