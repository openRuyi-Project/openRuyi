# SPDX-FileCopyrightText: (C) 2026 Institute of Software, Chinese Academy of Sciences (ISCAS)
# SPDX-FileCopyrightText: (C) 2026 openRuyi Project Contributors
# SPDX-FileContributor: HNO3Miracle <xiangao.or@isrc.iscas.ac.cn>
#
# SPDX-License-Identifier: MulanPSL-2.0

%define _name           spdystream
%define go_import_path  github.com/moby/spdystream

Name:           go-github-moby-spdystream
Version:        0.5.0
Release:        %autorelease
Summary:        Go library for github.com/moby/spdystream
License:        Apache-2.0
URL:            https://github.com/moby/spdystream
#!RemoteAsset:  sha256:70e7163424726142ecbac2a0b103721790ed80f6752c8f63021ab1412b0569b2
Source0:        https://github.com/moby/spdystream/archive/refs/tags/v0.5.0.tar.gz#/%{_name}-%{version}.tar.gz
BuildArch:      noarch
BuildSystem:    golangmodules

BuildOption(prep):  -n spdystream-0.5.0

BuildRequires:  go
BuildRequires:  go-rpm-macros

Provides:       go(github.com/moby/spdystream) = %{version}

%description
This package provides the Go library github.com/moby/spdystream.

%files
%doc README*
%license LICENSE*
%{go_sys_gopath}/%{go_import_path}

%changelog
%autochangelog
