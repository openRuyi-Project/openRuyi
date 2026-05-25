# SPDX-FileCopyrightText: (C) 2026 Institute of Software, Chinese Academy of Sciences (ISCAS)
# SPDX-FileCopyrightText: (C) 2026 openRuyi Project Contributors
# SPDX-FileContributor: Julian Zhu <julian.oerv@isrc.iscas.ac.cn>
# SPDX-FileContributor: HNO3Miracle <xiangao.or@isrc.iscas.ac.cn>
#
# SPDX-License-Identifier: MulanPSL-2.0

%define _name           toml
%define go_import_path  github.com/BurntSushi/toml
# It should be [no test files], but it just build failed and dont know why - Julian
%define go_test_exclude github.com/BurntSushi/toml/internal/toml-test

Name:           go-github-burntsushi-toml
Version:        1.6.0
Release:        %autorelease
Summary:        TOML parser for Golang with reflection
License:        MIT
URL:            https://github.com/burntsushi/toml
#!RemoteAsset:  sha256:eecda85357b0df8b623191a027de3ce43282cceb403f412200a6c5f9776b2098
Source0:        https://github.com/BurntSushi/toml/archive/refs/tags/v%{version}.tar.gz#/%{_name}-%{version}.tar.gz
BuildArch:      noarch
BuildSystem:    golangmodules

BuildRequires:  go
BuildRequires:  go-rpm-macros

Provides:       go(github.com/BurntSushi/toml) = %{version}
Provides:       go(github.com/burntsushi/toml) = %{version}

%description
TOML stands for Tom's Obvious, Minimal Language. This Go package
provides a reflection interface similar to Go's standard library json
and xml packages.

%files
%doc README*
%license COPYING*
%{go_sys_gopath}/%{go_import_path}

%changelog
%autochangelog
