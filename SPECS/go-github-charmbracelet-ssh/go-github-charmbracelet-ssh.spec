# SPDX-FileCopyrightText: (C) 2026 Institute of Software, Chinese Academy of Sciences (ISCAS)
# SPDX-FileCopyrightText: (C) 2026 openRuyi Project Contributors
# SPDX-FileContributor: Julian Zhu <julian.oerv@isrc.iscas.ac.cn>
#
# SPDX-License-Identifier: MulanPSL-2.0

%define _name           ssh
%define go_import_path  github.com/charmbracelet/ssh
%define commit_id ebfa259c73091350caed965eb59c2bb8cd90e7e1

Name:           go-github-charmbracelet-ssh
Version:        0+git20250826.ebfa259
Release:        %autorelease
Summary:        Easy SSH servers in Golang
License:        BSD-3-Clause
URL:            https://github.com/charmbracelet/ssh
#!RemoteAsset
Source0:        https://github.com/charmbracelet/ssh/archive/%{commit_id}.tar.gz#/%{_name}-%{version}.tar.gz
BuildArch:      noarch
BuildSystem:    golangmodules

BuildRequires:  go
BuildRequires:  go-rpm-macros
BuildRequires:  go(github.com/anmitsu/go-shlex)
BuildRequires:  go(github.com/charmbracelet/x)
BuildRequires:  go(github.com/creack/pty)
BuildRequires:  go(golang.org/x/crypto)
BuildRequires:  go(golang.org/x/sys)

Provides:       go(github.com/charmbracelet/ssh) = %{version}

Requires:       go(github.com/anmitsu/go-shlex)
Requires:       go(github.com/charmbracelet/x)
Requires:       go(github.com/creack/pty)
Requires:       go(golang.org/x/crypto)
Requires:       go(golang.org/x/sys)

%description
This Go package wraps the crypto/ssh package with
a higher-level API for building SSH servers. The
goal of the API was to make it as simple as using net/http,

%files
%license LICENSE*
%doc README*
%{go_sys_gopath}/%{go_import_path}

%changelog
%autochangelog
