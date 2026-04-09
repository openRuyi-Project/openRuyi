# SPDX-FileCopyrightText: (C) 2026 Institute of Software, Chinese Academy of Sciences (ISCAS)
# SPDX-FileCopyrightText: (C) 2026 openRuyi Project Contributors
# SPDX-FileContributor: Julian Zhu <julian.oerv@isrc.iscas.ac.cn>
#
# SPDX-License-Identifier: MulanPSL-2.0

%define _name           sftp
%define go_import_path  github.com/pkg/sftp

Name:           go-github-pkg-sftp
Version:        1.13.10
Release:        %autorelease
Summary:        SFTP support for the go.crypto/ssh package
License:        BSD-2-Clause
URL:            https://github.com/pkg/sftp
#!RemoteAsset
Source0:        https://github.com/pkg/sftp/archive/v%{version}.tar.gz#/%{_name}-%{version}.tar.gz
BuildArch:      noarch
BuildSystem:    golangmodules

# Skip flaky StatVFS test. https://github.com/pkg/sftp/issues/463
BuildOption(check):  -skip TestRequestStatVFS

BuildRequires:  go
BuildRequires:  go-rpm-macros
BuildRequires:  go(github.com/kr/fs)
BuildRequires:  go(github.com/stretchr/testify)
BuildRequires:  go(golang.org/x/crypto)

Provides:       go(github.com/pkg/sftp) = %{version}

Requires:       go(github.com/kr/fs)
Requires:       go(github.com/stretchr/testify)
Requires:       go(golang.org/x/crypto)

%description
The sftp package provides support for file system operations on remote
ssh servers using the SFTP subsystem. It also implements an SFTP server
for serving files from the filesystem.

%files
%license LICENSE*
%doc README*
%{go_sys_gopath}/%{go_import_path}

%changelog
%autochangelog
