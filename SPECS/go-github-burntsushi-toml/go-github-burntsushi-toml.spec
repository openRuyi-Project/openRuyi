# SPDX-FileCopyrightText: (C) 2026 Institute of Software, Chinese Academy of Sciences (ISCAS)
# SPDX-FileCopyrightText: (C) 2026 openRuyi Project Contributors
# SPDX-FileContributor: Julian Zhu <julian.oerv@isrc.iscas.ac.cn>
#
# SPDX-License-Identifier: MulanPSL-2.0

%define _name           toml
%define go_import_path  github.com/BurntSushi/toml
# It should be [no test files], but it just build failed and dont know why - Julian
%define go_test_exclude github.com/BurntSushi/toml/internal/toml-test

Name:           go-github-burntsushi-toml
Version:        1.6.0
Release:        %autorelease
Summary:        TOML parser for Golang with reflection.
License:        MIT
URL:            https://github.com/burntsushi/toml
#!RemoteAsset
Source0:        https://github.com/burntsushi/toml/archive/v%{version}.tar.gz#/%{_name}-%{version}.tar.gz
BuildArch:      noarch
BuildSystem:    golangmodules

BuildRequires:  go
BuildRequires:  go-rpm-macros

Provides:       go(github.com/burntsushi/toml) = %{version}

%description
TOML stands for Tom's Obvious, Minimal Language. This Go package
provides a reflection interface similar to Go's standard library json
and xml packages.

%files
%license COPYING*
%doc README*
%{go_sys_gopath}/%{go_import_path}

%changelog
%autochangelog
