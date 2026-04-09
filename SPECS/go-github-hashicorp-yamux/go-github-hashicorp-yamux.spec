# SPDX-FileCopyrightText: (C) 2026 Institute of Software, Chinese Academy of Sciences (ISCAS)
# SPDX-FileCopyrightText: (C) 2026 openRuyi Project Contributors
# SPDX-FileContributor: Julian Zhu <julian.oerv@isrc.iscas.ac.cn>
#
# SPDX-License-Identifier: MulanPSL-2.0

%define _name           yamux
%define go_import_path  github.com/hashicorp/yamux
# TODO: It only fail on riscv64 - Julian
%define go_test_ignore_failure 1

Name:           go-github-hashicorp-yamux
Version:        0.1.2
Release:        %autorelease
Summary:        TODO: short description
License:        MPL-2.0
URL:            https://github.com/hashicorp/yamux
#!RemoteAsset
Source0:        https://github.com/hashicorp/yamux/archive/v%{version}.tar.gz#/%{_name}-%{version}.tar.gz
BuildArch:      noarch
BuildSystem:    golangmodules

BuildRequires:  go
BuildRequires:  go-rpm-macros

Provides:       go(github.com/hashicorp/yamux) = %{version}

%description
Yamux (Yet another Multiplexer) is a multiplexing library for Golang. It
relies on an underlying connection to provide reliability and ordering,
such as TCP or Unix domain sockets, and provides stream-oriented
multiplexing. It is inspired by SPDY but is not interoperable with it.

%files
%license LICENSE*
%doc README*
%{go_sys_gopath}/%{go_import_path}

%changelog
%autochangelog
