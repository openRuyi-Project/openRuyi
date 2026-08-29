# SPDX-FileCopyrightText: (C) 2026 Institute of Software, Chinese Academy of Sciences (ISCAS)
# SPDX-FileCopyrightText: (C) 2026 openRuyi Project Contributors
# SPDX-FileContributor: HNO3Miracle <xiangao.or@isrc.iscas.ac.cn>
#
# SPDX-License-Identifier: MulanPSL-2.0

%define _name           ssh-agent
%define go_import_path  github.com/xanzy/ssh-agent

Name:           go-github-xanzy-ssh-agent
Version:        0.3.3
Release:        %autorelease
Summary:        Cross-platform SSH agent wrapper for Go
License:        Apache-2.0
URL:            https://github.com/xanzy/ssh-agent
#!RemoteAsset:  sha256:e15d693dd9aaa7647e1ca4b2fd7051047aa4ad6b3678ecb1ca95cd93c3c34ec9
Source0:        https://github.com/xanzy/ssh-agent/archive/refs/tags/v%{version}.tar.gz#/%{_name}-%{version}.tar.gz
BuildArch:      noarch
BuildSystem:    golangmodules

BuildRequires:  go
BuildRequires:  go-rpm-macros
BuildRequires:  go(golang.org/x/crypto)

Provides:       go(github.com/xanzy/ssh-agent) = %{version}

Requires:       go(golang.org/x/crypto)

%description
ssh-agent provides a Go wrapper for creating and using SSH authentication agents
across supported operating systems.

%files
%doc README.md
%license LICENSE
%{go_sys_gopath}/%{go_import_path}

%changelog
%autochangelog
