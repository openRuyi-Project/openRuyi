# SPDX-FileCopyrightText: (C) 2026 Institute of Software, Chinese Academy of Sciences (ISCAS)
# SPDX-FileCopyrightText: (C) 2026 openRuyi Project Contributors
# SPDX-FileContributor: HNO3Miracle <xiangao.or@isrc.iscas.ac.cn>
# SPDX-FileContributor: Julian Zhu <julian.oerv@isrc.iscas.ac.cn>
#
# SPDX-License-Identifier: MulanPSL-2.0

%define _name           spdystream
%define go_import_path  github.com/moby/spdystream

Name:           go-github-moby-spdystream
Version:        0.5.1
Release:        %autorelease
Summary:        SPDY stream multiplexing library for Go
License:        Apache-2.0
URL:            https://github.com/moby/spdystream
#!RemoteAsset:  sha256:1638c4402f3be21b09af56c1e8c5d44741bbff283629e68b1dc88949d6f79233
Source0:        https://github.com/moby/spdystream/archive/refs/tags/v%{version}.tar.gz#/%{_name}-%{version}.tar.gz
BuildArch:      noarch
BuildSystem:    golangmodules

BuildRequires:  go
BuildRequires:  go-rpm-macros

Provides:       go(github.com/moby/spdystream) = %{version}

%description
spdystream provides stream multiplexing over SPDY connections.

%files
%doc README*
%license LICENSE*
%{go_sys_gopath}/%{go_import_path}

%changelog
%autochangelog
