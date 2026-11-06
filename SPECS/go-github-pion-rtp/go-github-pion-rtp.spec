# SPDX-FileCopyrightText: (C) 2026 Institute of Software, Chinese Academy of Sciences (ISCAS)
# SPDX-FileCopyrightText: (C) 2026 openRuyi Project Contributors
#
# SPDX-License-Identifier: MulanPSL-2.0

%define _name           rtp
%define go_import_path  github.com/pion/rtp

Name:           go-github-pion-rtp
Version:        1.10.2
Release:        %autorelease
Summary:        A Go implementation of RTP
License:        MIT
URL:            https://github.com/pion/rtp
#!RemoteAsset:  sha256:80164cd92cb49080925829f2a38316391ce4fdcb61b69b1c8556e96e59e6c9b1
Source0:        https://github.com/pion/rtp/archive/v%{version}.tar.gz#/%{_name}-%{version}.tar.gz
BuildArch:      noarch
BuildSystem:    golangmodules

BuildRequires:  go
BuildRequires:  go-rpm-macros
BuildRequires:  go(github.com/pion/randutil)
BuildRequires:  go(github.com/stretchr/testify)

Provides:       go(github.com/pion/rtp) = %{version}

Requires:       go(github.com/pion/randutil)

%description
A Go implementation of RTP

%files
%doc README.md
%license LICENSE
%{go_sys_gopath}/%{go_import_path}

%changelog
%autochangelog
