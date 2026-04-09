# SPDX-FileCopyrightText: (C) 2026 Institute of Software, Chinese Academy of Sciences (ISCAS)
# SPDX-FileCopyrightText: (C) 2026 openRuyi Project Contributors
# SPDX-FileContributor: Julian Zhu <julian.oerv@isrc.iscas.ac.cn>
#
# SPDX-License-Identifier: MulanPSL-2.0

%define _name           go-checkpoint
%define go_import_path  github.com/hashicorp/go-checkpoint
# Test failure due to network connection part
%define go_test_ignore_failure 1

Name:           go-github-hashicorp-go-checkpoint
Version:        0.5.0
Release:        %autorelease
Summary:        Checkpoint is an internal service at Hashicorp that we use to check version information, broadcast security bulletins, etc.
License:        MPL-2.0
URL:            https://github.com/hashicorp/go-checkpoint
#!RemoteAsset
Source0:        https://github.com/hashicorp/go-checkpoint/archive/v%{version}.tar.gz#/%{_name}-%{version}.tar.gz
BuildArch:      noarch
BuildSystem:    golangmodules

BuildRequires:  go
BuildRequires:  go-rpm-macros
BuildRequires:  go(github.com/hashicorp/go-cleanhttp)
BuildRequires:  go(github.com/hashicorp/go-uuid)

Provides:       go(github.com/hashicorp/go-checkpoint) = %{version}

Requires:       go(github.com/hashicorp/go-cleanhttp)
Requires:       go(github.com/hashicorp/go-uuid)

%description
Go Checkpoint Client

Checkpoint (http://checkpoint.hashicorp.com) is an internal service at
Hashicorp that we use to check version information, broadcast security
bulletins, etc.

%files
%license LICENSE*
%doc README*
%{go_sys_gopath}/%{go_import_path}

%changelog
%autochangelog
