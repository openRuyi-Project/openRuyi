# SPDX-FileCopyrightText: (C) 2026 Institute of Software, Chinese Academy of Sciences (ISCAS)
# SPDX-FileCopyrightText: (C) 2026 openRuyi Project Contributors
#
# SPDX-License-Identifier: MulanPSL-2.0

%define _name           rtcp
%define go_import_path  github.com/pion/rtcp

Name:           go-github-pion-rtcp
Version:        1.2.14
Release:        %autorelease
Summary:        A Go implementation of RTCP
License:        MIT
URL:            https://github.com/pion/rtcp
#!RemoteAsset:  sha256:ab0674ed126edfafc8dcb1c70d269cf04d6498983e5ebe92c9c8ea776234d660
Source0:        https://github.com/pion/rtcp/archive/v%{version}.tar.gz#/%{_name}-%{version}.tar.gz
BuildArch:      noarch
BuildSystem:    golangmodules

BuildRequires:  go
BuildRequires:  go-rpm-macros
BuildRequires:  go(github.com/stretchr/testify)

Provides:       go(github.com/pion/rtcp) = %{version}

%description
A Go implementation of RTCP

%files
%doc README.md
%license LICENSE
%{go_sys_gopath}/%{go_import_path}

%changelog
%autochangelog
